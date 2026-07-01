from ai_common import copy_mock_output, note_mock_mode


def main():
    copy_mock_output(
        "okr_alignment_example.json",
        "ai_okr_alignment.json",
    )
    copy_mock_output(
        "okr_alignment_example.md",
        "ai_okr_alignment.md",
    )
    note_mock_mode("ai-workflows/prompts/align_okrs.md")


if __name__ == "__main__":
    main()
