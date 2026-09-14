// Package templates contains the shared, offline Hakopod catalog.
package templates

import "embed"

// Files is pinned with the repository submodule; runtime never fetches templates.
//go:embed catalog.json blueprints/*/hakopod.toml
var Files embed.FS
