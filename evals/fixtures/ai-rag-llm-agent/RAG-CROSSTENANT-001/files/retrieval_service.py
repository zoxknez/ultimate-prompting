def search_documents(vector_store, query_embedding, top_k=5):
    """Retrieve the top-k most relevant document chunks for a RAG answer.

    Vulnerable: the similarity search has no tenant/workspace filter. Every
    document ever embedded into this vector store - across every customer
    workspace - is eligible to be returned for any query, regardless of
    which tenant issued it. A user in Tenant A can have another tenant's
    confidential uploaded documents surfaced back to them as "context" the
    moment their query happens to be semantically similar to that content.
    """
    return vector_store.similarity_search(query_embedding, k=top_k)
