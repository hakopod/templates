# Langflow

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Langflow is a low-code app builder for RAG and multi-agent AI applications. It's Python-based and agnostic to any model, API, or database. 

## Requirements

- langflow: upstream requests root; adapt initialization to Hakopod non-root containers

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `langflow-database-url`: Value for LANGFLOW_DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `langflow-secret-key`: Value for LANGFLOW_SECRET_KEY. Use the upstream required format; keep stable and back up securely.
- `langflow-superuser-password`: Value for LANGFLOW_SUPERUSER_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/langflow-ai/langflow/tree/main
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/langflow

Application license: Review upstream license and edition.
