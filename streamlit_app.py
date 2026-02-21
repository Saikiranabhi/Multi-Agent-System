# import streamlit as st
# import os
# import sys
# from orchestrator.pipeline_manager import PipelineManager
# from storage.storage_manager import ensure_storage
# from utils.logger import logger

# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# if ROOT_DIR not in sys.path:
#     sys.path.insert(0, ROOT_DIR)

# UPLOAD_FOLDER = "storage/raw_pdfs"
# REPORT_FOLDER = "storage/reports"

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)
# os.makedirs(REPORT_FOLDER, exist_ok=True)

# manager = PipelineManager()

# st.set_page_config(
#     page_title="Multi Agent System",
#     layout="wide"
# )

# st.title("📄 Multi-Agent Intelligence System")
# st.caption("Upload a PDF → Automatic Gemini Analysis → 3-Page Research Report")

# # -----------------------------
# # Upload PDF Section
# # -----------------------------
# st.subheader("📤 Upload Research PDF")

# uploaded_file = st.file_uploader(
#     "Upload a PDF file",
#     type=["pdf"],
#     accept_multiple_files=False
# )

# if uploaded_file:
#     pdf_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

#     with open(pdf_path, "wb") as f:
#         f.write(uploaded_file.read())

#     st.success(f"Uploaded: {uploaded_file.name}")

#     # -----------------------------
#     # Run Analysis Button
#     # -----------------------------
#     if st.button("🧠 Run Automated Analysis"):
#         with st.spinner("Running multi-agent analysis..."):
#             try:
#                 report = manager.generate_report(pdf_path)

#                 report_file = os.path.join(
#                     REPORT_FOLDER,
#                     uploaded_file.name.replace(".pdf", "_report.txt")
#                 )

#                 with open(report_file, "w", encoding="utf-8") as f:
#                     f.write(report)

#                 st.success("Analysis Complete!")

#                 # Display Report
#                 st.subheader("📘 Generated Report")
#                 st.text_area("Final Output", report, height=600)

#                 st.download_button(
#                     label="⬇ Download Report",
#                     data=report,
#                     file_name=os.path.basename(report_file),
#                     mime="text/plain"
#                 )

#             except Exception as e:
#                 logger.error(str(e))
#                 st.error(f"Error: {e}")



import streamlit as st
import os
import sys
from orchestrator.pipeline_manager import PipelineManager
from storage.storage_manager import ensure_storage
from utils.logger import logger

# ----------------------------
# Path Setup
# ----------------------------
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

UPLOAD_FOLDER = "storage/raw_pdfs"
REPORT_FOLDER = "storage/reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

manager = PipelineManager()

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Multi-Agent Intelligence System",
    layout="wide",
    page_icon="🧠"
)

# ----------------------------
# Custom Modern CSS
# ----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: #ffffff;
}

/* Hero Section */
.hero {
    padding: 40px;
    border-radius: 20px;
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

.hero h1 {
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero p {
    font-size: 18px;
    opacity: 0.9;
}

/* Card Styling */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    margin-bottom: 30px;
}

/* Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: 600;
    border: none;
    transition: 0.3s;
}

div.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(135deg, #16a34a, #15803d);
}

/* Download Button */
div.stDownloadButton > button {
    background: linear-gradient(135deg, #3b82f6, #2563eb);
    color: white;
    border-radius: 12px;
    padding: 12px 25px;
    font-weight: 600;
    border: none;
}

/* Text Area */
textarea {
    background-color: #0f172a !important;
    color: #ffffff !important;
    border-radius: 12px !important;
}

/* File uploader */
section[data-testid="stFileUploader"] {
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero Section
# ----------------------------
st.markdown("""
<div class="hero">
    <h1>🧠 Multi-Agent Intelligence System</h1>
    <p>Upload a Research PDF → AI Multi-Agent Analysis → Generate Structured Research Report</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# Upload Section Card
# ----------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📤 Upload Research PDF")

uploaded_file = st.file_uploader(
    "Drag & Drop or Select a PDF",
    type=["pdf"],
    accept_multiple_files=False
)

if uploaded_file:
    pdf_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"✅ Uploaded: {uploaded_file.name}")

    if st.button("🚀 Run Automated Multi-Agent Analysis"):
        with st.spinner("🔎 Running AI agents and generating report..."):
            try:
                report = manager.generate_report(pdf_path)

                report_file = os.path.join(
                    REPORT_FOLDER,
                    uploaded_file.name.replace(".pdf", "_report.txt")
                )

                with open(report_file, "w", encoding="utf-8") as f:
                    f.write(report)

                st.success("🎉 Analysis Complete!")

                # ----------------------------
                # Report Section
                # ----------------------------
                st.markdown('</div>', unsafe_allow_html=True)
                st.markdown('<div class="card">', unsafe_allow_html=True)

                st.subheader("📘 Generated Research Report")

                st.text_area(
                    "Final Output",
                    report,
                    height=600
                )

                st.download_button(
                    label="⬇ Download Report",
                    data=report,
                    file_name=os.path.basename(report_file),
                    mime="text/plain"
                )

            except Exception as e:
                logger.error(str(e))
                st.error(f"❌ Error: {e}")

st.markdown('</div>', unsafe_allow_html=True)