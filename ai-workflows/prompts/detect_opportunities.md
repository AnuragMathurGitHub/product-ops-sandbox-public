# Prompt: Detect Product Opportunities

You are helping Product Operations turn signals into roadmap opportunities for FitPass Demo.

## Input Location

Read the notes in `input-notes/`. This workflow works best when several signals are combined, so
read all available note files (for example, the support tickets and the interview transcript).

You can also use existing results as supporting evidence:

```text
outputs/feedback_theme_summary.md
outputs/ai_feedback_classification.json
```

## Task

Identify product opportunities that the input actually supports.

Return:

- `opportunities`: a list of objects, each with:
  - `opportunity`: a short opportunity title
  - `customer_problem`: the user or buyer problem in plain language
  - `linked_metric`: the metric most related to the opportunity
  - `evidence`: a short, source grounded summary
  - `possible_solution_direction`: a direction to explore, not a committed solution
- `review_questions`: questions a human should answer before any roadmap commitment

## Output

Return JSON that follows:

```text
ai-workflows/schemas/opportunity_map.schema.json
```

When working inside the repo, write the draft to:

```text
outputs/ai_opportunity_map.json
```

Then also write a short easy-to-read summary next to it:

```text
outputs/ai_opportunity_map.md
```

If you are in a chat only tool that cannot write files, return the JSON and a short summary in the chat.

## Rules

- Use only the provided input.
- Do not invent customer data, company names, or unsupported metrics.
- Every opportunity must trace to evidence in the notes.
- Frame solutions as directions to explore, not as decisions.
- Keep the human review layer: opportunities are drafts for the team to prioritize.
