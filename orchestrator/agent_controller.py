from agents.ingestion_agent import IngestionAgent
from agents.embedding_agent import EmbeddingAgent
from agents.similarity_agent import SimilarityAgent
from agents.analysis_agent import AnalysisAgent
from agents.presenter_agent import PresenterAgent
from utils.logger import logger

class AgentController:
    def __init__(self):
        self.ingestion = IngestionAgent()
        self.embedding = EmbeddingAgent()
        self.similarity = SimilarityAgent()
        self.analysis = AnalysisAgent()
        self.presenter = PresenterAgent()

    def run_full_pipeline(self, pdf_path, query=None):
        logger.info("Starting Multi-Agent Pipeline...")

        # Step 1: Extract text
        raw_text = self.ingestion.run(pdf_path)

        # Step 2: Chunk + embed
        chunks = self.embedding.run(raw_text)

        # Step 3: Retrieve similarity context
        if query:
            context_chunks = self.similarity.run(query)
        else:
            context_chunks = chunks[:10]  # fallback context

        # Step 4: Deep analysis
        analysis_output = self.analysis.run(context_chunks)

        # Step 5: Final report generation
        report = self.presenter.run(analysis_output)

        logger.info("Pipeline complete")
        return report
