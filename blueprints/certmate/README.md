# CertMate

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

CertMate is an SSL certificate management system with a web UI and REST API. It automates issuing and renewing Let's Encrypt certificates via DNS-01 challenges across 20+ DNS providers, with unified backups and multi-account support.

## Requirements

- Non-root startup, writable paths and dependency readiness require runtime acceptance before enabling this preset

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `api-bearer-token`: Value for API_BEARER_TOKEN. Use the upstream required format; keep stable and back up securely.
- `cloudflare-token`: Value for CLOUDFLARE_TOKEN. Use the upstream required format; keep stable and back up securely.
- `secret-key`: Value for SECRET_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/fabriziosalmi/certmate
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/certmate

Application license: Review upstream license and edition.
