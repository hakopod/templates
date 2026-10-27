# Wiki.js

Wiki platform with PostgreSQL, using the Wiki.js 2.x line.

## Deployment

Native schema-v1 preset for a new installation. Two services: Wiki.js (`main`, public, port 3000) and a private PostgreSQL 17 service (`db`) with a 5 GiB volume. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

On first visit Wiki.js shows a setup page. Complete it before sharing the URL: whoever opens it first creates the administrator account.

## Secrets and storage

- `database-password`: shared by the database (`POSTGRES_PASSWORD`) and Wiki.js (`DB_PASS`). Keep it stable and back it up with the database.

Pages, users and settings live in PostgreSQL, so back up the `db` volume. The preset gives Wiki.js no data volume of its own: content stored by the optional Git storage module or the local file storage target would be lost on restart, so use the database or an external storage target.

Persistent services use one replica; scaling replicas does not create a database cluster. New installations only: an image update is not an automatic database-major-version migration.

## Sources

- https://github.com/requarks/wiki
- https://docs.requarks.io/install/docker
- https://github.com/requarks/wiki/blob/v2.5.315/dev/build/Dockerfile

Application license: AGPL-3.0.
