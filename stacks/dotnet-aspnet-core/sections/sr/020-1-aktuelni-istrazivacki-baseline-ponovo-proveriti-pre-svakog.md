## 1. Aktuelni Istrazivacki Baseline - Ponovo Proveriti Pre Svakog Audita

Ovaj baseline je polaziste, ne zamena za proveru pri svakom izvrsavanju. Pre preporuke ili izmene proveri aktuelne Microsoft izvore i stvarni projekat.

| Komponenta | Potvrdjeno stanje na 4. avgust 2026. | Obavezna provera pri auditu |
| --- | --- | --- |
| .NET 10 | Aktuelna production LTS linija; latest patch na support stranici je 10.0.10 (objavljen 14. jula 2026.); podrzan do 14. novembra 2028. | `dotnet --info`, `global.json`, TFM, production runtime/image i patch policy. |
| Starije linije | .NET 8 LTS i .NET 9 STS su u maintenance periodu; oba imaju EOL 10. novembra 2026. Nisu novi dugorocni baseline bez jasnog razloga. | Stvarni lifecycle, OS support i plan upgrade-a. |
| C# | C# 14 je stabilno izdanje povezano sa .NET 10. Jezik noviji od verzije povezane sa target frameworkom nije podrzan. | `LangVersion`, SDK, CI/IDE/generator/analyzer i TFM kompatibilnost. |
| Preview | .NET 11 i C# 15 su preview tehnologije na datum baseline-a | `allowPrerelease`, preview SDK/paketi i eksplicitno production odobrenje. |
| EF Core | EF Core 10 je LTS, zahteva .NET 10 SDK/runtime i podrzan je do 10. novembra 2028. (Napomena: .NET 10 runtime support traje do 14. novembra 2028. - datumi nisu identicni.) Migracije sa EF 9 na 10 zahtevaju pregled behavioral i source-breaking promena. | EF runtime/tools/provider verzije, breaking katalog i provider kompatibilnost. |
| Breaking changes | Upgrade nije samo promena `TargetFramework`; postoji katalog binarno, source i behavior nekompatibilnih promena. | Compatibility katalog, release notes i test suite za pogodjene tokove. |
| NuGet audit | Za `net10.0` NuGet Audit podrazumevano proverava direktne i tranzitivne pakete (`NuGetAuditMode=all`). Podrzani su repository-level audit, package source mapping, lock fajlovi i locked restore. | Effective NuGet/MSBuild konfiguraciju, audit source, suppression i resolved graf. |
| Migracije | Microsoft preporucuje pregledane SQL skripte, migration bundle ili kontrolisan migration job; automatski startup `Database.Migrate()` nosi operativni rizik. | Provider, SQL, lock/duration, rollout, backup/PITR i recovery. |
| Data Protection | Key ring mora biti perzistiran, zasticen i dostupan svim replikama; koristi se za cookies, antiforgery i zasticeni payload. | Storage, encryption-at-rest, application discriminator, permissions, rotation, backup i DR. |
| Resilience | Koristi `Microsoft.Extensions.Resilience` i `Microsoft.Extensions.Http.Resilience`; `Microsoft.Extensions.Http.Polly` je deprecated. | Pipeline, timeout/retry granice, telemetry, idempotency i upgrade put. |

Napomena: tvrdnja da je patch izdat 10. novembra 2026. nije vremenski moguca na datum ovog baseline-a; ne koristi je kao cinjenicu. Pri stvarnom auditu uvek koristi aktuelni release/support zapis.

