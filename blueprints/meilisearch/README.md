# Meilisearch

Deployment preset. Image digest and amd64/arm64 platforms checked; local container started as UID 10001 on arm64 with the preset environment and /health returned 200 and {"status":"available"}, / returned 200. Kubernetes volume ownership via fs_group not tested. Full runtime smoke test pending in CI.

Fast, typo-tolerant search engine with a REST API.

## Requirements

- Persistent storage at /meili_data; back up regularly or use dumps and snapshots.
- The master key protects the API in production mode. Create scoped search and admin keys from it for applications; do not ship the master key to browsers.
- Analytics are disabled with MEILI_NO_ANALYTICS=true.

## Credentials

- `master-key`: Meilisearch master key (generated token, at least 16 bytes). Keep it stable.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/meilisearch/meilisearch
- https://www.meilisearch.com/docs/learn/self_hosted/install_meilisearch_locally

Application license: MIT (Community Edition).
