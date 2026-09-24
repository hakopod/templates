# CouchDB

Private authenticated CouchDB with single-node initialization and persistent documents.

## Deployment

Native schema-v1 preset for a new installation. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

- Single-node database; one replica with persistent storage
- Private HTTP 5984; use a scoped application credential for database clients
- The admin account is configured from database-password; session-secret keeps cookie authentication stable across restarts.
- The single_node setting initializes system databases. Cluster distribution ports are not exposed. Runtime settings should be declared in versioned configuration; only database files persist.

## Secrets and storage

`database-password`, `session-secret` are application-scoped secret references. Generate or save them before deployment. Database connection bindings reuse those same saved passwords.

Persistent services use one replica; scaling replicas does not create a database cluster. The storage option applies to each claim. New installations only: an image/template update is not an automatic database-major-version migration.

## Verification

Reviewed on 24 September 2026. Image manifests and container configuration were inspected remotely without executing workloads. Runtime startup, application-specific workflows and backup restoration are not yet verified unless later evidence is recorded here.

## Sources

- https://dokploy.com/templates/couchdb
- https://docs.couchdb.org/en/stable/setup/single-node.html
- https://github.com/apache/couchdb-docker/blob/main/3.5.1/docker-entrypoint.sh
