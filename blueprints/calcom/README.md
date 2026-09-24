# Cal.com

Native Cal.com deployment with PostgreSQL and a tested non-root compatibility
image. The candidate supplies DATABASE_URL and DATABASE_DIRECT_URL from the
same generated database-password, a stable session-secret and a 32-character
hexadecimal encryption-key. No credentials are stored in TOML.

## Current release prerequisite

The wrapper was built from public source and passed the non-root URL replacement
check in [workflow 36007368796](https://github.com/hakopod/templates/actions/runs/36007368796).
Its immutable image is
`ghcr.io/hakopod/catalog-calcom:v5.9.1-hakopod.1@sha256:2b7212a649d609d59b9f7cfd6f1509d46f8b122c7dc7ed8179370cdada279ead`.
Hakopod organization policy currently disables public package visibility, so
anonymous pulls fail. The catalog keeps `candidate.toml` disabled until the image
is publicly retrievable. No private registry token is shipped with the catalog.

## Runtime and setup

The public wrapper makes the static URL replacement targets writable by UID/GID
1000 at image build time. Runtime uses no root, host socket or added capabilities.
Startup stops on a failed Prisma migration or app-store seed. The wrapper removes
shell tracing and never prints supplied database or application secrets.

A stable HTTPS origin is required. The public origin is substituted at startup;
DNS/TLS must point to the application's main service. Set up the initial account
before sharing. Configure upstream SMTP/calendar-provider credentials for email
and calendar integrations. The preset is AMD64-only because the upstream image
has no ARM64 manifest. PostgreSQL metadata persists and must be backed up together
with the encryption/signing secrets. This is a new-install preset; existing data
requires the upstream upgrade procedure.

## Evidence

Registry/image configuration and non-root static rewriting are verified. Full
application startup against PostgreSQL, scheduling/provider integration and
actual email delivery are separate acceptance checks. The engine's dedicated
catalog workflow covers startup after public image access is resolved.

## Sources

- https://dokploy.com/templates/calcom
- https://github.com/calcom/cal.com/blob/v5.9.1/Dockerfile
- https://github.com/calcom/cal.com/blob/v5.9.1/scripts/start.sh
- https://github.com/calcom/cal.com/blob/v5.9.1/scripts/replace-placeholder.sh
- ../../images/calcom/README.md
