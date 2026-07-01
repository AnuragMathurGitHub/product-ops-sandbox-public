# Outputs

This folder contains generated or example results from the sandbox workflows.

## How To Read Outputs

| Format | Best For | Example |
| --- | --- | --- |
| Markdown | Human readable summaries and team updates | Weekly readouts, metric summaries |
| JSON | Structured drafts that can be reviewed, validated, or reused | Feedback classification |

JSON is not meant to be less human. It is meant to keep fields consistent so an assistant, script, or reviewer can compare the same attributes across notes.

## Every AI Output Has A Readable Companion

Most structured AI workflows write **two** files: a `.json` draft and a matching `.md` summary.
Open the `.md` if you just want to read the result; open the `.json` if a script or reviewer needs
consistent fields.

## Included Outputs

| Output | What It Shows |
| --- | --- |
| `feedback_theme_summary.md` | Repeated feedback themes and severity counts |
| `roadmap_priority_scores.md` | Roadmap candidates scored with a transparent formula |
| `metrics_snapshot.md` | Basic product usage metrics |
| `okr_snapshot.md` | Sample objectives, key results, linked metrics, and status |
| `release_readiness_snapshot.md` | Release candidates, owners, and measurement windows |
| `ai_feedback_classification.json` + `.md` | How notes from `input-notes/` become structured feedback themes |
| `ai_research_synthesis.json` + `.md` | How research becomes themes, evidence, and insights |
| `ai_opportunity_map.json` + `.md` | How signals become product opportunity statements |
| `ai_product_planning_review.md` | How signals, opportunities, roadmap candidates, OKRs, release planning, and measurement connect |
| `ai_okr_alignment.json` + `.md` | How roadmap candidates may support current OKRs |
| `ai_release_measurement_plan.json` + `.md` | How release communication and measurement can be planned |
| `ai_weekly_product_insights.md` | A weekly Product Ops readout (Markdown only) |

Review outputs before using them for any product decision.
