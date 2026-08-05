## 7. Faza C - Identitet, Tenancy, Autorizacija I Pristanak

1. Proveri autentikaciju na svakoj spolja dostupnoj i internoj privilegovanoj putanji.
2. Proveri da tenant kontekst ne moze biti zadat ili promenjen untrusted input-om.
3. Testiraj object-level i action-level autorizaciju za retrieval, alate, memoriju, export, admin akcije i background job-ove.
4. Primeni retrieval ACL filtere pre nego sto candidate sadrzaj postane dostupan modelu.
5. Testiraj post-filtering bypass, gubitak metapodataka, cache curenje, shared-index curenje i cross-tenant join-ove.
6. Proveri least-privilege scope-ove za provider API-je, cloud identitete, OAuth, MCP, baze, storage, browser sesije i code execution.
7. Proveri pristanak, obavestenje i opoziv za memoriju, personalizaciju, snimanje, transkripciju i high-impact akcije.
8. Proveri da se odobrenja ne mogu replay-ovati, prosiriti, zameniti ili ponovo koristiti nakon promene parametara.
9. Ukljuci pozitivne i negativne authorization testove.

