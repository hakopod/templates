# GitLab CE

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

GitLab Community Edition is a free and open source platform for managing Git repositories, CI/CD pipelines, and project management.

## Requirements

- gitlab: mount /etc/gitlab is outside allowed application volume paths
- gitlab: review Compose shm_size=256m; no implicit host privileges or configuration mounts

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `gitlab-omnibus-config`: Value for GITLAB_OMNIBUS_CONFIG. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://gitlab.com/gitlab-org/gitlab-ce
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/gitlab-ce

Application license: Review upstream license and edition.
