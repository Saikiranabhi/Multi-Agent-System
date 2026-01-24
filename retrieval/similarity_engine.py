# import numpy as np
# from models.embedding_model import embedder
# from retrieval.faiss_store import index, stored_chunks

# def search_similar_chunks(query, k=8):
#     if index.ntotal == 0:
#         return []

#     query_embedding = embedder.encode(
#         [query],
#         convert_to_numpy=True,
#         normalize_embeddings=True
#     ).astype("float32")

#     scores, ids = index.search(query_embedding, k)

#     results = []
#     for idx in ids[0]:
#         if idx < len(stored_chunks):
#             results.append(stored_chunks[idx])

#     return results



from retrieval.faiss_store import index, stored_chunks, embedder

def search_similar_chunks(query, k=8):
    if index.ntotal == 0:
        return []

    query_embedding = embedder.encode(
        [query],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    scores, ids = index.search(query_embedding, k)

    results = []
    for idx in ids[0]:
        if idx < len(stored_chunks):
            results.append(stored_chunks[idx])

    return results
