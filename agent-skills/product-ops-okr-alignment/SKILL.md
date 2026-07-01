---
name: product-ops-okr-alignment
description: Connect product evidence, opportunity mapping, roadmap candidates, and current OKRs into an OKR alignment draft. Use when Product Ops needs to check which outcomes a candidate initiative may support.
---

# Product Ops OKR Alignment

Use this skill when the team needs to connect evidence and roadmap candidates to measurable outcomes.

## Canonical Inputs

- OKR data: `sample-data/okrs.csv`
- OKR snapshot: `outputs/okr_snapshot.md`
- Metrics: `outputs/metrics_snapshot.md`
- Feedback: `outputs/feedback_theme_summary.md`
- Roadmap scores: `outputs/roadmap_priority_scores.md`
- Opportunity map: `outputs/ai_opportunity_map.json`
- Planning review: `outputs/ai_product_planning_review.md`
- Prompt: `ai-workflows/prompts/align_okrs.md`
- Schema: `ai-workflows/schemas/okr_alignment.schema.json`
- Format: `references/okr-alignment-format.md`

## Workflow

1. Read the canonical prompt.
2. Read the current OKRs before suggesting any alignment.
3. Connect each candidate to the objective, key result, linked metric, supporting evidence, and review question.
4. Mark each alignment as strong, partial, or weak.
5. Write `outputs/ai_okr_alignment.json` and `outputs/ai_okr_alignment.md`.

## Guardrails

- OKRs are not created only from feedback.
- Treat the output as an alignment draft, not approved OKRs.
- Prefer outcome language over feature language.

## Reference

Read `references/okr-alignment-format.md` for the expected structure.
