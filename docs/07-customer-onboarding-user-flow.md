# Customer Onboarding User Flow

This guide is the customer-facing map for the public Product Ops Sandbox. Use it when you are
explaining the repo to a first-time visitor, improving the docs, or helping a team decide how to
adopt the sandbox.

The goal is simple: a new user should reach first value quickly, understand which tool lane fits
their situation, and know the next safe step.

## First Value

A first-time user reaches first value when they can say:

```text
I understand how product signals become reviewed planning outputs,
I know which files to open first,
and I know which lane to use for my next action.
```

For most users, the fastest first value is:

1. Open `START_HERE.md`.
2. Open one readable output in `outputs/`.
3. Ask an assistant to run one workflow, or run one deterministic script.
4. Review the output before making any product decision.

## Who The Onboarding Serves

| Visitor | What They Need First | First Success |
| --- | --- | --- |
| Product manager or Product Ops operator | Understand the loop and where inputs go | Can explain the workflow and open the right output |
| AI assistant user | Know what to ask the assistant to do | Assistant reads a prompt plus notes and writes a reviewed draft |
| Technical reviewer | Verify scripts, schemas, and safety boundaries | Runs scripts and tests without needing an API key |
| Team adopter | Safely adapt the sandbox to their product | Replaces one approved input and reviews the changed output |

## First-Time User Journey

```mermaid
journey
    title First-time Product Ops Sandbox journey
    section Arrive
      Land on README: 4: Reader
      Pick a path: 4: Reader
    section Orient
      Open START_HERE: 5: Reader
      Inspect outputs folder: 5: Reader
    section First value
      Run or ask for one workflow: 4: Reader, Assistant
      Review the markdown output: 5: Reader
    section Adopt
      Add one safe input: 4: Reader
      Run or ask again: 4: Reader, Assistant
      Decide the next change: 5: Reader, Team
```

## Full Onboarding Flow

```mermaid
flowchart TD
    A["Open README.md"] --> B["Choose your path"]
    B --> C{"What do you need first?"}

    C -->|Understand the sandbox| D["Read START_HERE.md"]
    C -->|See finished examples| E["Open outputs/*.md"]
    C -->|Use real AI with no key| F["Open repo in an assistant"]
    C -->|Run repeatable summaries| G["Run Python scripts"]
    C -->|Automate privately later| H["Read docs/04-api-extension.md"]

    D --> I["Open docs/00-product-ops-system-map.md"]
    E --> J["Compare inputs to outputs"]
    F --> K["Ask assistant to follow AGENTS.md"]
    G --> L["Run python -m unittest discover -s tests"]
    H --> M["Keep keys and real data private"]

    I --> N["Pick one workflow"]
    J --> N
    K --> N
    L --> N
    M --> N

    N --> O["Create or inspect one output"]
    O --> P["Human review"]
    P --> Q{"Ready to adapt?"}
    Q -->|No| R["Read docs/05-planning-loop.md"]
    Q -->|Yes| S["Follow docs/06-adapt-this-sandbox.md"]
    R --> P
    S --> T["Change one input, run or ask, review"]
    T --> P
```

## Lane Chooser

The repo has four lanes. Do not start with the API lane unless you already know you need private
automation.

```mermaid
flowchart LR
    Start["I want to use the sandbox"] --> Goal{"What is the goal?"}
    Goal -->|Learn only| Read["Read only<br/>GitHub browser<br/>No setup"]
    Goal -->|Synthesize notes| Agent["Agent lane<br/>IDE or terminal assistant<br/>Real AI, no repo key"]
    Goal -->|Demo repeatably| Mock["Mock demo<br/>python scripts/ai_*.py<br/>No AI call"]
    Goal -->|Schedule or scale| API["API extension<br/>scripts/ai_real.py or private service<br/>API key required"]

    Read --> Review["Review outputs"]
    Agent --> Review
    Mock --> Review
    API --> Review
    Review --> Decision["Human decision"]
```

| Lane | Tooling | Best First Use | Avoid When |
| --- | --- | --- | --- |
| Read only | GitHub browser | A PM or stakeholder wants to understand the workflow | You need changed outputs |
| Agent | Codex, Cursor, Claude Code, GitHub Copilot, Gemini CLI, or another assistant | You want real synthesis on notes with no repo API key | Your tool cannot read files and you cannot paste safe notes |
| Mock demo | Python standard library | You want deterministic sample outputs or an offline demo | You need fresh AI synthesis |
| API extension | Provider SDK plus private key | You need scheduled or backend automation with approved data | You are still learning the sandbox |

## Workflow Stack

```mermaid
flowchart LR
    subgraph Inputs["Inputs"]
        Notes["input-notes/*.md<br/>qualitative notes"]
        Data["sample-data/*.csv<br/>structured data"]
    end

    subgraph Instructions["Instructions"]
        Prompts["ai-workflows/prompts/*.md"]
        Schemas["ai-workflows/schemas/*.json"]
        Agents["AGENTS.md and agent-skills/"]
    end

    subgraph Execution["Execution lanes"]
        Assistant["Agent lane"]
        Scripts["Deterministic scripts"]
        Demo["Mock demo scripts"]
        PrivateAPI["Optional API extension"]
    end

    subgraph Results["Results"]
        JSON["outputs/*.json<br/>structured drafts"]
        Markdown["outputs/*.md<br/>readable summaries"]
        Review["Human review"]
    end

    Notes --> Prompts
    Data --> Scripts
    Prompts --> Schemas
    Prompts --> Assistant
    Agents --> Assistant
    Prompts --> Demo
    Prompts --> PrivateAPI
    Schemas --> Assistant
    Schemas --> PrivateAPI
    Assistant --> JSON
    Assistant --> Markdown
    Scripts --> Markdown
    Demo --> JSON
    Demo --> Markdown
    PrivateAPI --> JSON
    PrivateAPI --> Markdown
    JSON --> Review
    Markdown --> Review
```

## Recommended First Sessions

| Time | User | Path |
| --- | --- | --- |
| 5 minutes | Curious reader | Read README, then open `outputs/ai_weekly_product_insights.md` |
| 15 minutes | PM or Product Ops operator | Read `START_HERE.md`, inspect `input-notes/support-ticket-batch.md`, then open `outputs/ai_feedback_classification.md` |
| 20 minutes | Assistant user | Ask the assistant to read `AGENTS.md`, `ai-workflows/prompts/classify_feedback.md`, and `input-notes/support-ticket-batch.md`, then write the classification draft |
| 20 minutes | Technical reviewer | Run the deterministic scripts and `python -m unittest discover -s tests` |
| 45 minutes | Team adopter | Follow `docs/06-adapt-this-sandbox.md`, change one safe input, run or ask again, and review the changed output |

## Tool Map

| Need | Use This | Why |
| --- | --- | --- |
| Browse without setup | GitHub browser | The README, diagrams, and sample outputs render in place |
| Get a local copy | Download ZIP or `git clone` | Assistant and script workflows need file access |
| Real AI synthesis | IDE assistant, AI native IDE, or terminal agent | The assistant can read prompts, notes, and schemas from the repo |
| Repeatable calculations | Python scripts in `scripts/` | Counts, scores, and summaries should be deterministic |
| Reusable assistant behavior | `AGENTS.md`, `.github/prompts/`, `.claude/`, `.cursor/`, `agent-skills/` | Tool-specific entries point back to the same workflow contract |
| Private automation | `docs/04-api-extension.md` and `scripts/ai_real.py` | API keys and real data must stay out of the public repo |

## Best First Assistant Request

Use this in an assistant that can read files and run commands:

```text
Read README.md, START_HERE.md, and AGENTS.md.
Explain the Product Ops Sandbox in plain language.
Then run or draft the feedback classification workflow using
ai-workflows/prompts/classify_feedback.md and input-notes/support-ticket-batch.md.
Write the result to outputs/ai_feedback_classification.json and a readable summary to
outputs/ai_feedback_classification.md.
Use only evidence in the repo and do not invent facts.
```

If the assistant cannot access files, paste the prompt and safe note content manually. That is the
fallback path, not the main path.

## Adaptation Flow

The safest adoption pattern is one change at a time.

```mermaid
flowchart LR
    A["Copy or fork safely"] --> B["Update product context"]
    B --> C["Update success metrics"]
    C --> D["Replace one approved input"]
    D --> E["Run or ask one workflow"]
    E --> F["Review outputs"]
    F --> G{"Output trustworthy enough?"}
    G -->|No| H["Fix context, input, prompt, or schema"]
    H --> E
    G -->|Yes| I["Choose the next small change"]
    I --> D
```

Use this rule:

```text
Change one input. Run or ask. Review the output. Then change the next thing.
```

## Review Gates

Before a new user or team treats the sandbox as useful, confirm:

| Gate | Check |
| --- | --- |
| Safety | Public work uses fictional, synthetic, anonymized, or approved data only |
| Orientation | The user can identify `input-notes/`, `sample-data/`, `ai-workflows/`, and `outputs/` |
| Lane choice | The user knows whether they are reading, using an assistant, running mock demos, or using an API |
| First output | The user has opened or produced at least one readable Markdown output |
| Human review | The user understands that AI output is a draft, not a product decision |
| Next action | The user can name the next file they would change or inspect |

## What Not To Do First

- Do not start by connecting real customer systems to the public repo.
- Do not put API keys, private notes, or confidential data in committed files.
- Do not edit every CSV, prompt, and schema at once.
- Do not treat the mock demo scripts as live AI.
- Do not treat AI-generated JSON as an approved roadmap decision.

## Documentation Design Notes

This guide uses a few documentation choices intentionally:

| Choice | Reason |
| --- | --- |
| Mermaid diagrams | GitHub renders Mermaid in Markdown, and Mermaid supports flowcharts and user journey diagrams |
| Persona paths | Users arrive with different goals, so the first step should route them before giving commands |
| First value focus | New users should see a meaningful result before learning every folder |
| Diataxis-style separation | `START_HERE.md` is the guided tutorial, `docs/03-how-to-run-the-workflows.md` and `docs/06-adapt-this-sandbox.md` are how-to guides, and `docs/01-product-context.md`, `docs/02-success-metrics.md`, `docs/04-api-extension.md`, and `AGENTS.md` act more like explanation or reference |

References:

- GitHub Mermaid rendering: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams
- Mermaid flowcharts: https://mermaid.ai/open-source/syntax/flowchart.html
- Mermaid user journey diagrams: https://mermaid.ai/open-source/syntax/userJourney.html
- Diataxis documentation framework: https://diataxis.fr/

