import csv
from collections import defaultdict
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "okrs.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "okr_snapshot.md"


def read_okrs() -> list[dict[str, Any]]:
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_summary(records: list[dict[str, Any]]) -> str:
    by_objective: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)

    for record in records:
        by_objective[record["objective"]].append(record)

    lines = [
        "# OKR Snapshot",
        "",
        "This snapshot summarizes fictional product OKRs from the sample dataset.",
        "It shows which outcomes the planning work should support.",
        "",
    ]

    for objective, key_results in by_objective.items():
        lines.extend(
            [
                f"## {objective}",
                "",
                "| Key Result | Linked Metric | Baseline | Current | Target | Status |",
                "| --- | --- | ---: | ---: | ---: | --- |",
            ]
        )

        for item in key_results:
            lines.append(
                "| {key_result} | {linked_metric} | {baseline} | {current} | {target} | {status} |".format(
                    key_result=item["key_result"],
                    linked_metric=item["linked_metric"],
                    baseline=item["baseline"],
                    current=item["current"],
                    target=item["target"],
                    status=item["status"],
                )
            )

        lines.append("")

    lines.extend(
        [
            "## Product Ops Readout",
            "",
            "- OKRs should name outcomes, not feature commitments.",
            "- Roadmap candidates should explain which key result they support.",
            "- Metrics should be reviewed before and after launch so the team can learn.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    records = read_okrs()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(records), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
