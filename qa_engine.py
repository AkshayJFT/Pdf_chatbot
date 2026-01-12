from openai import OpenAI
import os
from qa_prompts import QA_SYSTEM_PROMPT, QA_USER_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def answer_question(
    question: str,
    current_slide: dict,
    brand_slides: list,
    products: list,
    model="gpt-4o-mini"
):
    brand_context = "\n".join(
        f"- {s['title']}: {s['content_summary']}"
        for s in brand_slides
    )

    product_context = "\n".join(
        f"- {p['product_name']}: {', '.join(p['features'])}"
        for p in products
    )

    prompt = QA_USER_PROMPT.format(
        question=question,
        current_slide=f"{current_slide['title']}: {current_slide['content_summary']}",
        brand_context=brand_context,
        product_context=product_context
    )

    response = client.chat.completions.create(
        model=model,
        temperature=0.2,
        messages=[
            {"role": "system", "content": QA_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()
