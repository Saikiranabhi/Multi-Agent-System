# from orchestrator.pipeline_manager import PipelineManager
# from storage.storage_manager import list_pdfs
# from retrieval.faiss_store import load_index
# from utils.logger import logger
# import sys
# import os

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# if ROOT_DIR not in sys.path:
#     sys.path.insert(0, ROOT_DIR)

# def run_system():
#     manager = PipelineManager()

#     load_index()

#     pdfs = list_pdfs()
#     if not pdfs:
#         logger.error("No PDFs found in storage/raw_pdfs")
#         return

#     for pdf in pdfs:
#         pdf_path = os.path.join("storage/raw_pdfs", pdf)
#         logger.info(f"Processing PDF: {pdf}")

#         report = manager.generate_report(pdf_path)

#         report_path = f"storage/reports/{pdf.replace('.pdf','')}_report.txt"
#         with open(report_path, "w", encoding="utf-8") as f:
#             f.write(report)

#         logger.info(f"Report saved: {report_path}")

# if __name__ == "__main__":
#     run_system()


import sys
import os

# Ensure project root is in Python path BEFORE imports
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from orchestrator.pipeline_manager import PipelineManager
from storage.storage_manager import list_pdfs
from retrieval.faiss_store import load_index
from utils.logger import logger


def run_system():
    manager = PipelineManager()

    # Load FAISS index if exists
    load_index()

    pdfs = list_pdfs()
    if not pdfs:
        logger.error("No PDFs found in storage/raw_pdfs")
        return

    for pdf in pdfs:
        pdf_path = os.path.join("storage/raw_pdfs", pdf)
        logger.info(f"Processing PDF: {pdf}")

        # Run multi-agent pipeline
        report = manager.generate_report(pdf_path)

        # Save report
        report_path = f"storage/reports/{pdf.replace('.pdf','')}_report.txt"
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(report)

        logger.info(f"Report saved: {report_path}")


if __name__ == "__main__":
    run_system()
