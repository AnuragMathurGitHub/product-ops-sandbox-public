# AGENTS.md

Guidance for AI coding agents (OpenAI Codex, Cursor, GitHub Copilot, Claude Code, Gemini CLI, and
others) working in the Product Ops Sandbox. This file is the single source of truth for how to run
the workflows. Tool specific entry points (`.claude/`, `.cursor/`, `.github/`) all point back here.

## What this repo is

A learning sandbox that turns scattered product signals into product decisions for a fictional
product called **FitPass Demo**. All data is fictional. There is no real company or customer data.

## The main thing agents do here: run a workflow

Inputs are files. You read them and write results. **No API key is required**; you are the AI.

1. Qualitative notes live in `input-notes/`. Structured data lives in `sample-data/`.
2. Each workflow is one prompt in `ai-workflows/prompts/`. Read the matching prompt and follow it.
3. Write the result to `outputs/`: a `.json` draft that matches the schema in
   `ai-workflows/schemas/`, plus a short, readable `.md` summary next to it.
4. Use only the evidence in the notes. Do not invent facts, numbers, quotes, or company names.

### Workflow map

| If the user asks to... | Follow this prompt | Write these outputs |
| --- | --- | --- |
| Classify feedback notes | `ai-workflows/prompts/classify_feedback.md` | `outputs/ai_feedback_classification.json` + `.md` |
| Synthesize research/interviews | `ai-workflows/prompts/synthesize_research.md` | `outputs/ai_research_synthesis.json` + `.md` |
| Detect product opportunities | `ai-workflows/prompts/detect_opportunities.md` | `outputs/ai_opportunity_map.json` + `.md` |
| Draft a weekly readout | `ai-workflows/prompts/weekly_product_insights.md` | `outputs/ai_weekly_product_insights.md` |

## Deterministic scripts (optional)

`python scripts/analyze_feedback.py`, `scripts/score_roadmap.py`, and `scripts/summarize_metrics.py`
read `sample-data/` and write Markdown to `outputs/`. They are deterministic.

The `scripts/ai_*.py` scripts are **mock demos**: they copy prepared example results into
`outputs/` so the workflow runs with no model and no API key. They do not call AI. The real AI path
is you, the agent, following the prompts above on real notes.

## Conventions

- Keep everything fictional, anonymized, or approved. This repo is public.
- Use ASCII only in committed files.
- Do not commit `.private/` (local working notes).
- Reusable skill packages live in `agent-skills/` (portable) and `.claude/skills/` (Claude Code).

## Safety

```text
AI drafts. Humans review. Teams decide.
```

Never present AI output as a final product decision. Always leave a human review step.
