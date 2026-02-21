

# from retrieval.faiss_store import index, stored_chunks, embedder

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


from retrieval.faiss_store import stored_chunks


def search_similar_chunks(query, k=8):
    """
    No embedding model available — return first k chunks as context.
    Gemini handles semantic understanding in the analysis step anyway.
    """
    if not stored_chunks:
        return []

    return stored_chunks[:k]