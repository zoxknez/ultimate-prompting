## 11. Phase G - RAG, Search And Knowledge Systems

### 11.1 Ingestion And Index Integrity

1. Inventory connectors, parsers, OCR, extraction libraries, preprocessing, chunking, embedding, indexing, and deletion paths.
2. Treat uploads and source content as untrusted. Scan and isolate active content where applicable.
3. Preserve stable source IDs, tenant and ACL metadata, timestamps, versions, lineage, and deletion markers.
4. Test malformed files, adversarial documents, hidden text, prompt injection, poisoned metadata, oversized content, duplicate documents, and parser discrepancies.
5. Verify re-index, update, tombstone, and delete propagation across all replicas and caches.
6. Verify index backups and restore procedures where the index is business-critical.

### 11.2 Retrieval Design

1. Do not assume a universal chunk size, overlap, top-k, embedding model, fusion method, or reranker.
2. Derive retrieval configuration from representative evaluations and domain structure.
3. Compare applicable approaches such as lexical, vector, hybrid, metadata-filtered, graph, structured query, parent-child, late chunking, long-context, and reranking.
4. Verify query rewriting, decomposition, expansion, and routing do not change user intent or bypass authorization.
5. Verify filters are applied before content exposure and remain consistent across retries and fallbacks.
6. Measure freshness, duplicate suppression, diversity, language coverage, and long-document behavior.
7. Record why the chosen retrieval design is appropriate for the target workload.

### 11.3 Retrieval Evaluation

Use representative and adversarial queries. Measure applicable metrics separately:

- retrieval coverage and answerability
- Recall@K, Precision@K, MRR, MAP, nDCG, or task-specific retrieval success
- ACL and tenant isolation success rate
- citation precision, citation recall, citation completeness, and source attribution correctness
- context relevance and context sufficiency
- answer groundedness, faithfulness, and unsupported-claim rate
- freshness and deletion compliance
- latency, token use, and cost per query
- performance by language, tenant, source type, document length, and critical user slice

Inspect examples manually. Do not use a single LLM judge as the sole source of truth.

