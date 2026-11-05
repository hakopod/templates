# Radicale

Deployment preset. Image digest, amd64/arm64 platforms and image config (radicale user 2999, docker-entrypoint.sh) checked from the registry. The preset skips the root-only entrypoint and runs Radicale as UID 2999. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Small CalDAV and CardDAV server for your calendars, contacts and task lists.

## Requirements

- One login: the configured username with the user-password secret. Calendar and contact apps sign in with it over the public HTTPS address.
- Each user sees only their own collections. Add more users by baking an htpasswd file into a derivative image.
- Back up the /data volume; every calendar and address book lives there.

## Credentials

- `user-password`: The password calendar and contact apps sign in with. At least 16 characters; rotating it signs every device out.

## Configuration

- `username` (Username): Login name for calendar and contact apps.

## Sources

- https://github.com/tomsquest/docker-radicale/tree/3.9.0.0
- https://radicale.org/v3.html#configuration

Application license: GPL-3.0.
