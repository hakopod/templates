# Glitchtip

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Glitchtip is simple, open source error tracking

## Requirements

- Non-root startup, writable paths and dependency readiness require runtime acceptance before enabling this preset
- Provision ReadWriteMany storage for shared volume uploads.
- Provision ReadWriteMany storage for shared volume uploads.
- Provision ReadWriteMany storage for shared volume uploads.

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `secret-key`: Value for SECRET_KEY. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `email`: Value for email. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://gitlab.com/glitchtip/
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/glitchtip

Application license: Review upstream license and edition.
