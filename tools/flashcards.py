import os
from llm_client import send_prompt_to_model


system_prompt = """
Generate a simple flashcard for the following topic.

Respond using this format, with the front and back separated by a colon (:) and a space, suitable for direct import into Anki:

<question>: <answer>

Topic: {user_prompt}
"""


def generate_flashcard(prompt: str, save_output: bool = False) -> str:
    full_prompt = system_prompt.format(user_prompt=prompt)
    response = send_prompt_to_model(full_prompt)

    result = getattr(response, "text", str(response))

    if save_output:
        out_dir = os.path.join(os.path.dirname(
            os.path.dirname(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "flashcards.txt")
        with open(out_path, "a", encoding="utf-8") as f:
            f.write(result.strip() + "\n")

    return result
