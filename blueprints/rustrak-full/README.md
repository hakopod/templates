# Rustrak (Full Stack)

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Self-hosted error tracking compatible with Sentry SDKs. Full stack: Rust server, web dashboard and PostgreSQL.

## Requirements

- Non-root startup, writable paths and dependency readiness require runtime acceptance before enabling this preset

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `create-superuser`: Value for CREATE_SUPERUSER. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `session-secret-key`: Value for SESSION_SECRET_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/rustrak/rustrak
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/rustrak-full

Application license: Review upstream license and edition.
