#!/usr/bin/env python3
"""Validate a repository skill manifest against the pinned common skill policy."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema
import yaml


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--skill-root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    skill_root = args.skill_root.resolve()
    manifest_path = args.manifest.resolve()
    consumer_root = manifest_path.parent.parent
    schema = json.loads((skill_root / "schemas/consumer-manifest.schema.json").read_text(encoding="utf-8"))
    registry = yaml.safe_load((skill_root / "config/skill-registry.yaml").read_text(encoding="utf-8"))
    manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    jsonschema.validate(manifest, schema, format_checker=jsonschema.FormatChecker())

    allowed = {item["id"] for item in registry["skills"] if item["mode"] in {"adapted", "enabled"}}
    forbidden = {item["id"] for item in registry["prohibited"] + registry["deferred"]}
    for skill in manifest["enabledSkills"]:
        if skill in forbidden or skill not in allowed:
            raise ValueError(f"{manifest_path}: skill {skill} is not enabled by the common registry")
    for entrypoint in manifest["entrypoints"]:
        relative = Path(entrypoint)
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError(f"{manifest_path}: entrypoint must stay within this repository: {entrypoint}")
        if not (consumer_root / relative).is_file():
            raise ValueError(f"{manifest_path}: entrypoint does not exist: {entrypoint}")
    if consumer_root.name != manifest["repository"]["id"]:
        raise ValueError(f"{manifest_path}: repository id differs from checkout directory name")
    print(f"Validated {manifest['repository']['id']} ({len(manifest['enabledSkills'])} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
