# Double Zero

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

00 is a self hostable SES dashboard for sending and monitoring emails with AWS

## Requirements

- Provide least-privilege AWS SES/SQS credentials and complete sender/domain verification in AWS.
- Uses an explicit persistent SQLite path. This is an SES dashboard; it does not expose an SMTP listener.
- After deployment, verify the canonical domain and configure HTTPS before using login or callbacks.

## Credentials

- `aws-access-key-id`: Supply a real upstream credential with only the permissions this service needs.
- `aws-secret-access-key`: Supply a real upstream credential with only the permissions this service needs.
- `secret-key-base`: At least 64 cryptographically random characters. Keep stable and back up securely.

## Ordinary configuration

- `aws-region`: Set aws region before reviewing the deployment.
- `sqs-url`: Set sqs queue url before reviewing the deployment.
- `system-email`: Set sender email before reviewing the deployment.

## Sources

- https://github.com/technomancy-dev/00
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/doublezero

Application license: Review upstream license and edition.
