#!/usr/bin/env python3
"""Read-only, revision-bound candidate finding triage through local Ollama.

Input sources are Git objects. Ollama receives only verified excerpts and has no
tools. Output is candidate review material, never an authority or readiness state.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import urllib.request
from urllib.parse import urlsplit
from pathlib import Path, PurePosixPath

import jsonschema


MODEL = "qwen3.5:4b-q4_K_M"
PROMPT_VERSION = "psdc-triage-v1"
RESULT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["findings"],
    "properties": {
        "findings": {
            "type": "array",
            "maxItems": 8,
            "items": {
                "type": "object",
                "additionalProperties": False,
                "required": ["claim", "basis", "citation", "uncertainty"],
                "properties": {
                    "claim": {"type": "string", "minLength": 1},
                    "basis": {"enum": ["documented_claim", "inference", "assumption", "recommendation"]},
                    "citation": {
                        "type": "object", "additionalProperties": False,
                        "required": ["path", "startLine", "endLine"],
                        "properties": {
                            "path": {"type": "string"},
                            "startLine": {"type": "integer", "minimum": 1},
                            "endLine": {"type": "integer", "minimum": 1},
                        },
                    },
                    "uncertainty": {"type": "string", "minLength": 1},
                },
            },
        }
    },
}
INPUT_SCHEMA = {
    "type": "object", "additionalProperties": False, "required": ["items"],
    "properties": {"items": {"type": "array", "minItems": 1, "items": {
        "type": "object", "additionalProperties": False,
        "required": ["repository", "commit", "path", "startLine", "endLine", "text", "sha256"],
        "properties": {
            "repository": {"type": "string", "pattern": "^[a-z][a-z0-9-]*$"},
            "commit": {"type": "string", "pattern": "^[a-f0-9]{40}$"},
            "path": {"type": "string", "minLength": 1},
            "startLine": {"type": "integer", "minimum": 1},
            "endLine": {"type": "integer", "minimum": 1},
            "text": {"type": "string", "minLength": 1},
            "sha256": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
        },
    }}},
}
SYSTEM = (
    "You produce candidate findings for a human PSDC reviewer. Use only the supplied "
    "excerpt. Cite its exact path and line numbers. Report uncertainty. An overlay "
    "cannot silently change a common contract. A document, schema check, or "
    "prototype does not establish deployment. Return an empty findings array if "
    "there is no supported finding. Never claim acceptance, deployment, or "
    "production status from this excerpt."
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, check=False)
    if result.returncode:
        raise ValueError(f"Git source lookup failed in {repo}: {result.stderr.decode(errors='replace').strip()}")
    return result.stdout


def validate_source(item: dict, repo: Path) -> None:
    path = item["path"]
    posix = PurePosixPath(path)
    if (posix.is_absolute() or any(part in {"", ".", ".."} for part in path.split("/"))
            or "\\" in path or ":" in path or path.startswith("-")):
        raise ValueError(f"Unsafe repository path: {path}")
    if item["endLine"] < item["startLine"]:
        raise ValueError("endLine precedes startLine")
    remote = git(repo, "remote", "get-url", "origin").decode().strip()
    slug = re.split(r"[/:]", remote.removesuffix(".git"))[-1].lower()
    if slug != item["repository"]:
        raise ValueError(f"Repository identity differs from origin: {item['repository']} != {slug}")
    source = git(repo, "show", f"{item['commit']}:{path}").decode("utf-8")
    lines = source.splitlines()
    if item["endLine"] > len(lines):
        raise ValueError(f"Line span exceeds {path} at {item['commit']}")
    excerpt = "\n".join(lines[item["startLine"] - 1:item["endLine"]])
    if item["text"] != excerpt or item["sha256"] != digest(excerpt.encode("utf-8")):
        raise ValueError(f"Frozen excerpt or hash differs from Git source: {path}")


def validate_findings(result: dict, item: dict) -> None:
    jsonschema.Draft202012Validator(RESULT_SCHEMA).validate(result)
    for finding in result["findings"]:
        cite = finding["citation"]
        if (cite["path"] != item["path"] or cite["startLine"] < item["startLine"]
                or cite["endLine"] > item["endLine"] or cite["endLine"] < cite["startLine"]):
            raise ValueError(f"Citation leaves verified excerpt: {cite}")


def ollama_json(url: str, endpoint: str, payload: dict | None = None) -> dict:
    parsed = urlsplit(url)
    if (parsed.scheme != "http" or parsed.hostname not in {"127.0.0.1", "::1", "localhost"}
            or parsed.username or parsed.password or parsed.path or parsed.query or parsed.fragment):
        raise ValueError("Ollama URL must be an unadorned local loopback HTTP origin")
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        f"{url.rstrip('/')}{endpoint}", data=data,
        headers={"Content-Type": "application/json"},
        method="POST" if data is not None else "GET",
    )
    # Refuse redirects so even a local endpoint cannot forward private excerpts.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, request, fp, code, msg, headers, newurl):
            raise ValueError("Ollama redirected the request; refusing to forward excerpts")

    with urllib.request.build_opener(NoRedirect()).open(request, timeout=120) as response:
        return json.load(response)


def model_digest(url: str) -> str:
    matches = [entry for entry in ollama_json(url, "/api/tags")["models"] if entry["name"] == MODEL]
    if len(matches) != 1 or not re.fullmatch(r"[a-f0-9]{64}", matches[0]["digest"]):
        raise ValueError(f"Exact Ollama model tag and digest required: {MODEL}")
    return matches[0]["digest"]


def triage(item: dict, url: str, cache: Path, model_sha: str, context: int) -> dict:
    settings = {"temperature": 0, "num_ctx": context}
    key = digest(json.dumps({"item": item, "modelDigest": model_sha,
                             "promptVersion": PROMPT_VERSION, "systemPrompt": SYSTEM,
                             "schema": RESULT_SCHEMA,
                             "settings": settings}, sort_keys=True).encode("utf-8"))
    target = cache / f"{key}.json"
    if target.exists():
        record = json.loads(target.read_text(encoding="utf-8"))
        validate_findings(record["result"], item)
        return {**record, "cacheHit": True}
    message = json.dumps(item, ensure_ascii=False, sort_keys=True)
    response = ollama_json(url, "/api/chat", {
        "model": MODEL, "stream": False, "think": False, "format": RESULT_SCHEMA,
        "options": settings, "keep_alive": "10m",
        "messages": [{"role": "system", "content": SYSTEM},
                     {"role": "user", "content": message}],
    })
    if response.get("done") is not True or response.get("model") != MODEL:
        raise ValueError("Unexpected or incomplete Ollama response")
    result = json.loads(response["message"]["content"])
    validate_findings(result, item)
    record = {"status": "candidate_review_only", "input": item, "model": MODEL,
              "modelDigest": model_sha, "context": context, "promptVersion": PROMPT_VERSION,
              "result": result, "cacheHit": False,
              "usage": {key: response.get(key) for key in
                        ("prompt_eval_count", "eval_count", "total_duration")}}
    cache.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(record, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return record


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Frozen JSON containing an items array")
    parser.add_argument("--repo", action="append", required=True, metavar="ID=PATH")
    parser.add_argument("--cache", type=Path, required=True, help="Local candidate-result cache")
    parser.add_argument("--ollama-url", default="http://127.0.0.1:11434")
    parser.add_argument("--context", type=int, choices=(4096, 8192), default=4096)
    parser.add_argument("--validate-only", action="store_true", help="Verify sources without model calls")
    args = parser.parse_args()
    document = json.loads(args.input.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(INPUT_SCHEMA).validate(document)
    repos = {}
    for spec in args.repo:
        repo_id, sep, location = spec.partition("=")
        if not sep or not repo_id or not location or repo_id in repos:
            parser.error("--repo must be a unique ID=PATH")
        repos[repo_id] = Path(location).resolve(strict=True)
    for item in document["items"]:
        if item["repository"] not in repos:
            raise ValueError(f"Missing --repo mapping: {item['repository']}")
        validate_source(item, repos[item["repository"]])
    if args.validate_only:
        print(json.dumps({"validatedSources": len(document["items"])}))
        return
    sha = model_digest(args.ollama_url)
    for item in document["items"]:
        print(json.dumps(triage(item, args.ollama_url, args.cache, sha, args.context),
                         ensure_ascii=False), flush=True)


if __name__ == "__main__":
    try:
        main()
    except (ValueError, json.JSONDecodeError, jsonschema.ValidationError) as exc:
        print(f"triage error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
