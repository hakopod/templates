# Bytebase

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Bytebase is a database management tool that allows you to manage your databases with ease. It provides a simple and effective solution for managing your databases from anywhere.

## Requirements

- bytebase: immutable image/architecture verification remains incomplete for bytebase/bytebase:3.3.0

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `pg-url`: Value for PG_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/bytebase/bytebase
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/bytebase

Application license: Review upstream license and edition.
