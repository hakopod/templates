# Excalidraw

Virtual whiteboard for sketching hand-drawn style diagrams, served as a static web app.

## Deployment prerequisites

`candidate.toml` records the intended topology but is intentionally excluded from deployment.

- The official image runs nginx as root on port 80 and fails as a non-root user, so Hakopod builds a wrapper from images/excalidraw/Dockerfile: the upstream static site on nginxinc/nginx-unprivileged (UID 101, port 8080).
- The preset becomes deployable once the wrapper image ghcr.io/hakopod/catalog-excalidraw:20260506-hakopod.1 is published and its digest replaces PENDING_PUBLISH in the candidate.
- Upstream publishes only a rolling latest tag; the wrapper is labelled by the Docker Hub push date of the pinned digest (2026-05-06), not a release version. Real-time collaboration needs a separate excalidraw-room service and is not included.

## Secrets and storage

No secrets and no persistent storage; the app is stateless. The root filesystem is read-only with a /tmp scratch volume for nginx.

## Verification

Image digests and amd64/arm64 platforms checked. Official image failed locally as UID 101 (permission denied on /var/cache/nginx). The wrapper is untested: the catalog-images.yml workflow builds both platforms and smoke-tests them (UID 101, no capabilities, read-only root with /tmp tmpfs, / returns 200 with a content marker) in GitHub Actions, and that run has not happened yet.

## Sources

- https://github.com/excalidraw/excalidraw#quick-start
- https://github.com/excalidraw/excalidraw/blob/master/Dockerfile
- images/excalidraw/Dockerfile

Application license: MIT.
