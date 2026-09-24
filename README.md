# Hakopod templates

Shared catalog for the open-source Hakopod engine and the Hakopod website.
Both consumers pin this repository as a Git submodule. The server embeds the
catalog at build time; installations do not execute remote template downloads.

Currently 77 entries: 40 deployment presets and 37 migration guides.
Every requested Dokploy blueprint has a migration record. A guide is **not** a
working deployment: unsupported initialization, host access, static config,
public UDP, or unresolved image/runtime requirements are listed explicitly.
The existing Valkey preset is retained rather than downgraded to the Compose blueprint.

## Layout

- `catalog.json`: shared names, prerequisites, secrets, configuration fields and verification status.
- `blueprints/<id>/hakopod.toml`: native deployment preset, consumed by the engine planner.
- `blueprints/<id>/candidate.toml`: incomplete native translation; never offered by the deploy API.
- `blueprints/<id>/README.md` and `migration.json`: setup and migration requirements.
- `images.lock.json`: registry provenance for digest and architecture checks.
- `embed.go`: build-time Go filesystem for the engine (uses the parent Go module).

## Configuration and secrets

Use the Hakopod catalog to select scope, application name, storage and architecture,
then review the rendered TOML. Blueprint files are planner inputs: do not deploy
placeholders unchanged. The planner replaces `{{config.name}}`, `{{site_host}}`
and the representative `https://catalog.example.test` origin inside decoded
string values. It never interpolates raw TOML. Site origins require HTTPS.
Secrets are named references only. Save their values in the application scope;
provider credentials must be issued by the provider, not random generated text.

The existing PostgreSQL/MySQL database options, Open WebUI provider/model options,
and vLLM model/revision options remain supported. Private databases stay private.
`public` enables HTTP ingress only. Additional ports are private; public custom
TCP requires administrator provisioning on self-hosted Hakopod. Public UDP and
host-network access are not implicitly introduced by a conversion.

See [the September completion review](REVIEW-2026-09-24.md) for the new native stacks, compatibility image and exact remaining blockers.

## Checks and updates

Run `python3 scripts/validate.py` here. In the consumer, run `go test ./internal/spec`
and the API tests, then opt into the named development-cluster runtime tests.
Registry inspection and schema validation are **not** runtime verification.
Update verification only after an actual test; never describe an untested preset as production-ready.

Commit catalog changes here first, then update the gitlink in both consumers to
the same commit. Use rebase merges. Do not put credentials, host files or customer
configuration in this repository. Review upstream licenses and preserve attribution.
