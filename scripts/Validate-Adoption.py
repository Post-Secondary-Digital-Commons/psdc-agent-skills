#!/usr/bin/env python3
"""Validate a PSDC component's proposed or accepted upstream-adoption record."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import jsonschema


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schemas/upstream-adoption-record.schema.json").read_text(encoding="utf-8"))
jsonschema.Draft202012Validator.check_schema(SCHEMA)
VALIDATOR = jsonschema.Draft202012Validator(SCHEMA, format_checker=jsonschema.FormatChecker())


def validate(record: dict) -> None:
    VALIDATOR.validate(record)
    if record["status"] != "accepted":
        return
    if record["selection"]["mode"] != "build":
        selected = record["selection"]
        if not any(
            candidate["project"] == selected["project"]
            and candidate["sourceRevision"] == selected["sourceRevision"]
            for candidate in record["candidates"]
        ):
            raise ValueError("Accepted upstream selection must match a reviewed candidate and revision")
    if any(
        token in candidate["sourceRevision"].lower()
        for candidate in record["candidates"]
        for token in ("pending", "unknown", "latest")
    ):
        raise ValueError("Accepted record contains an unpinned candidate revision")


def self_test() -> None:
    example = {
        "schemaVersion": 1,
        "componentId": "vs01.lab-worker",
        "repository": "psdc-compute",
        "scope": "common",
        "status": "proposed",
        "decisionOwner": "PSDC Compute Fabric Working Group",
        "governingRefs": ["ADR-0026"],
        "candidates": [],
        "selection": {"mode": "adapter", "rationale": "Exact upstream review remains pending"},
        "upstreamProvides": [],
        "psdcOwns": ["institutional admission"],
        "excluded": [],
        "evidence": [],
        "maintenance": {"owner": "unassigned", "updatePlan": "pending", "replacementTrigger": "pending"},
        "openGates": ["source review"],
    }
    validate(example)
    attempted_acceptance = {**example, "status": "accepted"}
    try:
        validate(attempted_acceptance)
    except jsonschema.ValidationError:
        pass
    else:
        raise AssertionError("Unreviewed proposed record was accepted")
    accepted = {
        **attempted_acceptance,
        "decisionRef": "ADR-9999-test-only",
        "candidates": [{
            "project": "synthetic-project",
            "sourceUrl": "https://example.org/source",
            "sourceRevision": "0123456789abcdef",
            "licenseEvidence": "SPDX: MIT",
            "fit": "synthetic match",
            "limitations": "test only",
        }],
        "selection": {
            "mode": "adapter", "project": "synthetic-project",
            "sourceRevision": "0123456789abcdef", "rationale": "synthetic test decision"
        },
        "evidence": [{
            "method": "synthetic test", "artifact": "in-memory fixture", "revision": "fixture-v1",
            "result": "passed", "limitations": "not a real adoption review",
        }],
    }
    validate(accepted)
    accepted["selection"] = {**accepted["selection"], "sourceRevision": "ffffffffffffffff"}
    try:
        validate(accepted)
    except ValueError:
        pass
    else:
        raise AssertionError("Unreviewed selected revision was accepted")
    print("Upstream adoption record validation self-test passed")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("records", type=Path, nargs="*")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
    for path in args.records:
        validate(json.loads(path.read_text(encoding="utf-8")))
        print(f"Validated {path}")
    if not args.self_test and not args.records:
        parser.error("provide record files or --self-test")


if __name__ == "__main__":
    main()
