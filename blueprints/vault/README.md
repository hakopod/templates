# Vault

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Vault is a tool for securely accessing secrets. A secret is anything that you want to tightly control access to, such as API keys, passwords, certificates, and more. Vault provides a unified interface to any secret, while providing tight access control and recording a detailed audit log. To sign in: In the Vault UI, select 'Token' as the authentication method (not GitHub), then enter the root token from the VAULT_DEV_ROOT_TOKEN_ID environment variable (auto-generated).

## Requirements

- The upstream blueprint runs Vault in development mode with an in-memory root token. Replace it with persistent storage, TLS, and an operator-owned init/unseal procedure; do not use it as production Vault.
- vault: command interpolation needs an explicit environment-aware startup adapter
- vault: review Compose cap_add=['IPC_LOCK']; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `vault-dev-root-token-id`: Value for VAULT_DEV_ROOT_TOKEN_ID. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/hashicorp/vault
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/vault

Application license: Review upstream license and edition.
