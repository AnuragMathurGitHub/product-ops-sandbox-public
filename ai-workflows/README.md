# AI Workflows

This folder contains reusable AI assisted workflows for Product Operations analysis.

The workflows use repo files as the source of truth:

```text
input-notes/
-> ai-workflows/prompts/
-> outputs/
```

You do not need an API key. The real workflow runs through your own AI assistant in an IDE, terminal
agent, AI native IDE, or approved chat tool. It reads a prompt and your notes and writes the result.
The `scripts/ai_*.py` mock scripts only copy prepared examples so you can inspect
the output shape; they do not call AI. See `AGENTS.md` for the shared workflow map agents should
follow.

## The Four Workflows

Each workflow is one prompt. Pick the prompt that matches the notes you have. Every prompt already
knows to read from `input-notes/` and where to write its result.

| Workflow | Sample Input | Prompt | Schema | Output |
| --- | --- | --- | --- | --- |
| Classify feedback | `../input-notes/support-ticket-batch.md` | `prompts/classify_feedback.md` | `schemas/feedback_classification.schema.json` | `../outputs/ai_feedback_classification.json` + `.md` |
| Synthesize research | `../input-notes/user-interview-transcript.md` | `prompts/synthesize_research.md` | `schemas/research_synthesis.schema.json` | `../outputs/ai_research_synthesis.json` + `.md` |
| Detect opportunities | all notes in `../input-notes/` | `prompts/detect_opportunities.md` | `schemas/opportunity_map.schema.json` | `../outputs/ai_opportunity_map.json` + `.md` |
| Weekly insights | `../input-notes/weekly-product-ops-packet.md` | `prompts/weekly_product_insights.md` | (Markdown, no schema) | `../outputs/ai_weekly_product_insights.md` |

## Start With Feedback Classification

It is the simplest workflow. Ask your assistant:

```text
Read ai-workflows/prompts/classify_feedback.md and input-notes/support-ticket-batch.md.
Classify the notes, write a draft to outputs/ai_feedback_classification.json, and write a short
readable summary to outputs/ai_feedback_classification.md.
Use only the evidence in the notes.
```

## Why This Is Useful

Product Ops teams often receive qualitative signals from support, sales, customer success, research, and partners. AI can create a first structured draft so humans can review themes, severity, linked metrics, and possible product opportunities faster.

The assistant should draft. The product team should decide.

## Guardrails

- Use fictional, anonymized, or approved notes only.
- Do not commit private customer data or personal information to the public repo.
- Review every AI generated claim against the source notes.
- Treat confidence as a review signal, not as proof.
- Keep the final product decision with accountable humans.
