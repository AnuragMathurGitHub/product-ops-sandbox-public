# API Extension

You do not need an API key to use this repo.

Most users should start with the **Agent** lane: open the repo in your IDE, AI native IDE, terminal
agent, or approved assistant, then ask it to read the prompt and notes. That gives real AI synthesis
with no API key.

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
| Learn the workflow | Read only or mock demo |
| Classify a few notes manually | Agent |
| Use your existing AI assistant with repo files | Agent |
| Run a weekly private scheduled batch | API extension |
| Connect internal systems or scheduled exports | API extension |
| Process approved data at scale | API extension |

## Where The Key Would Live

The key should live outside source code.

Different providers use different environment variable names. Common examples:

| Provider Or Gateway | Common Key Name | Notes |
| --- | --- | --- |
| OpenAI | `OPENAI_API_KEY` | Used by OpenAI SDKs |
| Anthropic Claude API | `ANTHROPIC_API_KEY` | Used for direct Anthropic API access |
| OpenRouter | `OPENROUTER_API_KEY` | Common for OpenRouter SDK and agent integrations |
| Internal model gateway | Team defined | Follow your company security guidance |

Example for a temporary PowerShell session:

```powershell
$env:OPENAI_API_KEY = "your_openai_key_here"
$env:ANTHROPIC_API_KEY = "your_anthropic_key_here"
$env:OPENROUTER_API_KEY = "your_openrouter_key_here"
```

Example for a persistent PowerShell setting:

```powershell
setx OPENAI_API_KEY "your_openai_key_here"
setx ANTHROPIC_API_KEY "your_anthropic_key_here"
setx OPENROUTER_API_KEY "your_openrouter_key_here"
```

Use only the variable that matches your provider. Do not set keys you do not need.

Do not put API keys in:

- `README.md`
- scripts
- prompts
- schemas
- CSV files
- note files
- committed `.env` files

## Where Private API Code Would Go

This public repo does not include a live API script because it should stay safe, provider neutral,
and easy to run.

If you add live API code for your own team, use one of these patterns:

| Pattern | Use When |
| --- | --- |
| Private fork | A team wants to adapt the sandbox internally |
| Separate private repo | You are connecting real systems or credentials |
| Local ignored script | You are experimenting on your machine |

The `.gitignore` includes local only patterns:

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

## Provider References

If a team chooses a provider for a private implementation, start with its official docs:

- OpenAI API quickstart: https://developers.openai.com/api/docs/quickstart
- OpenAI SDK and API key setup: https://developers.openai.com/api/docs/libraries
- OpenAI Structured Outputs: https://developers.openai.com/api/docs/guides/structured-outputs
- Anthropic Claude API getting started: https://docs.anthropic.com/en/docs/get-started
- Anthropic Claude Code authentication: https://docs.anthropic.com/en/docs/claude-code/iam
- OpenRouter authentication: https://openrouter.ai/docs/api/reference/authentication
- OpenRouter Codex CLI integration: https://openrouter.ai/docs/cookbook/coding-agents/codex-cli

The key implementation rule stays the same across providers:

```text
Do not hard code secrets.
Do not commit sensitive data.
Validate AI output.
Keep humans accountable for decisions.
```
