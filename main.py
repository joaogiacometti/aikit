import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse
import config


def parse_args():
    parser = argparse.ArgumentParser(
        description="AI kit command line interface")
    parser.add_argument(
        "--prompt",
        "-p",
        metavar="PROMPT",
        type=str,
        help="The prompt to use for the AI model",
        required=True
    )
    return parser.parse_args()


def send_prompt_to_model(prompt):
    api_key = os.getenv("AI_API_KEY")
    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    response = client.models.generate_content(
        model=config.model,
        contents=messages
    )

    print("Response from model:", response.text)


def main():
    load_dotenv()
    args = parse_args()
    send_prompt_to_model(args.prompt)


if __name__ == "__main__":
    main()
