pdf_intelligence_system/
│
├── main.py
├── config/
│   └── system_config.py
│
├── orchestrator/
│   ├── agent_controller.py
│   └── pipeline_manager.py
│
├── agents/
│   ├── ingestion_agent.py
│   ├── embedding_agent.py
│   ├── similarity_agent.py
│   ├── analysis_agent.py
│   └── presenter_agent.py
│
├── processing/
│   ├── pdf_parser.py
│   ├── text_chunker.py
│   └── content_cleaner.py
│
├── retrieval/
│   ├── faiss_store.py
│   └── similarity_engine.py
│
├── intelligence/
│   ├── reasoning_engine.py
│   ├── topic_extractor.py
│   └── contribution_mapper.py
│
├── output/
│   ├── report_builder.py
│   └── structured_formatter.py
│
├── storage/
│   ├── raw_pdfs/
│   ├── embeddings/
│   └── reports/
│
├── utils/
│   ├── logger.py
│   └── file_manager.py
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .env
├── .gitignore
└── README.md
