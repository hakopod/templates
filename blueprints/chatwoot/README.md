# Chatwoot

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Open-source customer engagement platform that provides a shared inbox for teams, live chat, and omnichannel support.

## Requirements

- Non-root startup, writable paths and dependency readiness require runtime acceptance before enabling this preset
- Provision ReadWriteMany storage for shared volume chatwoot-storage.
- Provision ReadWriteMany storage for shared volume chatwoot-storage.
- Provision ReadWriteMany storage for shared volume chatwoot-storage.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `redis-password`: Value for REDIS_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `redis-url`: Value for REDIS_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `secret-key-base`: Value for SECRET_KEY_BASE. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/chatwoot/chatwoot
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/chatwoot

Application license: Review upstream license and edition.
