import shutil
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_OUTPUTS = PROJECT_ROOT / "ai-workflows" / "sample-outputs"
OUTPUTS = PROJECT_ROOT / "outputs"


def copy_mock_output(example_name: str, output_name: str, announce: bool = True) -> None:
    source = SAMPLE_OUTPUTS / example_name
    destination = OUTPUTS / output_name

    if not source.exists():
        raise FileNotFoundError(f"Missing mock output source: {source}")

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    if announce:
        print(f"Wrote {destination}")


def note_mock_mode(prompt_relpath: str) -> None:
    """Explain that this run was a deterministic demo, and point to the real agent path."""
    print(
        "Mock mode: copied a prepared example. No AI model was called.\n"
        "To run this for real (real AI, no API key), open this repo in your AI assistant\n"
        f"and ask it to follow {prompt_relpath} with the repo inputs named in the prompt."
    )
