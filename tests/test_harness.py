import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

import harness
from harness import HarnessError, extract_json, run_step, validate

SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "required": ["theme", "severity"],
    "properties": {
        "theme": {"type": "string"},
        "severity": {"type": "string", "enum": ["Low", "Medium", "High", "Critical"]},
    },
}

VALID = '{"theme": "Failed check in", "severity": "High"}'
MISSING_FIELD = '{"theme": "Failed check in"}'
BAD_ENUM = '{"theme": "x", "severity": "Huge"}'
NOT_JSON = "Sorry, there is no object here."


def fake_model(responses):
    """A fake model that returns queued responses in order, ignoring the prompt."""
    queue = list(responses)

    def call(prompt):
        return queue.pop(0)

    return call


class HarnessTests(unittest.TestCase):
    def test_valid_output_passes_the_gate(self):
        data = run_step(fake_model([VALID]), "prompt", SCHEMA)
        self.assertEqual(data["severity"], "High")

    def test_retries_until_valid(self):
        model = fake_model([MISSING_FIELD, NOT_JSON, VALID])
        data = run_step(model, "prompt", SCHEMA, max_retries=3)
        self.assertEqual(data["theme"], "Failed check in")

    def test_fails_closed_after_retries(self):
        model = fake_model([MISSING_FIELD, BAD_ENUM, MISSING_FIELD])
        with self.assertRaises(HarnessError):
            run_step(model, "prompt", SCHEMA, max_retries=3)

    def test_validate_reports_violations(self):
        self.assertEqual(validate(SCHEMA, {"theme": "x", "severity": "High"}), [])
        self.assertTrue(validate(SCHEMA, {"theme": "x"}))  # missing severity
        self.assertTrue(validate(SCHEMA, {"theme": "x", "severity": "Nope"}))  # bad enum
        self.assertTrue(
            validate(SCHEMA, {"theme": "x", "severity": "High", "extra": 1})
        )  # extra key

    def test_extract_json_tolerates_code_fences(self):
        self.assertEqual(extract_json('```json\n{"a": 1}\n```'), {"a": 1})


class RealSchemaTests(unittest.TestCase):
    def test_harness_validates_a_real_sample_output(self):
        schema = json.loads(
            (
                PROJECT_ROOT / "ai-workflows" / "schemas" / "feedback_classification.schema.json"
            ).read_text(encoding="utf-8")
        )
        sample = json.loads(
            (
                PROJECT_ROOT
                / "ai-workflows"
                / "sample-outputs"
                / "feedback_classification_example.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(validate(schema, sample), [])


def run_cli(argv):
    """Run the harness command line quietly and return its exit code."""
    with contextlib.redirect_stdout(io.StringIO()):
        return harness.main(argv)


class CliTests(unittest.TestCase):
    SCHEMAS = PROJECT_ROOT / "ai-workflows" / "schemas"
    SAMPLES = PROJECT_ROOT / "ai-workflows" / "sample-outputs"

    def test_cli_accepts_a_matching_output(self):
        code = run_cli(
            [
                str(self.SAMPLES / "feedback_classification_example.json"),
                str(self.SCHEMAS / "feedback_classification.schema.json"),
            ]
        )
        self.assertEqual(code, 0)

    def test_cli_rejects_an_output_that_misses_the_contract(self):
        code = run_cli(
            [
                str(self.SAMPLES / "okr_alignment_example.json"),
                str(self.SCHEMAS / "feedback_classification.schema.json"),
            ]
        )
        self.assertEqual(code, 1)

    def test_cli_reports_usage_and_file_problems(self):
        self.assertEqual(run_cli([]), 2)
        self.assertEqual(
            run_cli(
                ["does_not_exist.json", str(self.SCHEMAS / "feedback_classification.schema.json")]
            ),
            2,
        )


if __name__ == "__main__":
    unittest.main()
