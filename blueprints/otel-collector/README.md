# OpenTelemetry Collector

Deployment preset. Image digest, amd64/arm64 platforms and image config (UID 10001, /otelcol-contrib entrypoint) checked from the registry. The template smoke workflow in GitHub Actions starts it on amd64 and arm64; not tested on Kubernetes.

Vendor-neutral pipeline that receives, processes and forwards traces, metrics and logs.

## Requirements

- Private OTLP/HTTP endpoint on port 4318 for apps on the same virtual network. gRPC on 4317 is not exposed.
- The bundled pipeline only prints what it receives to the service logs. Bake exporters for your backend into a derivative image with your own config.
- Stateless; nothing to back up.

## Credentials

No pre-deployment credential references.

## Sources

- https://opentelemetry.io/docs/collector/installation/
- https://opentelemetry.io/docs/collector/configuration/

Application license: Apache-2.0.
