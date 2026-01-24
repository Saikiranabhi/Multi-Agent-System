from intelligence.reasoning_engine import analyze_document
from utils.logger import logger

class AnalysisAgent:
    def run(self, context_chunks):
        logger.info("Running deep analytical reasoning...")
        analysis = analyze_document(context_chunks)
        return analysis
