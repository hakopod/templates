# Stack Auth

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Open-source Auth0/Clerk alternative. Stack Auth is a free and open source authentication tool that allows you to authenticate your users.

## Requirements

- stack-auth: upstream declares multiple public ports; map HTTP endpoints explicitly without treating private protocols as HTTP

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `stack-database-connection-string`: Supply the upstream-required credential for this reference; see migration requirements.
- `stack-direct-database-connection-string`: Supply the upstream-required credential for this reference; see migration requirements.
- `stack-server-secret`: Value for STACK_SERVER_SECRET. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

- `password`: Value for password. Enter ordinary configuration here; credentials belong in scoped secrets.
- `stack-email-host`: Value for STACK_EMAIL_HOST. Enter ordinary configuration here; credentials belong in scoped secrets.

## Sources

- https://github.com/stack-auth/stack-auth
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/stack-auth

Application license: Review upstream license and edition.
