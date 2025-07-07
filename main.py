from dotenv import load_dotenv
import argparse

from enums import ToolType
from tools.flashcards import generate_flashcard


def parse_args():
    parser = argparse.ArgumentParser(
        description="AI kit command line interface")
    parser.add_argument(
        "--tool",
        "-t",
        type=str,
        help="The tool to use for the AI model",
        choices=["flashcards"],
        required=True
    )
    parser.add_argument(
        "--prompt",
        "-p",
        type=str,
        help="The prompt to use for the AI model",
        required=True
    )
    parser.add_argument(
        "--save-output",
        "-s",
        action="store_true",
        help="Save the output to a file in the /out directory (optional)",
    )

    return parser.parse_args()


def main():
    load_dotenv()
    args = parse_args()

    if args.tool == ToolType.FLASHCARDS:
        result = generate_flashcard(args.prompt, args.save_output)
        print(result)


if __name__ == "__main__":
    main()
