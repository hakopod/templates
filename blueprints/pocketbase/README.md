# PocketBase

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Open Source backend in 1 file

## Requirements

- Uses the third-party adrianmusante container distribution; review that image separately from PocketBase.
- Administrator upsert runs on startup. Changing the secret resets the configured administrator password. Back up persistent data.

## Credentials

- `admin-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

- `admin-email`: Set administrator email before reviewing the deployment.

## Sources

- https://github.com/pocketbase/pocketbase
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/pocketbase

Application license: Review upstream license and edition.
