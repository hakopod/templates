# Browserless

Deployment preset. Registry digest/platforms checked. Development rollout timed out during image creation on a nearly full disk; runtime acceptance pending.

Browserless allows remote clients to connect and execute headless work, all inside of docker. It supports the standard, unforked Puppeteer and Playwright libraries, as well offering REST-based APIs for common actions like data collection, PDF generation and more.

## Requirements

- Clients must send browser-token. One concurrent browser and a bounded queue are configured.
- Do not expose unauthenticated browsing; pages and downloads run within the restricted container.

Reserve at least 8 GiB free disk before pulling/unpacking this browser image.

## Credentials

- `browser-token`: Random signing/encryption material, at least 32 characters. Keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/browserless/browserless
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/browserless

Application license: Review upstream license and edition.
