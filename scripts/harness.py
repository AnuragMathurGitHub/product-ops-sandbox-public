"""A small deterministic harness for AI workflows.

The model is probabilistic. This wraps a single AI call so the workflow is
deterministic at the boundary: call the model, then validate its output against a
schema, retry a fixed number of times on failure, and return validated data or
raise. The model call is injected, so the harness is fully testable with a fake
model and no API key.

The idea: code calculates, AI drafts, a gate checks, humans decide. Determinism
lives here in the harness, not in the model.

This module has no third-party dependencies. The schema check is a small subset of
JSON Schema (object, array, string, number, integer, boolean, required,
additionalProperties, enum), the same subset the repo's schemas use.
"""

import json


class HarnessError(Exception):
    """Raised when the model never produced output that satisfies the contract."""


def extract_json(text):
    """Pull the first JSON object out of model text, tolerating code fences."""
    cleaned = text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1] if "\n" in cleaned else cleaned
        if cleaned.endswith("```"):
            cleaned = cleaned[: cleaned.rfind("```")]
    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start == -1 or end == -1:
        raise ValueError("no JSON object found in the model output")
    return json.loads(cleaned[start : end + 1])


def validate(schema, value, path="$"):
    """Return a list of contract violations. An empty list means the value is valid."""
    errors = []
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path} is not one of {schema['enum']}")

    schema_type = schema.get("type")
    if schema_type == "object":
        if not isinstance(value, dict):
            return errors + [f"{path} should be an object"]
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{path} is missing required key '{key}'")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in sorted(set(value) - set(properties)):
                errors.append(f"{path} has unexpected key '{key}'")
        for key, child in properties.items():
            if key in value:
                errors += validate(child, value[key], f"{path}.{key}")
    elif schema_type == "array":
        if not isinstance(value, list):
            return errors + [f"{path} should be an array"]
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors += validate(item_schema, item, f"{path}[{index}]")
    elif schema_type == "string":
        if not isinstance(value, str):
            errors.append(f"{path} should be a string")
    elif schema_type == "integer":
        if not isinstance(value, int) or isinstance(value, bool):
            errors.append(f"{path} should be an integer")
    elif schema_type == "number":
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            errors.append(f"{path} should be a number")
    elif schema_type == "boolean":
        if not isinstance(value, bool):
            errors.append(f"{path} should be a boolean")
    return errors


def run_step(call_model, prompt, schema, max_retries=3):
    """Call the model, gate its output on the schema, and retry deterministically.

    call_model: a function that takes the prompt string and returns model text. It
    is the only probabilistic part, injected so this harness is testable with a
    fake model. Returns the validated data (a dict) or raises HarnessError after
    max_retries attempts.
    """
    last = "no attempts were made"
    for attempt in range(1, max_retries + 1):
        raw = call_model(prompt)
        try:
            data = extract_json(raw)
        except ValueError as error:
            last = f"attempt {attempt}: could not parse JSON ({error})"
            continue
        violations = validate(schema, data)
        if not violations:
            return data
        last = f"attempt {attempt}: {len(violations)} contract violation(s): {violations[:3]}"
    raise HarnessError(f"output never satisfied the contract. Last: {last}")
