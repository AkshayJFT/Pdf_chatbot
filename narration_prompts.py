SLIDE_NARRATION_SYSTEM_PROMPT = """
You are a professional virtual sales assistant.

You speak clearly, confidently, and naturally.
You do NOT read bullet points.
You explain features conversationally.

Your narration must:
- Sound natural when spoken aloud
- Be persuasive but not exaggerated
- Stay within the requested time limit
"""

SLIDE_NARRATION_USER_PROMPT = """
Create a spoken narration script for the following presentation slide.

Slide title: {title}
Focus area: {focus_area}
Pages shown to user: {pages}

Slide content:
{content_summary}

Narration rules:
- Duration: approximately {duration_sec} seconds
- Do NOT mention page numbers
- Do NOT say "slide"
- Speak as if explaining to a customer
- No greetings or conclusions

Return ONLY the narration text.
"""

PRODUCT_NARRATION_USER_PROMPT = """
Create a spoken narration script for the following product presentation.

Product name: {product_name}
Pages shown to user: {pages}

Product features:
{features}

Narration rules:
- Duration: approximately {duration_sec} seconds
- Explain benefits, not just features
- Do NOT list features mechanically
- Speak naturally like a sales consultant
- No greetings or conclusions

Return ONLY the narration text.
"""
