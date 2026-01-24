# from services.gemini_client import generate_response

# def extract_topics(text):
#     prompt = f"""
# Identify main research topics and scientific domains.

# Text:
# {text}

# Return list of topics.
# """
#     return generate_response(prompt)


from services.gemini_client import generate_response
from utils.logger import logger

def extract_topics(text):
    prompt = f"""
Identify main research topics and scientific domains.

Text:
{text}

Return list of topics.
"""
    logger.info("Extracting topics via Gemini API...")
    return generate_response(prompt)