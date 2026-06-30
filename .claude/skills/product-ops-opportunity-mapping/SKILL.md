---
name: product-ops-opportunity-mapping
description: Turn customer feedback, research insights, product metrics, sales notes, support themes, and customer success signals into product opportunity statements connected to the customer problem, a linked metric, evidence, and a possible solution direction. Use when preparing discovery, prioritization, roadmap planning, or OKR alignment.
---

# Product Ops Opportunity Mapping

Run the opportunity mapping workflow. Follow the canonical instructions (do not restate them):

- Prompt: `ai-workflows/prompts/detect_opportunities.md`
- Schema: `ai-workflows/schemas/opportunity_map.schema.json`
- Format: `agent-skills/product-ops-opportunity-mapping/references/opportunity-map-format.md`

Read all the notes in `input-notes/` (this workflow combines signals), map opportunities, and write
`outputs/ai_opportunity_map.json` plus a readable `outputs/ai_opportunity_map.md`.
Use only the evidence in the notes; do not invent facts.
