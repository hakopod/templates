# Inngest

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Inngest is a developer platform for serverless event-driven workflows. Build reliable, scalable background functions and workflows with built-in retries, scheduling, and observability.

## Requirements

- inngest: command interpolation needs an explicit environment-aware startup adapter
- redis: review Compose sysctls=['net.core.somaxconn=1024']; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `inngest-postgres-uri`: Supply the upstream-required credential for this reference; see migration requirements.
- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `jwt`: Value for jwt. Enter ordinary configuration here; credentials belong in scoped secrets.
- `password`: Value for password. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/inngest/inngest
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/inngest

Application license: Review upstream license and edition.
