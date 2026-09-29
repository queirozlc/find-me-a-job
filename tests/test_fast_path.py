import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest


ROOT = Path(__file__).parents[1]


def load_script(name: str):
    path = ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


GATE = load_script("resume_gate")
SENTINEL = load_script("worker_sentinel")
IDENTITY = load_script("cache_linkedin_identity")


class ResumeGateTest(unittest.TestCase):
    def setUp(self):
        self.base = (ROOT / "resumes" / "base-en.tex").read_text(encoding="utf-8")

    def test_base_parser_preserves_all_roles_bullets_and_metrics(self):
        self.assertEqual(4, len(GATE.roles(self.base)))
        self.assertEqual(16, len(GATE.bullets(self.base)))
        self.assertEqual({"7%", "15%", "18%", "20%", "25%", "26%", "33%"}, GATE.metrics(self.base))

    def test_code_review_claim_is_blocked_when_new(self):
        tailored = self.base.replace(
            "high-quality code in daily delivery",
            "high-quality code and upheld standards in code reviews",
        )
        claims = json.loads((ROOT / "claim-allowlist.json").read_text(encoding="utf-8"))
        failures = GATE.protected_claim_failures(self.base, tailored, claims)
        self.assertEqual(1, len(failures))
        self.assertIn("code-review", failures[0])

    def test_required_token_must_be_in_skills_and_experience(self):
        checks, _delta = GATE.check_resume(
            self.base,
            self.base,
            GATE.latex_to_text(self.base),
            {"language": "en", "required_tokens": ["Fastify"]},
            {"snapshot": GATE.latex_to_text(self.base)},
            {"protected_claims": []},
        )
        token_check = next(item for item in checks if item["name"] == "required_token_placement")
        self.assertEqual("FAIL", token_check["status"])
        self.assertIn("Skills and Experience", token_check["failures"][0])


class IdentityCacheTest(unittest.TestCase):
    def test_profile_validation_rejects_non_profile_content(self):
        with self.assertRaises(IDENTITY.IdentityCacheError):
            IDENTITY.validate_profile("https://linkedin.com", "Feed")


class WorkerSentinelTest(unittest.TestCase):
    def test_complete_sentinel_requires_and_verifies_artifacts(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "report.md"
            artifact.write_text("done\n", encoding="utf-8")
            sentinel = root / "task.complete.json"
            SENTINEL.write_sentinel(sentinel, "quill-example", "complete", [artifact])
            SENTINEL.verify_sentinel(sentinel, "quill-example")

    def test_complete_sentinel_rejects_empty_artifact(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            artifact = root / "empty.md"
            artifact.touch()
            with self.assertRaises(SENTINEL.SentinelError):
                SENTINEL.write_sentinel(root / "task.complete.json", "sieve-example", "complete", [artifact])


if __name__ == "__main__":
    unittest.main()
