import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import tasks


class ScanTests(unittest.TestCase):
    def test_scan_flags_seeded_problems(self):
        # The bad strings are assembled at runtime so this test file stays clean
        # when the scanner reads the repo.
        non_ascii = "em dash: " + chr(0x2014)
        wording = "this part is " + "coming " + "soon"
        secret = "key = " + "sk" + "-abc123"
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bad.md"
            bad.write_text(f"{non_ascii}\n{wording}\n{secret}\n", encoding="utf-8")
            findings = tasks.scan_tree(Path(tmp))
        self.assertEqual(len(findings), 3)
        self.assertIn("non-ASCII", findings[0])
        self.assertIn("forbidden wording", findings[1])
        self.assertIn("secret-shaped", findings[2])

    def test_scan_passes_on_a_clean_tree(self):
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "good.md"
            good.write_text("A perfectly ordinary line.\n", encoding="utf-8")
            self.assertEqual(tasks.scan_tree(Path(tmp)), [])

    def test_scan_skips_directories_and_files_on_the_skip_lists(self):
        bad_line = "coming " + "soon"
        with tempfile.TemporaryDirectory() as tmp:
            private = Path(tmp) / ".private"
            private.mkdir()
            (private / "notes.md").write_text(bad_line + "\n", encoding="utf-8")
            (Path(tmp) / "tasks.py").write_text(bad_line + "\n", encoding="utf-8")
            self.assertEqual(tasks.scan_tree(Path(tmp)), [])

    def test_the_repo_itself_scans_clean(self):
        self.assertEqual(tasks.scan_tree(tasks.REPO_ROOT), [])


if __name__ == "__main__":
    unittest.main()
