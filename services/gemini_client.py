# # import os
# # import google.generativeai as genai
# # from dotenv import load_dotenv
# # from utils.logger import logger

# # load_dotenv()

# # genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # model = genai.GenerativeModel("gemini-1.5-flash")

# # def generate_response(prompt: str) -> str:
# #     try:
# #         logger.info("Sending request to Gemini API...")
# #         response = model.generate_content(prompt)
# #         logger.info("Received response from Gemini API")
# #         return response.text
# #     except Exception as e:
# #         logger.error(f"Gemini API Error: {str(e)}")
# #         raise


# import os
# import google.generativeai as genai
# from dotenv import load_dotenv
# from utils.logger import logger

# load_dotenv()

# # Configure API key
# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("GEMINI_API_KEY not found in environment variables")

# genai.configure(api_key=api_key)

# # Use the correct model name
# model = genai.GenerativeModel("models/gemini-2.5-pro")

# def generate_response(prompt: str) -> str:
#     try:
#         logger.info("Sending request to Gemini API...")
#         response = model.generate_content(prompt)
#         logger.info("Received response from Gemini API")
#         return response.text
#     except Exception as e:
#         logger.error(f"Gemini API Error: {str(e)}")
#         raise

# # Optional: Function to list available models
# def list_available_models():
#     """Helper function to see all available models"""
#     for m in genai.list_models():
#         if 'generateContent' in m.supported_generation_methods:
#             print(f"Model: {m.name}")


import os
import google.generativeai as genai
from dotenv import load_dotenv
from utils.logger import logger
import time

load_dotenv()

# Configure API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# USE FLASH MODEL - Better free tier limits
# Flash has higher free limits than Pro
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Free tier limits for different models:
# gemini-2.5-flash: 15 RPM (requests per minute), 1M TPM (tokens per minute), 1500 RPD (requests per day)
# gemini-2.5-pro: 2 RPM, 32K TPM, 50 RPD (MUCH LOWER - that's why you hit the limit)

def generate_response(prompt: str, max_retries: int = 3) -> str:
    """
    Generate response from Gemini API with retry logic
    
    Args:
        prompt: The prompt to send to Gemini
        max_retries: Maximum number of retry attempts
        
    Returns:
        str: Generated text response
        
    Raises:
        Exception: If API call fails after retries
    """
    for attempt in range(max_retries):
        try:
            logger.info(f"Sending request to Gemini API (attempt {attempt + 1}/{max_retries})...")
            
            response = model.generate_content(prompt)
            
            if not response or not response.text:
                logger.error("Empty response from Gemini API")
                raise ValueError("Empty response received from Gemini")
                
            logger.info("Successfully received response from Gemini API")
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            
            # Check if it's a quota/rate limit error
            if "429" in error_msg or "quota" in error_msg.lower() or "rate limit" in error_msg.lower():
                logger.warning(f"Rate limit hit: {error_msg}")
                
                # Extract retry delay if available
                if "retry in" in error_msg.lower():
                    # Try to parse the retry delay
                    import re
                    match = re.search(r'retry in (\d+\.?\d*)', error_msg.lower())
                    if match:
                        wait_time = float(match.group(1))
                    else:
                        wait_time = 60  # Default 1 minute
                else:
                    wait_time = 60
                
                if attempt < max_retries - 1:
                    logger.info(f"Waiting {wait_time} seconds before retry...")
                    time.sleep(wait_time)
                    continue
                else:
                    logger.error("Max retries reached. Rate limit still active.")
                    raise Exception(f"Rate limit exceeded. Please wait before trying again. Original error: {error_msg}")
            else:
                logger.error(f"Gemini API Error: {error_msg}")
                raise
    
    raise Exception("Failed to get response after all retries")


def generate_response_with_config(prompt: str, temperature: float = 0.7, max_tokens: int = 2048) -> str:
    """
    Generate response with custom configuration
    """
    try:
        logger.info(f"Sending request with temp={temperature}, max_tokens={max_tokens}")
        
        generation_config = genai.GenerationConfig(
            temperature=temperature,
            max_output_tokens=max_tokens,
        )
        
        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )
        
        logger.info("Successfully received response from Gemini API")
        return response.text
        
    except Exception as e:
        logger.error(f"Gemini API Error: {str(e)}")
        raise