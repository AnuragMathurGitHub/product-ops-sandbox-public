---
name: product-ops-signal-triage
description: Classify unstructured product signals such as support tickets, sales notes, customer success notes, app reviews, and open ended feedback into product area, theme, severity, linked metric, evidence summary, and possible opportunity. Use when turning qualitative customer or internal feedback into a first pass Product Ops triage for human review.
---

# Product Ops Signal Triage

Run the feedback classification workflow. Follow the canonical instructions (do not restate them):

- Prompt: `ai-workflows/prompts/classify_feedback.md`
- Schema: `ai-workflows/schemas/feedback_classification.schema.json`
- Taxonomy: `agent-skills/product-ops-signal-triage/references/taxonomy.md`

Read the notes in `input-notes/` (or the file the user names), classify them, and write
`outputs/ai_feedback_classification.json` plus a readable `outputs/ai_feedback_classification.md`.
Use only the evidence in the notes; do not invent facts.
