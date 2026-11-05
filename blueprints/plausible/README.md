# Plausible Analytics

Lightweight, cookie-free web analytics. Community Edition 3.2.1 with bundled or
existing PostgreSQL and ClickHouse.

## Register the first account immediately

Registration is `invite_only`: the first account can sign up without an
invitation and becomes the owner. Open the URL and register as soon as the
deployment is ready, before anyone else finds it. Later users need an invitation.

## Deployment

Native schema-v1 preset for a new installation. With both databases bundled,
three services:

- `main`: Plausible, public, port 8000. Its first start creates both databases
  and runs the migrations, the same sequence as upstream's compose command, so
  allow several minutes.
- `db`: private PostgreSQL 17 with a 5 GiB volume for users, sites and settings.
- `events`: private ClickHouse 24.12, the release upstream pins, with a 5 GiB
  volume for pageviews and events. It uses the ClickHouse preset's bounded
  low-memory configuration; native TCP stays on loopback.

`BASE_URL` is the site host Hakopod assigns. Plausible builds links and the
tracking snippet from it, so finish custom domain and TLS setup before adding
the snippet to your sites. Changing the hostname later means updating every
snippet.

`DATABASE_URL` comes from a native postgres binding on `database-password`.
`CLICKHOUSE_DATABASE_URL` is assembled inside the container from
`clickhouse-password`; neither password is written into the TOML.

## Bundled or existing databases

PostgreSQL and ClickHouse are chosen independently. **Existing** removes that
service, its volume and the startup dependency, and takes a complete URL secret
instead:

- `database-url`: `postgresql://user:password@host:5432/plausible?sslmode=...`.
  Set `sslmode` explicitly. Plausible's `verify-full` also needs
  `sslrootcert=/etc/ssl/certs/ca-certificates.crt` (or a mounted private CA).
- `clickhouse-url`: `https://user:password@host:8443/plausible_events_db`. Use
  `http` only on a trusted private network.

Percent-encode special characters in credentials. Create the databases first
and use roles allowed to run Plausible's migrations: the startup still runs
`createdb` and `migrate`. The host must be reachable from the application
network; supplying a hostname does not create a network grant. Switching modes
does not migrate data.

## Secrets and storage

- `secret-key-base`: Plausible's `SECRET_KEY_BASE`, at least 64 characters.
  Rotating it signs everyone out and invalidates stored two-factor secrets.
- `database-password` (bundled PostgreSQL): shared by PostgreSQL and the
  Plausible connection URL.
- `clickhouse-password` (bundled ClickHouse): exactly 32 hexadecimal characters,
  so it is safe inside the ClickHouse URL. Generate it rather than typing one.

Back up both volumes. Persistent services use one replica; scaling does not
create a database cluster. An image update is not an automatic database-major
migration.

## Not configured

- Email: no mailer is set, so invitations and password resets may not arrive.
  Add `MAILER_EMAIL` and the `SMTP_*` variables in Edit TOML before relying on
  them.
- Google Search Console import and MaxMind geolocation are off. Country data
  uses the bundled DB-IP database, downloaded again after a restart.

## Sources

- https://github.com/plausible/community-edition/tree/v3.2.1
- https://github.com/plausible/community-edition/wiki/configuration
- https://github.com/plausible/analytics/blob/v3.2.1/Dockerfile

Application license: AGPL-3.0.
