# Release Measurement Format

Use the schema in `ai-workflows/schemas/release_measurement_plan.schema.json`.

Each plan should include:

| Field | Meaning |
| --- | --- |
| initiative | Release candidate |
| audience | People who need the message |
| launch_message | Plain language launch message |
| internal_readiness | What internal teams need before launch |
| linked_metric | Metric to watch |
| baseline | Starting point from available evidence |
| target_signal | Movement that would suggest the release helped |
| measurement_window | When the team should review results |
| owner | Person or team coordinating review |
| risk_to_watch | Risk or ambiguity to monitor |
| decision_after_measurement | What the team should decide after results are reviewed |

The output should make launch and learning visible before the release ships.
