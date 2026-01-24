import streamlit as st
import os
import sys
from orchestrator.pipeline_manager import PipelineManager
from storage.storage_manager import ensure_storage
from utils.logger import logger

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

UPLOAD_FOLDER = "storage/raw_pdfs"
REPORT_FOLDER = "storage/reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

manager = PipelineManager()

st.set_page_config(
    page_title="PDF Intelligence System",
    layout="wide"
)

st.title("📄 Multi-Agent PDF Intelligence System")
st.caption("Upload a PDF → Automatic Gemini Analysis → 3-Page Research Report")

# -----------------------------
# Upload PDF Section
# -----------------------------
st.subheader("📤 Upload Research PDF")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"],
    accept_multiple_files=False
)

if uploaded_file:
    pdf_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"Uploaded: {uploaded_file.name}")

    # -----------------------------
    # Run Analysis Button
    # -----------------------------
    if st.button("🧠 Run Automated Analysis"):
        with st.spinner("Running multi-agent analysis..."):
            try:
                report = manager.generate_report(pdf_path)

                report_file = os.path.join(
                    REPORT_FOLDER,
                    uploaded_file.name.replace(".pdf", "_report.txt")
                )

                with open(report_file, "w", encoding="utf-8") as f:
                    f.write(report)

                st.success("Analysis Complete!")

                # Display Report
                st.subheader("📘 Generated Report")
                st.text_area("Final Output", report, height=600)

                st.download_button(
                    label="⬇ Download Report",
                    data=report,
                    file_name=os.path.basename(report_file),
                    mime="text/plain"
                )

            except Exception as e:
                logger.error(str(e))
                st.error(f"Error: {e}")
