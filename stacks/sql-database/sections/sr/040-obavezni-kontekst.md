## Obavezni kontekst

| Polje | Vrednost |
| --- | --- |
| Sistem i poslovna svrha | `[NAZIV / SVRHA]` |
| Repozitorijum i commit | `[URL / PUTANJA / SHA]` |
| Engine, edition i patch | `[...]` |
| Hosting i regioni | `[...]` |
| Aplikacije, driver-i i ORM | `[...]` |
| Kriticne invarijante | `[NOVAC / ZALIHE / PRISTUP / NARUDZBINE / ...]` |
| Kolicina podataka i rast | `[...]` |
| SLO, RPO i RTO | `[...]` |
| Regulatorni i privacy scope | `[...]` |
| Audit rezim | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / PERFORMANCE_AUDIT / MIGRATION_AUDIT / INCIDENT_AND_RECOVERY]` |

Ako kontekst nedostaje, izvedi ga iz source-a, migracija, runtime metadata-e, catalog view-ova, monitoringa i deployment konfiguracije. Nerazresene stavke oznaci kao `UNVERIFIED`; ne nagadjaj.

