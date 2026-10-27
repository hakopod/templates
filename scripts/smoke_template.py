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
import argparse, base64, http.client, json, pathlib, platform, re, secrets, socket
import string, subprocess, sys, time, tomllib

ROOT = pathlib.Path(__file__).resolve().parents[1]
ORIGIN = "https://catalog.example.test"
# busybox 1.37.0 multi-arch index (amd64, arm64, ...), used only to chown volumes.
HELPER = "docker.io/library/busybox:1.37.0@sha256:bdf57e528e45e4433820e045b29b4597825a1c9e38353532d90a01445013f82e"
UNSUPPORTED = ("files", "job", "gpu", "bindings", "certificate_mounts", "ports", "database_client_profiles")


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
    return {ref: gen_secret(formats.get(ref, "token")) for ref in sorted(refs)}


def fixture(field):
    """Placeholder for a required field with no default, chosen from its metadata."""
    text = " ".join(str(field.get(k, "")) for k in ("name", "label", "description")).lower()
    if "email" in text:
        return "admin@example.test"
    if re.search(r"\b(url|uri|endpoint)\b|[-_](url|uri)\b", text):
        return "http://example.test"
    return "fixture"


def config_values(row):
    out = {}
    for f in row.get("config_fields", []):
        value = f.get("default", "")
        if not value and f.get("required"):
            value = fixture(f)
        out[f["name"]] = value
    return out


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
        user, fsg = svc.get("run_as_user", 0), svc.get("fs_group", 0)
        for vol, _, _ in volume_mounts(tid, name, svc, spec):
            volumes[vol] = None
            chown.append(["docker", "run", "--rm", "-v", f"{vol}:/v", HELPER, "sh", "-c",
                          f"chown -R {user}:{fsg} /v && chmod -R g+rwX /v && chmod g+s /v"])
    runs = []
    for name in order(services):
        svc = services[name]
        cmd = ["docker", "run", "-d", "--name", f"smoke-{tid}-{name}", "--network", net,
               "--network-alias", name, "--user", f"{svc.get('run_as_user', 0)}:{svc.get('run_as_group', 0)}",
               "--cap-drop", "ALL", "--security-opt", "no-new-privileges"]
        if svc.get("fs_group"):
            cmd += ["--group-add", str(svc["fs_group"])]
        if svc.get("read_only_root_filesystem"):
            cmd.append("--read-only")
        for t in svc.get("temporary_mounts", []):
            cmd += ["--tmpfs", f"{t['mount_path']}:rw,size={t.get('size_mib', 64)}m"]
        for vol, path, ro in volume_mounts(tid, name, svc, spec):
            cmd += ["-v", f"{vol}:{path}" + (":ro" if ro else "")]
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
            "chown": chown, "run": runs}


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


def smoke(tid, timeout):
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
    p = plan(tid, spec, row, sec, port)
    names = [f"smoke-{tid}-{n}" for n, _ in p["run"]]
    main = spec["services"]["main"]
    status, code, start = "failed", None, time.time()
    try:
        sh(p["network"], redact)
        for v in p["volumes"]:
            sh(["docker", "volume", "create", v], redact)
        for c in p["chown"]:
            sh(c, redact)
        for _, c in p["run"]:
            sh(c, redact)
        deadline = start + timeout
        while time.time() < deadline:
            states = sh(["docker", "inspect", "-f", "{{.Name}} {{.State.Status}}"] + names, redact).split("\n")
            dead = [x for x in states if x and not x.endswith(" running")]
            if dead:
                print("container not running:", ", ".join(dead))
                break
            code = http_code(port, main.get("healthcheck") or "/")
            if code and 200 <= code < 400:
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
    print(f"template={tid} arch={platform.machine()} image={main['image'].split('@')[0]} "
          f"status={status} seconds={time.time() - start:.0f} http={code}")
    return 0 if status == "ready" else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("template")
    ap.add_argument("--timeout", type=int, default=600)
    a = ap.parse_args()
    sys.exit(smoke(a.template, a.timeout))
