"""Integration checks for consumer pin and worktree identity validation."""

from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts/Validate-Consumer.py"
PACK_REVISION = subprocess.check_output(
    ["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True
).strip()


class ConsumerValidationTests(unittest.TestCase):
    def make_consumer(self, parent: Path, pin: str) -> Path:
        source = parent / "source"
        source.mkdir()
        subprocess.run(["git", "init", "-q", str(source)], check=True)
        (source / "README.md").write_text("# Consumer\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(source), "add", "README.md"], check=True)
        subprocess.run(
            ["git", "-C", str(source), "-c", "user.name=Test",
             "-c", "user.email=test@example.invalid", "commit", "-qm", "fixture"],
            check=True,
        )
        # Exercise a real linked worktree whose directory differs from origin.
        checkout = parent / "independent-worktree-name"
        subprocess.run(
            ["git", "-C", str(source), "worktree", "add", "-q", "--detach", str(checkout)],
            check=True,
        )
        subprocess.run(
            ["git", "-C", str(source), "remote", "add", "origin",
             "https://github.com/Post-Secondary-Digital-Commons/psdc-cloud.git"],
            check=True,
        )
        manifest = {
            "schemaVersion": 1,
            "repository": {
                "id": "psdc-cloud", "authority": "common",
                "context": "cloud", "lifecycle": "specification",
            },
            "skillPack": {
                "repository": "https://github.com/Post-Secondary-Digital-Commons/psdc-agent-skills",
                "revision": pin,
                "registry": "config/skill-registry.yaml",
                "policy": "docs/governance/AUTHORITY-AND-EVIDENCE.md",
            },
            "enabledSkills": ["psdc-evidence-audit"],
            "entrypoints": ["README.md"],
            "boundary": {
                "changeScope": "this-repository",
                "decisionAuthority": "psdc-architecture",
                "contractAuthority": "psdc-architecture",
            },
        }
        path = checkout / ".psdc/agent-skills.yaml"
        path.parent.mkdir()
        path.write_text(yaml.safe_dump(manifest), encoding="utf-8")
        return path

    def validate(self, manifest: Path, skill_root: Path = ROOT) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["python", str(VALIDATOR), str(manifest), "--skill-root", str(skill_root)],
            text=True, capture_output=True, check=False,
        )

    def make_pack_worktree(self, parent: Path) -> Path:
        checkout = parent / "pack-policy-checkout"
        subprocess.run(
            ["git", "-C", str(ROOT), "worktree", "add", "-q", "--detach", str(checkout),
             PACK_REVISION],
            check=True,
        )
        return checkout

    def test_matching_pin_accepts_independent_worktree_name(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = self.validate(self.make_consumer(Path(temporary), PACK_REVISION))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validated psdc-cloud", result.stdout)

    def test_mismatched_pin_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            result = self.validate(self.make_consumer(Path(temporary), "0" * 40))
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("skill pack pin", result.stderr)
        self.assertIn("differs from skill root HEAD", result.stderr)

    def test_self_manifest_is_explicit_exception(self) -> None:
        result = self.validate(ROOT / ".psdc/agent-skills.yaml")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Validated psdc-agent-skills", result.stdout)

    def test_dirty_pack_policy_rejected(self) -> None:
        for relative_path in (
            "config/skill-registry.yaml", "schemas/consumer-manifest.schema.json"
        ):
            with self.subTest(path=relative_path), tempfile.TemporaryDirectory() as temporary:
                parent = Path(temporary)
                pack = self.make_pack_worktree(parent)
                consumer = self.make_consumer(parent, PACK_REVISION)
                policy = pack / relative_path
                policy.write_text(policy.read_text(encoding="utf-8") + "\n", encoding="utf-8")
                result = self.validate(consumer, pack)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("differs from HEAD", result.stderr)

    def test_noncanonical_manifest_in_pack_root_is_not_self_exception(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            pack = self.make_pack_worktree(Path(temporary))
            alternate = pack / ".psdc/other-agent-skills.yaml"
            alternate.write_text(
                (pack / ".psdc/agent-skills.yaml").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            result = self.validate(alternate, pack)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("skill pack pin", result.stderr)


if __name__ == "__main__":
    unittest.main()
