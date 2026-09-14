# TimescaleDB

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

TimescaleDB is an open-source time-series database packaged as a PostgreSQL extension, optimized for fast ingest and real-time analytics with standard SQL.

## Requirements

- Private PostgreSQL 17 with the TimescaleDB extension preloaded.
- After initialization, an administrator must run CREATE EXTENSION IF NOT EXISTS timescaledb in the application database.
- Review Timescale license terms; set up backups and capacity for time-series workloads.

## Credentials

- `database-password`: At least 16 characters. Keep stable and include in protected backups.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/timescale/timescaledb
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/timescaledb

Application license: Review upstream license and edition.
