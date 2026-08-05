# Revizioni Izvestaj 04 - .NET / C# / ASP.NET Core / EF Core

## Status

- Paket: zavrsen
- Datum baseline-a: 2026-08-05
- Nova verzija: 2.0.0 production-candidate
- Jezici: engleski i srpski

## Glavni Problemi Prethodne Verzije

1. Prompt je bio kvalitetan i vec znatno siri od obicne checklist-e, ali nije imao standardizovan YAML metadata ugovor kao prethodno unapredjeni paketi.
2. Nije dovoljno strogo dokazivao source-to-runtime identitet izmedju commit-a, SDK-a, publish profila, image/package artefakta, deployment revision-a i stvarnog procesa.
3. Nedostajala je dovoljno detaljna kontrola MSBuild evaluacije, generated koda, source generator-a, plugin trust-a i dinamickog ucitavanja.
4. Nedovoljno su razradjeni serialization ugovori, globalizacija, native interop, Blazor circuit-i, proxy granice, output cache, distributed coordination i forensic readiness.
5. Test strategija nije imala obaveznu sveobuhvatnu acceptance matricu za duplicate, replay, cross-tenant, rollover, overload, shutdown, rollout i recovery scenarije.
6. Production readiness nije dovoljno eksplicitno ogranicen najslabijim neproverenim kriticnim slojem.

## Najvaznija Unapredjenja

- dodat kompletan usage contract, required inputs i pravilo za nedostajuce informacije;
- uveden `INCIDENT_MODE`;
- uvedena hijerarhija dokaza i evidence ceiling;
- dodat source-to-runtime identity chain i artifact provenance;
- detaljno prosireni SDK/TFM/C# compatibility, MSBuild, NuGet trust i generated code;
- dodate poslovne invarijante, state machine, serialization i contract evolution;
- prosireni async/backpressure, DI ownership, feature flags i kill switch;
- detaljno obradjeni Kestrel/IIS/YARP, middleware, OpenAPI, Identity, Blazor i browser security;
- prosireni cryptography, injection, outbound HTTP/DNS, cache/session/distributed lock;
- detaljno obradjeni EF provider behavior, transactions, outbox, migrations i zero-downtime backfill;
- prosireni messaging, webhook, hosted services, SignalR/SSE/gRPC, files i object storage;
- dodati OpenTelemetry privacy, CLR/GC/capacity, publish/trimming/AOT i hosting modeli;
- prosireni CI/CD, artifact promotion, rollout, rollback, DR, incident i migration overlay;
- dodato 12 obaveznih evidence matrica i 12 grupa acceptance scenarija.

## Aktuelni Baseline

- .NET 10 LTS, patch 10.0.10 na datum baseline-a, EOL 2028-11-14;
- .NET 8 LTS i .NET 9 STS u maintenance fazi, EOL 2026-11-10;
- C# 14 stable uz .NET 10, C# 15 preview na datum baseline-a;
- EF Core 10 LTS, EOL 2028-11-10;
- `NuGetAuditMode=all` po default-u za `net10.0+`;
- production migracije kroz pregledane SQL skripte, migration bundle ili kontrolisan job;
- `Microsoft.Extensions.Http.Polly` deprecated u korist aktuelnog resilience stack-a;
- Data Protection key ring zahteva proveru persistence-a, zastite, deljenja, backup-a i recovery-ja.

## Rezultat Kontrole

- EN/SR duzina: 927 / 927 linija;
- EN/SR naslovi: 89 / 89;
- line-shape odstupanja: 0;
- YAML frontmatter: validan;
- JSON baseline manifest: validan;
- Markdown code fence blokovi: balansirani;
- baseline hardcode scan: prosao;
- en dash, em dash i non-breaking hyphen u srpskom promptu: 0;
- repository parity checker: .NET par prolazi; preostali ocekivani problemi su samo neobradjeni Java/Spring i Python/PySide6 parovi.

