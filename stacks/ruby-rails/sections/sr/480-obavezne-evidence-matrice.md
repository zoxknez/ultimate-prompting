## Obavezne Evidence Matrice

### M1 - Source, Toolchain I Runtime Identitet

| Obavezna kolona | Dokaz |
| --- | --- |
| commit | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| Ruby engine i patch | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| Bundler i lock digest | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| artifact digest | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| uloga procesa | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| schema i release marker | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M2 - Topologija Procesa I Kapaciteta

| Obavezna kolona | Dokaz |
| --- | --- |
| web worker-i | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| thread-ovi | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| job worker-i | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| scheduler | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| Cable | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| database i cache konekcije | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M3 - Endpoint Autorizacija

| Obavezna kolona | Dokaz |
| --- | --- |
| ruta | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| akter | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| tenant | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| resurs | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| dozvoljena akcija | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| negativni slucaj | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M4 - Poslovne Invarijante

| Obavezna kolona | Dokaz |
| --- | --- |
| invarijanta | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| application kontrola | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| database kontrola | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| concurrency test | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| reconciliation | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| vlasnik | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M5 - Transakcije I Side Effect-i

| Obavezna kolona | Dokaz |
| --- | --- |
| tok | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| transaction manager | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| isolation | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| lock | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| spoljni efekat | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| crash recovery | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M6 - Jobovi I Scheduler-i

| Obavezna kolona | Dokaz |
| --- | --- |
| adapter | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| semantika isporuke | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| retry | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| idempotency | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| mixed-version | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| operator recovery | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M7 - Data I Migration Kompatibilnost

| Obavezna kolona | Dokaz |
| --- | --- |
| schema korak | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| stari kod | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| novi kod | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| backfill | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| cutover | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| rollback ili forward repair | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M8 - Security I Granice Tajni

| Obavezna kolona | Dokaz |
| --- | --- |
| asset | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| vlasnik | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| storage | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| rotacija | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| opoziv | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| incident dokaz | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M9 - Spoljne Zavisnosti

| Obavezna kolona | Dokaz |
| --- | --- |
| zavisnost | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| timeout budget | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| retry | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| circuit ili bulkhead | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| degraded mode | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| reconciliation | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M10 - Performanse I Kapacitet

| Obavezna kolona | Dokaz |
| --- | --- |
| workload | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| SLO | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| izmeren limit | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| bottleneck | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| headroom | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| scale ili shed akcija | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M11 - Release I Rollback

| Obavezna kolona | Dokaz |
| --- | --- |
| artefakt | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| canary | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| guardrail | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| abort prag | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| rollback koraci | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| verifikacija | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

### M12 - Backup, Restore I DR

| Obavezna kolona | Dokaz |
| --- | --- |
| skup podataka | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| backup dokaz | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| restore dokaz | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| RPO | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| RTO | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |
| reconciliation | `[VREDNOST / LINK / KOMANDA / REZULTAT]` |

