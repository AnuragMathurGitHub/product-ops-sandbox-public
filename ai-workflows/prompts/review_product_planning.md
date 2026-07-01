# Prompt: Product Planning Review

You are helping Product Operations review how signals connect to planning decisions for FitPass Demo.

## Input Location

Read these files:

```text
outputs/metrics_snapshot.md
outputs/feedback_theme_summary.md
outputs/roadmap_priority_scores.md
outputs/ai_feedback_classification.md
outputs/ai_research_synthesis.md
outputs/ai_opportunity_map.md
outputs/okr_snapshot.md
```

If a file is missing, say what is missing and continue with the available evidence.

## Task

Write a concise product planning review that shows how the loop connects:

```text
Signals explain what is happening.
Insights explain why it may matter.
Opportunities define what could improve.
Prioritization compares what deserves attention.
Roadmap candidates show what the team may build.
OKR alignment connects work to measurable outcomes.
Release planning prepares teams for launch.
Measurement checks whether the change worked.
```

Include these sections:

- `Evidence Chain`: connect the strongest signal to insight, opportunity, metric, and roadmap candidate
- `Planning Assessment`: explain what looks well supported and what still needs evidence
- `Roadmap Review`: list the candidates that deserve discussion, not a final commitment
- `OKR Connection`: explain which outcome the work may support
- `Decision Risks`: list risks the team should review before committing
- `Next Review`: state what should be measured or learned next

## Output

Write the result to:

```text
outputs/ai_product_planning_review.md
```

If you are in a chat only tool that cannot write files, return the Markdown in the chat.

## Rules

- Do not invent facts, numbers, quotes, or company names.
- Do not turn a roadmap candidate into a commitment.
- Do not say an OKR is final unless the input explicitly says it is final.
- Use plain language and keep the review useful for product, engineering, design, customer success, support, sales, marketing, and operations.
