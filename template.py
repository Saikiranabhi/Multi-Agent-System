import os

PROJECT_NAME = "pdf_intelligence_system"

FOLDERS = [
    "config",
    "orchestrator",
    "agents",
    "processing",
    "retrieval",
    "intelligence",
    "output",
    "storage/raw_pdfs",
    "storage/embeddings",
    "storage/reports",
    "utils"
]

FILES = [
    "main.py",
    "requirements.txt",
    "Dockerfile",
    "docker-compose.yml",
    ".env",
    ".gitignore",
    ".dockerignore",
    "README.md",

    "config/system_config.py",

    "orchestrator/agent_controller.py",
    "orchestrator/pipeline_manager.py",

    "agents/ingestion_agent.py",
    "agents/embedding_agent.py",
    "agents/similarity_agent.py",
    "agents/analysis_agent.py",
    "agents/presenter_agent.py",

    "processing/pdf_parser.py",
    "processing/text_chunker.py",
    "processing/content_cleaner.py",

    "retrieval/faiss_store.py",
    "retrieval/similarity_engine.py",

    "intelligence/reasoning_engine.py",
    "intelligence/topic_extractor.py",
    "intelligence/contribution_mapper.py",

    "output/report_builder.py",
    "output/structured_formatter.py",

    "utils/logger.py",
    "utils/file_manager.py"
]

def create_project():
    print(f"\n📁 Creating project: {PROJECT_NAME}\n")

    os.makedirs(PROJECT_NAME, exist_ok=True)

    # Create folders
    for folder in FOLDERS:
        path = os.path.join(PROJECT_NAME, folder)
        os.makedirs(path, exist_ok=True)
        print(f"Created folder: {path}")

    # Create files
    for file in FILES:
        path = os.path.join(PROJECT_NAME, file)
        with open(path, "w", encoding="utf-8") as f:
            pass
        print(f"Created file: {path}")

    # Add .keep to storage folders so Git tracks them
    storage_folders = [
        "storage/raw_pdfs",
        "storage/embeddings",
        "storage/reports"
    ]
    for folder in storage_folders:
        keep_path = os.path.join(PROJECT_NAME, folder, ".keep")
        with open(keep_path, "w") as f:
            pass

    print("\n✅ Project structure created successfully!")

if __name__ == "__main__":
    create_project()
