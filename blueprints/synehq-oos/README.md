# SyneHQ OOS

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending.

Open-source database explorer for the Hakopod /synehq integration.

## Requirements

- Kelvo query containment needs Linux cgroup v2 delegation and a seccomp profile permitting clone3; upstream reports its restricted Kubernetes pod probe failed, so Kubernetes deployment is unqualified.
- OOS_HAKOPOD_KEY_FILE must be a mode-0600 file readable by user 65532; Hakopod secret references are delivered as environment variables, so the key is not yet usable.
- The /healthz endpoint answers loopback requests only; no orchestrator HTTP probe is configured.
- Use one instance per Hakopod project and environment with fresh metadata; set OOS_HAKOPOD_SCOPE to the exact target scope string.

## Candidate credential references

- `hakopod-explorer-key`: Separate 32-byte Hakopod explorer key encoded as 64 lowercase hex characters. Do not reuse session, encryption, TLS or Kelvo keys.

## Ordinary configuration

Use the catalog options described in the root README. The image is built with `OOS_BASE_PATH=/synehq`; set `AUTH_URL` to the OOS origin without a path and `OOS_HAKOPOD_AUTHORITY_URL` to the engine URL ending in `/internal/database-explorer/authorize`.

## Sources

- https://github.com/SyneHQ/synehq-oos
- https://github.com/SyneHQ/synehq-oos/blob/ed0976531fb244bfab04c532e463858086609889/docs/hakopod-integration.md

Application license: Apache-2.0.
