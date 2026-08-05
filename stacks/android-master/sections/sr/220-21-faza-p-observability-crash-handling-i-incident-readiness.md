## 21. Faza P - Observability, Crash Handling I Incident Readiness

1. Inventarisi crash, ANR, performance, analytics, logging, tracing, remote config, feature flag i support diagnostics.
2. Proveri da su release logovi strukturirani, privacy-safe, rate-limited i korisni.
3. Proveri da se crash mapping i native symbols upload-uju za svaki release artefakt.
4. Korelisi app version, version code, varijantu, uredjaj, API, ABI, session, pseudonim naloga, network i feature state bez izlaganja osetljivih podataka.
5. Prati crash-free users, crash-free sessions, ANR, startup, jank, memory, battery, network error, worker failure, playback error i kriticne poslovne ishode.
6. Definisi alert threshold, owner-a, triage, containment, rollback i komunikaciju.
7. Proveri da feature flag i remote config imaju type, default, ownership, audit history, targeting safety, expiry i offline ponasanje.
8. Testiraj kill switch za rizicne feature-e, background job-ove, media source-ove i third-party SDK-ove.
9. Proveri da diagnostics moze bezbedno da se export-uje bez tajni ili user content-a.
10. Odrzavaj runbook za los release, signing problem, database migration failure, backend nekompatibilnost, kompromitovan SDK, policy rejection i widespread crash.
11. Proveri staged rollout, halt, rollback, hotfix i minimum-supported-version strategiju.
12. Sacuvaj dovoljno dokaza za post-incident analizu bez prekomernog prikupljanja podataka.

