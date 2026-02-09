<<<<<<< HEAD
# 📄 Multi-Agent System

> An advanced AI-powered system that automatically analyzes research papers , thesis papers and generates comprehensive multi-page reports using a multi-agent architecture powered by Google Gemini and FAISS vector search.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google-Gemini%202.5-orange.svg)](https://ai.google.dev/)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-green.svg)](https://github.com/facebookresearch/faiss)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 About

The **Multi-Agent PDF Intelligence System** is a sophisticated document analysis platform that leverages cutting-edge AI technologies to transform complex research papers into actionable insights. By employing a multi-agent architecture, the system orchestrates specialized AI agents to handle different aspects of document processing, from ingestion to final report generation.

### Key Highlights
- 🤖 **5 Specialized AI Agents** working in harmony
- 🧠 **Google Gemini 2.5** for deep semantic analysis
- 🔍 **FAISS Vector Database** for intelligent similarity search
- 📊 **Automated Report Generation** with structured insights
- 🎨 **Interactive Streamlit Interface** for easy access
- 🐳 **Docker Support** for seamless deployment

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     PDF Intelligence System                      │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
        ┌────────────────────────────────────────┐
        │     Pipeline Manager (Orchestrator)    │
        └────────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        │      Agent Controller          │
        └───────────────┬───────────────┘
                        │
        ┌───────────────┴───────────────────────────────┐
        │                                               │
        ▼               ▼               ▼               ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│  Ingestion   │ │  Embedding   │ │  Similarity  │ │   Analysis   │
│    Agent     │ │    Agent     │ │    Agent     │ │    Agent     │
│              │ │              │ │              │ │              │
│ PDF → Text   │ │ Text → Vec   │ │ Search Vec   │ │ AI Analysis  │
└──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘
        │               │               │               │
        └───────────────┴───────────────┴───────────────┘
                                 │
                                 ▼
                        ┌──────────────┐
                        │  Presenter   │
                        │    Agent     │
                        │              │
                        │ Report Gen   │
                        └──────────────┘
                                 │
                                 ▼
                        📄 Final Report
```

### Agent Responsibilities

| Agent | Responsibility | Technology |
|-------|---------------|------------|
| **Ingestion Agent** | Extracts raw text from PDF documents | PyPDF |
| **Embedding Agent** | Chunks text and creates vector embeddings | Sentence Transformers |
| **Similarity Agent** | Retrieves semantically similar content | FAISS |
| **Analysis Agent** | Performs deep semantic analysis | Google Gemini 2.5 |
| **Presenter Agent** | Generates structured multi-page reports | Custom Formatter |

---

## 🛠️ Tech Stack

### Core Technologies

#### **AI & ML**
- **Google Gemini 2.5 Flash** - Advanced LLM for document analysis
  - Natural language understanding
  - Research paper comprehension
  - Structured output generation
  
- **Sentence Transformers** - Text embedding generation
  - Model: `all-MiniLM-L6-v2`
  - 384-dimensional embeddings
  - Optimized for semantic similarity

- **FAISS (Facebook AI Similarity Search)** - Vector database
  - Inner product similarity search
  - In-memory indexing
  - Fast retrieval (< 100ms)

#### **Document Processing**
- **PyPDF** - PDF text extraction
- **LangChain Text Splitters** - Intelligent text chunking
  - Recursive character splitting
  - Configurable chunk size (1200 chars)
  - Overlap for context preservation (200 chars)

#### **Backend & Orchestration**
- **Python 3.11+** - Core programming language
- **Custom Multi-Agent System** - Orchestration framework
- **python-dotenv** - Environment management

#### **Frontend**
- **Streamlit** - Interactive web interface
  - File upload handling
  - Real-time processing updates
  - Report download functionality

#### **DevOps**
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration

#### **Dependencies**
```
google-generativeai==0.7.2
sentence-transformers==2.7.0
faiss-cpu==1.8.0
pypdf==4.2.0
langchain-text-splitters==0.2.1
numpy==1.26.4
torch==2.3.1
transformers==4.41.2
python-dotenv==1.0.1
streamlit==1.35.0
```

---

## 🔄 Processing Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ Step 1: PDF Ingestion                                           │
├─────────────────────────────────────────────────────────────────┤
│ Input: research_paper.pdf                                       │
│ Process: Extract text from all pages                            │
│ Output: Raw text string                                         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Step 2: Text Chunking & Embedding                               │
├─────────────────────────────────────────────────────────────────┤
│ Process:                                                        │
│  • Split text into 1200-char chunks (200 overlap)               │
│  • Generate 384-dim embeddings per chunk                        │
│  • Store in FAISS index                                         │
│ Output: Vector database with indexed chunks                     │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Step 3: Similarity Search                                       │
├─────────────────────────────────────────────────────────────────┤
│ Process:                                                        │
│  • Convert query to embedding                                   │
│  • Search FAISS index (top-k=8)                                 │
│  • Retrieve most relevant chunks                                │
│ Output: Context-relevant text segments                          │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Step 4: AI Analysis (Gemini 2.5)                                │
├─────────────────────────────────────────────────────────────────┤
│ Analyzes:                                                       │
│  • Research objectives                                          │
│  • Methodology & approach                                       │
│  • Core contributions                                           │
│  • Experimental evidence                                        │
│  • Novelty & innovation                                         │
│  • Strengths & weaknesses                                       │
│  • Limitations                                                  │
│  • Practical impact                                             │
│ Output: Structured analytical breakdown                         │
└─────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────┐
│ Step 5: Report Generation                                       │
├─────────────────────────────────────────────────────────────────┤
│ Creates:                                                        │
│  📘 PAGE 1 — Executive Summary                                  │
│  📘 PAGE 2 — Technical Analysis                                 │
│  📘 PAGE 3 — Insights & Impact                                  │
│ Output: Multi-page formatted report (TXT)                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## ✨ Features

### 🎯 Core Features

#### 1. **Intelligent PDF Processing**
- Automatic text extraction from complex PDFs
- Preserves document structure and context
- Handles multi-page research papers

#### 2. **Advanced Vector Search**
- FAISS-powered similarity search
- 384-dimensional semantic embeddings
- Sub-second retrieval times
- Persistent index storage

#### 3. **AI-Powered Analysis**
- Powered by Google Gemini 2.5 Flash
- Deep semantic understanding
- Research-focused analytical framework
- Structured output generation

#### 4. **Multi-Page Report Generation**
- Executive summary
- Technical deep-dive
- Impact assessment
- Downloadable TXT format

#### 5. **Interactive Web Interface**
- Drag-and-drop PDF upload
- Real-time processing status
- Inline report preview
- One-click download

#### 6. **Multi-Agent Architecture**
- Separation of concerns
- Modular and extensible
- Easy to debug and maintain
- Scalable design

### 🔧 Technical Features

- **Automatic Rate Limiting** - Respects Gemini API quotas
- **Retry Logic** - Handles transient failures
- **Comprehensive Logging** - Full audit trail
- **Docker Support** - One-command deployment
- **Environment Configuration** - Flexible settings via `.env`
- **Persistent Storage** - FAISS index persistence
- **Error Handling** - Graceful failure recovery

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Google Gemini API Key ([Get it here](https://aistudio.google.com/apikey))
- 2GB+ RAM (for embeddings)
- Docker (optional)

### Installation

#### Option 1: Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/pdf-intelligence-system.git
cd pdf-intelligence-system
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

5. **Run the system**

**CLI Mode:**
```bash
# Add PDFs to storage/raw_pdfs/
python main.py
# Reports will be saved to storage/reports/
```

**Web Interface:**
```bash
streamlit run streamlit_app.py
# Open http://localhost:8501
```

#### Option 2: Docker Deployment

```bash
# Build and run
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

---

## 📁 Project Structure

```
pdf-intelligence-system/
├── agents/                      # AI Agent implementations
│   ├── ingestion_agent.py      # PDF text extraction
│   ├── embedding_agent.py      # Vector embedding creation
│   ├── similarity_agent.py     # FAISS search
│   ├── analysis_agent.py       # Gemini analysis
│   └── presenter_agent.py      # Report generation
│
├── config/                      # Configuration management
│   └── system_config.py        # Environment variables
│
├── intelligence/                # AI intelligence modules
│   ├── reasoning_engine.py     # Core analysis logic
│   ├── topic_extractor.py      # Topic identification
│   └── contribution_mapper.py  # Contribution extraction
│
├── orchestrator/                # Pipeline orchestration
│   ├── agent_controller.py     # Agent coordination
│   └── pipeline_manager.py     # Workflow management
│
├── output/                      # Report formatting
│   ├── report_builder.py       # Multi-page reports
│   └── structured_formatter.py # Section formatting
│
├── processing/                  # Document processing
│   ├── pdf_parser.py           # PDF extraction
│   ├── text_chunker.py         # Text splitting
│   └── content_cleaner.py      # Text normalization
│
├── retrieval/                   # Vector search
│   ├── faiss_store.py          # FAISS index management
│   └── similarity_engine.py    # Search implementation
│
├── services/                    # External services
│   └── gemini_client.py        # Gemini API wrapper
│
├── storage/                     # Data storage
│   ├── raw_pdfs/               # Input PDFs
│   ├── embeddings/             # FAISS indices
│   └── reports/                # Generated reports
│
├── utils/                       # Utilities
│   ├── logger.py               # Logging configuration
│   ├── file_manager.py         # File operations
│   └── helpers.py              # Helper functions
│
├── main.py                      # CLI entry point
├── streamlit_app.py            # Web interface
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker orchestration
├── .env.example                # Environment template
└── README.md                   # This file
```

---

## 🔮 Future Enhancements

### Planned Features

#### 🎯 Short-term (v2.0)
- [ ] Support for multiple document formats (DOCX, TXT, HTML)
- [ ] Batch processing of multiple PDFs
- [ ] Custom query-based analysis
- [ ] Export reports to PDF/DOCX/Markdown
- [ ] Enhanced error reporting and validation
- [ ] Progress bars for long-running tasks
- [ ] Citation extraction and formatting

#### 🚀 Medium-term (v3.0)
- [ ] **Multi-Document Analysis**
  - Compare multiple research papers
  - Identify common themes
  - Generate comparative reports
  
- [ ] **Advanced Search**
  - Hybrid search (keyword + semantic)
  - Filters by date, author, topic
  - Relevance scoring
  
- [ ] **Knowledge Graph Integration**
  - Entity extraction
  - Relationship mapping
  - Visual knowledge representation

- [ ] **API Development**
  - RESTful API endpoints
  - Webhook support
  - API documentation (Swagger/OpenAPI)

#### 🌟 Long-term (v4.0)
- [ ] **Multi-Modal Analysis**
  - Image/diagram extraction
  - Table understanding
  - Chart analysis
  
- [ ] **Collaborative Features**
  - User annotations
  - Shared workspaces
  - Team reports
  
- [ ] **Advanced AI Capabilities**
  - Custom fine-tuned models
  - Domain-specific analysis
  - Automatic literature review generation
  
- [ ] **Enterprise Features**
  - User authentication & authorization
  - Role-based access control
  - Audit logging
  - Cloud storage integration (S3, GCS)
  - PostgreSQL/MongoDB for metadata

### Technical Improvements

#### Performance
- [ ] Async processing pipeline
- [ ] GPU acceleration for embeddings
- [ ] Distributed FAISS for large datasets
- [ ] Caching layer (Redis)
- [ ] Background job processing (Celery)

#### Scalability
- [ ] Kubernetes deployment
- [ ] Horizontal scaling
- [ ] Load balancing
- [ ] Message queue integration (RabbitMQ/Kafka)

#### Monitoring & Observability
- [ ] Prometheus metrics
- [ ] Grafana dashboards
- [ ] Distributed tracing (Jaeger)
- [ ] Error tracking (Sentry)

---

## 📊 Use Cases

### Academic Research
- Analyze research papers quickly
- Extract key contributions
- Identify methodology patterns
- Compare related work

### Business Intelligence
- Process industry reports
- Extract market insights
- Competitive analysis
- Trend identification

### Legal & Compliance
- Document review automation
- Policy analysis
- Compliance checking
- Risk assessment

### Healthcare
- Medical literature review
- Clinical trial analysis
- Drug research insights
- Treatment comparison

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

--- 

## 🙏 Acknowledgments

- Google Gemini Team for the powerful AI API
- Facebook Research for FAISS
- Sentence Transformers community
- Streamlit for the amazing web framework

---

**Made with ❤️ by [Sai Kiran Tungana]**
=======
---
title: AI Research Team
emoji: 🚀
colorFrom: red
colorTo: red
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: system that automatically analyzes research papers
license: mit
---

# Welcome to Streamlit!

Edit `/src/streamlit_app.py` to customize this app to your heart's desire. :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).
>>>>>>> 9632437b9cebc4c121c30023ba781edd035e9e79
