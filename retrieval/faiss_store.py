# import faiss
# import numpy as np
# import os
# # from models.embedding_model import embedder
# from config.system_config import FAISS_INDEX_PATH

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


import faiss
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from config.system_config import FAISS_INDEX_PATH

# Load embedding model inside retrieval layer
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
embedder = SentenceTransformer(EMBEDDING_MODEL_NAME)

dimension = embedder.get_sentence_embedding_dimension()
index = faiss.IndexFlatIP(dimension)

stored_chunks = []

def store_chunks(chunks):
    global stored_chunks

    embeddings = embedder.encode(
        chunks,
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    if embeddings.ndim == 1:
        embeddings = embeddings.reshape(1, -1)

    index.add(embeddings)
    stored_chunks.extend(chunks)

def save_index():
    os.makedirs(os.path.dirname(FAISS_INDEX_PATH), exist_ok=True)
    faiss.write_index(index, FAISS_INDEX_PATH)

def load_index():
    global index
    if os.path.exists(FAISS_INDEX_PATH):
        index = faiss.read_index(FAISS_INDEX_PATH)
