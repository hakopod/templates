# jellyfin

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Jellyfin is a Free Software Media System that puts you in control of managing and streaming your media. 

## Requirements

- CPU transcoding only; no host media mounts, hardware devices or discovery broadcast.
- After deployment, attach a permitted persistent media volume and add its path in Jellyfin. Complete administrator setup before sharing.
- After deployment, verify the canonical domain and configure HTTPS before using login or callbacks.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/jellyfin/jellyfin
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/jellyfin

Application license: Review upstream license and edition.
