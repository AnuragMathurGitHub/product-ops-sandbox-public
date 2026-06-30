# Research Synthesis Format

Use this structure for Product Ops research synthesis. It matches
`ai-workflows/schemas/research_synthesis.schema.json`.

## Output Shape

```text
themes:
- theme: a short pattern observed across the notes
  evidence: a short, source-grounded summary of what supports it
  implication: what it means for the product

insights:
- short, decision-useful statements

recommended_review_questions:
- questions a human should review before acting
```

## Guidance

- Keep evidence close to the source material.
- Use insights to explain what the themes may mean, not to assert new facts.
- Avoid turning one interview into a universal claim.
- Use review questions to flag what still needs validation.
