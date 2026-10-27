# Kafka

Deployment preset. Single-node Apache Kafka 4.4.0 in KRaft mode (no ZooKeeper), combined broker and controller, with persistent storage.

## Access

Kafka is internal only. Hakopod does not allow public TCP, so the broker is not reachable from outside the cluster and this preset cannot expose it.

- Clients in the same application connect to `main:9092` or to the full address below.
- Clients in other applications must be in a shared virtual network segment that includes the Kafka application, with the Kafka service attached to that segment. Join the segment in each application's TOML (`virtual_network` and `segment` on a network, then list it in the service's `networks`) and connect to `main.<kafka application namespace>.svc.cluster.local:9092`. Copy the exact address from the network inspector. With no `network_access` block, members of the segment may reach port 9092; the controller port 9093 is loopback only.
- The preset itself cannot name a shared network, because grants belong to the project; add the segment to the Kafka application's configuration after install.

## Why the advertised address is computed

A Kafka client uses the address in broker metadata, not the one it dialled. A bare `main` resolves inside the client's own namespace, so it only works for clients in the Kafka application's namespace. Every application has its own namespace, `hp-` plus a hash of the application ID (`internal/cluster/types.go:379-382`), and a service's cross-application address is `<service>.<namespace>.svc.cluster.local` (`internal/api/virtual_networks.go:187`). Cross-application traffic is allowed only through shared network policies, never by default (`internal/cluster/virtual_networks.go:52-79`; segments are declared at `internal/spec/spec.go:91-92`, validated at `internal/spec/spec.go:227`). Templates have no placeholder for the namespace: only `config.*`, `site_host` and `site_hostname` are substituted (`internal/spec/templates.go:517-525`), and the namespace depends on an application ID that does not exist while the template is rendered. The start command therefore reads the pod's DNS search domain (`hp-<hash>.svc.cluster.local`) from `/etc/resolv.conf` and sets `KAFKA_ADVERTISED_LISTENERS` to `PLAINTEXT://main.<domain>:9092` before running the image's normal start script. Outside Kubernetes (the CI harness) there is no such domain and it falls back to `main`. The command only reads a file and runs as the same non-root user.

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
