## 19. Faza O - Pouzdanost, Performanse I Trosak

1. Izmeri end-to-end i component-level latenciju, ukljucujuci time to first token, retrieval, reranking, tool pozive, queue i retry.
2. Izmeri token use, cache hit rate, provider cost, tool cost, storage cost i cost po uspesnom poslovnom ishodu.
3. Testiraj provider outage, regional failure, rate limiting, quota exhaustion, spore alate, malformed stream, dropped connection i partial response.
4. Proveri backpressure, queue limit, concurrency control, circuit breaker, bulkhead, cancellation i load shedding.
5. Spreci retry storm, duplicate side effect, runaway agent i nekontrolisan rast konteksta.
6. Definisi SLO, error budget, budget po korisniku ili tenant-u i graceful degradation.
7. Proveri da caching ne curi podatke, ne zaobilazi freshness, ne cuva obrisan sadrzaj niti mesa prompt i authorization kontekst.
8. Load testiraj realne multi-turn i tool-using workload-e, a ne samo pojedinacne model pozive.
9. Proveri capacity i cost pretpostavke prema izmerenim podacima.

