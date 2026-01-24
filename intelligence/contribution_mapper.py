from services.gemini_client import generate_response

def map_contributions(text):
    prompt = f"""
Extract and list key scientific contributions and innovations.

Text:
{text}

Return structured contribution list.
"""
    return generate_response(prompt)
