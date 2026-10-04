# Xem

Xem is a self-hosted email marketing workspace with a Go API and a Next.js/Bun
frontend. This preset uses the upstream `xemgo:sudo` backend and
`xemapp:sudo-self-hosted` frontend, pinned by digest after
[upstream PR #16](https://github.com/mailxem/mail/pull/16) merged at
`63b0809c2a4ba0965047ee20d08b101e0fac7c48`. The portable frontend's browser API base is `/api/v1`.

## Services and connection choices

The public Caddy proxy listens on port 8080. The frontend on port 3000 and API on
port 9001 are private. PostgreSQL, Redis and media storage each have an independent
bundled or existing choice. The default creates PostgreSQL, Redis and MinIO:

| PostgreSQL | Redis | Storage | Services created |
| --- | --- | --- | --- |
| Bundled | Bundled | Bundled MinIO | Proxy, frontend, API, PostgreSQL, Redis, MinIO |
| Existing | Bundled | Bundled MinIO | Proxy, frontend, API, Redis, MinIO |
| Bundled | Existing | Bundled MinIO | Proxy, frontend, API, PostgreSQL, MinIO |
| Existing | Existing | Bundled MinIO | Proxy, frontend, API, MinIO |
| Bundled | Bundled | Existing S3 | Proxy, frontend, API, PostgreSQL, Redis |
| Existing | Bundled | Existing S3 | Proxy, frontend, API, Redis |
| Bundled | Existing | Existing S3 | Proxy, frontend, API, PostgreSQL |
| Existing | Existing | Existing S3 | Proxy, frontend, API |

Each bundled dependency has one replica and its own persistent volume. Selecting
an existing service removes only its bundled service, volume and dependency.
Existing services retain their current credentials in scoped secret references.
A mode change does not copy data, rotate credentials or migrate an existing
deployment. Back up existing data before Xem applies startup migrations.

Existing PostgreSQL asks for host, port, database, user and TLS mode. The default
`verify-full` checks the hostname and a certificate trusted by the container's
system CA bundle. `require` encrypts without verifying identity; `disable` is for
trusted private networks. Existing Redis asks for host, port, optional ACL user,
database number 0–15 and TLS. Its default verifies the server certificate. Both
connections need approved network access; providing a hostname does not create
an external network grant. Private certificate authorities need a separately
mounted trusted CA file using the application's advanced configuration.

## Origin and authentication

Provide one stable HTTPS origin. Finish its custom-domain verification, route
and TLS before logging in. Caddy validates the configured host, passes the HTTPS
scheme, sends `/api/v1`, `/public` and `/t` to the API, and leaves `/api/auth` on
the frontend. It caps request bodies at 25 MB. `/health` reaches API health for
readiness probes; it does not prove that PostgreSQL, Redis or S3 work.

The frontend is built with `/api/v1`, so browser API calls remain on this
installation. Server authentication uses runtime
`INTERNAL_API_URL=http://backend:9001/api/v1`. Upstream also makes copied
public-form HTML submit to the installation's absolute origin when embedded on
another website. See [the upstream self-hosting guide](https://github.com/mailxem/mail/blob/63b0809c2a4ba0965047ee20d08b101e0fac7c48/docs/guides/self-hosting.mdx).

## Storage

**Bundled MinIO** is the default. It uses the pinned `pgsty/minio` community
distribution, a dedicated 5 GiB persistent volume, a generated `storage-user`
access ID and generated `storage-password`. The backend creates the private `xem-files`
bucket only when MinIO reports that it is missing. Initialization is bounded to
30 seconds and rechecks authenticated bucket access after creation; it never
changes bucket policy or makes objects public. Keep this password stable and
include media objects in independent backups. Single-instance MinIO is not
redundant storage.

The backend uploads directly to `http://storage:9000`. A separate public endpoint
signs browser reads for the installation's HTTPS origin. Caddy passes only
`GET` and `HEAD` requests beneath `/xem-files/`, preserves the complete Host,
object path and signed query, removes browser cookies and Authorization headers,
and marks responses `private, no-store`. Unsigned object requests remain subject
to MinIO authentication. Bucket listing, administration, the console and writes
have no public storage route.

**Existing S3-compatible storage** removes MinIO, its volume and the public file
route. Set `storage-bucket`, `storage-endpoint` and `storage-region`. The endpoint
is the full HTTPS S3 API origin with no bucket, path, query or credentials, and
must be reachable by both the API and browsers. The region controls SigV4 signing.
Supply provider-issued `storage-access-key` and `storage-secret-key` values scoped
to this dedicated bucket. The bucket must already exist; this mode never enables
bucket creation. Startup lists at most one object to check access, and the
application uploads objects and creates presigned GET URLs. Grant only bucket
list and object read/write permissions. Apply provider CORS for the installation's
HTTPS origin when browser access requires it.

The preset sets `S3_DISABLE_ACL=true`, so the upstream backend omits all object
ACL headers, including the ordinary `authenticated-read` and R2 `public-read`
values. The upstream default remains unchanged for other installations. This
permits ACL-disabled and bucket-owner-enforced storage. Keep the bucket policy
private: omitting an ACL cannot override an existing public policy.
Authenticated application reads use presigned URLs, which grant object access to
anyone holding the unexpired URL. Bucket recovery and retention remain the
operator's responsibility.

The backend uses `S3_ENDPOINT_URL` for its storage connection. Bundled storage adds
`S3_PUBLIC_ENDPOINT_URL` for returned object URLs and signing only, plus
`S3_CREATE_BUCKET=true`. Existing storage leaves those two options unset and
keeps ACL omission enabled. Bucket creation is intended for dedicated MinIO or
compatible storage; provision AWS S3 buckets separately. Xem still requires S3;
MinIO supplies that API using the dedicated persistent volume.

## Scoped credentials and initial setup

| Reference | Purpose |
| --- | --- |
| `database-password` | Bundled PostgreSQL password or the existing role's current password |
| `redis-password` | Bundled Redis password or the existing account's current password |
| `jwt-secret` | Stable API token signing key |
| `frontend-session-secret` | Stable key shared by `AUTH_SECRET` and `NEXTAUTH_SECRET` |
| `encryption-private-key` | Base64 of an unencrypted RSA private PEM key, 2048–4096 bits |
| `admin-password` | Initial administrator password, 16–72 bytes |
| `storage-user` | Generated dedicated MinIO access ID, bundled storage only |
| `storage-password` | Generated dedicated MinIO password, bundled storage only |
| `storage-access-key` | Bucket-scoped provider-issued access key, existing storage only |
| `storage-secret-key` | Matching provider-issued secret key, existing storage only |

The RSA value is Base64 of the entire PEM text, rather than Base64 DER or a raw
PEM block. The dashboard and API can generate it. Copy a generated value before
saving and retain the same key with protected database backups; changing it can
make encrypted sending-account credentials unreadable. Provider keys must come
from the storage provider and cannot be replaced with generated random text.

Set `admin-email`, `admin-name` and `team-name`. The administrator is seeded only
when no superadministrator exists. Updating these settings or its secret does
not reset an existing user's password. No invitation or verification message is
sent by this preset.

## Scope and operating limits

Managed SES sending, SMTP submission, managed notifications, payments, MCP and
hosted AI services are excluded. No customer AWS identity, OAuth credentials,
Infisical credentials or hosted model credentials are included. Configure a
user-owned sending provider inside Xem before sending mail. The application is
not a standalone SMTP server.

Every service runs as a non-root user. The API uses the large compute profile;
MinIO also uses large; the frontend and PostgreSQL use medium; Caddy and Redis
use small. MinIO limits concurrent API requests to 32. The API has a
768 MiB Go soft memory limit and two Go processors. Bundled PostgreSQL uses
64 MiB shared buffers and a 100-connection cap. Redis uses append-only persistence
and a 64 MiB no-eviction limit. The upstream API database pool allows up to 300
connections and its worker concurrency is fixed at 10; parsed worker settings
are not effective overrides. Review capacity and existing-service limits for
your actual workload. These starting sizes do not promise high availability or
unbounded throughput.

Back up PostgreSQL, Redis, media objects, RSA key and signing secrets together.
Verify restoration separately before relying on a backup policy. Keeping a PVC
through restart is not a backup restore test.

## Verification

The source fixes and native regressions are maintained upstream in
[PR #16](https://github.com/mailxem/mail/pull/16). The release workflows build the
backend and portable frontend for AMD64 and ARM64. `images.lock.json` records the
observed public registry indexes and the source commit used to verify them.
Registry metadata and CI results are distinct from application runtime evidence.

Earlier ARM64 development work exercised administrator login, same-origin browser
API calls and uploads using preceding development images with an external private
S3 fixture. The final five-case matrix stopped after development-node disk pressure
evicted PostgreSQL and Redis, before backend or bundled-MinIO assertions began.
That interrupted run does not establish bundled MinIO downloads through the public
proxy, PostgreSQL/Redis TLS, or restart persistence for the final images. Its
owned namespace, credentials, persistent volumes, worker and registry were removed.

The eight PostgreSQL/Redis/storage combinations are covered by planner/API
regressions. Runtime execution of the final public images, AMD64 runtime, public
ingress TLS, external-provider access, email delivery, bucket CORS and backup
restoration remain outside the recorded acceptance. See `migration.json` for
release and runtime evidence.

## Sources

- https://github.com/mailxem/mail/tree/63b0809c2a4ba0965047ee20d08b101e0fac7c48
- https://github.com/mailxem/mail/blob/63b0809c2a4ba0965047ee20d08b101e0fac7c48/docs/guides/self-hosting.mdx
- https://github.com/mailxem/mail/blob/63b0809c2a4ba0965047ee20d08b101e0fac7c48/server/internal/services/s3.go
- https://github.com/mailxem/mail/blob/63b0809c2a4ba0965047ee20d08b101e0fac7c48/.github/workflows/component-release.yml
- https://github.com/pgsty/minio

The catalog logo is the unmodified app icon from the upstream
`client/public/android-chrome-192x192.png` asset. Application source is licensed
under [GPL-3.0](https://github.com/mailxem/mail/blob/63b0809c2a4ba0965047ee20d08b101e0fac7c48/LICENSE).
