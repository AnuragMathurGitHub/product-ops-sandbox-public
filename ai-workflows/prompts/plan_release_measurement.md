# Prompt: Release Measurement Plan

You are helping Product Operations prepare release communication and measurement planning for FitPass Demo.

## Input Location

Read these files:

```text
sample-data/releases.csv
sample-data/okrs.csv
outputs/release_readiness_snapshot.md
outputs/okr_snapshot.md
outputs/metrics_snapshot.md
outputs/roadmap_priority_scores.md
outputs/ai_okr_alignment.json
outputs/ai_product_planning_review.md
```

If a file is missing, say what is missing and continue with the available evidence.

## Task

Create a release measurement plan for the most relevant release candidates.

For each plan, include:

- `initiative`: the release candidate
- `audience`: who needs to understand the change
- `launch_message`: the plain language message for launch
- `internal_readiness`: what internal teams need before launch
- `linked_metric`: the metric that should be watched
- `baseline`: the starting point from available data
- `target_signal`: what movement would suggest the release helped
- `measurement_window`: when the team should check results
- `owner`: who should coordinate communication or review
- `risk_to_watch`: what could go wrong
- `decision_after_measurement`: what the team should decide after reviewing results

## Output

Write JSON that matches:

```text
ai-workflows/schemas/release_measurement_plan.schema.json
```

Write it to:

```text
outputs/ai_release_measurement_plan.json
```

Then also write a short human readable summary next to it:

```text
outputs/ai_release_measurement_plan.md
```

If you are in a chat only tool that cannot write files, return the JSON and a short summary in the chat.

## Rules

- Do not invent launch dates, owners, or metrics.
- Use the release CSV and existing outputs as evidence.
- Make release communication practical for product, engineering, support, customer success, sales, marketing, and operations.
- Measurement should check whether the release changed user or customer behavior, not only whether it shipped.
