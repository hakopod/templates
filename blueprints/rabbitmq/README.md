# RabbitMQ

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

RabbitMQ is an open source multi-protocol messaging broker.

## Requirements

- Only the management UI can use HTTP ingress. AMQP remains private TCP on 5672.
- Single persistent node with a stable node name. Allocate at least 2 GiB free disk and configure backups.

## Credentials

- `broker-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/rabbitmq/rabbitmq-server
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/rabbitmq

Application license: Review upstream license and edition.
