# Kafka

Deployment preset. Single-node Apache Kafka 4.4.0 in KRaft mode (no ZooKeeper), combined broker and controller, with persistent storage.

## Access

Kafka is internal only. Apps in the same Hakopod project and environment connect to `main:9092`. Hakopod does not allow public TCP, so the broker is not reachable from outside the cluster and cannot be exposed by this preset.

## Requirements

- Persistent storage; one replica; one broker, so every replication factor is 1 and there is no fault tolerance
- JVM heap is the `Kafka heap` option: 512m, 1g (default), 2g or 4g, applied as both initial and maximum heap. The service size is fixed per preset, so it uses the compute profile (2458 MiB requested, 4916 MiB limit), enough for the 4g heap plus JVM overhead. The node must be able to schedule that request; the heap option does not shrink it.
- No authentication: the listener is PLAINTEXT with no SASL and no TLS. This is acceptable only because the service is cluster-internal. Do not expose it.

## Cluster ID

The image requires a cluster ID. The preset uses the fixed constant `MkU3OEVBNTcwNTJENDM2Qk` (the example ID from the Kafka documentation), set as `CLUSTER_ID`. It is not a secret. Storage formats on first start; changing the ID later against an existing volume makes the broker refuse to start.

## Runtime user

The image runs as `appuser` (UID 1000). The preset keeps that user so the image's own `/opt/kafka/config` (written at start) stays writable, and gives the data volume to it through the pod fsGroup.

## Not included

No Kafka UI is bundled. It would need a public route and most have no authentication by default. SASL and TLS are not configured.

## Verification

Image digest and amd64/arm64 platforms checked. Runtime is tested by the template smoke workflow in GitHub Actions (non-root, capabilities dropped, TCP connect to 9092 and container still running).

## Sources

- https://kafka.apache.org/documentation/#docker
- https://github.com/apache/kafka/tree/4.4.0/docker

Application license: Apache-2.0.
