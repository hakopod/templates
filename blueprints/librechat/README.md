# LibreChat

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

LibreChat is the ultimate open-source app for all your AI conversations, fully customizable and compatible with any AI provider (Openai, Ollama, Google etc.) â€” all in one sleek interface.

## Requirements

- librechat: mounted host/config asset ../files/librechat.yaml at /app/librechat.yaml needs a supported image/config adapter
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable
- Provision ReadWriteMany storage for shared volume librechat-data.
- Provision ReadWriteMany storage for shared volume librechat-data.
- Provision ReadWriteMany storage for shared volume librechat-data.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `anthropic-api-key`: Value for ANTHROPIC_API_KEY. Use the upstream required format; keep stable and back up securely.
- `jwt-refresh-secret`: Value for JWT_REFRESH_SECRET. Use the upstream required format; keep stable and back up securely.
- `jwt-secret`: Value for JWT_SECRET. Use the upstream required format; keep stable and back up securely.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `rag-google-api-key`: Value for RAG_GOOGLE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `rag-openai-api-key`: Value for RAG_OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `password`: Value for password. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/danny-avila/librechat
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/librechat

Application license: Review upstream license and edition.
