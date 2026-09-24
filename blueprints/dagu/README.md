# Dagu

Authenticated workflow scheduler with persistent DAGs, logs and run history.

## Deployment

Native schema-v1 preset for a new installation. The catalog renders `hakopod.toml`; never substitute plaintext credentials into TOML.

- One replica with persistent storage
- Shell workflows run inside the restricted application container; Docker socket and host tasks are unavailable
- Sign in as admin with the saved admin-password. Back up the complete /var/lib/dagu volume.
- Starts the scheduler and UI directly as UID 1000, bypassing the image entrypoint that requires sudo. Hakopod does not grant privileged execution to workflow steps.

## Secrets and storage

`admin-password` are application-scoped secret references. Generate or save them before deployment. Database connection bindings reuse those same saved passwords.

Persistent services use one replica; scaling replicas does not create a database cluster. The storage option applies to each claim. New installations only: an image/template update is not an automatic database-major-version migration.

## Verification

Verified on AMD64 and ARM64 in [runtime workflow 36012352984](https://github.com/hakopod/hakopod/actions/runs/36012352984) using named disposable Hakopod development clusters. The authenticated DAG API rejects unauthenticated access and accepts its configured credential. A marker in the persistent home survives a pod restart on the same claim. Owned fixture claims and dynamic volumes were reclaimed after the test.

These checks establish startup and the stated persistence behavior. Complete end-user workflows, upstream version upgrades and backup restoration were not tested.

## Sources

- https://dokploy.com/templates/dagu
- https://github.com/dagu-org/dagu/blob/v2.10.7/Dockerfile
- https://github.com/dagu-org/dagu/blob/v2.10.7/entrypoint.sh
- https://docs.dagu.cloud/configurations/authentication
