
# import faiss
# import numpy as np
# import os
# from sentence_transformers import SentenceTransformer
# from config.system_config import FAISS_INDEX_PATH

# # Load embedding model inside retrieval layer
# EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
# embedder = SentenceTransformer(EMBEDDING_MODEL_NAME)

# dimension = embedder.get_sentence_embedding_dimension()
# index = faiss.IndexFlatIP(dimension)

# stored_chunks = []

# def store_chunks(chunks):
#     global stored_chunks

#     embeddings = embedder.encode(
#         chunks,
#         convert_to_numpy=True,
#         normalize_embeddings=True
#     ).astype("float32")

#     if embeddings.ndim == 1:
#         embeddings = embeddings.reshape(1, -1)

#     index.add(embeddings)
#     stored_chunks.extend(chunks)

# def save_index():
#     os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
#     faiss.write_index(index, FAISS_INDEX_PATH)

# def load_index():
#     global index
#     if os.path.exists(FAISS_INDEX_PATH):
#         index = faiss.read_index(FAISS_INDEX_PATH)


import os
from config.system_config import FAISS_INDEX_PATH

# No FAISS, no embeddings — just store chunks in memory
stored_chunks = []


def store_chunks(chunks):
    global stored_chunks
    stored_chunks.extend(chunks)


def save_index():
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
    chunks_path = FAISS_INDEX_PATH.replace(".faiss", ".txt")
    with open(chunks_path, "w", encoding="utf-8") as f:
        f.write("\n---CHUNK---\n".join(stored_chunks))


def load_index():
    global stored_chunks
    chunks_path = FAISS_INDEX_PATH.replace(".faiss", ".txt")
    if os.path.exists(chunks_path):
        with open(chunks_path, "r", encoding="utf-8") as f:
            stored_chunks = f.read().split("\n---CHUNK---\n")