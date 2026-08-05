## 18. Faza N - Eval Sistem I Quality Engineering

### 18.1 Slojevi Evaluacije

Odvojeno evaluiraj:

1. deterministicko unit ponasanje
2. prompt i structured-output ponasanje
3. retrieval kvalitet
4. kvalitet odgovora i groundedness
5. izbor alata i ispravnost argumenata
6. kompletnu agent trajectory i final state
7. safety i policy adherence
8. ljudsku korisnost i task completion
9. latenciju, dostupnost i cost
10. produkcione ishode i incident signale

### 18.2 Dataset I Eksperimentalni Dizajn

1. Napravi verzionisane golden, adversarial, edge-case, multilingual i negative dataset-e iz reprezentativnih use case-ova.
2. Ukljuci kriticne poslovne slice-ove i retke high-impact slucajeve.
3. Razdvoji development, tuning, regression i final holdout skupove.
4. Prati provenance, licensing, PII status, contamination risk, vlasnistvo i istoriju izmena.
5. Za nedeterministicko ponasanje koristi ponovljena pokretanja i prijavi variance ili confidence interval gde ima smisla.
6. Pinuj ili zabelezi model, prompt, tool, retrieval, judge, seed, temperature i konfiguraciju.
7. Kalibrisi LLM judge-eve prema ljudskim labelama i testiraj judge bias, position bias, verbosity bias i self-preference.
8. Koristi deterministicke provere i human review gde su pouzdaniji od LLM judge-a.
9. Sacuvaj failing primere i nakon triage-a ih dodaj u regression suite.

### 18.3 Acceptance Gate-ovi

Pre evaluacije definisi eksplicitne pragove. Najmanje ukljuci:

- critical task success rate
- critical safety-policy pass rate
- authorization i tenant-isolation pass rate
- unsupported-claim ili hallucination rate
- citation correctness gde je potrebno
- tool-selection i argument-validity rate
- compliance odobrenja za ireverzibilne akcije
- p50, p95 i p99 latenciju ili primenjive SLO-ove
- timeout, retry i failure rate
- token i novcani cost po uspesnom zadatku
- regression toleranciju prema odobrenom baseline-u

Ne biraj pragove nakon sto vidis rezultate samo da bi audit prosao.

### 18.4 Online Evaluacija I Release Strategija

1. Koristi shadow, replay, canary ili ograniceni rollout gde je prikladno.
2. Spreci da eval saobracaj izazove stvarne side effect-e.
3. Prati user correction, abandonment, escalation, retry, complaint, incident i successful-completion signale.
4. Detektuj drift po modelu, promptu, source corpus-u, tenant-u, jeziku, alatu i use-case slice-u.
5. Definisi automatic rollback i kill-switch uslove.
6. Zahtevaj review pri promeni model alias-a, prompta, retrieval-a, alata, policy-ja ili MCP capability-ja.

