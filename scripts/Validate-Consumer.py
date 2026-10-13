#!/usr/bin/env python3
"""Validate a repository skill manifest against the pinned common skill policy."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

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

    # The canonical pack manifest cannot pin its eventual commit. Every other
    # manifest must use the policy at the exact commit named by its pin.
    self_manifest = skill_root / ".psdc/agent-skills.yaml"
    if manifest_path != self_manifest:
        revision = subprocess.run(
            ["git", "-C", str(skill_root), "rev-parse", "HEAD"],
            text=True, capture_output=True, check=False,
        )
        if revision.returncode != 0:
            raise ValueError(f"{skill_root}: skill root must be a Git checkout")
        actual_revision = revision.stdout.strip()
        pinned_revision = manifest["skillPack"]["revision"]
        if actual_revision != pinned_revision:
            raise ValueError(
                f"{manifest_path}: skill pack pin {pinned_revision} differs "
                f"from skill root HEAD {actual_revision}"
            )
        policy_files = ["config/skill-registry.yaml", "schemas/consumer-manifest.schema.json"]
        policy_diff = subprocess.run(
            ["git", "-C", str(skill_root), "diff", "--quiet", "HEAD", "--", *policy_files],
            text=True, capture_output=True, check=False,
        )
        if policy_diff.returncode == 1:
            raise ValueError(f"{skill_root}: skill registry or consumer schema differs from HEAD")
        if policy_diff.returncode != 0:
            raise ValueError(f"{skill_root}: could not verify skill policy against HEAD: {policy_diff.stderr.strip()}")

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
    remote = subprocess.run(
        ["git", "-C", str(consumer_root), "remote", "get-url", "origin"],
        text=True, capture_output=True, check=False,
    )
    if remote.returncode != 0:
        raise ValueError(f"{manifest_path}: origin remote is required to verify repository identity")
    remote_url = remote.stdout.strip()
    remote_path = urlparse(remote_url).path if "://" in remote_url else remote_url.split(":", 1)[-1]
    remote_id = remote_path.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")
    if remote_id != manifest["repository"]["id"]:
        raise ValueError(f"{manifest_path}: repository id {manifest['repository']['id']} differs from origin {remote_id}")
    print(f"Validated {manifest['repository']['id']} ({len(manifest['enabledSkills'])} skills)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
