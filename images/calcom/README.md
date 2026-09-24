# Cal.com non-root compatibility image

This small public wrapper uses the digest-pinned official Cal.com v5.9.1 image.
The upstream startup script replaces the public URL inside the built Next.js
files. The wrapper makes only those targets writable by UID/GID 1000 at image
build time. Runtime has no root, added capabilities or host mounts.

The replacement entrypoint fails on migration or app-store seed errors and does
not trace environment variables. PostgreSQL and both connection bindings must be
ready before startup. No customer values or private source enter this build.

`catalog-images.yml` builds and checks the wrapper on an AMD64 GitHub runner,
then publishes `ghcr.io/hakopod/catalog-calcom:v5.9.1-hakopod.1`. Resolve and pin its
resulting digest in the catalog only after publication. The workflow's permission
check is not full application startup acceptance; the engine's named development
cluster test covers the real database and server startup.

Upstream image/source licensing applies, including Cal.com AGPL obligations and
separate commercial features. Sources:

- https://github.com/calcom/cal.com/blob/v5.9.1/Dockerfile
- https://github.com/calcom/cal.com/blob/v5.9.1/scripts/start.sh
- https://github.com/calcom/cal.com/blob/v5.9.1/scripts/replace-placeholder.sh
