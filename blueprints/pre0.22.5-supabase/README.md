# SupaBase

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

The open source Firebase alternative. Supabase gives you a dedicated Postgres database to build your web, mobile, and AI applications. This is for dokploy version < 0.22.5.

## Requirements

- This is a historical Supabase stack for older Dokploy. Review an upstream-supported release set before migration; SQL bootstrap, gateway config and storage adapters remain required.
- kong: mounted host/config asset ../files/volumes/api/kong.yml at /home/kong/temp.yml needs a supported image/config adapter
- storage: mounted host/config asset ../files/volumes/storage at /var/lib/storage needs a supported image/config adapter
- imgproxy: mounted host/config asset ../files/volumes/storage at /var/lib/storage needs a supported image/config adapter
- functions: mounted host/config asset ../files/volumes/functions at /home/deno/functions needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/realtime.sql at /docker-entrypoint-initdb.d/migrations/99-realtime.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/webhooks.sql at /docker-entrypoint-initdb.d/init-scripts/98-webhooks.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/roles.sql at /docker-entrypoint-initdb.d/init-scripts/99-roles.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/jwt.sql at /docker-entrypoint-initdb.d/init-scripts/99-jwt.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/data at /var/lib/postgresql/data needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/_supabase.sql at /docker-entrypoint-initdb.d/migrations/97-_supabase.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/logs.sql at /docker-entrypoint-initdb.d/migrations/99-logs.sql needs a supported image/config adapter
- db: mounted host/config asset ../files/volumes/db/pooler.sql at /docker-entrypoint-initdb.d/migrations/99-pooler.sql needs a supported image/config adapter
- db: mount /etc/postgresql-custom is outside allowed application volume paths
- vector: mounted host/config asset ../files/volumes/logs/vector.yml at /etc/vector/vector.yml needs a supported image/config adapter
- vector: mounted host/config asset ${DOCKER_SOCKET_LOCATION} at /var/run/docker.sock needs a supported image/config adapter
- supavisor: mounted host/config asset ../files/volumes/pooler/pooler.exs at /etc/pooler/pooler.exs needs a supported image/config adapter
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `api-jwt-secret`: Value for API_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `auth-jwt-secret`: Value for AUTH_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `dashboard-password`: Value for DASHBOARD_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `db-password`: Value for DB_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `gotrue-db-database-url`: Value for GOTRUE_DB_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `gotrue-jwt-secret`: Value for GOTRUE_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `jwt-secret`: Value for JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `logflare-api-key`: Value for LOGFLARE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `metrics-jwt-secret`: Value for METRICS_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `pg-meta-db-password`: Value for PG_META_DB_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `pgpassword`: Value for PGPASSWORD. Use the upstream required format; keep stable and back up securely.
- `pgrst-app-settings-jwt-secret`: Value for PGRST_APP_SETTINGS_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `pgrst-db-uri`: Value for PGRST_DB_URI. Supply the complete connection URL with matching database credentials and private service DNS.
- `pgrst-jwt-secret`: Value for PGRST_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `postgres-backend-url`: Value for POSTGRES_BACKEND_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `secret-key-base`: Value for SECRET_KEY_BASE. Use the upstream required format; keep stable and back up securely.
- `supabase-db-url`: Value for SUPABASE_DB_URL. Supply the complete connection URL with matching database credentials and private service DNS.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/supabase/supabase
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/pre0.22.5-supabase

Application license: Review upstream license and edition.
