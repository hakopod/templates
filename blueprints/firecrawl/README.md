# Firecrawl

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Production-ready, authenticated Firecrawl with persistent queues, browser rendering, a generated API key, and interactive OpenAPI documentation.

## Requirements

- firecrawl-db: immutable image/architecture verification remains incomplete for postgres:17-alpine@sha256:18cfe3ef5e6815560c98237d6216d1e5119702fb0f3894c8785dd58b8bbe5d73
- firecrawl-db: review Compose configs=[{'source': 'db-init-prerequisites', 'target': '/docker-entrypoint-initdb.d/010-prerequisites.sql'}, {'source': 'db-init-schema', 'target': '/docker-entrypoint-initdb.d/020-current-schema.sql'}, {'source': 'db-init-constraints', 'target': '/docker-entrypoint-initdb.d/030-selfhost-constraints.sql'}, {'source': 'db-init-rpcs', 'target': '/docker-entrypoint-initdb.d/040-selfhost-rpcs.sql'}]; no implicit host privileges or configuration mounts
- firecrawl-db-seed: immutable image/architecture verification remains incomplete for postgres:17-alpine@sha256:18cfe3ef5e6815560c98237d6216d1e5119702fb0f3894c8785dd58b8bbe5d73
- firecrawl-db-seed: command interpolation needs an explicit environment-aware startup adapter
- firecrawl-db-seed: review Compose configs=[{'source': 'db-seed', 'target': '/seed.sql'}]; no implicit host privileges or configuration mounts
- firecrawl-db-seed: one-shot job must finish before dependent services start
- redis: immutable image/architecture verification remains incomplete for redis:7-alpine@sha256:ff02b58f971e7d7d156a1267e283fcbbeee91773b6aa36c49dac28ecfe28eadf
- redis: command interpolation needs an explicit environment-aware startup adapter
- rabbitmq: immutable image/architecture verification remains incomplete for rabbitmq:3-management@sha256:e582c0bc7766f3342496d8485efb5a1df782b5ce3886ad017e2eaae442311f69
- firecrawl: requires a successful one-shot initialization job; ordinary services restart continuously
- swagger-ui: immutable image/architecture verification remains incomplete for swaggerapi/swagger-ui:v5.32.14@sha256:3d93169968848d371a6a56ca1ab18b47a8906ba461b8eba0688866354f5431d5
- swagger-ui: review Compose configs=[{'source': 'firecrawl-openapi', 'target': '/tmp/openapi.json.gz.b64'}]; no implicit host privileges or configuration mounts
- gateway: immutable image/architecture verification remains incomplete for nginx:1.29-alpine@sha256:5616878291a2eed594aee8db4dade5878cf7edcb475e59193904b198d9b830de
- gateway: review Compose configs=[{'source': 'firecrawl-gateway-nginx', 'target': '/etc/nginx/conf.d/default.conf'}]; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `database-replica-url`: Value for DATABASE_REPLICA_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `firecrawl-api-key`: Value for FIRECRAWL_API_KEY. Use the upstream required format; keep stable and back up securely.
- `llamaparse-api-key`: Value for LLAMAPARSE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `nuq-database-url`: Value for NUQ_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `nuq-database-url-listen`: Value for NUQ_DATABASE_URL_LISTEN. Supply the complete connection URL with matching database credentials and private service DNS.
- `nuq-rabbitmq-url`: Value for NUQ_RABBITMQ_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openrouter-api-key`: Value for OPENROUTER_API_KEY. Use the upstream required format; keep stable and back up securely.
- `pgpassword`: Value for PGPASSWORD. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `proxy-password`: Value for PROXY_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `rabbitmq-default-pass`: Value for RABBITMQ_DEFAULT_PASS. Use the upstream required format; keep stable and back up securely.
- `redis-password`: Value for REDIS_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `redis-rate-limit-url`: Value for REDIS_RATE_LIMIT_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `redis-url`: Value for REDIS_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `searchapi-api-key`: Value for SEARCHAPI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `self-hosted-webhook-hmac-secret`: Value for SELF_HOSTED_WEBHOOK_HMAC_SECRET. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `uuid`: Value for uuid. Enter ordinary configuration here; credentials belong in scoped secrets.
- `hash`: Value for hash. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/firecrawl/firecrawl
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/firecrawl

Application license: Review upstream license and edition.
