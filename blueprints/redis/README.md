# Redis

Deployment preset. ARM64 authenticated Service DNS commands and AOF data survive persistent restart

Private authenticated Redis with append-only persistence.

## Requirements

- Review Redis 8 license options
- Persistent storage; no eviction when the data budget is full

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://redis.io/docs/latest/operate/oss_and_stack/management/security/
- https://redis.io/docs/latest/operate/oss_and_stack/management/persistence/

Application license: AGPL-3.0 / RSALv2 / SSPL-1.0 (upstream options).
