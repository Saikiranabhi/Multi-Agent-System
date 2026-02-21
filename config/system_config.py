import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

PDF_STORAGE_PATH = os.getenv("PDF_STORAGE_PATH", "storage/raw_pdfs")
REPORT_OUTPUT_PATH = os.getenv("REPORT_OUTPUT_PATH", "storage/reports")
FAISS_INDEX_PATH = os.getenv("FAISS_INDEX_PATH", "storage/embeddings/index.faiss")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
TOP_K_RESULTS = int(os.getenv("TOP_K_RESULTS", 8))
