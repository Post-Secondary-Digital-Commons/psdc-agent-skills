"""Synthetic, offline contract checks for the local candidate triage runner."""

import hashlib
import importlib.util
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("triage", Path(__file__).with_name("Triage-LocalEvidence.py"))
triage = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(triage)


class TriageTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.repo = self.root / "psdc-cloud"
        self.repo.mkdir()
        for args in (
            ("init", "-q"),
            ("config", "user.name", "Synthetic Test"),
            ("config", "user.email", "test@example.invalid"),
            ("remote", "add", "origin", "https://github.com/example/psdc-cloud.git"),
        ):
            subprocess.run(["git", "-C", str(self.repo), *args], check=True, capture_output=True)
        (self.repo / "spec.md").write_text(
            "# Test\nA document describes a scheduler.\nDeployment evidence is absent.\n",
            encoding="utf-8",
        )
        subprocess.run(["git", "-C", str(self.repo), "add", "spec.md"], check=True, capture_output=True)
        subprocess.run(["git", "-C", str(self.repo), "commit", "-qm", "fixture"], check=True, capture_output=True)
        commit = subprocess.run(["git", "-C", str(self.repo), "rev-parse", "HEAD"],
                                check=True, capture_output=True, text=True).stdout.strip()
        excerpt = "A document describes a scheduler.\nDeployment evidence is absent."
        self.item = {"repository": "psdc-cloud", "commit": commit, "path": "spec.md",
                     "startLine": 2, "endLine": 3, "text": excerpt,
                     "sha256": hashlib.sha256(excerpt.encode()).hexdigest()}

    def test_git_excerpts_and_citations_are_independent_of_model(self):
        triage.validate_source(self.item, self.repo)
        result = {"findings": [{"claim": "Deployment needs evidence", "basis": "inference",
                                "citation": {"path": "spec.md", "startLine": 2, "endLine": 3},
                                "uncertainty": "No environment was inspected."}]}
        triage.validate_findings(result, self.item)
        bad_item = {**self.item, "text": self.item["text"] + " fabricated"}
        with self.assertRaises(ValueError):
            triage.validate_source(bad_item, self.repo)
        bad_result = json.loads(json.dumps(result))
        bad_result["findings"][0]["citation"]["startLine"] = 1
        with self.assertRaises(ValueError):
            triage.validate_findings(bad_result, self.item)
        bad_result["findings"][0]["citation"]["startLine"] = 2
        bad_result["findings"][0]["readiness"] = "deployed"
        with self.assertRaises(triage.jsonschema.ValidationError):
            triage.validate_findings(bad_result, self.item)

    def test_one_ollama_request_then_verified_cache_hit(self):
        result = {"findings": []}
        response = {"model": triage.MODEL, "done": True,
                    "message": {"content": json.dumps(result)}, "eval_count": 4}
        cache = self.root / "cache"
        with patch.object(triage, "ollama_json", return_value=response) as api:
            first = triage.triage(self.item, "http://127.0.0.1:11434", cache, "a" * 64, 4096)
            second = triage.triage(self.item, "http://127.0.0.1:11434", cache, "a" * 64, 4096)
        self.assertEqual(api.call_count, 1)
        self.assertFalse(first["cacheHit"])
        self.assertTrue(second["cacheHit"])
        self.assertEqual(second["status"], "candidate_review_only")
        self.assertEqual(len(list(cache.glob("*.json"))), 1)

    def test_nonlocal_ollama_endpoint_is_rejected_before_network_access(self):
        with patch.object(triage.urllib.request, "build_opener") as opener:
            with self.assertRaisesRegex(ValueError, "local loopback"):
                triage.ollama_json("https://example.org", "/api/chat", {"private": "excerpt"})
            opener.assert_not_called()


if __name__ == "__main__":
    unittest.main()
