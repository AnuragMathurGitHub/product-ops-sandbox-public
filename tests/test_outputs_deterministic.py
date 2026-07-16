"""The repo's headline claim, as a test: the deterministic scripts reproduce the
committed outputs byte for byte from the committed sample data."""

import contextlib
import importlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

DETERMINISTIC_MODULES = [
    "analyze_feedback",
    "score_roadmap",
    "summarize_metrics",
    "summarize_okrs",
    "summarize_releases",
]


class DeterminismTests(unittest.TestCase):
    def test_deterministic_scripts_reproduce_committed_outputs(self):
        for name in DETERMINISTIC_MODULES:
            with self.subTest(script=name):
                module = importlib.import_module(name)
                committed = module.OUTPUT_FILE.read_text(encoding="utf-8")
                original = module.OUTPUT_FILE
                with tempfile.TemporaryDirectory() as tmp:
                    module.OUTPUT_FILE = Path(tmp) / original.name
                    try:
                        with contextlib.redirect_stdout(io.StringIO()):
                            module.main()
                        regenerated = module.OUTPUT_FILE.read_text(encoding="utf-8")
                    finally:
                        module.OUTPUT_FILE = original
                self.assertEqual(regenerated, committed)


if __name__ == "__main__":
    unittest.main()
