---
name: product-ops-planning-review
description: Review how product signals, insights, opportunities, roadmap candidates, OKRs, release planning, and measurement connect. Use when Product Ops needs to check whether the planning story is evidence based before a roadmap or planning discussion.
---

# Product Ops Planning Review

Use this skill to review the planning chain before the team commits to roadmap or OKR decisions.

## Canonical Inputs

- Metrics: `outputs/metrics_snapshot.md`
- Feedback: `outputs/feedback_theme_summary.md`
- Roadmap scores: `outputs/roadmap_priority_scores.md`
- AI drafts: `outputs/ai_feedback_classification.md`, `outputs/ai_research_synthesis.md`, `outputs/ai_opportunity_map.md`
- OKR snapshot: `outputs/okr_snapshot.md`
- Prompt: `ai-workflows/prompts/review_product_planning.md`
- Format: `references/planning-review-format.md`

## Workflow

1. Read the canonical prompt.
2. Connect evidence in this order: signals, insights, opportunities, prioritization, roadmap candidates, OKR alignment, release planning, measurement.
3. Name what is well supported and what still needs evidence.
4. Keep roadmap and OKR language as drafts for human review.
5. Write `outputs/ai_product_planning_review.md`.

## Guardrails

- Do not invent metrics, facts, or company context.
- Do not turn a candidate into a commitment.
- Make gaps visible so humans can decide.

## Reference

Read `references/planning-review-format.md` for the expected review shape.
