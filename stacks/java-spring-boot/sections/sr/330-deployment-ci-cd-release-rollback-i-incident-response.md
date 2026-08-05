## Deployment, CI/CD, Release, Rollback I Incident Response

### Packaging I Runtime Okruženje

- Proveri tačan JAR, layered JAR, WAR, native image, container, server package ili platform artefakt promovisan u svako okruženje preko immutable digest-a.
- Pregledaj container base image, JRE sadržaj, trust store, locale, timezone podatke, user-a, filesystem dozvole, capabilities, resource limite, read-only putanje, temp prostor i signal handling.
- Proveri reverse proxy, servlet container, JVM flagove, environment, mount-ovanu konfiguraciju, tajne, agente, sidecar-e, service mesh, DNS, sertifikate i startup komandu u deploy-ovanoj reviziji.
- Ne rebuild-uj između okruženja; promoviši isti pregledani artefakt i menjaj samo kontrolisanu environment konfiguraciju.
- Testiraj instalaciju, startup, readiness, traffic, shutdown, restart, zamenu node-a, image pull, registry outage, configuration grešku i rotaciju tajne.

### CI/CD I Poverenje Artefakta

- Mapiraj repository zaštite, odobrenja, runner trust, fork ponašanje, token-e, OIDC, environment gate-ove, tajne, cache-eve, artefakte, reusable workflow-e, plugin-e i deployment identitete.
- Pinuj third-party action-e, image-e, plugin-e, wrapper-e i preuzete alate immutable verzijom ili digest-om uz update i revocation proces.
- Odvoji izvršavanje nepoverljivog pull request-a od release kredencijala, signing key-eva, produkcionih mreža, package publication-a i mutable cache-eva.
- Generiši i sačuvaj test dokaze, dependency graph, SBOM, provenance, potpise gde se koriste, artifact digest, migration plan, release note i approval trag.
- Proveri da deployment koristi samo pregledani artefakt i da se provenance ili potpisi stvarno proveravaju gde politika tvrdi enforcement.

### Rollout, Kompatibilnost I Rollback

- Definiši preduslove, canary kohortu, progresiju saobraćaja, observation window, SLO i invariant guardrail-e, abort pragove, owner-a i rollback autoritet.
- Testiraj old/new application verzije sa old/new schema-om, event-ima, cache vrednostima, session-ima, token-ima, klijentima, job-ovima i background worker-ima tokom overlap-a.
- Razdvoji application rollback, configuration rollback, isključivanje feature-a, traffic shift, schema forward repair, data reconciliation i infrastructure rollback.
- Dokaži da rollback ne korumpira podatke, ne replay-uje nepovratne efekte, ne gubi poruke, ne invalidira session neočekivano i ne pokreće nekompatibilan stari kod protiv promenjene schema-e.
- Uvežbaj rollback iz parcijalnog rollout-a, neuspele migracije, dependency incidenta, security revocation-a, performance regresije i korumpirane konfiguracije.

### Incident I Trusted-Recovery Režim

- Definiši trigger-e za security, data-integrity, availability, privacy, supply-chain, signing-key, certificate, dependency i migration incidente.
- Sačuvaj timeline, release identitete, digest-e, konfiguraciju, logove, trace-ove, database dokaze, broker offset-e, audit zapise i relevantne volatile dokaze uz kontrolisan pristup.
- Obezbedi kill switch, opoziv kredencijala i ključeva, traffic izolaciju, pauzu consumer-a, pauzu job-a, write freeze, isključivanje feature-a i bezbedne degraded mode-ove.
- Rebuild-uj iz trusted source-a i toolchain-a posle supply-chain kompromitacije; redeployment nepoverljivog artefakta ne tretiraj kao sanaciju.
- Zahtevaj post-recovery verifikaciju poslovnih invarijanti, tenant izolacije, balance-a, queue-eva, index-a, fajlova, callback-ova, alert-a i monitoringa pre zatvaranja incidenta.


