## Rezimi Rada

Podrazumevani rezim: `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeno ponasanje |
| --- | --- |
| `AUDIT_ONLY` | Citaj, pregledaj i testiraj bez izmene source-a, lock fajlova, podataka, redova, credential-a ili infrastrukture. |
| `AUDIT_AND_SAFE_FIX` | Primeni niskorizicne potvrdjene popravke sa testovima; planiraj breaking, data, dependency i deployment izmene. |
| `FULL_IMPLEMENTATION` | Implementiraj u malim proverenim koracima; trazi eksplicitno odobrenje pre production migracije, deploy-a, queue replay-a ili rotacije tajni. |
| `FIX_CONFIRMED_ISSUES` | Menjaj samo nalaze podrzane reproduktivnim dokazom. |
| `SECURITY_AUDIT` | Prioritet su auth, tenancy, sesije, injection, fajlovi, serializacija, tajne, supply chain i administrativne povrsine. |
| `PERFORMANCE_AUDIT` | Meri web, jobove, SQL, GC, memoriju, pool-ove, redove, cache, realtime i deployment ponasanje u production-like rezimu. |
| `MIGRATION_AUDIT` | Audituj Ruby, Rails, Rack, Puma, Bundler, bazu, job backend, frontend defaults i mixed-version kompatibilnost. |
| `INCIDENT_AND_RECOVERY` | Prvo containment, sacuvaj dokaze, opozovi poverenje, vrati poznato dobro stanje, uskladi podatke i uradi hardening. |

