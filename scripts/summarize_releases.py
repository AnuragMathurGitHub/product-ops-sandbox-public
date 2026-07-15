import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "releases.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "release_readiness_snapshot.md"


def read_releases():
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_summary(records):
    lines = [
        "# Release Readiness Snapshot",
        "",
        "This snapshot summarizes fictional release candidates from the sample dataset.",
        "It helps teams connect launch communication and measurement before work ships.",
        "",
        "| Release | Initiative | Stage | Linked Metric | Owner | Measurement Window |",
        "| --- | --- | --- | --- | --- | --- |",
    ]

    for item in records:
        lines.append(
            "| {release_id} | {initiative} | {launch_stage} | {linked_metric} | {communication_owner} | {measurement_window} |".format(
                release_id=item["release_id"],
                initiative=item["initiative"],
                launch_stage=item["launch_stage"],
                linked_metric=item["linked_metric"],
                communication_owner=item["communication_owner"],
                measurement_window=item["measurement_window"],
            )
        )

    lines.extend(
        [
            "",
            "## Product Ops Readout",
            "",
            "- A release is not ready only because the work is built.",
            "- Teams should know who needs the message, what behavior should change, and which metric should move.",
            "- The measurement window should be chosen before launch, not after.",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    records = read_releases()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(records), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
