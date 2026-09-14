# Hoppscotch (AIO + Migrations)

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Hoppscotch Community Edition (All-in-One) with automatic database migrations. Includes backend, frontend, and admin under unified subpath routing.

## Requirements

- hoppscotch: requires a successful one-shot initialization job; ordinary services restart continuously
- migrate: one-shot job must finish before dependent services start

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `data-encryption-key`: Value for DATA_ENCRYPTION_KEY. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/hoppscotch/hoppscotch
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/hoppscotch

Application license: Review upstream license and edition.
