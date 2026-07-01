from ai_common import copy_mock_output, note_mock_mode


def main():
    copy_mock_output(
        "release_measurement_plan_example.json",
        "ai_release_measurement_plan.json",
    )
    copy_mock_output(
        "release_measurement_plan_example.md",
        "ai_release_measurement_plan.md",
    )
    note_mock_mode("ai-workflows/prompts/plan_release_measurement.md")


if __name__ == "__main__":
    main()
