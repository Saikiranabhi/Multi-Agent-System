import os
from config.system_config import PDF_STORAGE_PATH, REPORT_OUTPUT_PATH

def ensure_storage():
    os.makedirs(PDF_STORAGE_PATH, exist_ok=True)
    os.makedirs(REPORT_OUTPUT_PATH, exist_ok=True)

def list_pdfs():
    return [f for f in os.listdir(PDF_STORAGE_PATH) if f.endswith(".pdf")]

def report_path(filename):
    return os.path.join(REPORT_OUTPUT_PATH, filename)
