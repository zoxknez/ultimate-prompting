## 11. Faza G - RAG, Search I Knowledge Sistemi

### 11.1 Ingestion I Integritet Index-a

1. Popisi connector-e, parser-e, OCR, extraction biblioteke, preprocessing, chunking, embedding, indexing i delete putanje.
2. Upload-e i source sadrzaj tretiraj kao untrusted. Skeniraj i izoluj aktivni sadrzaj gde je primenjivo.
3. Sacuvaj stabilne source ID-jeve, tenant i ACL metadata, timestamp-e, verzije, lineage i deletion markere.
4. Testiraj malformed fajlove, adversarial dokumente, hidden text, prompt injection, poisoned metadata, oversized sadrzaj, duplicate dokumente i parser razlike.
5. Proveri reindex, update, tombstone i delete propagation kroz sve replike i cache slojeve.
6. Proveri backup i restore index-a gde je index poslovno kritican.

### 11.2 Retrieval Dizajn

1. Ne pretpostavljaj univerzalni chunk size, overlap, top-k, embedding model, fusion metod ili reranker.
2. Retrieval konfiguraciju izvedi iz reprezentativnih evaluacija i strukture domena.
3. Uporedi primenjive pristupe kao sto su lexical, vector, hybrid, metadata-filtered, graph, structured query, parent-child, late chunking, long-context i reranking.
4. Proveri da query rewriting, decomposition, expansion i routing ne menjaju nameru korisnika niti zaobilaze autorizaciju.
5. Proveri da se filteri primenjuju pre izlaganja sadrzaja i ostaju konzistentni kroz retry i fallback.
6. Izmeri freshness, duplicate suppression, diversity, language coverage i ponasanje na dugim dokumentima.
7. Zabelezi zasto je odabrani retrieval dizajn prikladan za ciljni workload.

### 11.3 Retrieval Evaluacija

Koristi reprezentativne i adversarial upite. Odvojeno meri primenjive metrike:

- retrieval coverage i answerability
- Recall@K, Precision@K, MRR, MAP, nDCG ili task-specific retrieval success
- ACL i tenant isolation success rate
- citation precision, citation recall, citation completeness i ispravnost source attribution-a
- context relevance i context sufficiency
- answer groundedness, faithfulness i unsupported-claim rate
- freshness i delete compliance
- latenciju, token use i cost po upitu
- performanse po jeziku, tenant-u, source tipu, duzini dokumenta i kriticnom user slice-u

Rucno pregledaj primere. Ne koristi jednog LLM judge-a kao jedini izvor istine.

