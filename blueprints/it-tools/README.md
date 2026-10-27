# IT Tools

Browser-based developer utilities, served as a static web app.

## Wrapper image

- The official image runs nginx as root on port 80 and fails as a non-root user, so Hakopod builds a wrapper from images/it-tools/Dockerfile: the upstream static site on nginxinc/nginx-unprivileged (UID 101, port 8080).

## Secrets and storage

No secrets and no persistent storage; the app is stateless. The root filesystem is read-only with a /tmp scratch volume for nginx.

## Verification

Wrapper image published by the catalog-images workflow in GitHub Actions; its multi-arch index digest and amd64/arm64 platforms checked. That workflow smoke-tests each platform (UID 101, no capabilities, read-only root with /tmp tmpfs, / returns 200 with a content marker). The template smoke workflow in GitHub Actions starts the preset itself; not tested on Kubernetes.

## Sources

- https://github.com/CorentinTh/it-tools#readme
- https://github.com/CorentinTh/it-tools/blob/main/Dockerfile
- images/it-tools/Dockerfile

Application license: GPL-3.0.
