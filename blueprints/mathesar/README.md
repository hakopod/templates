# Mathesar

Mathesar 0.12.0 with bundled PostgreSQL 17 or a database you already manage, plus
an HTTP proxy for the application and uploaded media. This is a new-install preset,
adapted from the upstream production Compose file. The preset passed the AMD64 and ARM64
development-cluster acceptance described below.

## Before deployment

1. Choose a storage class that supports `ReadWriteMany` and provide its name as
   `media-storage-class`. The backend writes media and Caddy reads the same claim.
   The class must support mounting the claim across the nodes where these services
   can run and allow UID/GID 1000 to write. A default local-path or ordinary
   block-storage class does not supply shared media storage.
2. Save `database-password` and `secret-key` in this application's scope. Generate
   the database password for a bundled database, or supply the current role's
   password for an existing database. Generate the signing key in either mode.
   Keep both values stable and include them in protected backups. The signing key
   must contain at least 64 random characters; the catalog generates 64 characters.
3. Set the stable HTTPS site URL. Route that hostname to `main` and finish domain
   verification and TLS setup before using login. Hakopod terminates TLS; Caddy
   listens on internal port 8080 and forwards the HTTPS scheme to Django.
4. Choose **Bundled PostgreSQL** or **Existing PostgreSQL**. Review the service
   budgets and persistent claims. The backend runs one Gunicorn worker; the
   bundled database permits 50 connections with 64 MiB shared buffers. This is a
   single-instance application, not a database cluster.
5. After the services become ready, open the HTTPS URL and complete Mathesar's
   first administrator setup before sharing the URL. The database password is
   not the administrator's browser login password.

## Services and storage

`main` is the only public service. It checks the configured hostname, serves
`/media/` from a read-only mount without directory browsing, and proxies other
requests to `backend`. Only the readiness and liveness endpoints are available
without that hostname so Kubernetes probes can check the service. PostgreSQL and
the backend are private. Choosing an existing database removes the bundled
PostgreSQL service and its claim; the proxy, backend and media claim remain.

## Using an existing database

Select **Existing PostgreSQL** and enter the host, port, database and login role.
Save that role's password as `database-password`. Provision a dedicated metadata
database before deployment and make the login role its owner. Upstream supports
PostgreSQL 13 and newer; this preset was exercised with PostgreSQL 17. The role
does not need superuser access. `CREATEDB` and `CREATEROLE` are optional privileges
for managing additional databases and roles through Mathesar. Startup applies upstream Mathesar migrations
to that database; it does not create the database or rotate the role's password.

The host must be reachable from the application's network. Configure any required
private network or egress permission separately; selecting a host does not grant
access to another application or network. Use the hostname in the server's
certificate when verifying TLS. **Verify server identity** verifies the certificate and
hostname; **Require encryption** encrypts traffic without verifying server
identity. **Disabled** permits plaintext and is only appropriate on a trusted
private network. The default is **Verify server identity**, using the image's system CA
bundle. For a private certificate authority, mount its CA certificate through a
service file in the reviewed TOML and point `PGSSLROOTCERT` at that file.

Mathesar 0.12.0 overwrites its Django connection options after reading
`POSTGRES_SSLMODE`. The preset mounts the upstream-supported production `local.py`
settings override, restoring the selected TLS mode and CA path while preserving
other options. This applies the choice to both Django and Mathesar's internal
database connection configuration. Libpq's `PGSSLMODE` and `PGSSLROOTCERT` are also
set so direct library connections inherit the same choice. Libpq uses a
10-second connection timeout.

Existing database infrastructure, access controls, backups, upgrades and deletion
remain under your management. Removing this Hakopod application does not remove
the external database. Mathesar's optional connections to user data databases are
configured after installation and are separate from this metadata connection.

## Runtime layout

The upstream application includes WhiteNoise for versioned static assets.
Startup runs upstream migrations and `collectstatic` before Gunicorn; collected
assets use a bounded temporary directory and are recreated after a restart.
Uploaded files live on the shared persistent media claim. Bundled PostgreSQL has
a separate persistent claim. No shared static volume, Caddy certificate volume,
root initializer, host socket or cluster credential is needed. All services
run under explicit non-root users.

This preserves upstream's public media URL behavior: possession of a media URL
allows downloading that object. Do not treat the proxy's media directory as
authorization-protected storage. Mathesar's `FILE_STORAGE_DICT` S3 settings apply
to file-column attachments, not these uploaded CSV/TSV datafiles. Upstream's
separate datafile storage settings support local files or Azure Blob Storage;
review that backend's access policy when changing this behavior.

The backend uses production settings with `DEBUG=false`, an exact allowed host,
and a scoped `SECRET_KEY`. The production settings override marks both session
and CSRF cookies `Secure`. It does not use upstream's automatic local database
fallback. Experimental per-user databases and Django's built-in admin are off.
Mathesar's own administration interface remains available. SSO, SMTP, external
database connections and custom branding remain optional upstream configuration.

The bundled database user is the initial PostgreSQL superuser, matching
Mathesar's upstream Compose defaults. It is confined to this private
database; no application receives Kubernetes credentials. Use appropriate roles
when connecting additional data sources.

## Recovery and upgrades

Back up PostgreSQL and uploaded media together, and retain the stable signing key
and database password. Database initialization variables apply only to an empty
data directory; changing a secret does not rotate the existing database role's
password. Losing the signing key can invalidate protected application data and
sessions. A volume is not a backup.

The bundled option uses the pinned official PostgreSQL 17 image rather than
upstream's automatic major-version upgrade image. An existing Compose installation needs
the upstream database, media and secret migration procedure. Review release
notes, take backups and test restores before upgrading Mathesar or PostgreSQL.
Do not point a new major PostgreSQL image at an existing data directory.

## Verification

The Mathesar 0.12.0 multi-platform registry manifest and published image
configuration were inspected for AMD64 and ARM64. Source inspection confirmed
startup migrations, static collection, WhiteNoise, HTTPS proxy handling and the
health endpoints. The PostgreSQL and Caddy pins are shared with existing presets.

On October 4, 2026, `TestLiveMathesarTemplate` passed on the named
`k3d-hakopod-dev` ARM64 development node and then on both native architectures in
[GitHub CI run 37184398017](https://github.com/hakopod/hakopod/actions/runs/37184398017),
using engine source `1b8e4a14d200e7f6ec002d77da7a8ea3a65e6561`. The CI test took
180.95 seconds on AMD64 and 175.53 seconds on ARM64. Both exercised the real images
and native plan through health checks, hostname rejection, administrator setup and login,
Secure cookie flags, static delivery, CSV upload and media download. The backend
ran as UID 1000 and collected 30,199,207 bytes of static files within its 128 MiB
temporary mount. Database, backend and proxy restarts preserved the claims,
administrator account and uploaded data.

The external-database phase redeployed the external-mode backend against the
retained, owned fixture database. It verified reattachment and data persistence;
it did not provision an independently operated database or validate every
private-network configuration. Separate real PostgreSQL handshakes verified
that `verify-full` rejects plaintext, untrusted certificates and mismatched
hostnames, and accepts the fixture server with its trusted test CA.

Media used an explicitly marked shared-filesystem fixture pinned to one node.
This exercises real shared storage and persistent bytes but does not qualify a
production, multi-node RWX storage class. The test accessed the proxy's private
HTTP listener and explicitly replayed Secure cookies while checking their flags;
public ingress TLS and browser interaction were not tested. Backup restoration
and production rollout remain unverified. Both CI architectures confirmed cleanup
of their owned application namespace, media files, PVCs, PVs and fixture storage
class after acceptance.

## Sources

- https://github.com/mathesar-foundation/mathesar/blob/0.12.0/docker-compose.yml
- https://github.com/mathesar-foundation/mathesar/blob/0.12.0/Dockerfile
- https://github.com/mathesar-foundation/mathesar/tree/0.12.0/config
- https://docs.mathesar.org/0.12.0/administration/install-via-docker-compose/
- https://github.com/mathesar-foundation/mathesar/blob/0.12.0/docs/docs/administration/install-from-scratch.md
- https://docs.mathesar.org/0.12.0/configuration/env-variables/
- https://hub.docker.com/_/postgres
- https://caddyserver.com/docs/caddyfile/directives/file_server
- https://github.com/mathesar-foundation/mathesar/blob/0.12.0/docs/docs/assets/images/logo.svg

Application license: GPL-3.0. The catalog logo is the unmodified upstream
documentation logo from the pinned release; the Mathesar name and logo remain
the upstream project's marks.
