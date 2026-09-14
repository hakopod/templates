# InfluxDB

Deployment preset. Image digests and registry platforms checked; non-root runtime acceptance pending.

InfluxDB 2.7 is the platform purpose-built to collect, store, process and visualize time series data.

## Requirements

- Start influxd directly with writable data paths; no forbidden /etc volume mount is required.
- Complete the first administrator, organization and bucket setup before sharing the URL. Store client API tokens securely and configure backups.

## Credentials

No pre-deployment credential references.

## Ordinary configuration

Use the catalog options described in the root README.

## Sources

- https://github.com/influxdata/influxdb
- https://github.com/Dokploy/templates/tree/830d6bbc8de2a8cb0c87d3c3f2294940ecd0e933/blueprints/influxdb

Application license: Review upstream license and edition.
