import csv
from collections import Counter, defaultdict
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "customer_feedback.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "feedback_theme_summary.md"


def read_feedback():
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_summary(records):
    by_theme = defaultdict(list)
    severity_counts = Counter()

    for record in records:
        theme = record["theme"]
        severity = record["severity"]
        by_theme[theme].append(record)
        severity_counts[severity] += 1

    lines = [
        "# Feedback Theme Summary",
        "",
        "This summary groups fictional customer feedback by theme and severity.",
        "It helps product teams spot repeated friction without replacing judgment.",
        "",
        "## Severity Counts",
        "",
        "| Severity | Count |",
        "| --- | ---: |",
    ]

    for severity in ["Critical", "High", "Medium", "Low"]:
        lines.append(f"| {severity} | {severity_counts.get(severity, 0)} |")

    lines.extend(
        [
            "",
            "## Themes",
            "",
            "| Theme | Records | High | Medium | Low | Linked Metrics |",
            "| --- | ---: | ---: | ---: | ---: | --- |",
        ]
    )

    sorted_themes = sorted(
        by_theme.items(),
        key=lambda item: (
            len(item[1]),
            sum(1 for record in item[1] if record["severity"] == "High"),
        ),
        reverse=True,
    )

    for theme, theme_records in sorted_themes:
        counts = Counter(record["severity"] for record in theme_records)
        metrics = sorted({record["linked_metric"] for record in theme_records})
        lines.append(
            "| {theme} | {records} | {high} | {medium} | {low} | {metrics} |".format(
                theme=theme,
                records=len(theme_records),
                high=counts.get("High", 0),
                medium=counts.get("Medium", 0),
                low=counts.get("Low", 0),
                metrics=", ".join(metrics),
            )
        )

    lines.extend(
        [
            "",
            "## Product Ops Readout",
            "",
            "- Repeated high severity themes should be reviewed against roadmap priorities.",
            "- Linked metrics help the team test whether a fix improved the journey.",
            "- This summary is a starting point for discussion, not a decision by itself.",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    records = read_feedback()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(records), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
