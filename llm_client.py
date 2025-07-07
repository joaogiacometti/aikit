import os
from google import genai
from google.genai import types
import config


def send_prompt_to_model(prompt):
    api_key = os.getenv("AI_API_KEY")

    if not api_key:
        raise ValueError("AI_API_KEY environment variable is not set.")

    client = genai.Client(api_key=api_key)

    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]

    try:
        response = client.models.generate_content(
            model=config.model,
            contents=messages
        )
    except Exception as e:
        raise RuntimeError(f"Failed to generate content: {e}")

    return response
