from pathlib import Path
import shutil


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SAMPLE_OUTPUTS = PROJECT_ROOT / "ai-workflows" / "sample-outputs"
OUTPUTS = PROJECT_ROOT / "outputs"


def copy_mock_output(example_name, output_name):
    source = SAMPLE_OUTPUTS / example_name
    destination = OUTPUTS / output_name

    if not source.exists():
        raise FileNotFoundError(f"Missing mock output source: {source}")

    OUTPUTS.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)
    print(f"Wrote {destination}")
