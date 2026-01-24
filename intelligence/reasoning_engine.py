# from intelligence.gemini_client import generate_response

# def analyze_document(context_chunks):
#     context = "\n".join(context_chunks)

#     prompt = f"""
# You are a senior academic research analyst.

# Analyze the document content deeply and extract:

# • Research objective  
# • Methodology  
# • Core contributions  
# • Experimental evidence  
# • Novelty  
# • Strengths  
# • Weaknesses  
# • Limitations  
# • Practical impact  

# Context:
# {context}

# Return a structured analytical breakdown.
# """

#     return generate_response(prompt)


from services.gemini_client import generate_response
from utils.logger import logger

def analyze_document(context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
You are a senior academic research analyst.

Analyze the document content deeply and extract:

- Research objective  
- Methodology  
- Core contributions  
- Experimental evidence  
- Novelty  
- Strengths  
- Weaknesses  
- Limitations  
- Practical impact  

Context:
{context}

Return a structured analytical breakdown.
"""

    logger.info("Calling Gemini API for document analysis...")
    return generate_response(prompt)