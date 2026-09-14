# Prometheus

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Prometheus is an open-source monitoring and alerting toolkit designed for reliability and scalability.

## Requirements

- Private endpoint with the image’s built-in self-scrape configuration. No cluster credentials or automatic host scraping are granted.
- Bake reviewed scrape targets into a derivative image and attach permitted virtual networks before monitoring other applications.
- Seven-day / 2 GB retention; allocate sufficient disk and configure remote storage separately.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/prometheus/prometheus
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/prometheus

Application license: Review upstream license and edition.
