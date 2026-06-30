# Agent Skills

This folder packages the Product Ops workflows as reusable agent skills.

Use a skill when you want an assistant to follow the same analysis pattern repeatedly instead of
starting from a blank chat each time. Each skill is a thin package: it points to the canonical prompt
and schema in `ai-workflows/` so the workflow logic lives in one place and never drifts.

## How To Think About Skills

```text
task -> context -> inputs -> rules -> output format -> review
```

A skill is a `SKILL.md` file with a `name` and a `description`. An assistant that supports skills
can load it when your request matches the description, or you can call it by name.

## Included Skills

| Skill | Use It For | Canonical Prompt | Output |
| --- | --- | --- | --- |
| `product-ops-signal-triage` | Classify support, sales, success, and review notes | `ai-workflows/prompts/classify_feedback.md` | `outputs/ai_feedback_classification.json` + `.md` |
| `product-ops-research-synthesis` | Turn interviews and research into themes and insights | `ai-workflows/prompts/synthesize_research.md` | `outputs/ai_research_synthesis.json` + `.md` |
| `product-ops-opportunity-mapping` | Turn combined signals into product opportunities | `ai-workflows/prompts/detect_opportunities.md` | `outputs/ai_opportunity_map.json` + `.md` |
| `product-ops-weekly-review` | Draft a weekly Product Ops readout | `ai-workflows/prompts/weekly_product_insights.md` | `outputs/ai_weekly_product_insights.md` |

## How To Use These Skills

### Option 1: Use In Place

Keep the skills here and ask any AI coding assistant:

```text
Use the skill at agent-skills/product-ops-signal-triage to classify the notes in input-notes/.
```

### Option 2: Claude Code (auto-loaded)

This repo also ships the same skills under `.claude/skills/`, so Claude Code loads them by
description. You can run them directly:

```text
/product-ops-signal-triage
```

For personal reuse across projects, copy a skill folder into `~/.claude/skills/<skill-name>/`.

### Option 3: Adapt For A Company Workflow

Change product areas, severity definitions, metric names, and review rules in the skill plus its
canonical prompt and schema. Keep the human review layer.

## How These Relate To The Rest Of The Repo

```text
ai-workflows/ = the canonical prompts, schemas, and examples
agent-skills/ = reusable skill packages that point to those prompts
.claude/, .cursor/, .github/ = thin per-tool entry points (see AGENTS.md)
scripts/ = deterministic Python plus mock demos
```

## Guardrails

- Use fictional, anonymized, or approved data only.
- Ask the assistant to cite evidence from the source notes.
- Review every output before it affects a product decision.
- These skills create structured drafts; they do not make decisions.
