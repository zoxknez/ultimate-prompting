# Revizija 01 - AI / RAG / LLM / Agent / Tool / MCP Audit Prompt

## Status

- Srpska verzija: zavrsena
- Engleska verzija: zavrsena
- Strukturna EN/SR paritet provera: prosla
- Broj linija pre: 114 po jeziku
- Broj linija posle: 668 po jeziku
- Broj heading-a pre: 20 po jeziku
- Broj heading-a posle: 51 po jeziku
- Baseline hardcode provera: prosla
- Markdown code fence provera: prosla
- En dash, em dash i non-breaking hyphen u srpskoj verziji: 0

## Glavni Problemi Prethodne Verzije

1. Prompt je bio kvalitetna kratka kontrolna lista, ali ne i kompletan production audit ugovor.
2. Sadrzao je fiksne chunking smernice koje nisu univerzalno validne.
3. Nije dovoljno razdvajao model behavior od deterministicke autorizacije i policy enforcement-a.
4. MCP deo nije pokrivao token audience, zabranu token passthrough-a, confused deputy, capability promene, server supply chain i experimental feature status.
5. Agent deo nije dovoljno pokrivao state machine, durable workflow, at-least-once izvrsavanje, idempotency, compensating action, paralelizam i partial failure.
6. Eval deo nije razdvajao retrieval, response, tool, trajectory, safety, human i online eval slojeve.
7. Nije postojao potpun eksperimentalni protokol za nondeterminism, holdout skupove, judge kalibraciju, varijansu i unapred definisane acceptance pragove.
8. Privacy i data lifecycle deo nije pokrivao provider retention, training, regional processing, deletion propagation, derived artifacts i eval dataset-e.
9. Nedostajali su puni incident response, kill switch, backup, restore, replay, rollback i kompromitovani corpus ili MCP runbook zahtevi.
10. Legal i regulatory deo bio je suvise tanak za EU AI Act, GDPR i sektorske sisteme.
11. Multimodal, voice, browser, computer use i code execution bili su samo kratko pomenuti.
12. Output handling nije dovoljno pokrivao downstream injection, formula injection, lazni UI success i high-impact explanation tokove.

## Najvaznija Unapredjenja

1. Uveden YAML front matter sa prompt ID-jem, verzijom, jezikom, statusom, default rezimom i required core fajlovima.
2. Uveden kompletan input contract i pravilo za rad sa nedostajucim informacijama.
3. Prosiren truth-first i protect-first ugovor.
4. Uvedena precizna AI-specific P0-P3 interpretacija.
5. Uveden AI bill of materials.
6. Uvedena puna arhitektura, data-flow, trust-boundary i permission analiza.
7. Prosireni identity, tenancy, object-level authorization, consent i approval binding zahtevi.
8. Prosiren data lifecycle, privacy, retention, deletion, provenance i dataset governance.
9. Uveden provider, model routing, fallback, strict structured output i failure-mode audit.
10. Uveden detaljan prompt i instruction architecture audit sa direct, indirect, multimodal i multi-turn injection testovima.
11. RAG deo sada zahteva eval-driven retrieval dizajn umesto univerzalnih chunking brojeva.
12. Uvedeni ingestion integrity, ACL, freshness, tombstone, delete propagation, backup i restore zahtevi.
13. Uveden kompletan tool execution i high-impact approval model.
14. MCP audit je prosiren na specifikaciju, OAuth, token audience, token passthrough, confused deputy, session, capability i supply-chain rizike.
15. Agent audit sada pokriva state machine, budget, loop, delegation, concurrency, retries, durable workflow i compensating action.
16. Prosireni memory poisoning, consent, correction, deletion i cross-tenant zahtevi.
17. Uvedene posebne faze za multimodal, voice, browser, computer i code use.
18. Uveden threat-driven adversarial test suite.
19. Uveden pun eval sistem sa dataset dizajnom, judge kalibracijom, varijansom, holdout-om i acceptance gate-ovima.
20. Uvedeni reliability, latency, capacity, cost, observability, incident response i disaster recovery zahtevi.
21. Uvedeni legal, regulatory, ethical i accessibility review zahtevi.
22. Uvedeni supply-chain, deployment i change management zahtevi.
23. Uvedena obavezna test matrica, forbidden shortcuts, final report schema i strozi Definition of Done.

## Primarni Baseline Izvori Dodati U Manifest

- NIST AI Risk Management Framework i NIST AI 600-1
- OWASP Top 10 for LLM and GenAI Applications 2025
- OWASP Top 10 for Agentic Applications 2026
- MITRE ATLAS
- Model Context Protocol specifikacija i security guidance
- OpenTelemetry GenAI semantic conventions
- Zvanicni EU AI Act portal

## Namerno Uklonjene Ili Ispravljene Pretpostavke

- Uklonjeno je univerzalno pravilo za chunk size i overlap.
- Uklonjena je tvrdnja da je odredjeni context window ili provider feature automatski production prednost.
- Uklonjeno je oslanjanje na jedan LLM judge ili jedan demo.
- Uklonjena je mogucnost da se prompt, classifier ili system message tretira kao security boundary.
- Uklonjena je implicitna pretpostavka da je tool call uspesan pre autoritativne backend potvrde.

## Sledeci Paket

Android / Kotlin / Jetpack Compose master audit prompt na srpskom i engleskom.
