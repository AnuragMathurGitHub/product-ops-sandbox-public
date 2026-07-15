from ai_common import copy_mock_output, note_mock_mode


def main() -> None:
    copy_mock_output(
        "weekly_product_insights_example.md",
        "ai_weekly_product_insights.md",
    )
    note_mock_mode("ai-workflows/prompts/weekly_product_insights.md")


if __name__ == "__main__":
    main()
