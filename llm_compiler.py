import json
import os
from prompts import SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def compile_presentation_json(pages: list, model="gpt-3.5-turbo"):
    pages_json = json.dumps(pages, indent=2)

    user_prompt = USER_PROMPT_TEMPLATE.format(
        pages_json=pages_json
    )

    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ]
    )

    raw_output = response.choices[0].message.content

    # Safety: ensure valid JSON
    try:
        structured_output = json.loads(raw_output)
    except json.JSONDecodeError:
        raise ValueError("LLM did not return valid JSON")

    return structured_output
