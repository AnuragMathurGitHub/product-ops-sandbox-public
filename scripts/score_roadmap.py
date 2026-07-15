import csv
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "roadmap_items.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "roadmap_priority_scores.md"


def to_float(value: str) -> float:
    return float(value)


def priority_score(item: dict[str, Any]) -> float:
    reach = to_float(item["reach"])
    impact = to_float(item["impact"])
    confidence = to_float(item["confidence"])
    effort = to_float(item["effort"])
    strategic_fit = to_float(item["strategic_fit"])
    return (reach * impact * confidence * strategic_fit) / effort


def read_items() -> list[dict[str, Any]]:
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        items: list[dict[str, Any]] = list(csv.DictReader(file))

    for item in items:
        item["score"] = priority_score(item)

    return sorted(items, key=lambda item: item["score"], reverse=True)


def build_summary(items: list[dict[str, Any]]) -> str:
    lines = [
        "# Roadmap Priority Scores",
        "",
        "These scores rank roadmap candidates with a transparent, RICE inspired formula.",
        "",
        "```text",
        "score = (reach * impact * confidence * strategic_fit) / effort",
        "```",
        "",
        "## What Each Factor Means",
        "",
        "| Factor | Meaning | Scale in the sample data |",
        "| --- | --- | --- |",
        "| reach | How many users or accounts the change affects in a period | 1 to 10 |",
        "| impact | How much it moves the linked metric when it lands | 1 to 10 |",
        "| confidence | How sure we are about the reach and impact estimates | 0 to 1 |",
        "| strategic_fit | How well it supports strategy, employer value, and renewal | 1 to 10 |",
        "| effort | Rough delivery cost; larger effort lowers the score | 1 to 10 |",
        "",
        "Standard RICE is `(reach * impact * confidence) / effort`. This repo adds `strategic_fit`",
        "so business importance stays visible in the math instead of hidden in a side conversation.",
        "Learn more about RICE: https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/",
        "",
        "## The Score Is A Decision Input, Not The Decision",
        "",
        "The ranking starts the conversation; product judgment finishes it. If a lower ranked item",
        "matters more to the business, that usually means an input assumption needs a second look.",
        "For example, `Launch activation reminder kit` ranks third here, but activation is central to",
        "employer value and renewal, so a team might raise its `strategic_fit` or revisit the impact",
        "estimate and re-run. The goal is to make assumptions explicit, not to trust the number blindly.",
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
            "- High scoring items combine reach, expected impact, confidence, and reasonable effort.",
            "- Lower scoring items may still matter when they reduce trust, renewal, or operational risk.",
            "- The useful conversation is often about the assumptions behind the score.",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    items = read_items()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(items), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
