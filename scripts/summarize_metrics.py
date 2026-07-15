import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_FILE = PROJECT_ROOT / "sample-data" / "product_events.csv"
OUTPUT_FILE = PROJECT_ROOT / "outputs" / "metrics_snapshot.md"


def read_events():
    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def count_events(events, event_name, success=None):
    matching = [event for event in events if event["event_name"] == event_name]
    if success is None:
        return len(matching)
    expected = "true" if success else "false"
    return sum(1 for event in matching if event["success"].lower() == expected)


def build_summary(events):
    total_users = len({event["user_id"] for event in events})
    activated_users = {
        event["user_id"]
        for event in events
        if event["event_name"] == "Membership Activated" and event["success"].lower() == "true"
    }
    activation_count = len(activated_users)
    activation_rate = activation_count / total_users if total_users else 0

    metrics = [
        ("Total users", total_users),
        ("Membership activation count", activation_count),
        ("Activation rate", f"{activation_rate:.1%}"),
        ("Check in completed count", count_events(events, "Check In Completed", True)),
        ("Check in failure count", count_events(events, "Check In Failed", False)),
        ("Support contacted count", count_events(events, "Support Contacted")),
        ("Booking completed count", count_events(events, "Class Booked", True)),
    ]

    lines = [
        "# Metrics Snapshot",
        "",
        "This snapshot summarizes fictional product event data from the sample dataset.",
        "",
        "| Metric | Value |",
        "| --- | ---: |",
    ]

    for metric, value in metrics:
        lines.append(f"| {metric} | {value} |")

    lines.extend(
        [
            "",
            "## Product Ops Readout",
            "",
            "- Activation is the first health check for the new member journey.",
            "- Completed and failed check ins show whether digital intent turns into real world usage.",
            "- Support contacts help identify friction that users cannot resolve on their own.",
            "- This is a small synthetic dataset, so the numbers are directional only.",
            "",
        ]
    )

    return "\n".join(lines)


def main():
    events = read_events()
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(build_summary(events), encoding="utf-8")
    print(f"Wrote {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
