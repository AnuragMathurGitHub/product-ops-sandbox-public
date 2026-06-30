# How The Workflows Run (User Flow)

This is the map of how you go from raw notes to a reviewed product decision, and how to run the AI
part without writing everything by hand.

## The whole system in one line

```text
INPUTS                 INSTRUCTIONS              EXECUTION LANE            OUTPUTS              HUMAN
input-notes/*.md   ->  ai-workflows/prompts/ ->  pick a lane (below)  ->  outputs/*.json   ->  review
sample-data/*.csv      ai-workflows/schemas/     + AGENTS.md / skills     outputs/*.md         + decide
```

The prompt and its schema are the single source of truth. Every tool entry point (`AGENTS.md`,
`.claude/`, `.cursor/`, `.github/`) is just a thin way to invoke that same prompt.

## The four lanes

| Lane | What it is | Real AI? | API key? | Use it when |
| --- | --- | --- | --- | --- |
| Read only | Open the finished files in `outputs/` | No | No | You want to see results and understand the shape |
| Agent | Your assistant reads the prompt + notes and writes the output | Yes | No | You have an AI assistant and want real synthesis on your own notes |
| Mock demo | `python scripts/ai_*.py` copies a prepared example | No | No | You want a deterministic example run, are offline, or have no assistant |
| API extension | A private script or service calls a model in your own environment | Yes | Yes | A team wants to automate at scale with approved data |

```text
Mock = a deterministic demo of what the output looks like (no AI).
Agent = actually do it with your assistant (real AI, no key).   <- the main lane
API  = automate it at scale in a private environment (real AI, key).
```

If the API row feels confusing, skip it. This public repo works without an API key. The API path is
for teams that later want scheduled or backend automation. See `docs/04-api-extension.md`.

## The Agent lane, made turnkey

The repo ships an `AGENTS.md` workflow map plus tool specific entry points so an assistant has clear
instructions. You usually do not need to paste long prompts manually.

Copy paste start:

```text
Clone https://github.com/AnuragMathurGitHub/product-ops-sandbox-public.git.
Open README.md and START_HERE.md.
Explain the workflow, then classify the sample feedback in input-notes/support-ticket-batch.md.
Write the result to outputs/ai_feedback_classification.json and outputs/ai_feedback_classification.md.
Do not invent facts.
```

| Tool | Turnkey way to run a workflow | Mechanism |
| --- | --- | --- |
| IDE assistant | Open the folder in Visual Studio Code, JetBrains, or another IDE and ask the assistant to read `START_HERE.md` | IDE workspace context |
| AI native IDE | Open the folder in Cursor or a similar tool, then ask for the workflow you want | `AGENTS.md` plus workspace files |
| Terminal agent | Ask Codex, Claude Code, Gemini CLI, or another terminal agent to clone or open the repo | `AGENTS.md` workflow guidance |
| GitHub Copilot in VS Code | Use a `/prompt` from `.github/prompts/`, or ask with `@workspace` | `.github/` plus `AGENTS.md` |
| Claude Code | `/classify-feedback`, or the `/product-ops-signal-triage` skill | `.claude/commands/` + `.claude/skills/` |
| ChatGPT or Claude chat | paste a prompt + notes (fallback) | no file access |

Every workflow writes a structured `.json` draft and a readable `.md` summary, except the weekly
readout, which is Markdown only.

## End to End Journeys

- **Product manager or operator (no code):** read the README and `START_HERE.md`, open `outputs/`
  to see finished examples (Read only), then open the repo in your assistant and say "walk me through
  this and classify the sample notes" (Agent). Read the `.md` summary, add your own note file to
  `input-notes/`, and run it again.
- **Technical reviewer:** clone the repo, run `python scripts/*.py` (mock demo) to see
  deterministic outputs, run the tests, then inspect the prompts and schemas. Wire the API lane in
  your own environment if you need to automate.
- **Team adopting it:** replace `input-notes/` and `sample-data/` with approved, anonymized data,
  adjust the product context and a skill's taxonomy, run the Agent lane on your notes, and later
  automate with the API lane.

## The principle

```text
Code calculates. AI drafts. Humans review. Teams decide.
```
