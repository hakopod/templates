# Outpost

Outpost v1.6.0 provides an API for tenant-scoped webhook delivery and an embeddable
customer portal. This preset follows the upstream Kubernetes deployment's separate
API, delivery and log roles. PostgreSQL, Redis and RabbitMQ can each be bundled or
supplied independently. All eight dependency combinations passed isolated
Kubernetes runtime acceptance on native AMD64 and ARM64. The tested scope and
remaining validation limits are recorded below.

## Before deployment

1. Select bundled or existing PostgreSQL, Redis and RabbitMQ independently. The
   bundled choices create three separate 5 GiB persistent volumes. Review the
   service resource limits and storage class for your expected event volume.
2. Save the stable `api-key`, `jwt-secret` and `encryption-secret` in this
   application's scope. The AES secret must contain exactly 32 ASCII hexadecimal
   characters; those characters form the 32-byte encryption key directly. Keep
   these values unchanged and retain them with coordinated database backups.
3. Save `redis-password` for either Redis mode. For bundled PostgreSQL and
   RabbitMQ, generate `database-password` and `broker-password`. For existing
   services, supply `database-url` and `broker-url` instead. Only secrets used by
   the selected services are required by the generated plan.
4. Review the rendered TOML and deploy. The `migrate` job first retries the
   upstream migration plan while the dependency connections become available,
   then runs `outpost migrate apply --yes` once, applying SQL migrations followed
   by Redis migrations. The API, delivery and log services wait for completion.
   A failed migration blocks the release; inspect the job before retrying.
5. Connect your application to the API using its bearer key, create tenants and
   destinations, and publish events through the upstream API. If you expose the
   API through a custom domain, verify the domain and finish HTTPS routing before
   transmitting credentials. Domain routing is configured after deployment;
   Outpost has no generic site-URL setting in this preset.

Outpost does not create a standalone administrator account. Its API key is a
server credential. Your application issues tenant-scoped JWTs for the embedded
portal; do not put the API key or JWT signing secret in browser code. Portal
branding, return URLs, topics, retry behavior and deployment ID retain upstream
defaults. Configure them deliberately through reviewed environment settings when
integrating the portal.

## Services

| Service | Purpose | Exposure and persistence |
| --- | --- | --- |
| `main` | Outpost API (`SERVICE=api`) | Only public service; HTTP on port 3333 |
| `delivery` | Delivery and retry workers | Private HTTP health endpoint on port 3333 |
| `log` | Delivery-log writer | Private HTTP health endpoint on port 3333 |
| `migrate` | SQL and Redis migrations | Job without a listener, once per release revision |
| `db` | Optional PostgreSQL 17 | Private port 5432; dedicated 5 GiB data volume |
| `redis` | Optional Redis 8 | Private port 6379; dedicated 5 GiB append-only data volume |
| `broker` | Optional RabbitMQ 4.1 | Private AMQP port 5672; dedicated 5 GiB data volume |

All Outpost roles use the same digest-pinned upstream image and run as UID/GID
65532. The upstream CLI entrypoint handles both migration and server commands;
no custom image build or Docker login is needed. The migration job receives
PostgreSQL, Redis, broker and encryption configuration because the upstream CLI
validates these settings before applying migrations. It does not receive API keys.
Planning may initialize upstream's migration bookkeeping table, but never applies
pending migrations. A failed apply is not retried automatically. Bundled PostgreSQL
uses the private connection without TLS; external URLs retain their explicit TLS policy.
All server roles expose upstream `/healthz`. The response also reports worker
state: upstream can return HTTP 200 while a worker is `degraded` and retrying
within its recovery budget, so monitor the response status as well as HTTP status.

The preset uses one replica per role. RabbitMQ has a stable local node name and
a dedicated `outpost` virtual host. Its management listener has no public route.
The broker, databases and worker health endpoints are not public TCP services.
Telemetry and unauthenticated pprof endpoints are disabled. No service receives
Kubernetes credentials, host sockets or operator files.

## Existing dependencies

Each external option removes only that bundled service and its volume. Outpost
still needs all three dependency types. Reachability, egress permissions and
private-network access must be configured separately; entering a hostname does
not grant access to another application's network.

**PostgreSQL:** create a dedicated database and login role, and store its complete
connection URL as `database-url`. Percent-encode credentials in the URL. Prefer
`sslmode=verify-full` with a certificate and hostname trusted by the image's CA
bundle. Plaintext connections are appropriate only on a trusted private network.
The role must own or have permission to create and alter Outpost's schema. The
migration job changes this supplied database; it does not create the database,
rotate the login password or take responsibility for its backups.

**Redis:** provide the host, port, optional ACL username and database number, and
save the account's existing password as `redis-password`. Use a dedicated Redis
keyspace for this installation. Redis stores tenants, destination credentials,
retry state and migration state; it is not a disposable cache. External TLS
defaults to certificate and hostname verification. The preset configures a
standalone Redis connection, not Redis Cluster or Sentinel. Private certificate
authorities require an explicitly reviewed trust configuration.

**RabbitMQ:** create a dedicated virtual host and account, then save its `amqp://`
or `amqps://` URL as `broker-url`. Percent-encode credentials and the virtual host
in the URL. Prefer AMQPS for networks that are not private and trusted. Outpost
declares its exchange, delivery/log queues and related dead-letter queues by
default, so grant the account suitable configure, write and read permissions
within that virtual host. Existing infrastructure is not deleted by Hakopod;
objects that Outpost creates inside it remain your responsibility.

The preset keeps the upstream deployment ID empty. Do not share the same
PostgreSQL database, Redis keyspace or RabbitMQ virtual host between independent
installations with these defaults. Shared-infrastructure namespacing requires a
separately reviewed Outpost deployment-ID and queue configuration.

## Capacity, recovery and upgrades

Bundled PostgreSQL permits 50 connections with 64 MiB shared buffers. Bundled
Redis has a 64 MiB data budget and `noeviction`; it rejects writes when that
budget is exhausted. Each Outpost role has a bounded Redis pool and one worker
per enabled consumer. RabbitMQ uses two Erlang schedulers and a 1 GiB free-disk
threshold. These are small initial service budgets, not a throughput guarantee.
Review memory, queue depth, retry backlog and storage growth before production
traffic. The bundled services are single instances without redundant replicas.

Back up PostgreSQL, Redis, RabbitMQ and the stable application keys together.
Coordinate producers and delivery workers to obtain a consistent recovery point,
and test a restore before relying on the backup. A persistent volume is not a
backup. Losing Redis or the AES key can lose tenant/destination state or make
encrypted destination credentials unreadable; losing RabbitMQ can lose queued
deliveries.

Database and broker initialization credentials apply to empty data directories.
Changing a saved secret does not rotate an existing role or account. Follow the
upstream upgrade and migration procedure, take protected backups, and inspect a
migration plan before upgrading an existing installation. The deployment job
changes SQL and Redis schemas; reverting an application image does not reverse
those changes. Do not change a database or broker major version on an existing
volume without its supported upgrade procedure.

This is a native new-install preset. The Kubernetes example's Helm values are
not a backup or migration format. Moving an existing Outpost installation
requires its existing data, queues and stable secrets, plus the appropriate
upstream migration steps.

## Verification and provenance

The released v1.6.0 tag resolves to
`27ebb3587ee974e55cf443c643b087db7bf9216e`. Anonymous registry inspection confirmed
the public Outpost image index and both AMD64/ARM64 configurations, including
the entrypoint, UID, working directory and matching source-revision labels.
The three reused dependency digests were independently checked for both native
architectures. Exact manifest/configuration digests and source-file hashes are
recorded in [provenance.json](provenance.json).

On 2026-10-05, [runtime acceptance run 37259478804](https://github.com/hakopod/hakopod/actions/runs/37259478804)
passed all 16 cases: every bundled/external PostgreSQL, Redis and RabbitMQ
combination on native AMD64 and ARM64. It tested Hakopod source
`708e0b1e75b5e69513a856322786519ddc4bc812` with catalog
`d6467a12881798a379ba6a71e8951fd88ed38049`.

Each case verified completed migrations before server startup, API-key and
tenant-JWT authorization, delivery to a private HTTP receiver, persisted events
and attempts, and successful operation after actual service and dependency pod
replacement. Tenants, existing JWTs and destination signing secrets survived
the restart; all three dependency PVC identities stayed unchanged. Redis
connections selected database 0 when bundled and database 2 in external fixtures.
The test also checked worker health, workload security settings, API-only ingress
configuration, and cleanup of its owned namespace, secrets and storage.

External dependencies in this matrix are real services with separate names in
the same isolated namespace. They exercise the external configuration fields
over private connections with TLS disabled. The receiver checks the delivered
JSON marker; it does not validate webhook signatures. Stable signing-secret
retrieval after restart checks credential persistence, without inspecting stored
ciphertext. These results do not qualify arbitrary providers, public TLS or
Internet delivery, portal integration, scaling, high availability, backup/restore,
existing-install upgrades, a production Outpost deployment, or hosted shared Cloud.
The harness uses Hakopod's planner and Kubernetes deployment client directly;
dashboard and CLI deployment workflows require their own acceptance.

Per-case job links and log hashes are recorded separately from registry inspection
in [provenance.json](provenance.json). The engine's
[runtime acceptance record](https://github.com/hakopod/hakopod/blob/main/docs/outpost-template-runtime.md)
describes the matrix and checks in more detail.

Sources:

- [Released Kubernetes example](https://github.com/hookdeck/outpost/blob/27ebb3587ee974e55cf443c643b087db7bf9216e/examples/kubernetes/outpost.yaml)
- [Migration guide](https://github.com/hookdeck/outpost/blob/27ebb3587ee974e55cf443c643b087db7bf9216e/docs/content/self-hosting/guides/migration.mdoc)
- [Runtime configuration](https://github.com/hookdeck/outpost/blob/27ebb3587ee974e55cf443c643b087db7bf9216e/internal/config/config.go)
- [Image build and entrypoint](https://github.com/hookdeck/outpost/tree/27ebb3587ee974e55cf443c643b087db7bf9216e/build)
- [Upstream API documentation](https://hookdeck.com/docs/outpost)

Outpost is licensed under Apache-2.0. The unmodified upstream logo and license
are retained in this catalog; the Outpost and Hookdeck names and logos remain
their owners' marks.
