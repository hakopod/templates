# Headscale

Self-hosted [Headscale](https://github.com/juanfont/headscale), an open source
control server for Tailscale clients. Your laptops, phones and servers run the
normal Tailscale app, log in to this server instead of Tailscale's, and join one
private WireGuard network (a tailnet).

This VPN is for your own devices and apps. It does not protect the Hakopod
dashboard or API. Private access to the dashboard is a separate, built-in
management VPN in Hakopod's settings.

## What this preset runs

- One `headscale/headscale` 0.29.6 service with SQLite in the 1 GiB volume at
  `/var/lib/headscale`. The volume also holds the server's private keys.
- Port 8080 is public over HTTPS at the site URL. Tailscale clients use it for
  login and for the control connection.
- It runs as UID 1000 with a read-only root and no added Linux capabilities.
  The upstream image runs as root.
- No relay server of its own. When two devices cannot connect directly, traffic
  goes through Tailscale's public DERP relays. It stays end-to-end encrypted;
  the relays cannot read it.
- MagicDNS names are `<device>.tailnet.internal`. Device DNS settings are left
  alone.
- No access policy is set, so every device in the tailnet can reach every other
  device. Add a policy file before you share the server with other people.

It is a single node and is not highly available.

## Why Headscale and not a WireGuard server

A WireGuard server such as wg-easy needs the `NET_ADMIN` capability, usually
`SYS_MODULE` and root, and a public UDP port. Hakopod drops all capabilities
from every service and publishes only HTTPS and TCP, so it cannot run one
safely. Headscale only coordinates: WireGuard runs inside the Tailscale client
on each device, and the server needs just one HTTPS port.

## Setup

1. Deploy the preset and keep the site URL stable. Clients store it, and
   changing it means logging every device in again.
2. Open a terminal on the `main` service with the command
   `["headscale", "users", "create", "alice"]`. The image has no shell, so give
   the command as a JSON list (dashboard) or with
   `hakopod terminal <app> --service main --pod <pod> --command-json '["headscale", "users", "list"]'`.
3. Create a login key: `["headscale", "preauthkeys", "create", "--user", "1", "--expiration", "24h"]`.
   Use the user ID from `users list`.
4. On each device: `tailscale up --login-server https://<site URL> --authkey <key>`.

Other useful commands: `["headscale", "nodes", "list"]` and
`["headscale", "nodes", "delete", "--identifier", "<id>"]`.

## Reaching your Hakopod apps over the tailnet

Devices on the tailnet reach each other. To reach apps running in Hakopod, one
device must advertise a route to them as a Tailscale subnet router, and you
approve the route with `["headscale", "nodes", "approve-routes", ...]`. This
preset does not set that up.

## Storage and backups

Back up the volume off-node. Losing `noise_private.key` makes every client log
in again; losing `db.sqlite` loses all users, devices and routes.

## Verification

Image digest, amd64/arm64 platforms and image config (root user,
`/ko-app/headscale` entrypoint, distroless base) checked from the registry. The
preset runs it as UID 1000 with a read-only root. The template smoke workflow in
GitHub Actions starts it and checks `/health`. Not tested on Kubernetes, and no
Tailscale client has been logged in to it.

## Sources

- https://github.com/juanfont/headscale/blob/v0.29.6/config-example.yaml
- https://github.com/juanfont/headscale/blob/v0.29.6/.goreleaser.yml
- https://github.com/juanfont/headscale/blob/v0.29.6/hscontrol/types/config.go
- https://headscale.net/stable/setup/install/container/

Application license: BSD-3-Clause.
