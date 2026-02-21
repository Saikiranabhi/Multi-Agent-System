# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")

# # model = genai.GenerativeModel("models/gemini-1.5-flash")

# def generate_response(prompt: str) -> str:
#     response = model.generate_content(prompt)
#     return response.text
