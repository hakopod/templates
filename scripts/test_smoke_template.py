"""Pure unit tests: no docker, no network. Run: python3 -m unittest scripts/test_smoke_template.py"""
import io, json, pathlib, sys, tomllib, unittest
from contextlib import redirect_stdout
from unittest import mock
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import smoke_template as st

ROOT = st.ROOT


def load(tid):
    # Blueprints may land before their catalog row; fall back to a minimal row.
    row = next((r for r in json.loads((ROOT / "catalog.json").read_text()) if r["id"] == tid),
               {"id": tid, "deployable": True, "config_fields": [], "secret_fields": []})
    return row, tomllib.loads((ROOT / "blueprints" / tid / "hakopod.toml").read_text())


class T(unittest.TestCase):
    def test_render(self):
        cfg = {"timezone": "UTC"}
        self.assertEqual(st.render("tz={{config.timezone}}", cfg, 1), "tz=UTC")
        self.assertEqual(st.render("{{site_host}}|{{site_hostname}}", cfg, 8080), "127.0.0.1:8080|127.0.0.1")
        self.assertEqual(st.render("https://catalog.example.test/x", cfg, 9), "http://127.0.0.1:9/x")

    def test_config_fixture(self):
        row = {"config_fields": [{"name": "admin_email", "required": True}, {"name": "x", "required": True},
                                 {"name": "tz", "default": "UTC", "required": True}]}
        self.assertEqual(st.config_values(row), {"admin_email": "admin@example.com", "x": "fixture", "tz": "UTC"})

    def test_secrets_shared_per_ref(self):
        row, spec = load("n8n-with-postgres")
        sec = st.make_secrets(row, spec)
        self.assertEqual(set(sec), {"database-password", "encryption-key"})
        p = st.plan("n8n-with-postgres", spec, row, sec, 5000)
        runs = dict(p["run"])
        pw = "POSTGRES_PASSWORD=" + sec["database-password"]
        self.assertIn(pw, runs["db"])
        self.assertIn("DB_POSTGRESDB_PASSWORD=" + sec["database-password"], runs["main"])
        self.assertEqual(len(sec["database-password"]), 24)
        self.assertEqual(len(st.gen_secret("hex")), 64)

    def test_n8n_args(self):
        row, spec = load("n8n-with-postgres")
        sec = {"database-password": "PW", "encryption-key": "EK"}
        p = st.plan("n8n-with-postgres", spec, row, sec, 5000)
        self.assertEqual([n for n, _ in p["run"]], ["db", "main"])
        main = dict(p["run"])["main"]
        self.assertEqual(main[:12], ["docker", "run", "-d", "--name", "smoke-n8n-with-postgres-main", "--network",
                                     "smoke-n8n-with-postgres", "--network-alias", "main", "--user", "1000:1000", "--group-add"])
        for part in (["--security-opt", "no-new-privileges"], ["-p", "127.0.0.1:5000:5678"],
                     ["-e", "N8N_HOST=127.0.0.1:5000"], ["-e", "WEBHOOK_URL=http://127.0.0.1:5000/"],
                     ["-e", "GENERIC_TIMEZONE=UTC"], ["-v", "smoke-n8n-with-postgres-main-data:/home/node/.n8n:nocopy"]):
            self.assertIn(part[0], main)
            self.assertIn(part[1], main)
        self.assertTrue(main[-1].startswith("n8nio/n8n:") and "@sha256:" in main[-1])  # image is last, no args
        db = dict(p["run"])["db"]
        self.assertEqual(db[-5:], ["postgres", "-c", "shared_buffers=64MB", "-c", "max_connections=50"])
        self.assertIn("max_connections=50", db)
        self.assertNotIn("-p", db)
        self.assertEqual(p["network"], ["docker", "network", "create", "smoke-n8n-with-postgres"])
        self.assertEqual(len(p["volumes"]), 2)
        self.assertIn("chgrp -R 70 /v", p["chown"][0][-1])

    def test_freshrss_command_tmpfs_and_directus_mounts(self):
        row, spec = load("freshrss")
        run = dict(st.plan("freshrss", spec, row, {}, 7)["run"])["main"]
        self.assertIn("--tmpfs", run)
        self.assertIn("/tmp:rw,size=128m", run)
        self.assertEqual(run[run.index("--entrypoint") + 1], "sh")
        self.assertIn("--group-add", run)
        row, spec = load("directus")
        sec = st.make_secrets(row, spec)
        p = st.plan("directus", spec, row, sec, 7)
        self.assertEqual(p["volumes"], ["smoke-directus-database", "smoke-directus-uploads"])
        self.assertEqual(len(p["chown"]), 2)

    def test_fixture_matches_field(self):
        f = st.fixture
        self.assertEqual(f({"name": "admin_email"}), "admin@example.com")
        self.assertEqual(f({"name": "owner", "description": "Contact email"}), "admin@example.com")
        self.assertEqual(f({"name": "api_url"}), "http://example.test")
        self.assertEqual(f({"name": "x", "description": "Public URL of the server"}), "http://example.test")
        self.assertEqual(f({"name": "x"}), "fixture")

    def test_security_ids_follow_hakopod(self):
        self.assertEqual(st.security_ids({"run_as_user": 0, "fs_group": 0}), (10001, 10001, 10001))
        self.assertEqual(st.security_ids({}), (10001, 10001, 10001))
        self.assertEqual(st.security_ids({"run_as_user": 70}), (70, 70, 70))
        self.assertEqual(st.security_ids({"run_as_user": 1000, "run_as_group": 5, "fs_group": 7}), (1000, 5, 7))
        row, spec = load("uptime-kuma")
        main = dict(st.plan("uptime-kuma", spec, row, {}, 3)["run"])["main"]
        self.assertEqual(main[main.index("--user") + 1], "10001:10001")

    def test_probe_http_when_healthcheck_path(self):
        with mock.patch.object(st, "http_code", return_value=200) as h, mock.patch.object(st, "tcp_open") as t:
            self.assertEqual(st.probe("/ping", 1, None, 100), (True, None, 200))
        h.assert_called_once_with(1, "/ping")
        t.assert_not_called()
        with mock.patch.object(st, "http_code", return_value=503):
            self.assertEqual(st.probe("/ping", 1, None, 100), (False, None, 503))

    def test_probe_tcp_needs_steady_connection(self):
        with mock.patch.object(st, "http_code") as h, mock.patch.object(st, "tcp_open", return_value=True):
            self.assertEqual(st.probe("", 1, None, 100), (False, 100, None))
            self.assertEqual(st.probe("", 1, 100, 100 + st.STABLE_SECONDS), (True, 100, None))
        h.assert_not_called()
        with mock.patch.object(st, "tcp_open", return_value=False):  # a drop resets the clock
            self.assertEqual(st.probe("", 1, 100, 200), (False, None, None))

    def test_kafka_is_private_and_published_for_the_harness(self):
        row, spec = load("kafka")
        main = spec["services"]["main"]
        self.assertFalse(main["public"])
        self.assertEqual(main["healthcheck"], "")
        run = dict(st.plan("kafka", spec, row, {}, 9099)["run"])["main"]
        self.assertIn("127.0.0.1:9099:9092", run)
        self.assertIn("CLUSTER_ID=MkU3OEVBNTcwNTJENDM2Qk", run)
        self.assertEqual(run[run.index("--user") + 1], "1000:1000")
        self.assertEqual(run[run.index("--entrypoint") + 1], "sh")  # computes the advertised listener
        self.assertNotIn("KAFKA_ADVERTISED_LISTENERS", " ".join(a for a in run if a.startswith("KAFKA_ADV")))

    def test_skip_not_deployable(self):
        row = next(r for r in json.loads((ROOT / "catalog.json").read_text()) if not r["deployable"])
        buf = io.StringIO()
        with mock.patch.object(st.subprocess, "run") as run, redirect_stdout(buf):
            self.assertEqual(st.smoke(row["id"], 1), 0)
        run.assert_not_called()
        self.assertIn("SKIP", buf.getvalue())

    def test_failure_cleans_up_and_hides_secrets(self):
        calls = []
        def fake(cmd, **kw):
            calls.append(cmd)
            if cmd[:3] == ["docker", "run", "-d"]:
                return mock.Mock(returncode=1, stdout="", stderr="boom " + next(a for a in cmd if a.startswith("POSTGRES_PASSWORD=")))
            return mock.Mock(returncode=0, stdout="", stderr="")
        buf = io.StringIO()
        with mock.patch.object(st.subprocess, "run", fake), mock.patch.object(st.platform, "machine", return_value="x86_64"), redirect_stdout(buf):
            self.assertEqual(st.smoke("n8n-with-postgres", 1), 1)
        self.assertNotRegex(buf.getvalue(), r"POSTGRES_PASSWORD=[A-Za-z0-9]{10}")
        self.assertIn(["docker", "network", "rm", "smoke-n8n-with-postgres"], calls)


if __name__ == "__main__":
    unittest.main()
