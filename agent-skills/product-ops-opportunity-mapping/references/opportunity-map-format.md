# Opportunity Map Format

Use this format to turn product signals into opportunity statements. It matches
`ai-workflows/schemas/opportunity_map.schema.json`.

## Opportunity Fields

| Field | Meaning |
| --- | --- |
| opportunity | Short label focused on the problem |
| customer_problem | Who has what problem and why it matters, in plain language |
| linked_metric | The metric most related to the opportunity |
| evidence | Short, source grounded summary of the supporting signal |
| possible_solution_direction | A direction to explore, not a committed solution |

The top level object also includes `review_questions`: questions a human should answer before any
roadmap commitment.

## Example Pattern

```text
opportunity: Help new members reach a useful first visit faster
customer_problem: New members can activate but still feel unsure what to do next.
linked_metric: First Successful Visit Rate
evidence: Interview and support notes mention an unclear next step after activation.
possible_solution_direction: Improve first week guidance and nearby option recommendations.
```

## Guardrails

- Write opportunities as problems before directions.
- Include at least one piece of evidence per opportunity.
- Use review questions when a signal is plausible but needs more evidence.
