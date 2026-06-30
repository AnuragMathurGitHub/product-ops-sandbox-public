# Prompt: Weekly Product Insights

You are preparing a weekly Product Operations readout for FitPass Demo.

## Input Location

Read the weekly packet from `input-notes/`:

```text
input-notes/weekly-product-ops-packet.md
```

You can also read the generated outputs for supporting detail:

```text
outputs/metrics_snapshot.md
outputs/feedback_theme_summary.md
```

## Task

Write a concise weekly readout for product, engineering, customer success, support, sales,
marketing, and operations.

Include these sections:

- `What Changed`: a few bullets on what stood out this week
- `Product Readout`: a small table with columns Area, Signal, and Suggested Follow-Up
- `Decision Questions`: a few questions for the team to decide on

## Output

This workflow produces a human-readable Markdown file (no JSON, because the readout is meant for
people, not for another script). Write it to:

```text
outputs/ai_weekly_product_insights.md
```

If you are in a chat-only tool that cannot write files, return the Markdown in the chat.

## Rules

- Use plain language. Keep the tone practical and honest.
- Use only the provided input. If the data is limited, say it is limited.
- Do not invent metrics or facts.
- Keep it short enough to read in a couple of minutes.
