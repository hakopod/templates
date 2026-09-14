# LiteLLM

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

LiteLLM is a lightweight OpenAI API-compatible proxy for managing multiple LLM providers with a single endpoint.

## Requirements

- litellm: upstream requests root; adapt initialization to Hakopod non-root containers

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `anthropic-api-key`: Value for ANTHROPIC_API_KEY. Use the upstream required format; keep stable and back up securely.
- `azure-api-key`: Value for AZURE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `cohere-api-key`: Value for COHERE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `infinity-api-key`: Value for INFINITY_API_KEY. Use the upstream required format; keep stable and back up securely.
- `infisical-token`: Value for INFISICAL_TOKEN. Use the upstream required format; keep stable and back up securely.
- `novita-api-key`: Value for NOVITA_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `or-api-key`: Value for OR_API_KEY. Use the upstream required format; keep stable and back up securely.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `replicate-api-key`: Value for REPLICATE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `replicate-api-token`: Value for REPLICATE_API_TOKEN. Use the upstream required format; keep stable and back up securely.
- `ui-password`: Value for UI_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `password`: Value for password. Enter ordinary configuration here; credentials belong in scoped secrets.
- `username`: Value for username. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/BerriAI/litellm
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/litellm

Application license: Review upstream license and edition.
