# Rocketchat

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Rocket.Chat is a free and open-source web chat platform that allows you to build and manage your own chat applications.

## Requirements

- rocketchat: immutable image/architecture verification remains incomplete for registry.rocket.chat/rocketchat/rocket.chat:6.9.2
- mongodb: immutable image/architecture verification remains incomplete for docker.io/bitnami/mongodb:5.0

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `allow-empty-password`: Value for ALLOW_EMPTY_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `reg-token`: Value for REG_TOKEN. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/RocketChat/Rocket.Chat
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/rocketchat

Application license: Review upstream license and edition.
