# Stage 1 is only a file source: the public upstream image, pinned by digest.
# Upstream publishes only a rolling "latest" (pushed 2026-05-06 for this digest)
# and 2021 sha-* tags, so there is no version tag to quote.
FROM docker.io/excalidraw/excalidraw:latest@sha256:f7ee194addd607bf831d2af0f0a34463dd4225e426cf35199ef0b12a803398e9 AS upstream

# Final stage keeps the unprivileged image's UID 101 and port 8080. The static
# site needs no SPA fallback, so the default nginx server config is kept.
FROM docker.io/nginxinc/nginx-unprivileged:1.30-alpine@sha256:f5116ed4606f3eb015dd4a8e28cb9b351476dc0ad4bc6e9f93b19cec130cdf03
LABEL org.opencontainers.image.title="Excalidraw (Hakopod non-root wrapper)" \
      org.opencontainers.image.source="https://github.com/excalidraw/excalidraw" \
      org.opencontainers.image.version="20260506" \
      org.opencontainers.image.licenses="MIT" \
      org.opencontainers.image.base.name="docker.io/nginxinc/nginx-unprivileged:1.30-alpine"
COPY --from=upstream --chown=101:101 /usr/share/nginx/html /usr/share/nginx/html
COPY LICENSE /licenses/excalidraw-LICENSE
USER 101
EXPOSE 8080
