# Infisical

Deployment preset. AMD64/ARM64 registry manifests checked; runtime acceptance pending

Self-hosted secrets workspace with private PostgreSQL and Redis.

## Requirements

- Use a stable HTTPS site URL; complete administrator setup
- encryption-key must be 32 hexadecimal characters; back it up securely
- database-url must target db:5432/app; redis-url must target redis:6379 with matching passwords
- Back up PostgreSQL and encryption keys together
- This is the Infisical server; Hakopod's optional operator integration is configured separately
- After deployment, open Custom domains, verify the site URL hostname, and apply routing and TLS before using login or callbacks

## Credentials

- `database-password`: Database password. Use at least 16 characters. Initialization values do not rotate a password in an existing database.
- `redis-password`: Private Redis password, at least 16 characters.
- `encryption-key`: Exactly 32 hexadecimal characters for this standard, non-FIPS image. Losing it makes stored secrets unreadable.
- `auth-secret`: 32 random bytes encoded as standard Base64 for authentication signing.
- `database-url`: PostgreSQL URL for hakopod at db:5432/app. Generate it after saving database-password to encode the matching password safely.
- `redis-url`: Redis URL for redis:6379. Generate it after saving redis-password to encode the matching password safely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://infisical.com/docs/self-hosting/configuration/envars

Application license: MIT core; enterprise extensions have separate terms.
