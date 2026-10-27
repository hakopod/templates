# Stirling PDF

Deployment preset. Image digest and amd64/arm64 platforms checked. The image's own user, start-up script and non-root start-up failures were inspected in a local container; a full non-root start with this preset was not completed. Runtime smoke test pending in CI.

Self-hosted PDF tools: merge, split, convert, compress, OCR and sign in the browser.

## Requirements

- Standard image variant (not the fat or ultra-lite one) with OCR and document conversion; the ultra-lite variant omits LibreOffice and OCR.
- JVM application: plan for about 1 GiB of memory; document conversion and OCR use more during large jobs.
- Runs as the image's own user (UID 1001). The preset overrides the container command to skip the image's start-up step that links diagnostic helpers into /usr/local/bin, which needs root.
- Telemetry is disabled with SYSTEM_ENABLE_ANALYTICS=false, and DISABLE_ADDITIONAL_FEATURES=true keeps the login and enterprise features off. The instance has no login, so protect the URL with Hakopod access controls or a private network.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/Stirling-Tools/Stirling-PDF
- https://docs.stirlingpdf.com/Installation/Docker%20Install/

Application license: MIT (core); enterprise features are separately licensed.
