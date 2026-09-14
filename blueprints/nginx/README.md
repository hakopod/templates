# Nginx

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Nginx is an High performance web server

## Requirements

- Uses the unprivileged NGINX image and its built-in welcome page.
- To serve your own site, build a derivative image containing static files and non-root NGINX configuration; do not mount an empty volume over /etc/nginx.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/nginx/nginx
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/nginx

Application license: Review upstream license and edition.
