# Ghost

Deployment preset. Image digests and platforms checked; runtime smoke test pending in CI.

Self-hosted publishing platform with a bundled private MySQL 8.4 database.

## Requirements

- Ghost 5 and later require MySQL 8 in production; this preset bundles a private MySQL 8.4 service with its own volume.
- Mail is not configured by default. Set Ghost mail environment variables before relying on member sign-in links, invitations or newsletters.
- Set the site address to the canonical HTTPS domain before first use; Ghost builds absolute links from it.
- Persistent storage for content and the database; one replica; configure backups.

## Credentials

Generated secret references: database-password, database-root-password.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://docs.ghost.org/install/docker

Application license: MIT.
