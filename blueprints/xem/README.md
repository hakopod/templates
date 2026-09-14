# xem.email

**Migration guide: not enabled for deployment.** Official AMD64/ARM64 manifests checked; deployment blocked by build-time frontend URL

Email marketing workspace; requires a frontend built for your API origin.

## Requirements

- The upstream frontend embeds NEXT_PUBLIC_API_URL at image build time
- Build and pin your frontend with your own API origin before deployment
- Provide database, Redis, JWT, session, encryption and administrator credentials
- SMTP sending needs your own provider setup; no hosted Xem or AI credentials are assumed
- See docs/templates-xem.md for the reviewed upstream pins and requirements
- After deployment, open Custom domains, verify the site URL hostname, and apply routing and TLS before using login or callbacks

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/mailxem/devops/blob/main/docs/kubernetes.md

Application license: GPL-3.0.
