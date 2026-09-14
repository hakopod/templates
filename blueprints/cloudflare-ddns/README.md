# Cloudflare DDNS

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

A small, feature-rich, and robust Cloudflare DDNS updater.

## Requirements

- Updates DNS to the public IPv4 observed from pod egress. Verify that it matches the server ingress address before enabling.
- Host networking and IPv6 discovery are not used. Scope the token to DNS editing for the intended zones.

## Credentials

- `dns-token`: Supply a real upstream credential with only the permissions this service needs.

## Ordinary configuration

- `domains`: Comma-separated fully qualified DNS names to update.

## Sources

- https://github.com/favonia/cloudflare-ddns
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/cloudflare-ddns

Application license: Review upstream license and edition.
