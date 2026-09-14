# Wordpress

**Migration guide: not enabled for deployment.** Native migration candidate; runtime acceptance pending. Not enabled for deployment.

Wordpress is a free and open source content management system (CMS) for publishing and managing websites.

## Requirements

- wordpress: mounted host/config asset ../files/uploads.ini at /usr/local/etc/php/conf.d/uploads.ini needs a supported image/config adapter
- Configuration files declared upstream require explicit provisioning before the native candidate is deployable

## Candidate credential references

This draft may include alternative providers; not every reference is required for every eventual configuration.

- `mysql-root-password`: Value for MYSQL_ROOT_PASSWORD. Use the upstream required format; keep stable and back up securely.
- `wordpress-db-password`: Value for WORDPRESS_DB_PASSWORD. Use the upstream required format; keep stable and back up securely.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/WordPress/WordPress
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/wordpress

Application license: Review upstream license and edition.
