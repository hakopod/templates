# bolt.diy

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Prompt, run, edit, and deploy full-stack web applications using any LLM you want!

## Requirements

- app: review Compose extra_hosts=['host.docker.internal:host-gateway']; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `anthropic-api-key`: Value for ANTHROPIC_API_KEY. Use the upstream required format; keep stable and back up securely.
- `google-generative-ai-api-key`: Value for GOOGLE_GENERATIVE_AI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `groq-api-key`: Value for GROQ_API_KEY. Use the upstream required format; keep stable and back up securely.
- `huggingface-api-key`: Value for HuggingFace_API_KEY. Use the upstream required format; keep stable and back up securely.
- `open-router-api-key`: Value for OPEN_ROUTER_API_KEY. Use the upstream required format; keep stable and back up securely.
- `openai-api-key`: Value for OPENAI_API_KEY. Use the upstream required format; keep stable and back up securely.
- `together-api-key`: Value for TOGETHER_API_KEY. Use the upstream required format; keep stable and back up securely.
- `xai-api-key`: Value for XAI_API_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/stackblitz-labs/bolt.diy
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/bolt.diy

Application license: Review upstream license and edition.
