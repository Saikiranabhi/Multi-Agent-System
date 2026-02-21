from retrieval.similarity_engine import search_similar_chunks
from utils.logger import logger

class SimilarityAgent:
    def run(self, query):
        logger.info("Retrieving similar content from FAISS...")
        chunks = search_similar_chunks(query)
        return chunks
