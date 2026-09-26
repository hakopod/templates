# GlitchTip

Deployment preset. Configuration mirrors a running deployment of this all-in-one layout. Not yet exercised by runtime acceptance in this repository.

Open source error tracking, compatible with Sentry clients.

## Layout

One GlitchTip service in its all-in-one role, which runs the web interface,
applies migrations and drains the background queue in a single process tree,
alongside a bundled PostgreSQL and a bundled Valkey.

The upstream compose layout splits that into separate migrate, web and worker
services sharing an uploads volume, which requires ReadWriteMany storage. That
was why the earlier candidate could not be enabled. One service needs only
ReadWriteOnce.

## Requirements

- One all-in-one service runs the web interface, migrations and the worker
- Bundled PostgreSQL and Valkey; persistent storage for the database and uploads
- A site host or custom domain must match GLITCHTIP_DOMAIN for links and origin checks
- Console mail by default; supply an SMTP URL before relying on notifications

## Credentials

- `database-url`: Value for DATABASE_URL. Supply the complete connection URL with matching database credentials and private service DNS.
- `secret-key`: Value for SECRET_KEY. Use the upstream required format; keep stable and back up securely.

Rotating the signing key invalidates existing sessions and password reset links.

## Ordinary configuration

Use the catalog options described in the root README. `email` sets the address
invitations and alerts are sent from.

Two optional features are on by default. `GLITCHTIP_ENABLE_DUCKDB` powers the
analytics views. `GLITCHTIP_ENABLE_MCP` exposes a Model Context Protocol
endpoint for reading issues, which is worth reviewing before it sits on a public
host. Either can be set to `False`.

Mail goes to the log until `EMAIL_URL` is changed to a real SMTP URL.

## Sources

- https://gitlab.com/glitchtip/
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/glitchtip
