from ai_common import copy_mock_output, note_mock_mode


def main():
    copy_mock_output(
        "opportunity_map_example.json",
        "ai_opportunity_map.json",
    )
    copy_mock_output(
        "opportunity_map_example.md",
        "ai_opportunity_map.md",
    )
    note_mock_mode("ai-workflows/prompts/detect_opportunities.md")


if __name__ == "__main__":
    main()
