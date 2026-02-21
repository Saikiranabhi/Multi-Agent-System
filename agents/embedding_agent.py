from processing.text_chunker import chunk_text
from retrieval.faiss_store import store_chunks
from utils.logger import logger

class EmbeddingAgent:
    def run(self, raw_text):
        logger.info("Chunking text for embeddings...")
        chunks = chunk_text(raw_text)

        logger.info("Storing embeddings in FAISS index...")
        store_chunks(chunks)

        return chunks
