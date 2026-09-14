# Open WebUI

Deployment preset. AMD64/ARM64 registry manifests checked; runtime acceptance pending

Self-hosted chat and tool workspace using an explicit external model provider.

## Requirements

- Choose a provider, model and provider-key; inference is billed by that provider
- Complete the first administrator account before sharing its URL
- Local Ollama and local embedding downloads are disabled
- Retain upstream branding as required by its license
- Workspace and attachments use persistent storage

## Credentials

- `provider-key`: API key from the selected provider. This must authorize the chosen model; generated random text will not work.
- `session-secret`: Signs sessions and protects persistent authentication material. Keep this stable and include it in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/open-webui/open-webui/blob/v0.11.3/backend/open_webui/env.py
- https://github.com/open-webui/open-webui/blob/v0.11.3/backend/open_webui/config.py

Application license: Open WebUI License (branding clause).
