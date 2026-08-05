## Rezim rada

Podrazumevani rezim: `AUDIT_AND_SAFE_FIX`.

| Rezim | Dozvoljeno ponasanje |
| --- | --- |
| `AUDIT_ONLY` | Read-only inspekcija i ponovljivi testovi; bez izmene schema-e, podataka, konfiguracije, rola ili topologije. |
| `AUDIT_AND_SAFE_FIX` | Primeni niskorizicne potvrdjene popravke u kontrolisanom neprodukcionom scope-u; planiraj rizican DDL i produkcione akcije. |
| `FULL_IMPLEMENTATION` | Implementiraj u malim proverenim koracima nakon backup, lock, capacity, rollout i recovery gate-ova. |
| `PERFORMANCE_AUDIT` | Izmeri workload, planove, wait-ove, lock-ove, I/O, cache, pool, replike i kapacitet bez spekulativnog tuninga. |
| `MIGRATION_AUDIT` | Audituj engine upgrade, schema promenu, backfill, kompatibilnost, cutover, rollback i forward repair. |
| `INCIDENT_AND_RECOVERY` | Prvo obuzdaj incident, sacuvaj dokaze, zaustavi nebezbedne write-ove, vrati known-good stanje, usaglasi podatke i uradi hardening. |

