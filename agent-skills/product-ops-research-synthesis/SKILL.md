---
name: product-ops-research-synthesis
description: Synthesize user interview notes, research transcripts, discovery calls, and qualitative product observations into themes, evidence, implications, insights, and review questions. Use when Product Ops needs to turn qualitative research into decision-ready evidence while keeping user context intact.
---

# Product Ops Research Synthesis

## Overview

Use this skill to turn qualitative research into reusable Product Ops evidence. Keep user context
intact while making patterns visible enough for product planning.

## Inputs And Outputs (single source of truth)

Follow the canonical prompt and schema so every tool produces the same shape:

- Notes: `input-notes/` (sample: `input-notes/user-interview-transcript.md`)
- Prompt: `ai-workflows/prompts/synthesize_research.md`
- Schema: `ai-workflows/schemas/research_synthesis.schema.json`
- Output: `outputs/ai_research_synthesis.json` plus a readable `outputs/ai_research_synthesis.md`

## Workflow

1. Read the transcript or notes and identify participant context.
2. Separate observations from interpretations.
3. Group repeated observations into themes, each with evidence and an implication.
4. Convert themes into a few decision-useful insights.
5. List review questions for follow-up research or analytics.

## Synthesis Rules

- Use only the provided input. Do not invent quotes or participant details.
- Do not overgeneralize from one interview.
- Keep evidence short and traceable to the source.
- Mark uncertain conclusions clearly in the review questions.

## References

Read `references/research-synthesis-format.md` for the structured synthesis format.
