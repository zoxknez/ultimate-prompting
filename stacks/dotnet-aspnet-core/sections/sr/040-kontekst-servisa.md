## Kontekst Servisa

| Polje | Vrednost |
| --- | --- |
| Servis | `[NAME]` |
| Namena | `[DESCRIPTION]` |
| Klijenti | `[WEB / MOBILE / DESKTOP / PARTNERS / PUBLIC]` |
| Arhitektura | `[MONOLITH / MODULAR MONOLITH / MICROSERVICE / WORKER / OTHER]` |
| Deployment | `[DOCKER / KUBERNETES / IIS / AZURE / VPS / SERVERLESS / OTHER]` |
| Runtime | `[TARGET FRAMEWORK / SDK / HOST OS]` |
| Podaci | `[SQL SERVER / POSTGRESQL / MYSQL / SQLITE / COSMOS / OTHER]` |
| Autentikacija | `[COOKIE / OIDC / JWT / API KEY / MTLS / OTHER]` |
| Kriticne operacije | `[PAYMENTS / INVENTORY / FILES / LICENSES / OTHER]` |
| Repozitorijum/arhiva | `[REPOZITORIJUM]` |
| Solution root | `[SOLUTION_ROOT]` |
| Ocekivano ponasanje | `[OCEKIVANO_PONASANJE]` |
| Poznati problemi | `[POZNATI_PROBLEMI]` |
| Workload | `[WORKLOAD]` |
| Hosting/OS | `[HOSTING / OS]` |
| Messaging/cache/storage | `[MESSAGING / CACHE / STORAGE]` |
| Identity/deployment/CI | `[IDENTITY_PROVIDER / DEPLOYMENT / CI_CD]` |
| Baseline/kompatibilnost | `[ZAHTEVANI_BASELINE / KOMPATIBILNOST]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |
| Regulatorni i dodatni zahtevi | `[REGULATORNI_ZAHTEVI / OGRANICENJA]` |

Kod, project fajlovi, lock fajlovi, runtime konfiguracija, izvrsene komande, ponasanje deployovanog artefakta i ogranicenja baze su dokazi. Dokumentacija i roadmap fajlovi su samo kontekst.

Ako podatak nije prosledjen, pokusaj da ga utvrdis iz solution-a, konfiguracije, CI i deployment artefakata; u suprotnom oznaci `NEPROVERENO`. Ne pretpostavljaj Azure, SQL Server, Windows hosting, stateless arhitekturu niti ASP.NET Core aplikaciju samo na osnovu C#/.NET prisustva.

