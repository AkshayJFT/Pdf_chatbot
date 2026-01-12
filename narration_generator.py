import openai
import os
from narration_prompts import (
    SLIDE_NARRATION_SYSTEM_PROMPT,
    SLIDE_NARRATION_USER_PROMPT,
    PRODUCT_NARRATION_USER_PROMPT
)

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_slide_narration(slide, duration_sec=45, model="gpt-3.5-turbo"):
    prompt = SLIDE_NARRATION_USER_PROMPT.format(
        title=slide["title"],
        focus_area=slide["focus_area"],
        pages=slide["pages"],
        content_summary=slide["content_summary"],
        duration_sec=duration_sec
    )

    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.4,
        messages=[
            {"role": "system", "content": SLIDE_NARRATION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()


def generate_product_narration(product, duration_sec=45, model="gpt-3.5-turbo"):
    features_text = "\n".join(product["features"])

    prompt = PRODUCT_NARRATION_USER_PROMPT.format(
        product_name=product["product_name"],
        pages=product["pages"],
        features=features_text,
        duration_sec=duration_sec
    )

    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.4,
        messages=[
            {"role": "system", "content": SLIDE_NARRATION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response["choices"][0]["message"]["content"].strip()
