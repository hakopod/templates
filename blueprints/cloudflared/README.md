# Cloudflared

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

A lightweight daemon that securely connects local services to the internet through Cloudflare Tunnel.

## Requirements

- Uses pod networking, not the host network. Configure tunnel origins using reachable private service DNS.
- Attach this service to an explicitly permitted virtual network for cross-application origins. localhost refers to this container.
- Create and configure the tunnel in your own Cloudflare account; image updates follow application deployments.

## Credentials

- `tunnel-token`: Supply a real upstream credential with only the permissions this service needs.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/cloudflare/cloudflared
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/cloudflared

Application license: Review upstream license and edition.
