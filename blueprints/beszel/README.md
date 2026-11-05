# Beszel

Deployment preset. Image digest, amd64/arm64 platforms and image config (root user, /beszel entrypoint) checked from the registry; USER_EMAIL, USER_PASSWORD and APP_URL read from the v0.21.1 source. The preset runs it as UID 1000. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Lightweight server monitoring hub with history, alerts and Docker stats from small agents.

## Requirements

- This is the hub only. Install the Beszel agent on each machine you want to watch, then add it in the hub with the key the hub shows.
- The first administrator is created from the configured email and the admin-password secret on the first start only.
- Back up the /beszel_data volume; it holds users, systems and history.

## Credentials

- `admin-password`: At least 16 characters. Keep stable and include in protected backups.

## Configuration

- `admin-email` (Administrator email): Email address for the first administrator. Used only on the first start.

## Sources

- https://github.com/henrygd/beszel/blob/v0.21.1/internal/migrations/initial-settings.go
- https://beszel.dev/guide/hub-installation

Application license: MIT.
