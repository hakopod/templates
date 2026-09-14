# Qdrant

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

An open-source vector database designed for high-performance similarity search and storage of embeddings.

## Requirements

- Authenticated HTTP and gRPC are private; use permitted private networking for clients.
- Single node; configure snapshots and backups separately.

## Credentials

- `api-key`: Random signing/encryption material, at least 32 characters. Keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/qdrant/qdrant
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/qdrant

Application license: Review upstream license and edition.
