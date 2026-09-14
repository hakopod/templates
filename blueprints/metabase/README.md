# Metabase

Deployment preset. AMD64/ARM64 registry manifests checked; runtime acceptance pending

Analytics workspace with its own private PostgreSQL application database.

## Requirements

- Complete administrator setup before sharing its URL
- Back up PostgreSQL and the credential encryption key together
- Uses the open-source edition

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.
- `credential-encryption-key`: Encrypts saved database connection credentials. Keep this stable and include it in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker
- https://www.metabase.com/docs/latest/databases/encrypting-details-at-rest

Application license: AGPL-3.0.
