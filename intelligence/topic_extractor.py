from services.gemini_client import generate_response

def extract_topics(text):
    prompt = f"""
Identify main research topics and scientific domains.

Text:
{text}

Return list of topics.
"""
    return generate_response(prompt)
