# Start Here

This guide walks you through the Product Ops Sandbox in the order a first-time reader should use it.

You do not need to know Python to start. You can read the examples, use an AI assistant, or run the scripts later if you want.

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
| Read only | PMs, operators, learners, curious readers | GitHub browser |
| AI-assisted | Product Ops, PMs, non-engineers | ChatGPT, Codex, Claude, Cursor, Copilot, or another assistant |
| Technical | Analysts, engineers, technical PMs | Python and a terminal |

If you are not sure, start with **Read only**.

If you do not have the files yet, go back to the README and follow **How To Get The Files**.

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

## Step 3: Know Where Inputs Go

The repo separates inputs by type.

| Input Type | Where It Goes | Example Files |
| --- | --- | --- |
| Unstructured product notes | `input-notes/` | Support notes, sales notes, customer success notes, interview transcripts |
| Structured data | `sample-data/` | CSV files for events, feedback records, roadmap items, OKRs |
| AI workflow instructions | `ai-workflows/` | Prompts, schemas, and sample AI outputs |

Use this rule:

```text
Notes and transcripts go in input-notes/.
Spreadsheet-like data goes in sample-data/.
Generated results go in outputs/.
```

### What Counts As An Input Note?

An input note is any qualitative product signal written in human language.

Examples:

- support ticket batch
- sales call notes
- customer success meeting notes
- user interview transcript
- partner feedback
- app review excerpts

Do not use sensitive or private data. Use fictional, anonymized, or approved notes only.

## Step 4: Look At The Outputs

Open `outputs/`.

The outputs show what the workflow produces.

| Output | What It Helps Answer | Human-Readable? |
| --- | --- | --- |
| `metrics_snapshot.md` | What is happening in the product? | Yes |
| `feedback_theme_summary.md` | What feedback themes repeat? | Yes |
| `roadmap_priority_scores.md` | Which roadmap items look strongest? | Yes |
| `ai_feedback_classification.json` | How can qualitative feedback become structured themes? | Structured for review |
| `ai_opportunity_map.json` | Which product opportunities emerge from the signals? | Structured for review |
| `ai_weekly_product_insights.md` | What would a weekly Product Ops readout look like? | Yes |

Why JSON?

```text
JSON keeps AI output structured.
Markdown makes summaries easy for people to read.
```

For example, JSON is useful when an assistant or script needs fields like `theme`, `severity`, and `linked_metric`. Markdown is better for final summaries and team updates.

## Step 5: Try One AI-Assisted Workflow

You do not need an API key for this.

The workflow is folder-based:

```text
input-notes/
-> ai-workflows/prompts/
-> outputs/
```

Try this:

1. Open the sample note file: `input-notes/support-ticket-batch.md`.
2. Open the matching prompt in `ai-workflows/prompts/`.
3. Ask your assistant to read both files from the repo.
4. Ask it to write the result into `outputs/` or show the result in chat.
5. Review the result before using it for decisions.

To use your own notes later, add a new `.md` file inside `input-notes/`. Keep the content fictional, anonymized, or approved.

Example request for Codex, Claude Code, Cursor, or Copilot:

```text
Read ai-workflows/prompts/classify_feedback.md and the notes in input-notes/.
Classify the notes into product area, theme, severity, linked metric, evidence summary, and possible opportunity.
Write the draft output to outputs/ai_feedback_classification.json.
Do not invent facts.
```

If you are using a chat-only assistant that cannot access files, copy the prompt and anonymized note content into the chat manually.

## Step 6: Run The Scripts

This step is optional, but it shows the deterministic workflow.

| Script | Input | Output | Why Run It |
| --- | --- | --- | --- |
| `scripts/analyze_feedback.py` | `sample-data/customer_feedback.csv` | `outputs/feedback_theme_summary.md` | See repeated feedback themes and severity counts |
| `scripts/score_roadmap.py` | `sample-data/roadmap_items.csv` | `outputs/roadmap_priority_scores.md` | Compare roadmap candidates with a transparent formula |
| `scripts/summarize_metrics.py` | `sample-data/product_events.csv` | `outputs/metrics_snapshot.md` | Create a basic product metrics snapshot |

Run:

```bash
python scripts/analyze_feedback.py
python scripts/score_roadmap.py
python scripts/summarize_metrics.py
```

These scripts are deterministic. If the input files do not change, the outputs should not change.

## Step 7: Understand Mock AI Workflows

The mock AI scripts do not call a live AI model.

They copy prepared example outputs into `outputs/` so you can see the workflow without needing an API key.

| Script | Input Idea | Output | Why It Exists |
| --- | --- | --- | --- |
| `scripts/ai_classify_feedback.py` | Notes from `input-notes/` | `outputs/ai_feedback_classification.json` | Shows how qualitative notes can become structured feedback themes |
| `scripts/ai_synthesize_research.py` | Interview notes | `outputs/ai_research_synthesis.json` | Shows how research can become themes, insights, and implications |
| `scripts/ai_detect_opportunities.py` | Combined signals | `outputs/ai_opportunity_map.json` | Shows how signals can become opportunity statements |
| `scripts/ai_generate_weekly_summary.py` | Metrics plus themes | `outputs/ai_weekly_product_insights.md` | Shows a weekly Product Ops readout |

Run:

```bash
python scripts/ai_classify_feedback.py
python scripts/ai_synthesize_research.py
python scripts/ai_detect_opportunities.py
python scripts/ai_generate_weekly_summary.py
```

Live AI mode can be added with approved data, credentials, and model access. Mock mode is the safe default.

## Step 8: Adapt It To Your Product

Start small.

Do not replace everything at once.

Recommended order:

| Step | What To Change | Where |
| --- | --- | --- |
| 1 | Product context | `docs/01-product-context.md` |
| 2 | Success metrics | `docs/02-success-metrics.md` |
| 3 | One structured CSV | `sample-data/` |
| 4 | One anonymized note file | `input-notes/` |
| 5 | One AI prompt | `ai-workflows/prompts/` |
| 6 | One output review | `outputs/` |
| 7 | Taxonomy or roadmap assumptions | `docs/` and `agent-skills/` |

The safest first adaptation is:

```text
Replace one note file in input-notes/.
Ask an assistant to classify it.
Review the output.
Then decide what to change next.
```

## Useful Assistant Requests

You can ask your assistant:

```text
Explain the Product Ops Sandbox to me in simple terms.
```

```text
Walk me through this repo one step at a time. Stop after each step and ask if I understand.
```

```text
Look at input-notes/ and tell me which workflow should process each note file.
```

```text
Run the deterministic scripts, explain what each output means, and tell me what product decisions they support.
```

```text
Help me adapt this sandbox for my product. Ask me the minimum questions needed before changing files.
```

## What To Read Next

| If You Want To... | Open |
| --- | --- |
| Understand the full system | `docs/00-product-ops-system-map.md` |
| Understand the fictional product | `docs/01-product-context.md` |
| Understand metrics | `docs/02-success-metrics.md` |
| Understand qualitative inputs | `input-notes/README.md` |
| Understand AI-assisted workflows | `ai-workflows/README.md` |
| Reuse workflows with an agent | `agent-skills/README.md` |
| Check data and AI safety | `SECURITY.md` |

## Simple Mental Model

Keep this in mind:

```text
Structured data goes through scripts.
Qualitative notes go through AI-assisted synthesis.
Humans review the output.
Teams decide what to do.
```
