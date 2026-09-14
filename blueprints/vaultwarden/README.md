# Vaultwarden

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Unofficial Bitwarden compatible server written in Rust, formerly known as bitwarden_rs

## Requirements

- Public signups are disabled. Use /admin with the configured token to invite users.
- Configure SMTP in Vaultwarden if email invitations are needed. Back up its database and attachments.
- After deployment, verify the canonical domain and configure HTTPS before using login or callbacks.

## Credentials

- `admin-token`: Random signing/encryption material, at least 32 characters. Keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/dani-garcia/vaultwarden
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/vaultwarden

Application license: Review upstream license and edition.
