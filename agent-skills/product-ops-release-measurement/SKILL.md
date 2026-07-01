---
name: product-ops-release-measurement
description: Draft release communication and measurement plans from release candidates, OKR alignment, roadmap scores, and product metrics. Use when Product Ops needs to prepare teams for launch and define how success will be reviewed.
---

# Product Ops Release Measurement

Use this skill when a roadmap candidate needs launch communication and a measurement plan.

## Canonical Inputs

- Release data: `sample-data/releases.csv`
- OKR data: `sample-data/okrs.csv`
- Release snapshot: `outputs/release_readiness_snapshot.md`
- OKR snapshot: `outputs/okr_snapshot.md`
- Metrics: `outputs/metrics_snapshot.md`
- Roadmap scores: `outputs/roadmap_priority_scores.md`
- OKR alignment: `outputs/ai_okr_alignment.json`
- Planning review: `outputs/ai_product_planning_review.md`
- Prompt: `ai-workflows/prompts/plan_release_measurement.md`
- Schema: `ai-workflows/schemas/release_measurement_plan.schema.json`
- Format: `references/release-measurement-format.md`

## Workflow

1. Read the canonical prompt.
2. Select release candidates with evidence and measurable outcomes.
3. Draft the launch message, internal readiness needs, linked metric, baseline, target signal, owner, risk, and next decision.
4. Keep the output practical for product, engineering, support, customer success, sales, marketing, and operations.
5. Write `outputs/ai_release_measurement_plan.json` and `outputs/ai_release_measurement_plan.md`.

## Guardrails

- Do not invent launch dates, owners, metrics, or targets.
- Measurement should check behavior change, not only shipping.
- Treat the plan as a draft for human review.

## Reference

Read `references/release-measurement-format.md` for the expected structure.
