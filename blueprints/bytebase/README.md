# Bytebase

Database change management with a private PostgreSQL metadata database.

## Deployment

Native schema-v1 preset for a new installation. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

- New installation with PostgreSQL metadata and persistent Bytebase data
- Complete administrator setup before sharing; existing installations require upstream upgrade review
- Replaces the unavailable 3.3.0 image candidate with verified multi-architecture 3.22.1 manifests.
- PG_URL is assembled from the same scoped password used by the database. No duplicate URL credential or embedded database is used. Back up both metadata and /var/opt/bytebase.

## Secrets and storage

`database-password` are application-scoped secret references. Generate or save them before deployment. Database connection bindings reuse those same saved passwords.

Persistent services use one replica; scaling replicas does not create a database cluster. The storage option applies to each claim. New installations only: an image/template update is not an automatic database-major-version migration.

## Verification

Reviewed on 24 September 2026. Image manifests and container configuration were inspected remotely without executing workloads. Runtime startup, application-specific workflows and backup restoration are not yet verified unless later evidence is recorded here.

## Sources

- https://dokploy.com/templates/bytebase
- https://github.com/bytebase/bytebase/blob/3.22.1/scripts/Dockerfile
- https://www.bytebase.com/docs/get-started/self-host/
- https://www.bytebase.com/docs/how-to/manage-workspace/external-postgres/
