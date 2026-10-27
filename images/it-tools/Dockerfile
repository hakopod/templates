# Stage 1 is only a file source: the public upstream release, pinned by digest.
# It runs nginx as root on port 80, so only its static site is reused.
FROM docker.io/corentinth/it-tools:2024.10.22-7ca5933@sha256:8b8128748339583ca951af03dfe02a9a4d7363f61a216226fc28030731a5a61f AS upstream

# Final stage keeps the unprivileged image's UID 101 and adds nothing at runtime.
FROM docker.io/nginxinc/nginx-unprivileged:1.30-alpine@sha256:f5116ed4606f3eb015dd4a8e28cb9b351476dc0ad4bc6e9f93b19cec130cdf03
LABEL org.opencontainers.image.title="IT Tools (Hakopod non-root wrapper)" \
      org.opencontainers.image.source="https://github.com/CorentinTh/it-tools" \
      org.opencontainers.image.version="2024.10.22-7ca5933" \
      org.opencontainers.image.licenses="GPL-3.0-only" \
      org.opencontainers.image.base.name="docker.io/nginxinc/nginx-unprivileged:1.30-alpine"
COPY --from=upstream --chown=101:101 /usr/share/nginx/html /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY LICENSE /licenses/it-tools-LICENSE
USER 101
EXPOSE 8080
