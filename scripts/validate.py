#!/usr/bin/env python3
"""Validate shared metadata and native preset invariants using only Python 3.11+."""
import json, pathlib, re, tomllib
root = pathlib.Path(__file__).resolve().parents[1]
rows = json.loads((root / "catalog.json").read_text())
seen = set()
for row in rows:
    ident = row["id"]
    assert re.fullmatch(r"[a-z0-9][a-z0-9.-]{0,63}", ident), ident
    assert ident not in seen, ident
    seen.add(ident)
    folder = root / "blueprints" / ident
    assert (folder / "README.md").is_file(), ident
    assert row["requirements"] and row["sources"] and row["verification"], ident
    file = folder / ("hakopod.toml" if row["deployable"] else "candidate.toml")
    if not file.exists():
        assert not row["deployable"] and ident == "xem", ident
        continue
    spec = tomllib.loads(file.read_text())
    assert spec["schema_version"] == 1 and spec["services"], ident
    def secret_refs(value):
        if isinstance(value, dict):
            for key, child in value.items():
                if key == "ref" and isinstance(child, str):
                    yield child
                else:
                    yield from secret_refs(child)
        elif isinstance(value, list):
            for child in value:
                yield from secret_refs(child)
    refs = set(secret_refs(spec))
    assert refs == set(row["required_secrets"]), ident
    assert refs <= {field["name"] for field in row["secret_fields"]}, ident
    if not row["deployable"]:
        assert not (folder / "hakopod.toml").exists(), ident
        continue
    assert row["architectures"], ident
    for service in spec["services"].values():
        assert re.search(r"@sha256:[0-9a-f]{64}$", service["image"]), ident
        assert service.get("run_as_user", 0) >= 0, ident
        assert not service.get("public_tcp"), ident
        for value in service.get("env", {}).values():
            assert "${" not in value, ident
    assert set(row["architectures"]) <= {"amd64", "arm64"}, ident
print(f"Validated {len(rows)} entries ({sum(row['deployable'] for row in rows)} deployment presets).")
