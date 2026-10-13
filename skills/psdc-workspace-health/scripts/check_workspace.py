#!/usr/bin/env python3
"""Run PSDC workspace structural checks without changing the checkout."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


PACK_ROOT = Path(__file__).resolve().parents[3]
EXPECTED_REMOTE = re.compile(
    r"(?:https://github\.com/|git@github\.com:|ssh://git@github\.com/)"
    r"post-secondary-digital-commons/psdc-workspace(?:\.git)?$",
    re.IGNORECASE,
)


def run(command: list[str], *, cwd: Path | None = None, timeout: int = 180) -> dict:
    try:
        result = subprocess.run(
            command, cwd=cwd, text=True, encoding="utf-8", errors="replace",
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"status": "failed", "detail": str(exc)}
    return {
        "status": "passed" if result.returncode == 0 else "failed",
        "exitCode": result.returncode,
        "detail": result.stdout[-2000:].strip(),
    }


def git(workspace: Path, *arguments: str) -> str:
    result = run(["git", "-C", str(workspace), *arguments])
    if result["status"] != "passed":
        raise ValueError(f"Cannot inspect workspace Git {arguments}: {result['detail']}")
    return result["detail"].strip()


def inspect(workspace: Path, checkout: Path) -> dict:
    if not (workspace / "repos.yaml").is_file():
        raise ValueError("Workspace catalog repos.yaml is missing")
    if not checkout.is_dir():
        raise ValueError("Checkout parent is missing")
    remote = git(workspace, "remote", "get-url", "origin")
    if not EXPECTED_REMOTE.fullmatch(remote):
        raise ValueError("Workspace origin does not match the PSDC workspace repository")
    head = git(workspace, "rev-parse", "HEAD")
    baseline = git(workspace, "rev-parse", "origin/main")
    dirty = bool(git(workspace, "status", "--porcelain"))
    report: dict = {
        "schemaVersion": 1,
        "workspace": {"head": head, "originMain": baseline, "stale": head != baseline, "dirty": dirty},
        "checks": {},
        "evidenceBoundary": "Structural and artifact checks only; no runtime or deployment claim",
    }

    generator = workspace / "scripts/Build-WorkspaceCommandCenter.py"
    if generator.is_file():
        with tempfile.TemporaryDirectory(prefix="psdc-workspace-health-") as temporary:
            command = [sys.executable, str(generator), "--workspace-root", str(workspace),
                       "--checkout-root", str(checkout), "--output-root", temporary]
            check = run(command, cwd=workspace)
            if check["status"] == "passed":
                status_file = Path(temporary) / "registry/generated-workspace-status.json"
                if status_file.is_file():
                    snapshot = json.loads(status_file.read_text(encoding="utf-8"))
                    check["generatedViews"] = len(list((Path(temporary) / "Maps/Generated").glob("*.md")))
                    check["online"] = snapshot.get("online")
                    check["missingCheckouts"] = [
                        item["id"] for item in snapshot.get("commonRepositories", [])
                        + snapshot.get("institutionOverlays", [])
                        if not item.get("exists") and item.get("declaredStatus") != "planned"
                    ]
                    if check["missingCheckouts"]:
                        check["status"] = "failed"
                else:
                    check = {"status": "failed", "detail": "Generator omitted status artifact"}
            report["checks"]["commandCenter"] = check
    else:
        report["checks"]["commandCenter"] = {"status": "not_run", "detail": "Generator absent at inspected HEAD"}

    link_script = workspace / "scripts/Test-Documentation.ps1"
    shell = shutil.which("pwsh")
    if link_script.is_file() and shell:
        report["checks"]["documentation"] = run(
            [shell, "-NoProfile", "-File", str(link_script), "-Root", str(checkout)],
            cwd=workspace,
        )
    else:
        report["checks"]["documentation"] = {
            "status": "not_run", "detail": "Documentation checker or PowerShell 7 unavailable",
        }

    report["checks"]["skillScope"] = run(
        [sys.executable, str(PACK_ROOT / "scripts/Build-ApplicationScope.py"),
         "--check", "--workspace-root", str(workspace),
         "--checkout-root", str(checkout)], cwd=PACK_ROOT,
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workspace-root", type=Path, required=True)
    parser.add_argument("--checkout-root", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = inspect(args.workspace_root.resolve(), args.checkout_root.resolve())
    except ValueError as exc:
        print(json.dumps({"schemaVersion": 1, "error": str(exc)}, indent=2))
        return 2
    print(json.dumps(report, indent=2))
    return 0 if all(item["status"] == "passed" for item in report["checks"].values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
