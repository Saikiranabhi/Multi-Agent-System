from services.gemini_client import generate_response
from utils.logger import logger

def map_contributions(text):
    prompt = f"""
Extract and list key scientific contributions and innovations.

Text:
{text}

Return structured contribution list.
"""
    logger.info("Mapping contributions via Gemini API...")
    return generate_response(prompt)
