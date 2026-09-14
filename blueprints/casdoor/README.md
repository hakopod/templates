# Casdoor

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

An open-source UI-first Identity and Access Management (IAM) / Single-Sign-On (SSO) platform with web UI supporting OAuth 2.0, OIDC, SAML, CAS, LDAP, SCIM, WebAuthn, TOTP, MFA, and more.

## Requirements

- casdoor: mounted host/config asset ../files/app.conf at /conf/app.conf needs a supported image/config adapter
- casdoor: mounted host/config asset ../files/init_data.json at /init_data.json needs a supported image/config adapter
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `postgres-password`: Value for POSTGRES_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/casdoor/casdoor
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/casdoor

Application license: Review upstream license and edition.
