# Prompt: Classify Product Feedback

You are helping with Product Operations analysis for a fictional product called FitPass Demo.

## Input Location

Read qualitative product notes from `input-notes/`.

For the first run, use:

```text
input-notes/support-ticket-batch.md
```

If the user provides another note file, use that file instead.

## Task

Classify each note into structured product feedback.

For each item, return:

- `source_id`
- `product_area`
- `theme`
- `severity`
- `linked_metric`
- `evidence_summary`
- `possible_opportunity`
- `confidence`

## Allowed Severity Values

- `Low`
- `Medium`
- `High`
- `Critical`

## Allowed Product Areas

- `Activation`
- `Search`
- `Booking`
- `Check In`
- `Employer reporting`
- `Partner data`
- `Notifications`
- `Habit`
- `Other`

## Allowed Confidence Values

- `Low`
- `Medium`
- `High`

## Output

Return JSON that follows:

```text
ai-workflows/schemas/feedback_classification.schema.json
```

When working inside the repo, write the draft to:

```text
outputs/ai_feedback_classification.json
```

Then also write a short easy-to-read summary next to it:

```text
outputs/ai_feedback_classification.md
```

If you are in a chat only tool that cannot write files, return the JSON and a short summary in the chat.

## Rules

- Use only the provided notes.
- Do not invent customers, numbers, metrics, or product facts.
- Keep evidence summaries short and traceable to the note.
- Use `Other` if the product area is unclear.
- Use `Low` confidence when the note is ambiguous.
