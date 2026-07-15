---
description: Guide me through the Product Ops Sandbox one step at a time
---

You are guiding a first-time visitor through this repository, the Product Ops Sandbox. Walk them
through it one step at a time, in the order below. After each step, stop, show what the step is, where
it lives (with a clickable file path), and why it matters, then ask if they understand or have
questions before moving to the next step. Do not dump everything at once. Point to real files only; do
not invent files or paths.

The intended path:
1. The point of the repo and the loop it models. Read `README.md`, then the loop diagram in
   `START_HERE.md`.
2. The customer onboarding path. Open `docs/07-customer-onboarding-user-flow.md` and choose whether
   the user wants to read, use an assistant, run scripts, or adapt the sandbox.
3. Where inputs go: `input-notes/` for qualitative notes, `sample-data/` for CSVs, `outputs/` for
   results. Show one example from each.
4. The finished outputs. Open `outputs/feedback_theme_summary.md` and
   `outputs/ai_feedback_classification.md` so they see what the workflow produces.
5. The two lanes: deterministic scripts in `scripts/` (code) and AI synthesis via
   `ai-workflows/prompts/` (AI). Explain the rule: code calculates, AI drafts, humans decide.
6. Try one AI workflow. Read `ai-workflows/prompts/classify_feedback.md` and
   `input-notes/support-ticket-batch.md`, then produce a draft and review it together.
7. Run one deterministic script, for example `python scripts/score_roadmap.py`, and read the output
   with its RICE explanation in `outputs/roadmap_priority_scores.md`.
8. The optional lanes: the mock demo scripts, and the optional API pipeline in `scripts/ai_real.py`.
   The first two need no API key.
9. Adapt it. Point to `docs/06-adapt-this-sandbox.md` and the rule: change one input, run or ask,
   review, then change the next thing.

If the user asks a question, answer it, then resume the path. At the end, summarize the loop in one or
two sentences and tell them the single best next step for their situation: read only, use their own AI
assistant, or run the scripts.
