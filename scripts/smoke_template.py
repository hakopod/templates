#!/usr/bin/env python3
"""Start a Hakopod template with the docker CLI and wait for its main service.

Usage: python3 scripts/smoke_template.py <template-id> [--timeout 600]

Runs in CI only (needs docker). Renders placeholders like Hakopod's planner:
{{config.x}} -> catalog default (or a fixture), https://catalog.example.test,
{{site_host}} and {{site_hostname}} -> http://127.0.0.1:<port>. Plain http means
apps that insist on https origins (secure cookies, OAuth callbacks) are only
checked for starting and answering their healthcheck, not for login flows.
Python 3.11+, standard library only.
"""
import argparse, base64, http.client, json, pathlib, platform, re, secrets, socket, tempfile
import string, subprocess, sys, time, tomllib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ORIGIN = "https://catalog.example.test"
FILES_DIR = pathlib.Path(tempfile.gettempdir()) / "hakopod-smoke-files"
# busybox 1.37.0 multi-arch index (amd64, arm64, ...), used only to chown volumes.
HELPER = "docker.io/library/busybox:1.37.0@sha256:bdf57e528e45e4433820e045b29b4597825a1c9e38353532d90a01445013f82e"
UNSUPPORTED = ("job", "gpu", "bindings", "ports", "database_client_profiles")


def gen_secret(fmt):
    alnum = string.ascii_letters + string.digits
    if fmt == "password":
        return "".join(secrets.choice(alnum) for _ in range(24))
    if fmt in ("hex", "hex32", "token64"):
        return secrets.token_hex(32)
    if fmt == "base64-32":
        return base64.b64encode(secrets.token_bytes(32)).decode()
    # token and anything else (provider-key, urls, certs): opaque random text.
    # ponytail: certificates/private keys/URLs are not really generated; add when a template needs them.
    return secrets.token_urlsafe(32)


def make_secrets(row, spec):
    """One value per secret ref, shared by every service that uses the ref."""
    formats = {f["name"]: f.get("format", "token") for f in row.get("secret_fields", [])}
    refs = {s["ref"] for svc in spec["services"].values() for s in svc.get("secrets", {}).values()}
    refs |= {f["secret"]["ref"] for svc in spec["services"].values() for f in svc.get("files", {}).values() if f.get("secret")}
    return {ref: gen_secret(formats.get(ref, "token")) for ref in sorted(refs)}


def fixture(field):
    """Placeholder for a required field with no default, chosen from its metadata."""
    text = " ".join(str(field.get(k, "")) for k in ("name", "label", "description")).lower()
    if "email" in text:
        return "admin@example.com"
    if re.search(r"\b(url|uri|endpoint)\b|[-_](url|uri)\b", text):
        return "https://example.test" if "https" in text else "http://example.test"
    return "fixture"


def config_values(row):
    out = {}
    for f in row.get("config_fields", []):
        value = f.get("default", "")
        if not value and f.get("required"):
            value = fixture(f)
        out[f["name"]] = value
    return out


def security_ids(svc):
    """Pod user, group and fsGroup exactly as Hakopod computes them.

    internal/cluster/deploy.go:565 starts every pod at RunAsUser=RunAsGroup=10001,
    RunAsNonRoot=true, seccomp RuntimeDefault; container: AllowPrivilegeEscalation
    =false, capabilities drop ALL (deploy.go:532).
    internal/cluster/workloads.go:50-60 then:
      run_as_user > 0 -> uid = gid = run_as_user; run_as_user 0/unset stays 10001
        (it is NOT root, and run_as_user 0 never means root);
      fsGroup = uid (line 54); run_as_group > 0 overrides gid (55); fs_group > 0
        overrides fsGroup (58) - an fs_group of 0 means "same as the uid";
      readOnlyRootFilesystem = the service flag (61);
      FSGroupChangePolicy = OnRootMismatch (65), i.e. kubelet fixes group
        ownership of a volume once, not on every start.
    Kubernetes applies fsGroup by setting the volume's GROUP to fsGroup, making it
    group-writable with setgid, and adds fsGroup as a supplemental group of the
    container; the owning user stays root. The harness mirrors that (chgrp, not chown).
    Not modelled: node_profile.go:214 / sidecars.go:132 force root in special profiles.
    """
    uid = svc.get("run_as_user", 0) or 10001
    gid = svc.get("run_as_group", 0) or uid
    return uid, gid, svc.get("fs_group", 0) or uid


def render(value, config, port):
    for name, v in config.items():
        value = value.replace("{{config.%s}}" % name, v)
    value = value.replace("{{site_host}}", f"127.0.0.1:{port}").replace("{{site_hostname}}", "127.0.0.1")
    return value.replace(ORIGIN, f"http://127.0.0.1:{port}")


def order(services):
    done, out = set(), []
    def visit(name):
        if name in done:
            return
        done.add(name)
        for dep in services[name].get("depends_on", []):
            visit(dep)
        out.append(name)
    for name in sorted(services):
        visit(name)
    return out


def volume_mounts(tid, name, svc, spec):
    """(volume name, mount path, read_only) for each persistent mount of a service."""
    res = []
    if svc.get("volume"):
        res.append((f"smoke-{tid}-{name}-data", svc["volume"]["mount_path"], False))
    for m in svc.get("mounts", []):
        res.append((f"smoke-{tid}-{m['volume']}", m["mount_path"], bool(m.get("read_only"))))
    return res


def plan(tid, spec, row, secret_values, port, config=None):
    """Return {'network', 'volumes', 'chown', 'run'} docker argument lists. Pure."""
    config = config_values(row) if config is None else config
    services = spec["services"]
    net = f"smoke-{tid}"
    volumes, chown = {}, []
    for name, svc in services.items():
        fsg = security_ids(svc)[2]
        for vol, _, _ in volume_mounts(tid, name, svc, spec):
            volumes[vol] = None
            chown.append(["docker", "run", "--rm", "-v", f"{vol}:/v", HELPER, "sh", "-c",
                          f"chgrp -R {fsg} /v && chmod -R g+rwX /v && chmod g+s /v"])
    runs, files, certs = [], [], []
    for name in order(services):
        svc = services[name]
        uid, gid, fsg = security_ids(svc)
        cmd = ["docker", "run", "-d", "--name", f"smoke-{tid}-{name}", "--network", net,
               "--network-alias", name, "--user", f"{uid}:{gid}", "--group-add", str(fsg),
               "--cap-drop", "ALL", "--security-opt", "no-new-privileges"]
        if svc.get("read_only_root_filesystem"):
            cmd.append("--read-only")
        for t in svc.get("temporary_mounts", []):
            cmd += ["--tmpfs", f"{t['mount_path']}:rw,size={t.get('size_mib', 64)}m"]
        for vol, path, ro in volume_mounts(tid, name, svc, spec):
            # nocopy: Docker would otherwise copy the image directory's contents and
            # root ownership into the empty volume, which Kubernetes never does.
            cmd += ["-v", f"{vol}:{path}:nocopy" + (",ro" if ro else "")]
        for key, f in sorted(svc.get("files", {}).items()):
            # Like kubelet with fsGroup: root-owned, group fs_group, group read added.
            host = str(FILES_DIR / f"{tid}-{name}-{key}")
            body = f["content"] if "content" in f else secret_values[f["secret"]["ref"]]
            files.append({"path": host, "body": body, "mode": (f.get("mode") or 0o444) | 0o440, "gid": fsg})
            cmd += ["-v", f"{host}:{f['mount_path']}:ro"]
        for i, m in enumerate(svc.get("certificate_mounts", [])):
            # Stands in for Hakopod's tls.crt/tls.key Secret volume: a throwaway
            # self-signed pair, root-owned, group fs_group, mode 0440.
            host = str(FILES_DIR / f"{tid}-{name}-cert-{i}")
            certs.append({"dir": host, "gid": fsg})
            cmd += ["-v", f"{host}:{m['mount_path']}:ro"]
        for k, v in sorted(svc.get("env", {}).items()):
            cmd += ["-e", f"{k}={render(v, config, port)}"]
        for k, s in sorted(svc.get("secrets", {}).items()):
            cmd += ["-e", f"{k}={secret_values[s['ref']]}"]
        if svc.get("working_dir"):
            cmd += ["-w", svc["working_dir"]]
        if name == "main":
            cmd += ["-p", f"127.0.0.1:{port}:{svc['port']}"]
        command = svc.get("command", [])
        if command:
            cmd += ["--entrypoint", command[0]]
        cmd += [svc["image"]] + command[1:] + svc.get("args", [])
        runs.append((name, cmd))
    return {"network": ["docker", "network", "create", net], "volumes": sorted(volumes),
            "chown": chown, "files": files, "certs": certs, "run": runs}


def skip_reason(row, spec):
    if not row["deployable"]:
        return "not deployable (migration guide)"
    if "main" not in spec["services"]:
        return "no main service"
    arch = {"x86_64": "amd64", "amd64": "amd64", "aarch64": "arm64", "arm64": "arm64"}.get(platform.machine().lower())
    if arch not in row["architectures"]:
        return f"runner architecture {arch} not supported by the template"
    for name, svc in spec["services"].items():
        for key in UNSUPPORTED:
            if svc.get(key):
                return f"service {name} uses {key}, which the smoke test cannot emulate"
    return None


def sh(cmd, redact, check=True):
    p = subprocess.run(cmd, capture_output=True, text=True)
    out = p.stdout + p.stderr
    for s in redact:
        out = out.replace(s, "***")
    if check and p.returncode:
        raise RuntimeError(f"{cmd[1]} {cmd[2]} failed: {out.strip()[-1500:]}")
    return out


def http_code(port, path):
    try:
        c = http.client.HTTPConnection("127.0.0.1", port, timeout=5)
        c.request("GET", path if path.startswith("/") else "/" + path)
        return c.getresponse().status
    except (OSError, http.client.HTTPException):
        return None


def tcp_open(port):
    """True if something answers on the port and keeps the connection open.

    Docker's published-port proxy accepts connections even when nothing listens in the
    container and then closes them, so an immediate close does not count as open.
    """
    try:
        with socket.create_connection(("127.0.0.1", port), timeout=5) as c:
            c.settimeout(1)
            try:
                return c.recv(1) != b""
            except socket.timeout:
                return True  # open and waiting for the client, as Kafka does
    except OSError:
        return False


STABLE_SECONDS = 45  # outlasts startup deadlines such as SyneHQ OOS's 30 s Kelvo check


def probe(path, port, since, now, stable=STABLE_SECONDS):
    """One readiness check -> (ready, since, http_code).

    A healthcheck path means HTTP 2xx/3xx. An empty path means the service is not
    necessarily HTTP (Kafka, databases): ready once the port has accepted connections
    continuously for `stable` seconds; the caller's loop already fails if any container
    stopped, so that also proves the process stays up.
    """
    if path:
        code = http_code(port, path)
        return bool(code and 200 <= code < 400), since, code
    since = (since or now) if tcp_open(port) else None
    return since is not None and now - since >= stable, since, None


def smoke(tid, timeout, overrides=None):
    row = next((r for r in json.loads((ROOT / "catalog.json").read_text()) if r["id"] == tid), None)
    if row is None:
        sys.exit(f"unknown template {tid}")
    file = ROOT / "blueprints" / tid / "hakopod.toml"
    spec = tomllib.loads(file.read_text()) if file.exists() else {"services": {}}
    reason = skip_reason(row, spec) if file.exists() else "no hakopod.toml"
    if not row["deployable"] or reason:
        print(f"SKIP {tid}: {reason}")
        return 0
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        port = s.getsockname()[1]
    sec = make_secrets(row, spec)
    redact = list(sec.values())
    p = plan(tid, spec, row, sec, port, {**config_values(row), **(overrides or {})})
    names = [f"smoke-{tid}-{n}" for n, _ in p["run"]]
    main = spec["services"]["main"]
    status, code, start, since = "failed", None, time.time(), None
    try:
        sh(p["network"], redact)
        for v in p["volumes"]:
            sh(["docker", "volume", "create", v], redact)
        for c in p["chown"]:
            sh(c, redact)
        FILES_DIR.mkdir(exist_ok=True)
        for f in p["files"]:
            pathlib.Path(f["path"]).write_text(f["body"])
            sh(["sudo", "chown", f"0:{f['gid']}", f["path"]], redact)
            sh(["sudo", "chmod", format(f["mode"], "o"), f["path"]], redact)
        for c in p["certs"]:
            pathlib.Path(c["dir"]).mkdir(exist_ok=True)
            sh(["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1", "-subj", "/CN=smoke.test",
                "-addext", "subjectAltName=DNS:smoke.test", "-keyout", c["dir"] + "/tls.key", "-out", c["dir"] + "/tls.crt"], redact)
            sh(["sudo", "chown", "-R", f"0:{c['gid']}", c["dir"]], redact)
            sh(["sudo", "chmod", "0440", c["dir"] + "/tls.key", c["dir"] + "/tls.crt"], redact)
            sh(["sudo", "chmod", "0550", c["dir"]], redact)
        for _, c in p["run"]:
            sh(c, redact)
        deadline = start + timeout
        while time.time() < deadline:
            states = sh(["docker", "inspect", "-f", "{{.Name}} {{.State.Status}}"] + names, redact).split("\n")
            dead = [x for x in states if x and not x.endswith(" running")]
            if dead:
                print("container not running:", ", ".join(dead))
                break
            ready, since, code = probe(main.get("healthcheck", ""), port, since, time.time())
            if ready:
                status = "ready"
                break
            time.sleep(2)
        else:
            print(f"timed out after {timeout}s")
    except RuntimeError as e:
        print(e)
    finally:
        if status != "ready":
            for n in names:
                print(f"--- logs {n} (last 200 lines)")
                print(sh(["docker", "logs", "--tail", "200", n], redact, check=False))
        for n in names:
            sh(["docker", "rm", "-f", "-v", n], redact, check=False)
        sh(["docker", "network", "rm", p["network"][-1]], redact, check=False)
        for v in p["volumes"]:
            sh(["docker", "volume", "rm", "-f", v], redact, check=False)
        for f in p["files"]:
            sh(["sudo", "rm", "-f", f["path"]], redact, check=False)
        for c in p["certs"]:
            sh(["sudo", "rm", "-rf", c["dir"]], redact, check=False)
    print(f"template={tid} arch={platform.machine()} image={main['image'].split('@')[0]} "
          f"status={status} seconds={time.time() - start:.0f} http={code}")
    return 0 if status == "ready" else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("template")
    ap.add_argument("--timeout", type=int, default=600)
    ap.add_argument("--set", action="append", default=[], metavar="NAME=VALUE", help="override a catalog config field")
    a = ap.parse_args()
    sys.exit(smoke(a.template, a.timeout, dict(item.split("=", 1) for item in a.set)))
