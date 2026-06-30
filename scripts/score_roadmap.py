from pathlib import Path
import csv


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "roadmap_items.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "roadmap_priority_scores.md"


def to_float(value):
    return float(value)


def priority_score(item):
    reach = to_float(item["reach"])
    impact = to_float(item["impact"])
    confidence = to_float(item["confidence"])
    effort = to_float(item["effort"])
    strategic_fit = to_float(item["strategic_fit"])
    return (reach * impact * confidence * strategic_fit) / effort


def read_items():
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        items = list(csv.DictReader(file))

    for item in items:
        item["score"] = priority_score(item)

    return sorted(items, key=lambda item: item["score"], reverse=True)


def build_summary(items):
    lines = [
        "# Roadmap Priority Scores",
        "",
        "Formula:",
        "",
        "```text",
        "score = (reach * impact * confidence * strategic_fit) / effort",
        "```",
        "",
        "This score supports judgment but does not replace judgment.",
        "Teams should still consider risk, customer commitments, strategy, and sequencing.",
        "",
        "| Rank | Item | Product Area | Status | Linked Metric | Score |",
        "| ---: | --- | --- | --- | --- | ---: |",
    ]

    for rank, item in enumerate(items, start=1):
        lines.append(
            "| {rank} | {title} | {area} | {status} | {metric} | {score:.1f} |".format(
                rank=rank,
                title=item["title"],
                area=item["product_area"],
                status=item["status"],
                metric=item["linked_metric"],
                score=item["score"],
            )
        )

    lines.extend(
        [
            "",
            "## Product Ops Readout",
            "",
            "- High-scoring items combine reach, expected impact, confidence, and reasonable effort.",
            "- Lower-scoring items may still matter when they reduce trust, renewal, or operational risk.",
            "- The useful conversation is often about the assumptions behind the score.",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    items = read_items()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(items), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
