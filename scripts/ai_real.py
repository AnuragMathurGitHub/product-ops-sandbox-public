"""Optional real-AI pipeline for the Product Ops Sandbox (the API lane).

This script calls a real model with YOUR OWN API key and regenerates the drafts
in outputs/. It is the opt-in "API extension" lane. You do NOT need it: the agent
lane (your own assistant reads the prompts and notes) and the mock demo
(scripts/ai_*.py) both work with no key. Use this only when you want a
one-command, hands-off run in your own environment.

Providers (set PRODUCT_OPS_PROVIDER):
    anthropic   Anthropic Claude        key ANTHROPIC_API_KEY    (default)
    openai      OpenAI                   key OPENAI_API_KEY
    openrouter  OpenRouter (many models) key OPENROUTER_API_KEY

OpenAI and OpenRouter both use the 'openai' package (OpenRouter is OpenAI-API
compatible; the script just points it at a different base URL). Anthropic uses
the 'anthropic' package. The script imports only the one you actually use.

Quick start:

    pip install -r requirements-ai.txt         # or just the SDK for your provider
    export ANTHROPIC_API_KEY=your-anthropic-key
    python scripts/ai_real.py                   # run every workflow
    python scripts/ai_real.py classify_feedback # run one workflow

Model:
    Set PRODUCT_OPS_MODEL to the current model ID from your provider. Model names
    change, so the repo does not hard code a default model. For example:

    PRODUCT_OPS_PROVIDER=openai PRODUCT_OPS_MODEL=<model-id> python scripts/ai_real.py
    PRODUCT_OPS_PROVIDER=openrouter PRODUCT_OPS_MODEL=<model-id> python scripts/ai_real.py

Notes:
    - The review and weekly workflows read files that the deterministic scripts
      and earlier steps produce, so run the deterministic scripts first if your
      outputs/ folder is empty (see START_HERE.md, Step 6).
    - Every model reply passes through the schema gate in scripts/harness.py:
      the reply must parse as JSON and satisfy the workflow's schema, with up to
      three attempts, or the workflow fails with a clear error instead of
      writing a bad draft.
    - Outputs are drafts for a human to review, exactly like the other lanes.
"""

import json
import os
import sys
from pathlib import Path

from harness import HarnessError, run_step

PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = PROJECT_ROOT / "outputs"

MAX_TOKENS = 16000
MAX_ATTEMPTS = 3

# Provider settings. default_model is None where the provider's model names change
# often and we would rather require an explicit PRODUCT_OPS_MODEL than ship a
# guess. base_url is only needed for OpenAI-compatible gateways like OpenRouter.
PROVIDERS = {
    "anthropic": {
        "key_var": "ANTHROPIC_API_KEY",
        "package": "anthropic",
        "default_model": None,
        "base_url": None,
    },
    "openai": {
        "key_var": "OPENAI_API_KEY",
        "package": "openai",
        "default_model": None,
        "base_url": None,
    },
    "openrouter": {
        "key_var": "OPENROUTER_API_KEY",
        "package": "openai",
        "default_model": None,
        "base_url": "https://openrouter.ai/api/v1",
    },
}

# Each workflow declares its prompt, the inputs to send, an optional schema, and
# where the result is written. json_out is None for Markdown-only workflows.
# The order matters: review and weekly read files earlier steps produce.
WORKFLOWS = {
    "classify_feedback": {
        "prompt": "classify_feedback.md",
        "inputs": ["input-notes/support-ticket-batch.md"],
        "schema": "feedback_classification.schema.json",
        "json_out": "ai_feedback_classification.json",
        "md_out": "ai_feedback_classification.md",
    },
    "synthesize_research": {
        "prompt": "synthesize_research.md",
        "inputs": ["input-notes/user-interview-transcript.md"],
        "schema": "research_synthesis.schema.json",
        "json_out": "ai_research_synthesis.json",
        "md_out": "ai_research_synthesis.md",
    },
    "detect_opportunities": {
        "prompt": "detect_opportunities.md",
        "inputs": [
            "input-notes/support-ticket-batch.md",
            "input-notes/user-interview-transcript.md",
            "input-notes/weekly-product-ops-packet.md",
        ],
        "schema": "opportunity_map.schema.json",
        "json_out": "ai_opportunity_map.json",
        "md_out": "ai_opportunity_map.md",
    },
    "align_okrs": {
        "prompt": "align_okrs.md",
        "inputs": ["sample-data/okrs.csv", "sample-data/roadmap_items.csv"],
        "schema": "okr_alignment.schema.json",
        "json_out": "ai_okr_alignment.json",
        "md_out": "ai_okr_alignment.md",
    },
    "plan_release_measurement": {
        "prompt": "plan_release_measurement.md",
        "inputs": ["sample-data/releases.csv", "sample-data/product_events.csv"],
        "schema": "release_measurement_plan.schema.json",
        "json_out": "ai_release_measurement_plan.json",
        "md_out": "ai_release_measurement_plan.md",
    },
    "review_product_planning": {
        "prompt": "review_product_planning.md",
        "inputs": [
            "outputs/ai_opportunity_map.json",
            "outputs/roadmap_priority_scores.md",
            "outputs/metrics_snapshot.md",
        ],
        "schema": None,
        "json_out": None,
        "md_out": "ai_product_planning_review.md",
    },
    "weekly_product_insights": {
        "prompt": "weekly_product_insights.md",
        "inputs": [
            "outputs/metrics_snapshot.md",
            "outputs/feedback_theme_summary.md",
        ],
        "schema": None,
        "json_out": None,
        "md_out": "ai_weekly_product_insights.md",
    },
}

SYSTEM_JSON = (
    "You are a Product Operations assistant working on a fictional product "
    "called FitPass Demo. Follow the workflow instructions exactly. Use only "
    "the provided inputs; do not invent customers, numbers, metrics, or product "
    "facts. Respond with a single JSON object and nothing else: no code fences, "
    "no commentary. The object must have exactly two keys: 'output' (the "
    "structured result the instructions describe, matching the referenced "
    "schema) and 'markdown' (a short, plain-English summary of that result, "
    "starting with a Markdown H1 title)."
)

SYSTEM_MARKDOWN = (
    "You are a Product Operations assistant working on a fictional product "
    "called FitPass Demo. Follow the workflow instructions exactly. Use only "
    "the provided inputs; do not invent customers, numbers, metrics, or product "
    "facts. Respond with a single JSON object and nothing else: no code fences, "
    "no commentary. The object must have exactly one key: 'markdown' (the full "
    "result as Markdown, starting with a Markdown H1 title)."
)


def read_text(relpath):
    """Read a repo file. Return a visible placeholder if it is missing."""
    path = PROJECT_ROOT / relpath
    if not path.exists():
        return f"(missing file: {relpath})"
    return path.read_text(encoding="utf-8")


def build_user_content(cfg):
    """Assemble the prompt, inputs, and optional schema into one user message."""
    parts = ["# Workflow instructions\n", read_text(f"ai-workflows/prompts/{cfg['prompt']}")]
    if cfg["schema"]:
        parts.append("\n\n# Target JSON schema\n")
        parts.append(read_text(f"ai-workflows/schemas/{cfg['schema']}"))
    parts.append("\n\n# Inputs")
    for relpath in cfg["inputs"]:
        parts.append(f"\n\n## {relpath}\n")
        parts.append(read_text(relpath))
    return "".join(parts)


def envelope_schema(cfg):
    """The contract for one model reply, enforced by the harness gate.

    JSON workflows must reply with {"output": <matches the workflow schema>,
    "markdown": <string>}. Markdown-only workflows must reply with
    {"markdown": <string>}. This is the same contract SYSTEM_JSON and
    SYSTEM_MARKDOWN describe to the model.
    """
    properties = {"markdown": {"type": "string"}}
    required = ["markdown"]
    if cfg["schema"]:
        workflow_schema = json.loads(read_text(f"ai-workflows/schemas/{cfg['schema']}"))
        properties["output"] = workflow_schema
        required = ["output", "markdown"]
    return {
        "type": "object",
        "additionalProperties": False,
        "required": required,
        "properties": properties,
    }


def call_model(client, provider, model, system, user):
    """Send one request through the selected provider and return the text."""
    if provider == "anthropic":
        response = client.messages.create(
            model=model,
            max_tokens=MAX_TOKENS,
            system=system,
            messages=[{"role": "user", "content": user}],
        )
        return "".join(block.text for block in response.content if block.type == "text")

    # OpenAI-compatible path (openai, openrouter). No token cap is set here so the
    # same call works across models that use max_tokens vs max_completion_tokens.
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
    )
    return response.choices[0].message.content or ""


def run_workflow(client, provider, model, name, cfg):
    """Run one workflow through the schema gate and write its outputs.

    Return True on success. The harness calls the model, checks the reply
    against the envelope contract, and retries up to MAX_ATTEMPTS times before
    failing, so a reply that never satisfies the schema writes nothing.
    """
    is_json = cfg["json_out"] is not None
    system = SYSTEM_JSON if is_json else SYSTEM_MARKDOWN
    user = build_user_content(cfg)
    contract = envelope_schema(cfg)
    print(f"Running {name} on {provider}:{model} ...")

    def call(prompt):
        return call_model(client, provider, model, system, prompt)

    try:
        obj = run_step(call, user, contract, max_retries=MAX_ATTEMPTS)
    except HarnessError as error:
        print(f"  Gate failed: {error}")
        return False
    gate_name = cfg["schema"] if cfg["schema"] else "markdown envelope"
    print(f"  Draft passed the schema gate ({gate_name}).")

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    if is_json:
        json_path = OUTPUTS / cfg["json_out"]
        json_path.write_text(json.dumps(obj["output"], indent=2) + "\n", encoding="utf-8")
        print(f"  Wrote {json_path}")

    md_path = OUTPUTS / cfg["md_out"]
    md_path.write_text(obj["markdown"].rstrip() + "\n", encoding="utf-8")
    print(f"  Wrote {md_path}")
    return True


def make_client(provider, cfg):
    """Import the provider SDK lazily and build a client."""
    if provider == "anthropic":
        import anthropic

        return anthropic.Anthropic()

    import openai

    kwargs = {"api_key": os.environ[cfg["key_var"]]}
    if cfg["base_url"]:
        kwargs["base_url"] = cfg["base_url"]
    return openai.OpenAI(**kwargs)


def main(argv):
    provider = os.environ.get("PRODUCT_OPS_PROVIDER", "anthropic").lower()
    if provider not in PROVIDERS:
        print(f"Unknown PRODUCT_OPS_PROVIDER '{provider}'. Use one of: {', '.join(PROVIDERS)}.")
        return 1
    cfg = PROVIDERS[provider]

    if not os.environ.get(cfg["key_var"]):
        print(
            f"No {cfg['key_var']} found in the environment.\n"
            f"This is the optional API lane (provider: {provider}). Set your own key first:\n"
            f"    export {cfg['key_var']}=your-key-here   (macOS/Linux)\n"
            f"    setx {cfg['key_var']} your-key-here      (Windows, then reopen the shell)\n"
            "Never commit your key. See docs/04-api-extension.md.\n"
            "You can also use the agent lane (your own assistant) or the mock\n"
            "demo (python scripts/ai_classify_feedback.py) with no key at all."
        )
        return 1

    try:
        client = make_client(provider, cfg)
    except ImportError:
        print(
            f"The '{cfg['package']}' package is not installed (needed for provider '{provider}').\n"
            "Install the API-lane dependencies:\n"
            "    pip install -r requirements-ai.txt"
        )
        return 1

    model = os.environ.get("PRODUCT_OPS_MODEL") or cfg["default_model"]
    if not model:
        print(
            f"Provider '{provider}' has no built-in default model.\n"
            "Set the model explicitly, for example:\n"
            f"    PRODUCT_OPS_MODEL=<model-id> python scripts/ai_real.py"
        )
        return 1

    requested = argv or list(WORKFLOWS)
    unknown = [name for name in requested if name not in WORKFLOWS]
    if unknown:
        print(f"Unknown workflow(s): {', '.join(unknown)}")
        print(f"Available: {', '.join(WORKFLOWS)}")
        return 1

    failures = 0
    for name in requested:
        try:
            if not run_workflow(client, provider, model, name, WORKFLOWS[name]):
                failures += 1
        except Exception as error:  # keep going so one failure does not stop the run
            print(f"  {name} failed: {error}")
            failures += 1

    print(
        f"\nDone. {len(requested) - failures} of {len(requested)} workflow(s) "
        "succeeded. Review the drafts in outputs/ before using them."
    )
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
