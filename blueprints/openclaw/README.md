# Openclaw

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

WhatsApp gateway CLI with Pi RPC agent - self-hosted AI-powered messaging platform

## Requirements

- browser: review Compose shm_size=2g; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `ai-gateway-api-key`: Value for AI_GATEWAY_API_KEY. Use the upstream required format; keep stable and back up securely.
- `anthropic-api-key`: Value for ANTHROPIC_API_KEY. Use the upstream required format; keep stable and back up securely.
- `auth-password`: Value for AUTH_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `aws-access-key-id`: Value for AWS_ACCESS_KEY_ID. Use the upstream required format; keep stable and back up securely.
- `aws-secret-access-key`: Value for AWS_SECRET_ACCESS_KEY. Use the upstream required format; keep stable and back up securely.
- `aws-session-token`: Value for AWS_SESSION_TOKEN. Use the upstream required format; keep stable and back up securely.
- `cerebras-api-key`: Value for CEREBRAS_API_KEY. Use the upstream required format; keep stable and back up securely.
- `copilot-github-token`: Value for COPILOT_GITHUB_TOKEN. Use the upstream required format; keep stable and back up securely.
- `deepgram-api-key`: Value for DEEPGRAM_API_KEY. Use the upstream required format; keep stable and back up securely.
- `discord-bot-token`: Value for DISCORD_BOT_TOKEN. Use the upstream required format; keep stable and back up securely.
- `gemini-api-key`: Value for GEMINI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `groq-api-key`: Value for GROQ_API_KEY. Use the upstream required format; keep stable and back up securely.
- `kimi-api-key`: Value for KIMI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `minimax-api-key`: Value for MINIMAX_API_KEY. Use the upstream required format; keep stable and back up securely.
- `mistral-api-key`: Value for MISTRAL_API_KEY. Use the upstream required format; keep stable and back up securely.
- `moonshot-api-key`: Value for MOONSHOT_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openclaw-gateway-token`: Value for OPENCLAW_GATEWAY_TOKEN. Use the upstream required format; keep stable and back up securely.
- `opencode-api-key`: Value for OPENCODE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openrouter-api-key`: Value for OPENROUTER_API_KEY. Use the upstream required format; keep stable and back up securely.
- `slack-app-token`: Value for SLACK_APP_TOKEN. Use the upstream required format; keep stable and back up securely.
- `slack-bot-token`: Value for SLACK_BOT_TOKEN. Use the upstream required format; keep stable and back up securely.
- `synthetic-api-key`: Value for SYNTHETIC_API_KEY. Use the upstream required format; keep stable and back up securely.
- `telegram-bot-token`: Value for TELEGRAM_BOT_TOKEN. Use the upstream required format; keep stable and back up securely.
- `venice-api-key`: Value for VENICE_API_KEY. Use the upstream required format; keep stable and back up securely.
- `xai-api-key`: Value for XAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `xiaomi-api-key`: Value for XIAOMI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `zai-api-key`: Value for ZAI_API_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `openclaw-primary-model`: Value for OPENCLAW_PRIMARY_MODEL. Enter ordinary configuration here; credentials belong in scoped secrets.
- `ollama-base-url`: Value for OLLAMA_BASE_URL. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/openclaw/openclaw
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/openclaw

Application license: Review upstream license and edition.
