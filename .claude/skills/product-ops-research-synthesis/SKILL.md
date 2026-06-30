---
name: product-ops-research-synthesis
description: Synthesize user interview notes, research transcripts, discovery calls, and qualitative product observations into themes, evidence, implications, insights, and review questions. Use when Product Ops needs to turn qualitative research into decision ready evidence while keeping user context intact.
---

# Product Ops Research Synthesis

Run the research synthesis workflow. Follow the canonical instructions (do not restate them):

- Prompt: `ai-workflows/prompts/synthesize_research.md`
- Schema: `ai-workflows/schemas/research_synthesis.schema.json`
- Format: `agent-skills/product-ops-research-synthesis/references/research-synthesis-format.md`

Read the interview or research notes in `input-notes/` (or the file the user names), synthesize them,
and write `outputs/ai_research_synthesis.json` plus a readable `outputs/ai_research_synthesis.md`.
Use only the evidence in the notes; do not invent facts.
