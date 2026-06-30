# Agent Skills

This folder describes reusable AI assistant workflows for Product Operations tasks.

Use it when you want an assistant to follow the same analysis pattern repeatedly instead of starting from a blank chat each time.

## How To Think About Skills

An agent skill is a reusable instruction package:

```text
task
-> context
-> inputs
-> rules
-> output format
-> review checklist
```

In this sandbox, the first reusable pattern is feedback classification:

| Element | Location |
| --- | --- |
| Notes | `input-notes/` |
| Prompt | `ai-workflows/prompts/classify_feedback.md` |
| Schema | `ai-workflows/schemas/feedback_classification.schema.json` |
| Output | `outputs/ai_feedback_classification.json` |

## Safe Use

- Keep real customer data out of the public repo.
- Ask the assistant to cite evidence from source notes.
- Review the output before making a product decision.
- Treat the skill as a repeatable assistant workflow, not as automated judgment.
