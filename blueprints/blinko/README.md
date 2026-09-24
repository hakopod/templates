# Blinko

Private notes and AI workspace with PostgreSQL and persistent uploaded files.

## Deployment

Native schema-v1 preset for a new installation. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

- Stable HTTPS origin; one application replica
- Back up PostgreSQL and /app/.blinko together; configure AI providers inside Blinko
- Database migrations and seed setup complete before the server starts; failures stop startup.
- The .blinko volume retains attachments, vectors and local database dump files. It does not replace independent backups. Complete the first account setup before sharing the URL.

Temporary export archives use a bounded 128 MiB `/app/backup` directory; downloads there do not survive a restart. Persistent attachments and vectors remain in `/app/.blinko`.

## Secrets and storage

`database-password`, `session-secret` are application-scoped secret references. Generate or save them before deployment. Database connection bindings reuse those same saved passwords.

Persistent services use one replica; scaling replicas does not create a database cluster. The storage option applies to each claim. New installations only: an image/template update is not an automatic database-major-version migration.

## Verification

Reviewed on 24 September 2026. Image manifests and container configuration were inspected remotely without executing workloads. Runtime startup, application-specific workflows and backup restoration are not yet verified unless later evidence is recorded here.

## Sources

- https://dokploy.com/templates/blinko
- https://github.com/blinkospace/blinko/blob/1.6.3/dockerfile
- https://github.com/blinkospace/blinko/blob/1.6.3/shared/lib/pathConstant.ts
