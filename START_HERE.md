# Start Here

This guide walks you through the Product Ops Sandbox in the order a first-time reader should use it.

You do not need to know Python to start. You can read the examples, use the AI prompts, or ask an AI assistant to guide you through the repo.

By the end, you should understand how product feedback, user research, product data, prioritization, OKRs, release communication, and AI-assisted workflows connect.

## What You Will Learn

You will learn how a Product Ops workflow can move from raw signals to product decisions:

```text
signals
-> insights
-> opportunities
-> roadmap
-> OKRs
-> release communication
-> measurement
```

The repo uses a fictional product called **FitPass Demo** and fictional data. It is safe to inspect, adapt, and discuss publicly.

## Before You Start

Choose the path that matches how you want to use the repo.

| Path | Best For | What You Need |
| --- | --- | --- |
| Read only | Hiring managers, recruiters, PMs, operators | GitHub browser |
| AI-assisted | PMs, Product Ops, learners, non-engineers | ChatGPT, Codex, Claude, Cursor, Copilot, or another assistant |
| Technical | Analysts, engineers, technical PMs | Python and a terminal |

If you are not sure, start with **Read only**.

## Step 1: Understand The Product

Start with the fictional product.

FitPass Demo is a B2B2C corporate wellness app:

- employers are the buyers
- employees are the daily users
- gyms and wellness providers are partners
- product, support, sales, customer success, marketing, and operations all see different signals

The important business question is not simply:

```text
How do we get more usage?
```

The better question is:

```text
How do we help employees reach enough value that employers can see the benefit is worth keeping?
```

## Step 2: Understand The Operating Loop

Product Ops connects signals that often live in separate places.

```text
customer feedback
+ user research
+ product analytics
-> themes and insights
-> product opportunities
-> prioritization
-> roadmap
-> OKRs
-> release communication
-> measurement
```

This is the core idea of the repo.

## Step 3: Look At The Inputs

The repo separates inputs by type.

| Input Type | Folder | Example |
| --- | --- | --- |
| Structured data | `sample-data/` | Product events, feedback records, roadmap items, OKRs |
| Messy notes | `input-notes/` | Support tickets, sales notes, customer success notes, interview transcripts |
| AI instructions | `ai-workflows/` | Prompts, schemas, sample AI outputs |

For now, think of structured data as spreadsheet-like data and messy notes as human language.

## Step 4: Look At The Outputs

Open `outputs/`.

The outputs show what the workflow produces.

| Output | What It Helps Answer |
| --- | --- |
| `metrics_snapshot.md` | What is happening in the product? |
| `feedback_theme_summary.md` | What feedback themes repeat? |
| `roadmap_priority_scores.md` | Which roadmap items look strongest? |
| `ai_feedback_classification.json` | How can messy feedback become structured themes? |
| `ai_opportunity_map.json` | Which product opportunities emerge from the signals? |
| `ai_weekly_product_insights.md` | What would a weekly Product Ops readout look like? |

You can understand the project by reading the outputs before running anything.

## Step 5: Try One AI-Assisted Workflow

You do not need an API key for this.

Use your preferred assistant: ChatGPT, Codex, Claude, Claude Code, Cursor, GitHub Copilot, or another approved tool.

Try this:

1. Open `ai-workflows/prompts/classify_feedback.md`.
2. Open one sample note file from `input-notes/`.
3. Copy both into your assistant.
4. Ask it to classify the notes.
5. Compare the result with the sample output.

Example request:

```text
Use this prompt to classify the following anonymized support notes.
Return themes, severity, linked metrics, and possible product opportunities.
Do not invent facts.
```

Important: use fictional, anonymized, or approved notes only.

## Step 6: Run The Scripts

This step is optional.

If you are comfortable with a terminal, run:

```bash
python scripts/analyze_feedback.py
python scripts/score_roadmap.py
python scripts/summarize_metrics.py
```

Then run the mock AI workflows:

```bash
python scripts/ai_classify_feedback.py
python scripts/ai_synthesize_research.py
python scripts/ai_detect_opportunities.py
python scripts/ai_generate_weekly_summary.py
```

The mock AI scripts use sample outputs. They do not need an API key.

## Step 7: Adapt It To Your Product

Start small.

Do not try to replace everything at once.

Recommended order:

1. Update the product context.
2. Update the success metrics.
3. Replace one structured CSV file.
4. Add one anonymized note file.
5. Run or ask an assistant to run one workflow.
6. Review the output.
7. Adjust the taxonomy, prompts, and roadmap assumptions.

## Useful Assistant Requests

You can ask your assistant:

```text
Explain the Product Ops Sandbox to me in simple terms.
```

```text
Walk me through this repo one step at a time. Stop after each step and ask if I understand.
```

```text
Help me adapt this sandbox for my product. Ask me the minimum questions needed before changing files.
```

```text
Use the AI workflow prompts to classify these anonymized customer notes.
```

```text
Run the scripts, explain the outputs, and tell me what product decisions they support.
```

## What To Read Next

| If You Want To... | Open |
| --- | --- |
| Understand the full system | `docs/00-product-ops-system-map.md` |
| Understand the fictional product | `docs/01-product-context.md` |
| Understand metrics | `docs/02-success-metrics.md` |
| Understand AI-assisted workflows | `ai-workflows/README.md` |
| Reuse workflows with an agent | `agent-skills/README.md` |
| Check data and AI safety | `SECURITY.md` |

## Simple Mental Model

Keep this in mind:

```text
Structured data goes through scripts.
Messy notes go through AI-assisted synthesis.
Humans review the output.
Teams decide what to do.
```
