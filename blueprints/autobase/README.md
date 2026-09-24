# Autobase

PostgreSQL automation console requiring a dedicated operator-controlled host.

## Deployment prerequisites

`candidate.toml` describes the native service topology but is intentionally excluded from deployment.

- Official console requires the host Docker socket and /tmp/ansible host directory to launch automation containers. These are intentionally unavailable to Hakopod application workloads.
- The all-in-one image initializes PostgreSQL and Nginx as root; a restricted non-root pod cannot run its supervisor setup.

- Dedicated trusted operator host running the upstream stack
- Host automation privileges; not supported as a tenant application
- The candidate preserves application ports, credentials and persistent data declarations; it deliberately omits privileged host sockets and bind mounts.
- Do not deploy this file unchanged. Use the upstream dedicated-host installation until a reviewed remote execution adapter exists.

## Secrets and storage

`console-token`, `database-password` are application-scoped secret references. Generate or save them before deployment. Database connection bindings reuse those same saved passwords.

Persistent services use one replica; scaling replicas does not create a database cluster. The storage option applies to each claim. New installations only: an image/template update is not an automatic database-major-version migration.

## Verification

Reviewed on 24 September 2026. Image manifests and container configuration were inspected remotely without executing workloads. Runtime startup, application-specific workflows and backup restoration are not yet verified unless later evidence is recorded here.

## Sources

- https://dokploy.com/templates/autobase
- https://github.com/vitabaks/autobase/blob/2.7.2/console/docker-compose.yml
- https://github.com/vitabaks/autobase/blob/master/console/docker-compose.yml
