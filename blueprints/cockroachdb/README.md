# CockroachDB

Deployment preset. ARM64 TLS SQL rejects missing credentials; data survives persistent restart

Secure single-node SQL database with operator-supplied TLS certificates.

## Requirements

- Review upstream license eligibility and registration
- Provide CA, node certificate and key; certificate SAN must include main and localhost
- Use a client certificate to initialize SQL users; admin HTTP is loopback only
- Single node is not highly available

## Credentials

- `database-ca`: PEM CA certificate. Keep the CA private key outside this application.
- `database-node-cert`: PEM certificate for the node principal, signed by the CA, with server/client use and main and localhost DNS names.
- `database-node-key`: Unencrypted PEM private key matching the node certificate. SQL clients still need their own client certificates.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://www.cockroachlabs.com/docs/stable/start-a-local-cluster-in-docker-linux
- https://www.cockroachlabs.com/docs/stable/create-security-certificates-openssl

Application license: CockroachDB Software License.
