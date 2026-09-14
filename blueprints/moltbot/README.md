# Moltbot

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

WhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

## Requirements

- moltbot-gateway: immutable image/architecture verification remains incomplete for ghcr.io/moltbot/clawdbot:2026.1.24-1

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `clawdbot-gateway-token`: Value for CLAWDBOT_GATEWAY_TOKEN. Use the upstream required format; keep stable and back up securely.
- `openrouter-api-key`: Value for OPENROUTER_API_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `claude-ai-session-key`: Value for CLAUDE_AI_SESSION_KEY. Enter ordinary configuration here; credentials belong in scoped secrets.
- `claude-web-session-key`: Value for CLAUDE_WEB_SESSION_KEY. Enter ordinary configuration here; credentials belong in scoped secrets.
- `claude-web-cookie`: Value for CLAUDE_WEB_COOKIE. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/moltbot/moltbot
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/moltbot

Application license: Review upstream license and edition.
