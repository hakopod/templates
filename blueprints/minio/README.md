# Minio

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

MinIO is an open source object storage server compatible with Amazon S3 cloud storage service. This template uses pgsty/minio, the actively maintained community fork, because MinIO Inc. stopped publishing Docker images in October 2025 and archived the upstream open source project in February 2026.

## Requirements

- Uses the pgsty community distribution. Review its maintenance and licensing independently.
- S3 on 9000 and console on 9001 are private. Do not send S3 TCP traffic to an HTTP hostname configured for the console.
- Create restricted client access keys after setup. Single-node storage is not redundant; configure off-node backups.

## Credentials

- `root-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/pgsty/minio
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/minio

Application license: Review upstream license and edition.
