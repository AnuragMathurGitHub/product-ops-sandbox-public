---
name: product-ops-weekly-review
description: Create a weekly Product Ops readout from product metrics, feedback themes, research insights, and roadmap signals. Use when preparing a concise cross-functional product update for product, engineering, support, customer success, sales, marketing, and operations.
---

# Product Ops Weekly Review

## Overview

Use this skill to prepare a short cross-functional weekly Product Ops readout. The goal is to help
teams see what changed, what matters, and what decisions are needed.

## Inputs And Outputs (single source of truth)

Follow the canonical prompt so every tool produces the same shape:

- Input: `input-notes/weekly-product-ops-packet.md`
- Supporting detail: `outputs/metrics_snapshot.md`, `outputs/feedback_theme_summary.md`
- Prompt: `ai-workflows/prompts/weekly_product_insights.md`
- Output: `outputs/ai_weekly_product_insights.md` (Markdown only, because the readout is for people)

## Workflow

1. Summarize what changed this week in a few plain-language bullets.
2. Build a small Product Readout table: Area, Signal, Suggested Follow-Up.
3. List a few Decision Questions for the team.

## Review Rules

- Keep it concise and easy to scan.
- Say when the data is limited, directional, or synthetic.
- Avoid generic executive language.
- Do not invent trends without comparison data.

## References

Read `references/weekly-review-format.md` for the readout format.
