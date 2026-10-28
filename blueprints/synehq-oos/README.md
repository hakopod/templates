# SyneHQ OOS

Open-source database explorer for the Hakopod `/synehq` integration.

## Pod mode

This template runs OOS with `OOS_RUNTIME=kubernetes`. A Kubernetes pod cannot be given a delegated cgroup subtree, so Kelvo runs query workers without per-query cgroups. The 768 MiB pod limit is the only memory, CPU and process boundary, and one runaway query can restart the explorer. Landlock, the worker seccomp filter, non-root execution and the read-only root filesystem still apply. Nodes need Linux with Landlock ABI 3 or later.

For per-query cgroups, run OOS on a Linux Docker host with `deploy/run-container.sh` instead.

## Requirements

- One instance per Hakopod project and environment, with fresh metadata. An existing standalone installation cannot be taken over.
- **Hakopod URL:** the HTTPS origin of this Hakopod installation. OOS asks `<Hakopod URL>/internal/database-explorer/authorize` to validate every session.
- **Explorer scope:** the exact scope string of the matching engine target, such as `demo/development`.
- `hakopod-explorer-key`: a separate 32-byte key encoded as 64 lowercase hex characters. It is mounted as a read-only file at `/etc/synehq/hakopod.key`, never as an environment variable. Do not reuse session, encryption, TLS or Kelvo keys.

## Connect Hakopod

After the app is running, add a target to the engine's `HAKOPOD_EXPLORER_TARGETS_FILE`:

```toml
[[targets]]
scope = "demo/development"
project = "demo"
environment = "development"
url = "https://<this app's domain>/synehq"
key_file = "/path/to/explorer-demo.key"
```

The key file holds the same `hakopod-explorer-key` value and has mode 0600. **Explore databases** appears for users who can query databases in that scope.

## Sources

- https://github.com/SyneHQ/synehq-oos
- https://github.com/SyneHQ/synehq-oos/blob/main/docs/hakopod-integration.md

Application license: Apache-2.0.
