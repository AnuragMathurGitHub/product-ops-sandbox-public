# AI Workflows

This folder contains reusable AI-assisted workflows for Product Operations analysis.

The workflows use repo files as the source of truth:

```text
input-notes/
-> ai-workflows/prompts/
-> outputs/
```

You do not need an API key for the first workflow. Use an approved assistant such as ChatGPT, Codex, Claude, Claude Code, Cursor, Copilot, or another tool your team allows.

## First Workflow

Use feedback classification first.

| File | Purpose |
| --- | --- |
| `../input-notes/support-ticket-batch.md` | Fictional qualitative input notes |
| `prompts/classify_feedback.md` | Instructions for the assistant |
| `schemas/feedback_classification.schema.json` | Expected JSON structure |
| `../outputs/ai_feedback_classification.json` | Example structured output |

Ask your assistant:

```text
Read ai-workflows/prompts/classify_feedback.md and input-notes/support-ticket-batch.md.
Classify the notes and write a draft result to outputs/ai_feedback_classification.json.
Use only the evidence in the notes.
```

## Why This Is Useful

Product Ops teams often receive qualitative signals from support, sales, customer success, research, and partners. AI can create a first structured draft so humans can review themes, severity, linked metrics, and possible product opportunities faster.

The assistant should draft. The product team should decide.

## Guardrails

- Use fictional, anonymized, or approved notes only.
- Do not add private customer data or personal information.
- Review every AI-generated claim against the source notes.
- Treat confidence as a review signal, not as proof.
- Keep the final product decision with accountable humans.
