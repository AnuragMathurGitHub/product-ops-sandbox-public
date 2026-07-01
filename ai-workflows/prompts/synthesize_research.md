# Prompt: Synthesize Research Notes

You are helping with Product Operations research synthesis for a fictional product called FitPass Demo.

## Input Location

Read qualitative research from `input-notes/`.

For the first run, use:

```text
input-notes/user-interview-transcript.md
```

If the user provides another interview or research note, use that file instead.

## Task

Read the transcript or research notes and produce a concise synthesis.

Return:

- `themes`: a list of objects, each with:
  - `theme`: a short pattern observed across the notes
  - `evidence`: a short, source grounded summary of what supports the theme
  - `implication`: what the theme means for the product
- `insights`: a list of short statements that are useful for decisions
- `recommended_review_questions`: questions a human should review before acting

## Output

Return JSON that follows:

```text
ai-workflows/schemas/research_synthesis.schema.json
```

When working inside the repo, write the draft to:

```text
outputs/ai_research_synthesis.json
```

Then also write a short easy-to-read summary next to it:

```text
outputs/ai_research_synthesis.md
```

If you are in a chat only tool that cannot write files, return the JSON and a short summary in the chat.

## Rules

- Use only the provided notes.
- Do not invent participants, quotes, numbers, or product facts.
- Keep evidence short and traceable to the input.
- Prefer fewer, clearer themes over many shallow ones.
- Mark uncertain conclusions as uncertain in the review questions.
