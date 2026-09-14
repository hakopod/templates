# Flowise

Deployment preset. AMD64/ARM64 registry manifests checked; runtime acceptance pending

Self-hosted visual agent and workflow builder with selectable model nodes.

## Requirements

- Create the first administrator, then select provider/model nodes and save their credentials in Flowise
- Create or import an agent flow and protect its prediction API with an API key
- No model weights or ready-made autonomous flow are installed
- Persist SQLite, uploaded files and credential encryption keys together
- Tool execution uses this service's restricted container
- After deployment, open Custom domains, verify the site URL hostname, and apply routing and TLS before using login or callbacks

## Credentials

- `credential-encryption-key`: Encrypts saved model and tool credentials. Keep this stable and include it in protected backups.
- `session-secret`: Signs browser sessions. Keep this stable and include it in protected backups.
- `token-hash-secret`: Protects token hashes. Keep this stable and include it in protected backups.
- `token-refresh-secret`: Signs refresh tokens. Keep this stable and include it in protected backups.
- `token-signing-secret`: Signs access tokens. Keep this stable and include it in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/FlowiseAI/Flowise/blob/flowise%403.1.4/docker/.env.example

Application license: Apache-2.0 core; enterprise extensions have separate terms.
