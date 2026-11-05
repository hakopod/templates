# pgAdmin

Deployment preset. Image digest, amd64/arm64 platforms and image config (UID 5050, /entrypoint.sh) checked from the registry; the restricted-context fallback to port 8080 read from the REL-9_19 entrypoint. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Web administration and query tool for PostgreSQL.

## Requirements

- Sign in with the configured email and the admin-password secret, then add your servers. Databases on Hakopod must share a virtual network with this app.
- Password-reset email is off; Postfix is not started.
- Back up the /var/lib/pgadmin volume; it holds saved servers and stored passwords.

## Credentials

- `admin-password`: At least 16 characters. Keep stable and include in protected backups.

## Configuration

- `admin-email` (Administrator email): Email address you sign in with.

## Sources

- https://github.com/pgadmin-org/pgadmin4/blob/REL-9_19/pkg/docker/entrypoint.sh
- https://www.pgadmin.org/docs/pgadmin4/latest/container_deployment.html

Application license: PostgreSQL.
