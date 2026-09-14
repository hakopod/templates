# n8n + Worker + Runner with Redis/Postgres and Ollama

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

n8n is an open source low-code platform for automating workflows and integrations with PostgreSQL database and Ollama AI model.

## Requirements

- Non-root startup, writable paths and dependency readiness require runtime acceptance before enabling this preset
- Provision ReadWriteMany storage for shared volume ollama-storage.
- Provision ReadWriteMany storage for shared volume ollama-storage.
- Provision ReadWriteMany storage for shared volume ollama-storage.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `db-postgresdb-password`: Value for DB_POSTGRESDB_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `n8n-encryption-key`: Value for N8N_ENCRYPTION_KEY. Use the upstream required format; keep stable and back up securely.
- `n8n-runners-auth-token`: Value for N8N_RUNNERS_AUTH_TOKEN. Use the upstream required format; keep stable and back up securely.
- `n8n-user-management-jwt-secret`: Value for N8N_USER_MANAGEMENT_JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `username`: Value for username. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/n8n-io/n8n
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/n8n-runner-postgres-ollama

Application license: Review upstream license and edition.
