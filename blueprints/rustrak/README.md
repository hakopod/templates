# Rustrak

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

Self-hosted error tracking compatible with Sentry SDKs. Server only, written in Rust: 32 MB of memory at idle, with SQLite storage. No external database required.

## Requirements

- SQLite data persists at /data. Back up the data and session secret together.
- Supply administrator as email:password using a strong password; this is a compound credential, not an ordinary environment variable.

## Credentials

- `administrator`: Administrator credential in upstream email:password format.
- `session-secret`: At least 64 cryptographically random characters. Keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/rustrak/rustrak
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/rustrak

Application license: Review upstream license and edition.
