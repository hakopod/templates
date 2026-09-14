# Valkey

Deployment preset. ARM64 authenticated Service DNS commands verified

Private key-value database with append-only persistence.

## Requirements

- Persistent storage; one replica
- No eviction: writes fail when the data budget is full

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://valkey.io/topics/security/
- https://valkey.io/topics/persistence/

Application license: BSD-3-Clause.
