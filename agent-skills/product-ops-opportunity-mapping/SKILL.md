---
name: product-ops-opportunity-mapping
description: Turn customer feedback, research insights, product metrics, sales notes, support themes, and customer success signals into product opportunity statements connected to the customer problem, a linked metric, evidence, and a possible solution direction. Use when preparing discovery, prioritization, roadmap planning, or OKR alignment.
---

# Product Ops Opportunity Mapping

## Overview

Use this skill to bridge synthesis and planning. The output should help a team discuss which
problems deserve roadmap attention and why.

## Inputs And Outputs (single source of truth)

Follow the canonical prompt and schema so every tool produces the same shape:

- Notes: all files in `input-notes/` (this workflow combines several signals)
- Supporting evidence: `outputs/feedback_theme_summary.md`, `outputs/ai_feedback_classification.json`
- Prompt: `ai-workflows/prompts/detect_opportunities.md`
- Schema: `ai-workflows/schemas/opportunity_map.schema.json`
- Output: `outputs/ai_opportunity_map.json` plus a readable `outputs/ai_opportunity_map.md`

## Workflow

1. Combine the available signals: notes, feedback themes, and metrics.
2. Identify repeated or high-impact customer problems.
3. Write each opportunity in problem language, not feature language.
4. Link each opportunity to a metric and short evidence.
5. Offer a possible solution direction, not a committed solution.
6. Add review questions for what still needs validation.

## Opportunity Rules

- Do not turn every complaint into a feature.
- Keep the customer problem separate from the proposed direction.
- Prefer evidence-backed opportunities over loud anecdotes.
- Each opportunity must trace to evidence in the input.

## References

Read `references/opportunity-map-format.md` for the structured opportunity format.
