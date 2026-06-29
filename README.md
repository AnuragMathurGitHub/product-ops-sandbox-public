# Product Ops Sandbox

A practical Product Operations sandbox that shows how product teams can turn scattered signals into clearer product decisions.

This repo uses a fictional product, fictional data, simple Python workflows, and AI-assisted examples to model a modern Product Ops operating loop:

```text
feedback + research + product data
-> insights
-> opportunities
-> prioritization
-> roadmap
-> OKRs
-> release communication
-> measurement
```

The goal is not to build a production tool. The goal is to make the workflow easy to understand, run, and adapt.

## What This Is

Product Ops teams often work across many signal sources:

- product analytics
- customer feedback
- user research
- support issues
- sales and customer success notes
- roadmap requests
- OKRs
- release communication

Those signals usually live in different places. The value comes from connecting them into a repeatable decision system.

This sandbox shows one lightweight version of that system.

## Who This Is For

| Audience | What You Can Use This For |
| --- | --- |
| Product Operations managers | A simple operating model for connecting signals to planning |
| Product managers | A practical example of metrics, feedback, research, roadmap, and OKR alignment |
| Startup operators | A lightweight template before buying or integrating heavier tools |
| Students and career switchers | A concrete way to understand Product Ops workflows |
| Hiring managers and recruiters | A portfolio artifact that shows structured product thinking |
| AI workflow builders | Examples of where AI helps with synthesis, not final decisions |

## Fictional Product Example

The sandbox uses a fictional product called **FitPass Demo**.

FitPass Demo is a corporate wellness app where employees can:

- activate a wellness membership
- search for gyms and classes
- book classes
- check in at partner gyms
- track wellness activity

The product is fictional. The data is fictional. There is no connection to any real company.

## Product Problem

The core product problem is simple:

```text
Employees may sign up, but not enough of them activate,
find a useful option, book, check in, and build a repeat habit.
```

That creates questions for the product team:

- Where do users drop off?
- What do customers and users complain about?
- What does research tell us about the behavior?
- Which opportunities should be prioritized?
- Which metrics should improve?
- How should teams communicate changes?
- How do we know whether a release worked?

## What This Repo Demonstrates

This sandbox connects the main pieces of Product Ops work:

| Area | What It Shows |
| --- | --- |
| Product context | Who the users, buyers, partners, and internal teams are |
| Success metrics | What the team should measure and why |
| Product analytics | Which events answer important product questions |
| Customer feedback | How feedback can be tagged, grouped, and linked to metrics |
| User research | How qualitative notes become themes and insights |
| Prioritization | How roadmap candidates can be compared without replacing judgment |
| OKRs | How product work connects to measurable outcomes |
| Release communication | How teams prepare for launch and post-release learning |
| AI-assisted workflows | How AI can help synthesize messy text with human review |
| Agent skills | How repeatable AI workflows can be packaged for reuse |

## Two Operating Lanes

The repo separates work into two lanes.

### 1. Deterministic Structured Workflows

Use Python when the answer should be calculated.

Examples:

- count product events
- calculate activation rate
- group feedback by theme
- score roadmap items
- generate a metrics snapshot

This lane is repeatable. If the input does not change, the output should not change.

### 2. AI-Assisted Qualitative Workflows

Use AI assistance when the input is messy language.

Examples:

- support ticket batches
- sales call notes
- customer success meeting notes
- user interview transcripts
- open-ended survey responses

AI can help create a first draft of themes, insights, classifications, and opportunity statements. A human still reviews the output before it influences roadmap decisions.

```text
Code calculates.
AI drafts.
Humans decide.
```

## How To Read This Repo

If you only have 5 minutes:

1. Read this README.
2. Review the Product Ops operating loop.
3. Open the sample outputs.
4. Skim the AI workflow examples.
5. Look at the agent skills if you want reusable workflows.

If you have 30 minutes:

1. Read the system map.
2. Review the fictional product context.
3. Inspect the sample data.
4. Run the scripts.
5. Compare the generated outputs.
6. Review the AI prompts, schemas, and sample outputs.
7. Review the agent skills and adapt one workflow.

## Repository Map

The public repo is organized around how a reader learns and uses the system.

```text
product-ops-sandbox/
|-- README.md
|-- START_HERE.md
|-- WALKTHROUGH.md
|-- SECURITY.md
|-- LICENSE
|-- docs/
|   |-- 00-product-ops-system-map.md
|   |-- 01-product-context.md
|   |-- 02-success-metrics.md
|   |-- 03-product-analytics-tracking-plan.md
|   |-- 04-customer-feedback-system.md
|   |-- 05-user-research-repository.md
|   |-- 06-roadmap-prioritization.md
|   |-- 07-okr-planning.md
|   |-- 08-release-communication.md
|   |-- 09-ai-assisted-product-ops.md
|   `-- 10-agent-skills.md
|-- sample-data/
|-- scripts/
|-- outputs/
|-- ai-workflows/
|-- agent-skills/
|-- tests/
|-- requirements.txt
`-- requirements-ai.txt
```

## How To Run It

The core scripts use Python and standard library modules.

```bash
python scripts/analyze_feedback.py
python scripts/score_roadmap.py
python scripts/summarize_metrics.py
```

The AI-assisted scripts run in mock mode by default. They do not require an API key.

```bash
python scripts/ai_classify_feedback.py
python scripts/ai_synthesize_research.py
python scripts/ai_detect_opportunities.py
python scripts/ai_generate_weekly_summary.py
```

Optional live AI mode can be added with an approved API key and model endpoint. Mock mode is the default so the repo stays safe and easy to run.

## What You Should See

The scripts generate readable outputs:

| Output | Purpose |
| --- | --- |
| `feedback_theme_summary.md` | Shows repeated feedback themes and severity counts |
| `roadmap_priority_scores.md` | Shows prioritized roadmap candidates using a transparent formula |
| `metrics_snapshot.md` | Shows basic product usage metrics |
| `ai_feedback_classification.json` | Shows structured AI-assisted feedback classification |
| `ai_research_synthesis.json` | Shows AI-assisted research synthesis |
| `ai_opportunity_map.json` | Shows how messy signals become opportunity statements |
| `ai_weekly_product_insights.md` | Shows a weekly Product Ops summary |

## Why JSON Appears In The AI Examples

Some AI outputs are saved as JSON because structured output is easier to review and reuse.

For example:

```json
{
  "theme": "Failed check-in",
  "severity": "High",
  "linked_metric": "Check-in Failed Count"
}
```

Markdown is better for human summaries. JSON is better when another script, workflow, or agent needs a predictable structure.

## What This Is Not

This repo is not:

- a real analytics platform
- a replacement for Mixpanel, Productboard, Condens, or any other commercial tool
- connected to a real company
- based on real customer data
- an AI system that makes product decisions automatically

It models the workflows those tool categories often support:

- analytics planning
- feedback management
- research synthesis
- roadmap prioritization
- OKR alignment
- release communication
- AI-assisted synthesis

## Security And Data Handling

This repo is designed for public learning.

Do not add:

- real customer data
- real interview transcripts
- private company notes
- API keys
- tokens
- passwords
- confidential business information

Use fictional, synthetic, or fully anonymized examples only.

## Current Build Status

This public version is being assembled step by step.

The first goal is to make the GitHub landing page clear. The next files will add the guided walkthrough, docs, sample data, scripts, outputs, AI workflows, and reusable agent skills.

