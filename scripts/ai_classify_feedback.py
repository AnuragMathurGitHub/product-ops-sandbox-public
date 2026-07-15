from ai_common import copy_mock_output, note_mock_mode


def main() -> None:
    copy_mock_output(
        "feedback_classification_example.json",
        "ai_feedback_classification.json",
    )
    copy_mock_output(
        "feedback_classification_example.md",
        "ai_feedback_classification.md",
    )
    note_mock_mode("ai-workflows/prompts/classify_feedback.md")


if __name__ == "__main__":
    main()
