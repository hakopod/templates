# listmonk

Deployment preset. Image digest, amd64/arm64 platforms and image config (root user, docker-entrypoint.sh) checked from the registry; install and upgrade sequence taken from the v6.2.0 compose file. The preset runs it as UID 1000. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Self-hosted newsletter and mailing list manager with PostgreSQL.

## Requirements

- Sign in with the configured admin user and the admin-password secret, then set Root URL and an SMTP server under Settings before sending anything.
- Media uploads go to /listmonk/uploads; set that path under Settings, Media.
- Back up the PostgreSQL volume; subscribers and campaigns live there.

## Credentials

- `admin-password`: At least 16 characters. Keep stable and include in protected backups.
- `database-password`: At least 16 characters. Keep stable and include in protected backups.

## Configuration

- `admin-user` (Admin username): Username of the first administrator, created on the first start only.

## Sources

- https://github.com/knadh/listmonk/blob/v6.2.0/docker-compose.yml
- https://listmonk.app/docs/configuration/

Application license: AGPL-3.0.
