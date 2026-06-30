# API Extension

You do not need an API key to use this repo.

Most users should start with the **Agent** lane: open the repo in Codex, Cursor, Claude Code, GitHub
Copilot, or another approved assistant, then ask it to read the prompt and notes. That gives real AI
synthesis with no API key.

The API path is only for teams that want private automation later.

## What An API Key Means

An API key is a private credential that lets a program call an AI provider directly.

In this repo, that would mean:

```text
a private script or service
-> reads input-notes/
-> reads ai-workflows/prompts/
-> optionally reads ai-workflows/schemas/
-> calls an AI model through an API
-> writes outputs/
-> human reviews the result
```

The key is not used by the public sample scripts. The public `scripts/ai_*.py` files are mock demos:
they copy prepared outputs and do not call any AI provider.

## When You Would Use The API Path

Use an API only when you need automation that a chat or coding assistant cannot provide.

| Need | Better Lane |
| --- | --- |
| Learn the workflow | Read-only or mock demo |
| Classify a few notes manually | Agent |
| Use your existing AI assistant with repo files | Agent |
| Run a weekly private scheduled batch | API extension |
| Connect internal systems or scheduled exports | API extension |
| Process approved data at scale | API extension |

## Where The Key Would Live

The key should live outside source code.

For OpenAI, the common environment variable is:

```text
OPENAI_API_KEY
```

Example for a temporary PowerShell session:

```powershell
$env:OPENAI_API_KEY = "your_api_key_here"
```

Example for a persistent PowerShell setting:

```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

Do not put API keys in:

- `README.md`
- scripts
- prompts
- schemas
- CSV files
- note files
- committed `.env` files

## Where Private API Code Would Go

This public repo does not include a live API script because it should stay safe, provider-neutral,
and easy to run.

If you add live API code for your own team, use one of these patterns:

| Pattern | Use When |
| --- | --- |
| Private fork | A team wants to adapt the sandbox internally |
| Separate private repo | You are connecting real systems or credentials |
| Local ignored script | You are experimenting on your machine |

The `.gitignore` includes local-only patterns:

```text
scripts/private-*
scripts/local-*
requirements-private*.txt
requirements-local*.txt
private-data/
local-inputs/
sensitive-data/
```

So a local experiment might be named:

```text
scripts/private-live-classify-feedback.py
```

## What A Live Script Would Do

A live script should follow the same repo contract:

1. Read an input file, for example `input-notes/private-support-notes.md`.
2. Read the matching prompt, for example `ai-workflows/prompts/classify_feedback.md`.
3. Read the schema, for example `ai-workflows/schemas/feedback_classification.schema.json`.
4. Call the model through the provider API.
5. Validate the JSON output against the schema.
6. Write a JSON draft and a readable Markdown summary into `outputs/`.
7. Require human review before product decisions.

The API should change only the execution lane. It should not change the Product Ops logic.

## OpenAI Example References

If a team chooses OpenAI for a private implementation, start with:

- API quickstart: https://developers.openai.com/api/docs/quickstart
- SDK and API key setup: https://developers.openai.com/api/docs/libraries
- Text generation with the Responses API: https://developers.openai.com/api/docs/guides/text
- Structured Outputs for JSON schemas: https://developers.openai.com/api/docs/guides/structured-outputs
- Production best practices: https://developers.openai.com/api/docs/guides/production-best-practices

The key implementation rule stays the same across providers:

```text
Do not hard-code secrets.
Do not commit sensitive data.
Validate AI output.
Keep humans accountable for decisions.
```
