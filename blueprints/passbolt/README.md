# Passbolt

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Passbolt is an open source credential platform for modern teams. A versatile, battle-tested solution to manage and collaborate on passwords, accesses, and secrets. All in one.

## Requirements

- passbolt: command interpolation needs an explicit environment-aware startup adapter
- passbolt: mount /etc/passbolt/gpg is outside allowed application volume paths
- passbolt: mount /etc/passbolt/jwt is outside allowed application volume paths

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `datasources-default-password`: Value for DATASOURCES_DEFAULT_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `email-transport-default-password`: Value for EMAIL_TRANSPORT_DEFAULT_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `mariadb-password`: Value for MARIADB_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `mariadb-root-password`: Value for MARIADB_ROOT_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/passbolt/passbolt_api
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/passbolt

Application license: Review upstream license and edition.
