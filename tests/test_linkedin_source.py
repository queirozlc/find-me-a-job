import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).parents[1] / "scripts" / "linkedin_source.py"
SPEC = importlib.util.spec_from_file_location("linkedin_source", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class CandidateFilterTest(unittest.TestCase):
    def test_week_recency_urls_use_verified_linkedin_values(self):
        self.assertIn("f_TPR=r604800", MODULE.jobs_url("typescript", "week"))
        self.assertIn("datePosted=%5B%22past-week%22%5D", MODULE.posts_url("typescript", "week"))

    def test_valid_remote_typescript_role_reaches_preflight(self):
        candidate = {
            "title": "Senior TypeScript Engineer",
            "company": "Example",
            "location": "Brazil (Remote)",
            "header": "Posted 20 minutes ago",
            "description": "Build Node.js services with TypeScript for a remote LATAM team.",
            "apply_url": "https://example.com/jobs/123",
        }

        status, reasons, review = MODULE.classify_candidate(candidate, ["BairesDev"])

        self.assertEqual("preflight", status)
        self.assertEqual([], reasons)
        self.assertEqual([], review)

    def test_deterministic_knockouts_reject_before_preflight(self):
        candidate = {
            "title": "Senior JavaScript Engineer",
            "company": "BairesDev",
            "location": "Brazil (Hybrid)",
            "header": "Reposted 1 hour ago · Over 100 people clicked apply",
            "description": "JavaScript and TypeScript role.",
            "apply_url": "https://empresa.gupy.io/jobs/123",
        }

        status, reasons, _review = MODULE.classify_candidate(candidate, ["BairesDev"])

        self.assertEqual("rejected", status)
        self.assertEqual(
            {
                "reposted",
                "over_100_applicants",
                "company_blocklist",
                "gupy",
                "hybrid_or_onsite",
            },
            set(reasons),
        )

    def test_event_sink_streams_preflight_and_writes_completion_sentinel(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "source"
            sink = MODULE.EventSink(output)
            sink.emit({"event": "candidate", "job_id": "1", "status": "preflight"})
            sink.emit({"event": "candidate", "job_id": "2", "status": "rejected"})
            sink.emit({"event": "run_finished", "failures": [], "ok": True})

            self.assertEqual(1, len((output / "preflight.jsonl").read_text().splitlines()))
            completion = (output / "run.complete.json").read_text()
            self.assertIn('"event": "run_finished"', completion)
            self.assertIn('"ok": true', completion)


if __name__ == "__main__":
    unittest.main()
