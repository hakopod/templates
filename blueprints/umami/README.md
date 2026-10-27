# Umami

Privacy-friendly web analytics with PostgreSQL.

## Change the default login immediately

A new Umami install has the account `admin` with the password `umami`. Anyone who finds the URL can sign in with it. Sign in as soon as the deployment is reachable, open Settings, Profile, and change the password before adding any website or sharing the URL.

## Deployment

Native schema-v1 preset for a new installation. Two services: Umami (`main`, public, port 3000) and a private PostgreSQL 17 service (`db`) with a 5 GiB volume. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

Umami needs `DATABASE_URL`, which embeds the database password. The preset uses a native `[services.main.bindings.DATABASE_URL]` binding: Hakopod builds the URL at deploy time from the same `database-password` secret that protects the database, so the password is never written into the TOML.

## Secrets and storage

- `database-password`: shared by the database and the Umami connection URL. Keep it stable and back it up with the database.
- `app-secret`: Umami's `APP_SECRET`, used to sign sessions. Rotating it signs everyone out.

All Umami data lives in PostgreSQL. Back up the `db` volume. Persistent services use one replica; scaling replicas does not create a database cluster. New installations only: an image update is not an automatic database-major-version migration. Telemetry is turned off with `DISABLE_TELEMETRY`.

## Requirements

Add your tracking script from Settings, Websites, after the first login. The tracker is served from the same origin, so use a stable HTTPS domain.

## Sources

- https://github.com/umami-software/umami
- https://umami.is/docs/install
- https://github.com/umami-software/umami/blob/v3.4.1/Dockerfile

Application license: MIT.
