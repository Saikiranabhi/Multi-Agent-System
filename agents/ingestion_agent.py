from processing.pdf_parser import extract_text_from_pdf
from utils.logger import logger

class IngestionAgent:
    def run(self, pdf_path):
        logger.info(f"Ingesting PDF: {pdf_path}")
        text = extract_text_from_pdf(pdf_path)
        return text
