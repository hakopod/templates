# Grafana Loki

Deployment preset. Image digest, amd64/arm64 platforms and image config (UID 10001, /usr/bin/loki entrypoint) checked from the registry. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Log storage and query engine from Grafana Labs, queried with LogQL from Grafana.

## Requirements

- Private endpoint without authentication. Add it to Grafana as a Loki data source at http://<service>:3100, and push logs from agents on the same virtual network.
- Single-binary mode on the local filesystem with seven days of retention; use object storage and a scalable deployment for larger volumes.
- Back up the /loki volume if logs must outlive the node.

## Credentials

No pre-deployment credential references.

## Sources

- https://grafana.com/docs/loki/latest/configure/examples/configuration-examples/
- https://github.com/grafana/loki/blob/v3.7.9/cmd/loki/loki-local-config.yaml

Application license: AGPL-3.0.
