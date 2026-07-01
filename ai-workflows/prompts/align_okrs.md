# Prompt: OKR Alignment

You are helping Product Operations connect planning evidence to product OKRs for FitPass Demo.

## Input Location

Read these files:

```text
sample-data/okrs.csv
outputs/okr_snapshot.md
outputs/metrics_snapshot.md
outputs/feedback_theme_summary.md
outputs/roadmap_priority_scores.md
outputs/ai_opportunity_map.json
outputs/ai_product_planning_review.md
```

If a file is missing, say what is missing and continue with the available evidence.

## Task

Create an OKR alignment draft.

Important framing:

```text
OKRs are not created only from feedback.
OKRs come from product strategy, company priorities, and measurable outcomes.
Feedback, research, analytics, and roadmap candidates help test whether the current work supports those outcomes.
```

For each useful alignment, include:

- `objective`: the product objective being supported
- `key_result`: the measurable key result
- `linked_metric`: the metric connected to the key result
- `supporting_evidence`: the evidence from metrics, feedback, research, or opportunity mapping
- `related_opportunity`: the opportunity that may help the objective
- `roadmap_candidate`: the roadmap item that may support the key result
- `alignment_assessment`: whether the alignment is strong, partial, or weak
- `human_review_needed`: what a product leader should review before using it

## Output

Write JSON that matches:

```text
ai-workflows/schemas/okr_alignment.schema.json
```

Write it to:

```text
outputs/ai_okr_alignment.json
```

Then also write a short easy-to-read summary next to it:

```text
outputs/ai_okr_alignment.md
```

If you are in a chat only tool that cannot write files, return the JSON and a short summary in the chat.

## Rules

- Use only the provided evidence.
- Treat the result as an alignment draft, not as approved OKRs.
- Prefer outcome language over feature language.
- Keep humans accountable for the final OKR decision.
