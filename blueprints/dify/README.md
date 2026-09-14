# Dify

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Dify is an open-source LLM app development platform. Build AI workflows, RAG pipelines, agents and chatbots with a visual interface and publish them as APIs or web apps.

## Requirements

- nginx: mounted host/config asset ../files/dify-nginx.conf at /etc/nginx/conf.d/default.conf needs a supported image/config adapter
- init-permissions: one-shot job must finish before dependent services start
- api: requires a successful one-shot initialization job; ordinary services restart continuously
- worker: requires a successful one-shot initialization job; ordinary services restart continuously
- redis: command interpolation needs an explicit environment-aware startup adapter
- ssrf-proxy: mounted host/config asset ../files/dify-squid.conf at /etc/squid/squid.conf needs a supported image/config adapter
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable
- Provision ReadWriteMany storage for shared volume dify-app-storage.
- Provision ReadWriteMany storage for shared volume dify-app-storage.
- Provision ReadWriteMany storage for shared volume dify-app-storage.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `api-key`: Value for API_KEY. Use the upstream required format; keep stable and back up securely.
- `celery-broker-url`: Value for CELERY_BROKER_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `code-execution-api-key`: Value for CODE_EXECUTION_API_KEY. Use the upstream required format; keep stable and back up securely.
- `db-password`: Value for DB_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `dify-inner-api-key`: Value for DIFY_INNER_API_KEY. Use the upstream required format; keep stable and back up securely.
- `inner-api-key-for-plugin`: Value for INNER_API_KEY_FOR_PLUGIN. Use the upstream required format; keep stable and back up securely.
- `pgvector-password`: Value for PGVECTOR_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `redis-password`: Value for REDIS_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `rediscli-auth`: Value for REDISCLI_AUTH. Use the upstream required format; keep stable and back up securely.
- `secret-key`: Value for SECRET_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `base64`: Value for base64. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/langgenius/dify
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/dify

Application license: Review upstream license and edition.
