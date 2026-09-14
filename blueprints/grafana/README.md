# Grafana

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Grafana is an open source platform for data visualization and monitoring.

## Requirements

- Uses Grafana OSS rather than the Enterprise image in the upstream blueprint.
- Sign in as admin with the configured secret. Configure data sources after deployment.
- Back up /var/lib/grafana and configure external backups.

## Credentials

- `admin-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/grafana/grafana
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/grafana

Application license: AGPL-3.0.
