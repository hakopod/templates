# ClickHouse

Deployment preset. ARM64 authenticated HTTP queries and data survive persistent restart

Private authenticated HTTP analytics database with persistent data.

## Requirements

- HTTP port 8123 only; native TCP is not exposed
- Persistent storage; one replica; background pools bounded

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/ClickHouse/ClickHouse/blob/master/docker/server/README.md

Application license: Apache-2.0.
