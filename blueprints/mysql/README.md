# MySQL

Deployment preset. ARM64 non-root startup, SQL dump and fresh-database restore verified

Private MySQL 8.4 LTS database with persistent storage.

## Requirements

- Separate application and root password references
- Persistent storage; one replica; configure backups

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.
- `database-root-password`: Separate MySQL root password, at least 16 characters. Do not use the application password.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://hub.docker.com/_/mysql

Application license: GPL-2.0.
