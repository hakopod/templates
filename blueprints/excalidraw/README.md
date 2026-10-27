# Excalidraw

Virtual whiteboard for sketching hand-drawn style diagrams, served as a static web app.

## Wrapper image

- The official image runs nginx as root on port 80 and fails as a non-root user, so Hakopod builds a wrapper from images/excalidraw/Dockerfile: the upstream static site on nginxinc/nginx-unprivileged (UID 101, port 8080).
- Upstream publishes only a rolling latest tag; the wrapper is labelled by the Docker Hub push date of the pinned digest (2026-05-06), not a release version. Real-time collaboration needs a separate excalidraw-room service and is not included.

## Secrets and storage

No secrets and no persistent storage; the app is stateless. The root filesystem is read-only with a /tmp scratch volume for nginx.

## Verification

Wrapper image published by the catalog-images workflow in GitHub Actions; its multi-arch index digest and amd64/arm64 platforms checked. That workflow smoke-tests each platform (UID 101, no capabilities, read-only root with /tmp tmpfs, / returns 200 with a content marker). The template smoke workflow in GitHub Actions starts the preset itself; not tested on Kubernetes.

## Sources

- https://github.com/excalidraw/excalidraw#quick-start
- https://github.com/excalidraw/excalidraw/blob/master/Dockerfile
- images/excalidraw/Dockerfile

Application license: MIT.
