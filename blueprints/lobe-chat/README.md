# Lobe Chat

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Lobe Chat - an open-source, modern-design AI chat framework.

## Requirements

- Uses the client-storage Lobe Chat variant. Chat data lives in users’ browsers; this is not the server-database edition.
- OpenAI provider credentials and a unique access code replace upstream sample credentials.

## Credentials

- `access-code`: At least 16 characters. Keep stable and include in protected backups.
- `provider-key`: Supply a real upstream credential with only the permissions this service needs.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/lobehub/lobe-chat
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/lobe-chat

Application license: Review upstream license and edition.
