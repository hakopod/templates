# Huly

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Huly â€” All-in-One Project Management Platform (alternative to Linear, Jira, Slack, Notion, Motion)

## Requirements

- nginx: immutable image/architecture verification remains incomplete for nginx:1.21.3
- nginx: mounted host/config asset ../files/volumes/nginx/.huly.nginx at /etc/nginx/conf.d/default.conf needs a supported image/config adapter
- minio: immutable image/architecture verification remains incomplete for minio/minio:RELEASE.2024-11-07T00-52-20Z
- elastic: immutable image/architecture verification remains incomplete for elasticsearch:7.14.2
- rekoni: immutable image/architecture verification remains incomplete for hardcoreeng/rekoni-service:${HULY_VERSION}
- rekoni: choose and pin a compatible release image
- transactor: immutable image/architecture verification remains incomplete for hardcoreeng/transactor:${HULY_VERSION}
- transactor: choose and pin a compatible release image
- collaborator: immutable image/architecture verification remains incomplete for hardcoreeng/collaborator:${HULY_VERSION}
- collaborator: choose and pin a compatible release image
- account: immutable image/architecture verification remains incomplete for hardcoreeng/account:${HULY_VERSION}
- account: choose and pin a compatible release image
- workspace: immutable image/architecture verification remains incomplete for hardcoreeng/workspace:${HULY_VERSION}
- workspace: choose and pin a compatible release image
- front: immutable image/architecture verification remains incomplete for hardcoreeng/front:${HULY_VERSION}
- front: choose and pin a compatible release image
- fulltext: immutable image/architecture verification remains incomplete for hardcoreeng/fulltext:${HULY_VERSION}
- fulltext: choose and pin a compatible release image
- stats: immutable image/architecture verification remains incomplete for hardcoreeng/stats:${HULY_VERSION}
- stats: choose and pin a compatible release image
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `secret`: Value for SECRET. Use the upstream required format; keep stable and back up securely.
- `server-secret`: Value for SERVER_SECRET. Use the upstream required format; keep stable and back up securely.
- `storage-config`: Value for STORAGE_CONFIG. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/hcengineering/huly-selfhost
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/huly

Application license: Review upstream license and edition.
