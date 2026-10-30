# Maddy SMTP

Deployment preset. Image digest and amd64/arm64 platforms checked; container
start with a mounted certificate checked by the template smoke test. Delivery
and certificate issuance need a real installation.

A send-only SMTP submission server for your own apps. Apps sign in on port 587,
upgrade to TLS with STARTTLS, and send from your domain. Maddy signs every
message with DKIM and either delivers it straight to the recipient's mail server
or passes it to a relay provider such as Amazon SES, Mailgun or Postmark.

## Requirements

- Public TCP port 587 provisioned by the installation administrator: set it at
  install time with `public_tcp_ports`, or afterwards with
  `sudo python3 ./installer/modules.py public-tcp --ports 587` from the installer
  kit. Open the same port in the cloud and host firewall.
- The installation's TLS issuer. Hakopod issues and renews a certificate for this
  service's generated hostname (`main-<id>.<your apps domain>`, shown on the
  service page) before the container starts. Apps connect to that hostname.
- Direct delivery needs outbound TCP 25 and reverse DNS for the server hostname.
  Many cloud providers block port 25; choose relay delivery there.
- Send-only: there is no inbound mail on port 25 and no IMAP mailbox.

## After deployment

1. Create a sending account from the service terminal:

   ```sh
   maddy -config /etc/maddy/maddy.conf creds create app@example.com
   ```

   An account may send only as its own address.
2. Publish DNS for the sender domain: the DKIM record from
   `/data/dkim_keys/<domain>_default.dns`, an SPF record that allows this server
   or your relay, and a DMARC record.
3. Point your app at the generated hostname, port 587, STARTTLS, with the
   account's address and password.

## Credentials

- `relay-password`: relay password or SMTP API key, such as an Amazon SES SMTP
  password. With direct delivery it is not used; save any placeholder.

## Ordinary configuration

- `sender-domain`: the domain your apps send from.
- `hostname`: the name this server announces, such as `mail.example.com`.
- `delivery`: `direct` or `relay`.
- `relay` and `relay-user` (relay only): the provider endpoint, such as
  `tcp://email-smtp.us-east-1.amazonaws.com:587`, and its username.

## Backups

`/data` holds the account database, DKIM private keys and the outgoing queue.
Back it up; a lost DKIM key means publishing a new DNS record.

## Sources

- https://github.com/foxcpp/maddy
- https://maddy.email/

Application license: GPL-3.0.
