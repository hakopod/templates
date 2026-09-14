# Jitsi Meet

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Jitsi Meet is an open-source video conferencing platform for secure, self-hosted meetings.

## Requirements

- Jitsi video media requires a public UDP path; Hakopod currently supports public HTTP and administrator-provisioned self-hosted TCP, not public UDP.
- web: immutable image/architecture verification remains incomplete for jitsi/web:${JITSI_IMAGE_VERSION:-unstable}
- web: choose and pin a compatible release image
- prosody: immutable image/architecture verification remains incomplete for jitsi/prosody:${JITSI_IMAGE_VERSION:-unstable}
- prosody: choose and pin a compatible release image
- jicofo: immutable image/architecture verification remains incomplete for jitsi/jicofo:${JITSI_IMAGE_VERSION:-unstable}
- jicofo: choose and pin a compatible release image
- jvb: immutable image/architecture verification remains incomplete for jitsi/jvb:${JITSI_IMAGE_VERSION:-unstable}
- jvb: choose and pin a compatible release image

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `jicofo-auth-password`: Value for JICOFO_AUTH_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `jicofo-component-secret`: Value for JICOFO_COMPONENT_SECRET. Use the upstream required format; keep stable and back up securely.
- `jvb-auth-password`: Value for JVB_AUTH_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `jwt-app-secret`: Value for JWT_APP_SECRET. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/jitsi/docker-jitsi-meet
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/jitsi

Application license: Review upstream license and edition.
