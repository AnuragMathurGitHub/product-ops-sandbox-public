---
name: product-ops-signal-triage
description: Classify unstructured product signals such as support tickets, sales notes, customer success notes, app reviews, and open-ended feedback into product area, theme, severity, linked metric, evidence summary, and possible opportunity. Use when turning qualitative customer or internal feedback into a first-pass Product Ops triage for human review.
---

# Product Ops Signal Triage

## Overview

Use this skill to convert qualitative product signals into a structured triage. Treat the output as
a draft for human review, not a final roadmap decision.

## Inputs And Outputs (single source of truth)

This skill runs the feedback classification workflow. Do not restate the fields here; follow the
canonical prompt and schema so every tool produces the same shape:

- Notes: `input-notes/` (sample: `input-notes/support-ticket-batch.md`)
- Prompt: `ai-workflows/prompts/classify_feedback.md`
- Schema: `ai-workflows/schemas/feedback_classification.schema.json`
- Output: `outputs/ai_feedback_classification.json` plus a readable `outputs/ai_feedback_classification.md`

## Workflow

1. Read the notes from `input-notes/` and assign each item a stable `source_id`.
2. Classify each item by product area, theme, severity, linked metric, and confidence.
3. Preserve evidence with a short, source-grounded summary.
4. Suggest a possible opportunity only when the input supports it.
5. Produce the summary block (top themes, highest-severity items, review questions).

## Classification Rules

- Use only the provided input.
- Do not invent quotes, metrics, company names, or business impact.
- Mark uncertain conclusions as `Low` or `Medium` confidence.
- Prefer product-area labels from `references/taxonomy.md`.
- Keep severity tied to user or business impact, not emotional wording alone.

## References

Read `references/taxonomy.md` to standardize product areas, severity, confidence, and linked metrics.
