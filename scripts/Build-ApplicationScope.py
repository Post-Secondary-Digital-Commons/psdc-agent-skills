#!/usr/bin/env python3
"""Render a revision-bound skill application map from repository manifests."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SCOPE = ROOT / "config/application-scope.yaml"
REGISTRY = ROOT / "config/skill-registry.yaml"
SNAPSHOT = ROOT / "config/application-scope-snapshot.json"
DOCUMENT = ROOT / "docs/governance/SKILL-APPLICATION-SCOPE.md"


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(["git", "-C", str(repo), *args], text=True,
                            capture_output=True, check=False)
    if result.returncode:
        raise ValueError(f"{repo}: git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def validate_policy(scope: dict, registry: dict) -> None:
    if scope.get("schemaVersion") != 1:
        raise ValueError("Unsupported application-scope schema version")
    allowed = {entry["id"] for entry in registry["skills"]
               if entry["mode"] in {"adapted", "enabled"}}
    seen: set[str] = set()
    for profile in scope["profiles"]:
        if not profile["repositories"] or not profile["skills"]:
            raise ValueError(f"Empty repository or skill scope: {profile['id']}")
        if len(profile["repositories"]) != len(set(profile["repositories"])):
            raise ValueError(f"Repeated repository in profile {profile['id']}")
        if len(profile["skills"]) != len(set(profile["skills"])):
            raise ValueError(f"Repeated skill in profile {profile['id']}")
        forbidden = set(profile["skills"]) - allowed
        if forbidden:
            raise ValueError(f"Profile {profile['id']} recommends gated or unknown skills: {sorted(forbidden)}")
        for repo_id in profile["repositories"]:
            if repo_id in seen:
                raise ValueError(f"Repository appears in more than one profile: {repo_id}")
            seen.add(repo_id)


def read_policy() -> tuple[dict, dict]:
    scope = yaml.safe_load(SCOPE.read_text(encoding="utf-8"))
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    validate_policy(scope, registry)
    return scope, registry


def snapshot_from_workspace(workspace: Path, scope: dict, pack_revision: str) -> dict:
    catalog_revision = git(workspace, "rev-parse", "origin/main").strip()
    catalog = yaml.safe_load(git(workspace, "show", "origin/main:repos.yaml"))
    if catalog.get("schemaVersion") != 3:
        raise ValueError("Expected the workspace v3 repository catalog")
    entries = []
    for item in catalog["repositories"]:
        entries.append(item["repository"])
        entries.extend(overlay for overlay in item.get("institutionOverlays", [])
                       if overlay.get("status") != "planned")
    expected = {repo_id for profile in scope["profiles"] for repo_id in profile["repositories"]}
    actual = {entry["id"] for entry in entries}
    if expected != actual:
        raise ValueError(f"Scope/catalog mismatch: missing={sorted(actual - expected)}, extra={sorted(expected - actual)}")
    records = []
    for entry in entries:
        checkout = workspace / entry["path"]
        if not checkout.resolve().is_relative_to(workspace.resolve()):
            raise ValueError(f"Catalog path leaves workspace: {entry['path']}")
        revision = git(checkout, "rev-parse", "origin/main").strip()
        raw = git(checkout, "show", "origin/main:.psdc/agent-skills.yaml")
        manifest = yaml.safe_load(raw)
        if manifest["repository"]["id"] != entry["id"]:
            raise ValueError(f"Manifest identity mismatch: {entry['id']}")
        records.append({
            "id": entry["id"], "path": entry["path"], "revision": revision,
            "manifestSha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "packRevision": manifest["skillPack"]["revision"],
            "authority": manifest["repository"]["authority"],
            "lifecycle": manifest["repository"]["lifecycle"],
            "enabledSkills": manifest["enabledSkills"],
        })
    return {"schemaVersion": 1, "catalogRevision": catalog_revision,
            "packRevision": pack_revision,
            "registrySha256": hashlib.sha256(REGISTRY.read_bytes()).hexdigest(),
            "repositories": records}


def validate_snapshot(snapshot: dict, scope: dict, registry: dict) -> None:
    if snapshot.get("schemaVersion") != 1:
        raise ValueError("Unsupported snapshot schema version")
    if snapshot.get("registrySha256") != hashlib.sha256(REGISTRY.read_bytes()).hexdigest():
        raise ValueError("Skill registry changed since the scope snapshot was generated")
    expected = {repo_id for profile in scope["profiles"] for repo_id in profile["repositories"]}
    records = snapshot["repositories"]
    actual = [record["id"] for record in records]
    if len(actual) != len(set(actual)) or set(actual) != expected:
        raise ValueError("Snapshot does not account for each scoped repository exactly once")
    allowed = {entry["id"] for entry in registry["skills"]
               if entry["mode"] in {"adapted", "enabled"}}
    for record in records:
        if len(record["enabledSkills"]) != len(set(record["enabledSkills"])):
            raise ValueError(f"Duplicate enabled skill in {record['id']}")
        if record["packRevision"] == snapshot["packRevision"]:
            invalid = set(record["enabledSkills"]) - allowed
            if invalid:
                raise ValueError(f"Current-pin manifest enables gated/unknown skills in {record['id']}: {sorted(invalid)}")
        if not re.fullmatch(r"[a-f0-9]{40}", record["revision"]) or not re.fullmatch(r"[a-f0-9]{40}", record["packRevision"]):
            raise ValueError(f"Unpinned revision in {record['id']}")
        if not re.fullmatch(r"[a-f0-9]{64}", record["manifestSha256"]):
            raise ValueError(f"Invalid manifest digest in {record['id']}")


def same_sources(current: dict, committed: dict) -> bool:
    """Ignore only a self-repo commit bump with identical consumer manifest."""
    current = copy.deepcopy(current)
    original = {record["id"]: record for record in committed["repositories"]}
    for record in current["repositories"]:
        if record["id"] == "psdc-agent-skills" and record["id"] in original:
            prior = original[record["id"]]
            if record["manifestSha256"] == prior["manifestSha256"]:
                record["revision"] = prior["revision"]
    return current == committed


def self_test() -> None:
    scope, registry = read_policy()
    bad_scope = copy.deepcopy(scope)
    bad_scope["profiles"][0]["skills"].append("implement")
    try:
        validate_policy(bad_scope, registry)
    except ValueError:
        pass
    else:
        raise AssertionError("Prohibited skill was accepted as a recommendation")
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    validate_snapshot(snapshot, scope, registry)
    bad_snapshot = copy.deepcopy(snapshot)
    bad_snapshot["repositories"][0]["id"] = bad_snapshot["repositories"][1]["id"]
    try:
        validate_snapshot(bad_snapshot, scope, registry)
    except ValueError:
        pass
    else:
        raise AssertionError("Duplicate repository identity was accepted")
    bumped = copy.deepcopy(snapshot)
    self_record = next(record for record in bumped["repositories"]
                       if record["id"] == "psdc-agent-skills")
    self_record["revision"] = "a" * 40
    if not same_sources(bumped, snapshot):
        raise AssertionError("Unchanged self manifest did not tolerate merge commit")
    self_record["manifestSha256"] = "b" * 64
    if same_sources(bumped, snapshot):
        raise AssertionError("Changed self manifest was accepted as unchanged")
    other_bump = copy.deepcopy(snapshot)
    other_bump["repositories"][0]["revision"] = "a" * 40
    if same_sources(other_bump, snapshot):
        raise AssertionError("Another repository's changed commit was accepted")


def render(snapshot: dict, scope: dict) -> str:
    records = {record["id"]: record for record in snapshot["repositories"]}
    different_pins = sum(record["packRevision"] != snapshot["packRevision"]
                         for record in snapshot["repositories"])
    lines = [
        "# Skill Application Scope",
        "",
        "> Generated from `config/application-scope.yaml`, `config/skill-registry.yaml`,",
        "> the workspace catalog, and each repository's `origin/main` consumer manifest.",
        "> This is a revision-bound structural snapshot, not evidence that an agent used a skill.",
        "",
        "## Read this map",
        "",
        "A profile names useful methods for a repository's work, **not** automatic enablement.",
        "The consumer manifest lists declared opt-ins at its own pinned pack revision.",
        "A task triggers only the applicable enabled method, subject to its gate, repository",
        "instructions, and explicit user authority. The [registry](../../config/skill-registry.yaml)",
        "sets current pack-wide modes; the [inventory](COMPLETE-SKILL-INVENTORY.md)",
        "explains every skill. An older consumer pin is **not** validated against newer rules.",
        "",
        f"Workspace catalog revision: `{snapshot['catalogRevision']}`. Pack revision",
        f"inspected when generated: `{snapshot['packRevision']}`. Source manifests and commits",
        "are recorded in `config/application-scope-snapshot.json`.",
        f"**{different_pins} of {len(records)}** consumer pins differ from that pack revision;",
        "this map does not silently upgrade them.",
        "",
        "## Repository and area profiles",
        "",
        "| Profile / repositories | Areas and trigger | Relevant methods | Evidence boundary |",
        "|---|---|---|---|",
    ]
    for profile in scope["profiles"]:
        repos = ", ".join(f"`{repo_id}`" for repo_id in profile["repositories"])
        methods = ", ".join(f"`{skill}`" for skill in profile["skills"])
        lines.append(f"| **{profile['id']}**: {repos} | {profile['areas']} Trigger: {profile['trigger']} | {methods} | {profile['evidenceBoundary']} |")
    lines += [
        "", "## Declared consumer opt-ins at the inspected revisions", "",
        "| Repository | Commit | Pack pin | Declared enabled skills |",
        "|---|---|---|---|",
    ]
    for profile in scope["profiles"]:
        for repo_id in profile["repositories"]:
            record = records[repo_id]
            pin = record["packRevision"][:12]
            if record["packRevision"] != snapshot["packRevision"]:
                pin += " (older/different)"
            enabled = ", ".join(f"`{skill}`" for skill in record["enabledSkills"])
            lines.append(f"| `{repo_id}` | `{record['revision'][:12]}` | `{pin}` | {enabled} |")
    lines += [
        "", "## Task selection and completion", "",
        "1. Identify the owning repository, changed area, manifest revision, and authority.",
        "2. Use a relevant method only if the manifest enables it and the pinned pack permits it.",
        "   Resolve an older pin at its own revision; do not apply today's registry retroactively.",
        "3. Match evidence to the claim: code tests, physical lab safety, institution approval,",
        "   deployment, and sustained operation are different checks.",
        "4. Record the exact checks and omitted checks. A skill, manifest, or generated map",
        "   never grants permission to merge, publish, enroll devices, or deploy.",
        "", "## Refresh and verification", "",
        "From `psdc-agent-skills`, refresh after fetching the workspace and consumer",
        "repositories' `origin/main` refs:", "",
        "```powershell",
        "python scripts/Build-ApplicationScope.py --refresh --workspace-root C:\\path\\to\\psdc-workspace",
        "python scripts/Build-ApplicationScope.py --check --workspace-root C:\\path\\to\\psdc-workspace",
        "```", "",
        "`--check` without a workspace verifies the committed snapshot against the registry",
        "and generated document. With a workspace it additionally detects source drift.",
        "A new skill-pack commit alone is ignored when its consumer manifest digest is unchanged;",
        "a changed manifest still fails the check.",
        "Neither mode tests actual agent behavior or product readiness.", "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace-root", type=Path)
    parser.add_argument("--refresh", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("Application scope self-test passed")
        return
    if args.refresh == args.check:
        parser.error("choose exactly one of --refresh or --check")
    scope, registry = read_policy()
    if args.refresh:
        if not args.workspace_root:
            parser.error("--refresh requires --workspace-root")
        snapshot = snapshot_from_workspace(args.workspace_root.resolve(), scope,
                                           git(ROOT, "rev-parse", "origin/main").strip())
        validate_snapshot(snapshot, scope, registry)
        SNAPSHOT.write_text(json.dumps(snapshot, indent=2) + "\n", encoding="utf-8")
        DOCUMENT.write_text(render(snapshot, scope), encoding="utf-8")
    else:
        snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
        validate_snapshot(snapshot, scope, registry)
        if args.workspace_root:
            current = snapshot_from_workspace(args.workspace_root.resolve(), scope,
                                              snapshot["packRevision"])
            if not same_sources(current, snapshot):
                raise ValueError("Workspace or consumer manifests differ from committed snapshot; refresh deliberately")
        if DOCUMENT.read_text(encoding="utf-8").replace("\r\n", "\n") != render(snapshot, scope):
            raise ValueError("Application-scope document is out of sync with its sources")
    print(f"Application scope passed: {len(snapshot['repositories'])} repositories, {len(scope['profiles'])} profiles")


if __name__ == "__main__":
    main()
