# Outputs

This folder contains generated or example results from the sandbox workflows.

## How To Read Outputs

| Format | Best For | Example |
| --- | --- | --- |
| Markdown | Human-readable summaries and team updates | Weekly readouts, metric summaries |
| JSON | Structured drafts that can be reviewed, validated, or reused | Feedback classification |

JSON is not meant to be less human. It is meant to keep fields consistent so an assistant, script, or reviewer can compare the same attributes across notes.

## Included Outputs

| Output | What It Shows |
| --- | --- |
| `feedback_theme_summary.md` | Repeated feedback themes and severity counts |
| `roadmap_priority_scores.md` | Roadmap candidates scored with a transparent formula |
| `metrics_snapshot.md` | Basic product usage metrics |
| `ai_feedback_classification.json` | How qualitative notes from `input-notes/` can become structured feedback themes |
| `ai_research_synthesis.json` | How qualitative research can become themes and insights |
| `ai_opportunity_map.json` | How signals can become product opportunity statements |
| `ai_weekly_product_insights.md` | A weekly Product Ops readout |

Review outputs before using them for any product decision.
