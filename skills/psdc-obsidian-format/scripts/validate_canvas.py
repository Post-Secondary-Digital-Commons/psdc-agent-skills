#!/usr/bin/env python3
"""Check JSON Canvas structure and local file targets without Obsidian."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


SKIP = {".git", "node_modules", ".venv", "venv", "vendor", "dist", "build"}
NODE_TYPES = {"text", "file", "link", "group"}


def check_document(document: object, vault: Path) -> list[str]:
    if not isinstance(document, dict):
        return ["Canvas root must be an object"]
    nodes = document.get("nodes", [])
    edges = document.get("edges", [])
    if not isinstance(nodes, list) or not isinstance(edges, list):
        return ["Canvas nodes and edges must be arrays"]
    errors: list[str] = []
    seen: set[str] = set()
    node_ids: set[str] = set()
    for index, node in enumerate(nodes):
        if not isinstance(node, dict):
            errors.append(f"Node {index} must be an object")
            continue
        identifier = node.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"Node {index} has no ID")
        elif identifier in seen:
            errors.append(f"Duplicate ID: {identifier}")
        else:
            seen.add(identifier)
            node_ids.add(identifier)
        kind = node.get("type")
        if not isinstance(kind, str) or kind not in NODE_TYPES:
            errors.append(f"Node {index} has invalid type: {kind}")
        for field in ("x", "y", "width", "height"):
            if type(node.get(field)) is not int:
                errors.append(f"Node {index} needs integer {field}")
        content_field = {"text": "text", "file": "file", "link": "url"}.get(kind) if isinstance(kind, str) else None
        if content_field and not isinstance(node.get(content_field), str):
            errors.append(f"Node {index} needs {content_field}")
        if kind == "file" and isinstance(node.get("file"), str):
            path = (vault / node["file"]).resolve()
            if not path.is_relative_to(vault.resolve()) or not path.is_file():
                errors.append(f"Node {index} file target is missing or outside the vault")
    for index, edge in enumerate(edges):
        if not isinstance(edge, dict):
            errors.append(f"Edge {index} must be an object")
            continue
        identifier = edge.get("id")
        if not isinstance(identifier, str) or not identifier:
            errors.append(f"Edge {index} has no ID")
        elif identifier in seen:
            errors.append(f"Duplicate ID: {identifier}")
        else:
            seen.add(identifier)
        for field in ("fromNode", "toNode"):
            if not isinstance(edge.get(field), str) or edge[field] not in node_ids:
                errors.append(f"Edge {index} has unresolved {field}")
    return errors


def self_test() -> None:
    sample = {"nodes": [
        {"id": "a", "type": "text", "x": 0, "y": 0, "width": 200, "height": 100, "text": "Source"},
        {"id": "b", "type": "text", "x": 300, "y": 0, "width": 200, "height": 100, "text": "View"},
    ], "edges": [{"id": "c", "fromNode": "a", "toNode": "b"}]}
    if check_document(sample, Path.cwd()):
        raise AssertionError("Valid Canvas fixture failed")
    broken = json.loads(json.dumps(sample))
    broken["edges"][0]["toNode"] = "absent"
    if not any("unresolved toNode" in error for error in check_document(broken, Path.cwd())):
        raise AssertionError("Dangling Canvas edge was accepted")
    broken["edges"][0]["id"] = "a"
    if not any("Duplicate ID" in error for error in check_document(broken, Path.cwd())):
        raise AssertionError("Duplicate Canvas ID was accepted")
    malformed = json.loads(json.dumps(sample))
    malformed["nodes"][0]["type"] = []
    if not any("invalid type" in error for error in check_document(malformed, Path.cwd())):
        raise AssertionError("Malformed Canvas node type was accepted")
    print("Canvas positive and negative fixtures passed")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    if args.vault is None:
        parser.error("provide a vault root or --self-test")
    vault = args.vault.resolve()
    if not vault.is_dir():
        parser.error("vault root does not exist")
    files = [path for path in vault.rglob("*.canvas") if not SKIP.intersection(path.relative_to(vault).parts)]
    failures = []
    for path in files:
        try:
            errors = check_document(json.loads(path.read_text(encoding="utf-8")), vault)
        except (OSError, json.JSONDecodeError) as exc:
            errors = [str(exc)]
        failures.extend(f"{path.relative_to(vault)}: {error}" for error in errors)
    for failure in failures:
        print(failure)
    print(f"Canvas check: {len(files)} files, {len(failures)} findings")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
