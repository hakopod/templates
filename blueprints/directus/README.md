# Directus

Deployment preset. Image digests and platforms checked; runtime smoke test pending in CI.

Headless CMS and data platform using SQLite on persistent volumes.

## Requirements

- Uses SQLite on a persistent volume by default. SQLite suits small sites; move to PostgreSQL before heavy write load or multiple replicas.
- Back up both the database volume and the uploads volume together.
- Set the site address to the canonical HTTPS domain; Directus uses it for links and cookies.
- Mail is not configured by default; password reset and invitations need an email transport.

## Credentials

Generated secret references: admin-password, secret.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://docs.directus.io/self-hosted/docker-guide.html

Application license: BUSL-1.1 (free for organisations under the upstream revenue threshold; review the license).
