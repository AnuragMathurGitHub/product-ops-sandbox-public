from ai_common import copy_mock_output, note_mock_mode


def main():
    copy_mock_output(
        "product_planning_review_example.md",
        "ai_product_planning_review.md",
    )
    note_mock_mode("ai-workflows/prompts/review_product_planning.md")


if __name__ == "__main__":
    main()
