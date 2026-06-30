# Input Notes

Use this folder for unstructured product notes.

These are qualitative signals written in human language. They are different from CSV-style structured data.

## What Goes Here

Add fictional, anonymized, or approved notes such as:

| Note Type | Example File Name |
| --- | --- |
| Support ticket batch | `support-ticket-batch.md` |
| Sales call notes | `sales-call-notes.md` |
| Customer success meeting notes | `customer-success-meeting.md` |
| User interview transcript | `user-interview-transcript.md` |
| Partner feedback | `partner-feedback.md` |
| App review excerpts | `app-review-excerpts.md` |

## What Does Not Go Here

Do not add:

- real customer data
- personal information
- private company notes
- raw confidential transcripts
- API keys or credentials

## How To Use This Folder

1. Open the sample file `support-ticket-batch.md`, or add one new `.md` note file.
2. Choose the matching prompt from `ai-workflows/prompts/`.
3. Ask your AI assistant to read the note file and prompt.
4. Ask it to write a draft output into `outputs/`.
5. Review the output before using it for decisions.

Example assistant request:

```text
Read input-notes/support-ticket-batch.md and ai-workflows/prompts/classify_feedback.md.
Classify the notes into product area, theme, severity, linked metric, evidence summary, and possible opportunity.
Write the draft output to outputs/ai_feedback_classification.json.
Do not invent facts.
```

## Recommended First File

Start with the included sample:

```text
input-notes/support-ticket-batch.md
```

Keep it short. Five to ten notes are enough for a first test.
