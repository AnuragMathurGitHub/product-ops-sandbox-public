import json
import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from ai_common import OUTPUTS, copy_mock_output
from analyze_feedback import build_summary as build_feedback_summary
from score_roadmap import priority_score
from summarize_metrics import build_summary as build_metrics_summary
from summarize_metrics import count_events
from summarize_okrs import build_summary as build_okr_summary
from summarize_releases import build_summary as build_release_summary


class StructuredScriptTests(unittest.TestCase):
    def test_priority_score_formula(self):
        item = {
            "reach": "100",
            "impact": "4",
            "confidence": "0.5",
            "effort": "2",
            "strategic_fit": "3",
        }

        self.assertEqual(priority_score(item), 300.0)

    def test_count_events_filters_success(self):
        events = [
            {"event_name": "Check In Failed", "success": "false"},
            {"event_name": "Check In Failed", "success": "true"},
            {"event_name": "Check In Completed", "success": "true"},
        ]

        self.assertEqual(count_events(events, "Check In Failed"), 2)
        self.assertEqual(count_events(events, "Check In Failed", False), 1)
        self.assertEqual(count_events(events, "Check In Completed", True), 1)

    def test_feedback_summary_groups_themes(self):
        records = [
            {
                "theme": "Failed check in",
                "severity": "High",
                "linked_metric": "Check In Failed Count",
            },
            {
                "theme": "Failed check in",
                "severity": "Medium",
                "linked_metric": "Check In Failed Count",
            },
        ]

        summary = build_feedback_summary(records)

        self.assertIn("Failed check in", summary)
        self.assertIn("Check In Failed Count", summary)

    def test_metrics_summary_handles_empty_input(self):
        summary = build_metrics_summary([])

        self.assertIn("| Total users | 0 |", summary)
        self.assertIn("| Activation rate | 0.0% |", summary)

    def test_okr_summary_groups_objectives(self):
        records = [
            {
                "objective": "Improve first value",
                "key_result": "Reduce failed check ins",
                "linked_metric": "Check In Failed Count",
                "baseline": "2",
                "current": "2",
                "target": "1",
                "status": "Needs focus",
            }
        ]

        summary = build_okr_summary(records)

        self.assertIn("Improve first value", summary)
        self.assertIn("Reduce failed check ins", summary)

    def test_release_summary_lists_measurement_window(self):
        records = [
            {
                "release_id": "REL-001",
                "initiative": "Improve check in fallback",
                "launch_stage": "Discovery",
                "linked_metric": "Check In Failed Count",
                "communication_owner": "Product Ops",
                "measurement_window": "Two weeks after release",
            }
        ]

        summary = build_release_summary(records)

        self.assertIn("Improve check in fallback", summary)
        self.assertIn("Two weeks after release", summary)


class MockWorkflowTests(unittest.TestCase):
    def test_copy_mock_output_copies_example(self):
        output_name = "_test_mock_output.json"
        destination = OUTPUTS / output_name

        try:
            copy_mock_output("feedback_classification_example.json", output_name, announce=False)
            self.assertTrue(destination.exists())
            payload = json.loads(destination.read_text(encoding="utf-8"))
            self.assertIn("items", payload)
        finally:
            if destination.exists():
                destination.unlink()

    def test_copy_mock_output_missing_source_raises(self):
        with self.assertRaises(FileNotFoundError):
            copy_mock_output("does_not_exist.json", "_test_should_not_be_written.json")


class SampleOutputSchemaTests(unittest.TestCase):
    SCHEMAS = PROJECT_ROOT / "ai-workflows" / "schemas"
    EXAMPLES = PROJECT_ROOT / "ai-workflows" / "sample-outputs"
    OUTPUTS_DIR = PROJECT_ROOT / "outputs"
    CASES = [
        ("feedback_classification.schema.json", "feedback_classification_example.json"),
        ("research_synthesis.schema.json", "research_synthesis_example.json"),
        ("opportunity_map.schema.json", "opportunity_map_example.json"),
        ("okr_alignment.schema.json", "okr_alignment_example.json"),
        ("release_measurement_plan.schema.json", "release_measurement_plan_example.json"),
    ]
    OUTPUT_CASES = [
        ("feedback_classification.schema.json", "ai_feedback_classification.json"),
        ("research_synthesis.schema.json", "ai_research_synthesis.json"),
        ("opportunity_map.schema.json", "ai_opportunity_map.json"),
        ("okr_alignment.schema.json", "ai_okr_alignment.json"),
        ("release_measurement_plan.schema.json", "ai_release_measurement_plan.json"),
    ]

    def validate_schema(self, schema, value, path="$"):
        schema_type = schema.get("type")

        if schema_type == "object":
            self.assertIsInstance(value, dict, f"{path} should be an object")

            for key in schema.get("required", []):
                self.assertIn(key, value, f"{path} is missing required key '{key}'")

            properties = schema.get("properties", {})
            if schema.get("additionalProperties") is False:
                extra_keys = sorted(set(value) - set(properties))
                self.assertEqual(extra_keys, [], f"{path} has unexpected keys")

            for key, child_schema in properties.items():
                if key in value:
                    self.validate_schema(child_schema, value[key], f"{path}.{key}")

        elif schema_type == "array":
            self.assertIsInstance(value, list, f"{path} should be an array")
            item_schema = schema.get("items")
            if item_schema:
                for index, item in enumerate(value):
                    self.validate_schema(item_schema, item, f"{path}[{index}]")

        elif schema_type == "string":
            self.assertIsInstance(value, str, f"{path} should be a string")

    def test_examples_match_their_schemas(self):
        for schema_name, example_name in self.CASES:
            schema = json.loads((self.SCHEMAS / schema_name).read_text(encoding="utf-8"))
            example = json.loads((self.EXAMPLES / example_name).read_text(encoding="utf-8"))
            self.validate_schema(schema, example)

    def test_generated_outputs_match_their_schemas(self):
        for schema_name, output_name in self.OUTPUT_CASES:
            schema = json.loads((self.SCHEMAS / schema_name).read_text(encoding="utf-8"))
            output = json.loads((self.OUTPUTS_DIR / output_name).read_text(encoding="utf-8"))
            self.validate_schema(schema, output)


if __name__ == "__main__":
    unittest.main()
