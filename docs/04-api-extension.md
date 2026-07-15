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

The key is not used by the mock demo scripts (for example `scripts/ai_classify_feedback.py`), which
copy prepared outputs and do not call any AI provider. The one script that does use your key is the
optional `scripts/ai_real.py` pipeline described below.

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

## Run The Included API Pipeline

This repo ships one optional live script, `scripts/ai_real.py`. It reads the same prompts, schemas,
and notes the other lanes use, calls a real model with your own key, and writes drafts into
`outputs/`. It is off the critical path: the repo still runs with no key through the agent lane and
the mock demo.

### Choose A Provider

The script is provider neutral, like the agent lane. Set `PRODUCT_OPS_PROVIDER`:

| `PRODUCT_OPS_PROVIDER` | Key variable | Python package | Model |
| --- | --- | --- | --- |
| `anthropic` (default) | `ANTHROPIC_API_KEY` | `anthropic` | set `PRODUCT_OPS_MODEL` to a current Anthropic model |
| `openai` | `OPENAI_API_KEY` | `openai` | set `PRODUCT_OPS_MODEL` to a current OpenAI model |
| `openrouter` | `OPENROUTER_API_KEY` | `openai` | set `PRODUCT_OPS_MODEL` to a current OpenRouter model ID |

OpenAI and OpenRouter share the `openai` package: OpenRouter is OpenAI-API compatible, so the script
just points it at OpenRouter's base URL. Install only the package for the provider you use; the
script imports just that one.

### Anthropic (default)

```bash
pip install anthropic
export ANTHROPIC_API_KEY=your-anthropic-key    # your own key; never commit it
export PRODUCT_OPS_MODEL=your-current-model-id
python scripts/ai_real.py                      # run every workflow
python scripts/ai_real.py classify_feedback    # or run a single workflow
```

Windows PowerShell:

```powershell
pip install anthropic
$env:ANTHROPIC_API_KEY = "your-anthropic-key"
$env:PRODUCT_OPS_MODEL = "your-current-model-id"
python scripts/ai_real.py
```

Use a current model ID from your provider account.

### OpenAI

Set your `OPENAI_API_KEY` first (see "Where The Key Would Live" above), then:

```bash
pip install openai
PRODUCT_OPS_PROVIDER=openai PRODUCT_OPS_MODEL=your-current-model-id python scripts/ai_real.py
```

### OpenRouter

Set your `OPENROUTER_API_KEY` first (same as above), then:

```bash
pip install openai
PRODUCT_OPS_PROVIDER=openrouter PRODUCT_OPS_MODEL=your-current-model-id python scripts/ai_real.py
```

`PRODUCT_OPS_MODEL` is required for every provider. Check your provider's current model names before
running the script.

### The Schema Gate

The model is probabilistic, so `scripts/ai_real.py` makes the workflow deterministic at the
boundary instead: every reply passes through the gate in `scripts/harness.py` before anything is
written. The reply must parse as JSON and satisfy the workflow's schema. On a bad reply the script
retries up to three times, then fails with a clear error instead of writing a bad draft.

The same gate works from the command line for any lane, including drafts an assistant wrote in the
agent lane:

```bash
python scripts/harness.py outputs/ai_feedback_classification.json ai-workflows/schemas/feedback_classification.schema.json
```

It prints any contract violations and exits 0 when the draft matches the schema.

### Notes

If no key is set, the script does not crash. It prints how to set a key and reminds you the agent and
mock lanes need none. Run the deterministic scripts first (see `START_HERE.md`, Step 6) if `outputs/`
is empty, because the review and weekly workflows read files those scripts produce.

Available workflow names: `classify_feedback`, `synthesize_research`, `detect_opportunities`,
`align_okrs`, `plan_release_measurement`, `review_product_planning`, `weekly_product_insights`.

## Where More Private API Code Would Go

`scripts/ai_real.py` is intentionally small and safe to publish: it holds no key, makes no network
call until you set one, and keeps the Product Ops logic in the shared prompts and schemas. For
heavier or company-specific automation, keep that code private. Use one of these patterns:

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
5. Validate the JSON output against the schema. `scripts/harness.py` is a working example: it
   parses the reply, checks it against the schema, retries a fixed number of times, and fails
   closed.
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
