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


# from services.gemini_client import generate_response
# from utils.logger import logger

# def analyze_document(context_chunks):
#     context = "\n".join(context_chunks)

#     prompt = f"""
# You are a senior academic research analyst.

# Analyze the document content deeply and extract:

# # - Research objective  
# # - Methodology  
# # - Core contributions  
# # - Experimental evidence  
# # - Novelty  
# # - Strengths  
# # - Weaknesses  
# # - Limitations  
# # - Practical impact  

# Generate a TWO-PAGE academic report on MARA.

# PAGE 1 must contain:
# - Research objective
# - System architecture overview
# - Methodology
# - Core contributions

# PAGE 2 must contain:
# - Novelty analysis
# - Strengths
# - Weaknesses
# - Limitations
# - Practical impact
# - Future improvements

# STRICT RULES:
# - Do NOT repeat content across pages
# - Do NOT restate objectives or methodology on Page 2
# - Each section must introduce NEW information
# - Write concisely in academic tone
# - Assume Page 2 has access to Page 1 content


# Context:
# {context}

# Return a structured analytical breakdown.
# """

#     logger.info("Calling Gemini API for document analysis...")
#     return generate_response(prompt)




from services.gemini_client import generate_response
from utils.logger import logger

def analyze_document(context_chunks):
    context = "\n".join(context_chunks)

    prompt = f"""
You are a senior academic research analyst tasked with creating a comprehensive, structured analysis.

Analyze the document content and provide a DETAILED breakdown in the following format:

RESEARCH OBJECTIVE:
- Clearly state the main goal/problem the paper addresses
- Be specific and concise (2-3 sentences)

METHODOLOGY:
- List key approaches, techniques, or frameworks used
- Include specific details like algorithms, datasets, experimental setup
- Use bullet points for clarity

CORE CONTRIBUTIONS:
- List 3-5 numbered key contributions
- Be specific about what's novel or improved
- Quantify when possible (e.g., "30% improvement")

EXPERIMENTAL EVIDENCE:
- Summarize key results and metrics
- Include specific numbers, datasets, comparisons
- Mention baselines if available

NOVELTY & INNOVATION:
- What makes this work unique or groundbreaking?
- How does it differ from prior work?
- Use ⭐ for highlighting key innovations

STRENGTHS:
- List major strengths (3-5 points)
- Use ✓ checkmarks
- Focus on methodology, results, and contribution quality

WEAKNESSES:
- List limitations or concerns (2-4 points)
- Use ✗ marks
- Be constructive and specific

LIMITATIONS:
- Technical or scope limitations
- Generalizability concerns
- Missing evaluations or comparisons

PRACTICAL IMPACT:
- Real-world applications
- Industry use cases
- Research community impact
- Use 🎯 for different categories

Context:
{context}

Provide a thorough, well-structured analysis with clear section headers and formatting as shown above.
"""

    logger.info("Calling Gemini API for document analysis...")
    return generate_response(prompt)