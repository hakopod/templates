# Zipline

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

A ShareX/file upload server that is easy to use, packed with features, and with an easy setup!

## Requirements

- zipline: mounted host/config asset ../files/uploads at /zipline/uploads needs a supported image/config adapter
- zipline: mounted host/config asset ../files/public at /zipline/public needs a supported image/config adapter

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `core-secret`: Value for CORE_SECRET. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/diced/zipline
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/zipline

Application license: Review upstream license and edition.
