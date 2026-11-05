# VictoriaMetrics

Deployment preset. Image digest, amd64/arm64 platforms and image config (root user, /victoria-metrics-prod entrypoint) checked from the registry. The preset runs it as UID 65534. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Fast, compact time-series database that accepts Prometheus remote write and answers PromQL.

## Requirements

- Private endpoint without authentication. Point Prometheus remote_write or Grafana at http://<service>:8428 from the same virtual network.
- Single-node with 30 days of retention. Nothing is scraped until you send data or bake a -promscrape.config into a derivative image.
- Back up the /storage volume with vmbackup or a volume snapshot.

## Credentials

No pre-deployment credential references.

## Sources

- https://docs.victoriametrics.com/victoriametrics/single-server-victoriametrics/

Application license: Apache-2.0.
