# FreshRSS

Deployment preset. Image digest and amd64/arm64 platforms checked; local container started as UID 1000 on arm64 and /i/ returned 200.

Self-hosted RSS feed reader using SQLite on a persistent volume.

## Requirements

- Persistent block or local storage for /var/www/FreshRSS/data (SQLite databases, user settings and feed cache)
- Complete the installer at /i/ before sharing the URL; choose SQLite when asked for a database
- The upstream image expects to run as root. This preset starts Apache as UID 1000 on port 8080 with a private copy of its configuration under /tmp, and skips the image entrypoint
- The built-in cron job needs root, so CRON_MIN is not available. Refresh feeds from the web interface, the API, or an external scheduler calling app/actualize_script.php

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/FreshRSS/FreshRSS/blob/edge/Docker/README.md
- https://github.com/FreshRSS/FreshRSS/blob/edge/Docker/entrypoint.sh

Application license: AGPL-3.0.
