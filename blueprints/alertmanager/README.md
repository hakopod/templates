# Alertmanager

Deployment preset. Image digest, amd64/arm64 platforms and image config (nobody user, /bin/alertmanager entrypoint) checked from the registry. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Prometheus Alertmanager: deduplicates, groups and routes alerts to email, chat and paging services.

## Requirements

- Private endpoint without authentication. Point Prometheus at http://<service>:9093 from the same virtual network.
- Runs the image's example configuration, which delivers to nowhere. Bake your receivers and routes into a derivative image.
- Single instance; clustering is off. The /alertmanager volume keeps silences and notification state.

## Credentials

No pre-deployment credential references.

## Sources

- https://prometheus.io/docs/alerting/latest/configuration/

Application license: Apache-2.0.
