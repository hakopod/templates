# PostHog

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

PostHog is an open-source product analytics platform with feature flags, session replay, surveys, A/B testing and a customer data pipeline, all in one tool.

## Requirements

- init-assets: command interpolation needs an explicit environment-aware startup adapter
- db: mounted host/config asset ../files/db-init at /docker-entrypoint-initdb.d needs a supported image/config adapter
- zookeeper: immutable image/architecture verification remains incomplete for zookeeper:3.7.0
- clickhouse: requires a successful one-shot initialization job; ordinary services restart continuously
- web: immutable image/architecture verification remains incomplete for posthog/posthog:${POSTHOG_VERSION}
- web: choose and pin a compatible release image
- web: requires a successful one-shot initialization job; ordinary services restart continuously
- worker: immutable image/architecture verification remains incomplete for posthog/posthog:${POSTHOG_VERSION}
- worker: choose and pin a compatible release image
- plugins: immutable image/architecture verification remains incomplete for posthog/posthog-node:${POSTHOG_NODE_VERSION}
- plugins: choose and pin a compatible release image
- plugins: requires a successful one-shot initialization job; ordinary services restart continuously
- ingestion-general: immutable image/architecture verification remains incomplete for posthog/posthog-node:${POSTHOG_NODE_VERSION}
- ingestion-general: choose and pin a compatible release image
- ingestion-general: requires a successful one-shot initialization job; ordinary services restart continuously
- ingestion-sessionreplay: immutable image/architecture verification remains incomplete for posthog/posthog-node:${POSTHOG_NODE_VERSION}
- ingestion-sessionreplay: choose and pin a compatible release image
- ingestion-sessionreplay: requires a successful one-shot initialization job; ordinary services restart continuously
- recording-api: immutable image/architecture verification remains incomplete for posthog/posthog-node:${POSTHOG_NODE_VERSION}
- recording-api: choose and pin a compatible release image
- feature-flags: requires a successful one-shot initialization job; ordinary services restart continuously
- livestream: upstream requests root; adapt initialization to Hakopod non-root containers
- livestream: mounted host/config asset ../files/livestream/configs.yml at /configs/configs.yml needs a supported image/config adapter
- objectstorage: immutable image/architecture verification remains incomplete for minio/minio:RELEASE.2025-04-22T22-12-26Z
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable
- Provision ReadWriteMany storage for shared volume posthog-assets.
- Provision ReadWriteMany storage for shared volume geoip-data.
- Provision ReadWriteMany storage for shared volume posthog-assets.
- Provision ReadWriteMany storage for shared volume geoip-data.
- Provision ReadWriteMany storage for shared volume posthog-assets.
- Provision ReadWriteMany storage for shared volume geoip-data.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `behavioral-cohorts-database-url`: Value for BEHAVIORAL_COHORTS_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `clickhouse-api-password`: Value for CLICKHOUSE_API_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `clickhouse-app-password`: Value for CLICKHOUSE_APP_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `cyclotron-database-url`: Value for CYCLOTRON_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `encryption-salt-keys`: Value for ENCRYPTION_SALT_KEYS. Use the upstream required format; keep stable and back up securely.
- `livestream-jwt-secret`: Value for LIVESTREAM_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `minio-root-password`: Value for MINIO_ROOT_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `object-storage-access-key-id`: Value for OBJECT_STORAGE_ACCESS_KEY_ID. Use the upstream required format; keep stable and back up securely.
- `object-storage-secret-access-key`: Value for OBJECT_STORAGE_SECRET_ACCESS_KEY. Use the upstream required format; keep stable and back up securely.
- `persons-database-url`: Value for PERSONS_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `persons-db-reader-url`: Supply the upstream-required credential for this reference; see migration requirements.
- `persons-db-writer-url`: Supply the upstream-required credential for this reference; see migration requirements.
- `persons-read-database-url`: Value for PERSONS_READ_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `persons-write-database-url`: Value for PERSONS_WRITE_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `pgpassword`: Value for PGPASSWORD. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `read-database-url`: Value for READ_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `redis-url`: Value for REDIS_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `secret-key`: Value for SECRET_KEY. Use the upstream required format; keep stable and back up securely.
- `session-recording-v2-s3-access-key-id`: Value for SESSION_RECORDING_V2_S3_ACCESS_KEY_ID. Use the upstream required format; keep stable and back up securely.
- `session-recording-v2-s3-secret-access-ke`: Value for SESSION_RECORDING_V2_S3_SECRET_ACCESS_KEY. Use the upstream required format; keep stable and back up securely.
- `write-database-url`: Value for WRITE_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/PostHog/posthog
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/posthog

Application license: Review upstream license and edition.
