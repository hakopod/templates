# PostgreSQL

Deployment preset. ARM64 startup, SQL and persistent restart verified

Persistent relational database on a private endpoint.

## Requirements

- Persistent storage; one replica
- Configure separate database backups

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://hub.docker.com/_/postgres

Application license: PostgreSQL.
