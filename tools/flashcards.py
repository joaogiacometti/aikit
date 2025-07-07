from llm_client import send_prompt_to_model


system_prompt = """
Generate a simple flashcard with a front and a back for the following topic.

Respond using this format:
Front: <question>
Back: <answer>

Topic: {user_prompt}
"""


def generate_flashcard(prompt: str) -> str:
    full_prompt = system_prompt.format(user_prompt=prompt)
    response = send_prompt_to_model(full_prompt)

    return getattr(response, "text", str(response))
