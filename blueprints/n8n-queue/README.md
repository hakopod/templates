# n8n Queue Mode

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

n8n running in queue mode for high-throughput production workloads: the main instance handles the editor and webhooks while a scalable pool of workers executes workflows from a Redis (Bull) queue, backed by PostgreSQL.

## Requirements

- Uses the same pinned n8n 2 release across variants. Review upstream upgrade notes before importing workflows from older releases.
- Complete first-owner setup before sharing. Preserve the encryption key with database backups.
- Task runners are not included in this variant; configure external runners before using code tasks that require them.
- After deployment, verify the canonical domain and configure HTTPS before using login or callbacks.

## Credentials

- `database-password`: At least 16 characters. Keep stable and include in protected backups.
- `encryption-key`: Random signing/encryption material, at least 32 characters. Keep stable and back up securely.
- `redis-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

- `timezone`: Set timezone before reviewing the deployment.

## Sources

- https://github.com/n8n-io/n8n
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/n8n-queue

Application license: Sustainable Use License; enterprise features have separate terms.
