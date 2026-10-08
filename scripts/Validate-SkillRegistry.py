#!/usr/bin/env python3
"""Check skill-pack inventory, gated paths, and native skill routing."""

from __future__ import annotations

from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    registry = yaml.safe_load((ROOT / "config/skill-registry.yaml").read_text(encoding="utf-8"))
    active = registry["skills"]
    deferred = registry["deferred"]
    prohibited = registry["prohibited"]
    omitted = registry["notAdded"]
    all_entries = active + deferred + prohibited + omitted
    ids = [item["id"] for item in all_entries]
    if len(ids) != len(set(ids)):
        raise ValueError("A skill has more than one disposition")
    upstream = [item for item in active if item["source"] == "mattpocock-skills"]
    upstream += deferred + prohibited + omitted
    if len(upstream) != registry["upstreams"]["mattpocock-skills"]["expectedSkillCount"]:
        raise ValueError("Upstream inventory count differs from pinned revision")
    vendor_ids = {item["id"] for item in upstream if item not in omitted}
    actual_vendor_ids = {
        path.name for path in (ROOT / "vendor/mattpocock").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    if vendor_ids != actual_vendor_ids:
        raise ValueError(f"Vendor/registry mismatch: missing={vendor_ids - actual_vendor_ids}, extra={actual_vendor_ids - vendor_ids}")
    for item in active + deferred + prohibited:
        skill_path = ROOT / item["path"]
        if not (skill_path / "SKILL.md").is_file():
            raise ValueError(f"Missing skill entrypoint: {item['path']}")
    native_ids = {
        path.name for path in (ROOT / "skills").iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    }
    registered_native = {item["id"] for item in active if item["source"] == "psdc"}
    if native_ids != registered_native:
        raise ValueError("Native skill and registry entries differ")
    print(f"Skill registry passed: {len(upstream)} pinned upstream skills, {len(actual_vendor_ids)} vendored, {len(omitted)} not added, {len(native_ids)} PSDC-native")


if __name__ == "__main__":
    main()
