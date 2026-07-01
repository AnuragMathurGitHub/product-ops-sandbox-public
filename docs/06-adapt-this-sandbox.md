# Adapt This Sandbox To Your Product

This guide shows how to turn the FitPass Demo sandbox into a Product Ops workspace for your own
product. It is practical: it names the exact files to edit, which files to keep as templates, and
which local or private files to create so you never commit sensitive data.

The rule that keeps this safe and simple:

```text
Change one input. Run or ask. Review the output. Then change the next thing.
```

Do not replace everything at once. One change at a time is easier to trust and easier to undo.

## Before You Start

1. Make your own copy. Fork the repo or download it, then work in a private repository if you will
   use real company context. Keep this public sandbox fictional.
2. Use fictional, synthetic, anonymized, or approved data in anything public. Use real data only in a
   private environment where you have permission and clear data handling controls.
3. Keep the folder shape. The scripts, prompts, and skills expect notes in `input-notes/`, structured
   data in `sample-data/`, and results in `outputs/`. Change the contents, not the layout, at first.

## The Adaptation Order

Work top to bottom. Each row is one safe change.

| Step | What To Change | File Or Folder | Keep As Template? |
| --- | --- | --- | --- |
| 1 | Product context (users, buyers, problem) | `docs/01-product-context.md` | Rewrite for your product |
| 2 | Success metrics | `docs/02-success-metrics.md` | Rewrite for your product |
| 3 | One structured CSV | `sample-data/` | Keep the column headers at first |
| 4 | One notes file | `input-notes/` | Add a new file; keep the shape |
| 5 | One prompt | `ai-workflows/prompts/` | Adjust taxonomy and guardrails |
| 6 | Matching schema (only if fields change) | `ai-workflows/schemas/` | Edit fields to match the prompt |
| 7 | One agent skill | `agent-skills/` | Adjust taxonomy, format, review rules |
| 8 | OKRs and release assumptions | `sample-data/okrs.csv`, `sample-data/releases.csv` | Keep headers; change rows |

## Step By Step

### 1 and 2: Tell your product story

Open `docs/01-product-context.md` and describe your real users, buyers, partners, and the core
product problem. Then open `docs/02-success-metrics.md` and list the metrics that matter for your
product. These two files are the context every other step leans on, so change them first.

### 3: Replace one structured file

Pick one file in `sample-data/`, for example `customer_feedback.csv` or `roadmap_items.csv`. Keep the
existing column headers the first time so the scripts still run. Change only the rows. Then run the
matching script and read the output:

```bash
python scripts/analyze_feedback.py     # sample-data/customer_feedback.csv -> outputs/feedback_theme_summary.md
python scripts/score_roadmap.py        # sample-data/roadmap_items.csv     -> outputs/roadmap_priority_scores.md
python scripts/summarize_metrics.py    # sample-data/product_events.csv    -> outputs/metrics_snapshot.md
python scripts/summarize_okrs.py       # sample-data/okrs.csv              -> outputs/okr_snapshot.md
python scripts/summarize_releases.py   # sample-data/releases.csv          -> outputs/release_readiness_snapshot.md
```

If a script fails, a column header probably changed. Put the original header back, or update the
script to match your new header once you are comfortable.

### 4: Add one notes file

Create a new file in `input-notes/`, for example `input-notes/my-support-notes.md`, and paste a small
batch of short, fictional or anonymized notes. Keep the same shape as
`input-notes/support-ticket-batch.md`. If the notes are sensitive and you are working privately, name
the file with a `private-` or `local-` prefix so `.gitignore` helps prevent an accidental commit.

Then ask your assistant to process it, or run the matching mock or API workflow. See
`docs/03-how-to-run-the-workflows.md` for the exact request.

### 5 and 6: Adjust the prompt and schema

Open the prompt that matches your workflow in `ai-workflows/prompts/`, for example
`classify_feedback.md`. Change the allowed product areas, themes, severities, and any guardrails to
fit your product. If you add or rename output fields, update the matching schema in
`ai-workflows/schemas/` so the structured output stays valid.

### 7: Adjust an agent skill

If you use the agent skills, open the matching folder in `agent-skills/` and update its taxonomy,
output format, and review rules so a coding assistant produces the shape you want. Keep the skill
description accurate so tools can tell when to use it.

### 8: Update OKRs and release assumptions

Edit `sample-data/okrs.csv` and `sample-data/releases.csv`. Keep the headers, change the rows, and
re-run `summarize_okrs.py` and `summarize_releases.py`. Remember the framing: OKRs come from strategy
and product outcomes, and this repo shows how product evidence can support or challenge them. It does
not generate OKRs from raw feedback.

## Files To Keep As Templates

Do not delete these. They show the shape your own files should follow:

- `input-notes/support-ticket-batch.md` and the other note files
- one row of each CSV in `sample-data/`
- the prompts in `ai-workflows/prompts/` and schemas in `ai-workflows/schemas/`
- the sample outputs in `ai-workflows/sample-outputs/`

## Local And Private Files To Create

For anything sensitive, use the ignored patterns already in `.gitignore`:

- `input-notes/private-*` or `input-notes/local-*` for real notes
- `sample-data/private-*` or `sample-data/local-*` for real data
- `outputs/private-*` or `outputs/local-*` for real results
- `.env` for an API key if you use the optional API lane (see `docs/04-api-extension.md`)

## Safety Checklist Before You Share

- No real customer data, credentials, or confidential business information in any committed file.
- Sensitive files use a `private-` or `local-` prefix, or live in a private repository.
- The public copy stays fictional, synthetic, anonymized, or approved.
- Review `SECURITY.md` before sharing anything.

## What To Read Next

- `docs/03-how-to-run-the-workflows.md` for the exact per workflow requests.
- `docs/05-planning-loop.md` for how signals, OKRs, release, and measurement connect.
- `docs/04-api-extension.md` for the optional API lane.
