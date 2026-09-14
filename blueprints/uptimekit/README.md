# Uptimekit

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

The modern open-source status page and monitoring solution.

## Requirements

- clickhouse: upstream requests root; adapt initialization to Hakopod non-root containers

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `clickhouse-password`: Value for CLICKHOUSE_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `redis-url`: Value for REDIS_URL. Supply the complete connection URL with matching database credentials and private service DNS.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/uptimekit/uptimekit
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/uptimekit

Application license: Review upstream license and edition.
