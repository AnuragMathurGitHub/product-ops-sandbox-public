from ai_common import copy_mock_output, note_mock_mode


def main():
    copy_mock_output(
        "research_synthesis_example.json",
        "ai_research_synthesis.json",
    )
    copy_mock_output(
        "research_synthesis_example.md",
        "ai_research_synthesis.md",
    )
    note_mock_mode("ai-workflows/prompts/synthesize_research.md")


if __name__ == "__main__":
    main()
