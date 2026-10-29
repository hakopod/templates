# Rivet Engine

Self-hosted [Rivet](https://github.com/rivet-dev/rivet) engine. Rivet Actors are
long-running, stateful processes with their own storage, used for AI agents,
durable workflows and realtime rooms. The engine schedules and routes them; your
actor code runs in a separate RivetKit app that connects out to it.

## What this preset runs

- One `rivetdev/engine` 2.3.31 service on file-system storage (RocksDB in the
  10 GiB volume at `/var/lib/rivet-engine`), the same mode as upstream's
  single-host Docker Compose setup.
- Port 6420 serves the API, the dashboard and actor traffic. It is private by
  default.
- It runs as UID 1000 with a read-only root and `/tmp` as scratch space. The
  upstream image runs as root.

It is a single node and is not highly available. Multi-node Rivet uses PostgreSQL
and NATS; this preset does not set those up.

## Secrets and storage

- `admin-token`: the engine's admin token (`RIVET__AUTH__ADMIN_TOKEN`). Runners
  and the dashboard use it. Keep it stable.
- The volume holds all actor state. Back it up off-node.

## Running your actors on Hakopod

Deploy your RivetKit app as its own application with a worker service: no
`port`, because it only connects out to the engine.

```toml
[services.actors]
image = "ghcr.io/you/your-rivetkit-app@sha256:..."
termination_grace_seconds = 60

[services.actors.env]
RIVET_ENDPOINT = "http://main.<engine namespace>.svc.cluster.local:6420"

[services.actors.secrets.RIVET_TOKEN]
ref = "rivet-admin-token"
```

- Each actor gets up to 15 seconds to save its state on shutdown, so keep the
  grace period at 60 seconds or more.
- The worker can reach the engine only through a shared virtual network segment
  that both applications join. Copy the engine's exact address from the network
  inspector. Alternatively, make port 6420 public and use its HTTPS address.
- Save the same admin token value as a secret in the worker's application.
- Workers scale by adding replicas. New replicas connect out and start serving
  actors without any extra registration.

## Verification

Image digest, amd64/arm64 platforms and image config (root user,
`rivet-engine start` entrypoint) checked from the registry. The preset runs it
as UID 1000 with a read-only root. The template smoke workflow in GitHub Actions
starts it and checks `/metadata`. Not tested on Kubernetes, and no actor has been
run against it.

## Sources

- https://github.com/rivet-dev/rivet/tree/v2.3.31/self-host/control-plane/docker-compose
- https://github.com/rivet-dev/rivet/blob/v2.3.31/docker/engine/Dockerfile
- https://github.com/rivet-dev/rivet/blob/v2.3.31/engine/artifacts/config-schema.json

Application license: Apache-2.0.
