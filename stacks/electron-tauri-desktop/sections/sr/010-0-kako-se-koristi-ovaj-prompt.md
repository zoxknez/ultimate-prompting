## 0. Kako se koristi ovaj prompt

### 0.1 Obavezni ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, arhiva i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Framework i tip aplikacije | `[ELECTRON / TAURI / MESOVITO / NEPOZNATO]` |
| Poslovna svrha i kriticni tokovi | `[TOKOVI / INVARIJANTE]` |
| Podrzani operativni sistemi i arhitekture | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / DRUGO]` |
| Formati i kanali distribucije | `[INSTALLER / PRODAVNICA / ENTERPRISE / PORTABLE / AUTO-UPDATE]` |
| Identitet, licenciranje, placanja i privilegovane operacije | `[SISTEMI / VLASNICI]` |
| Lokalna skladista, fajlovi, cache i tajne | `[LOKACIJE / FORMATI / VLASNICI]` |
| Udaljeni servisi, origin-i i mrezno poverenje | `[API-JI / ORIGIN-I / PROXY-JI / SERTIFIKATI]` |
| Potpisivanje, notarizacija i update infrastruktura | `[KLJUCEVI / PROVAJDERI / FEED-OVI / KANALI]` |
| Ciljevi dostupnosti, pokretanja, latencije i resursa | `[SLO / BUDZETI]` |
| Privatnost, uskladjenost, rezidentnost i zadrzavanje podataka | `[PRAVILA / REGIONI]` |
| Poznati incidenti, defekti i planirane migracije | `[KONTEKST]` |
| Produkcioni pristup i ovlascenje za izmene | `[READ / WRITE / ODOBRAVACI]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Pravilo za nedostajuce informacije

1. Nastavi bezbedno otkrivanje kada su ulazi nepotpuni; ne blokiraj ceo audit.
2. Zakljucuj samo iz sadrzaja repozitorijuma, lock fajlova, razresenih dependency grafova, build izlaza, zapakovanih artefakata, potpisa, instaliranog stanja, runtime dokaza, telemetrije i autoritativne dokumentacije.
3. Oznaci nerazresene pretpostavke kao `UNVERIFIED` i navedi tacan dokaz, platformu, kredencijal, odobrenje ili hardver potreban za potvrdu.
4. Trazi samo pristup, odobrenje, kredencijale, poslovne odluke ili fizicke uredjaje koji materijalno blokiraju potvrdu ili bezbednu popravku.
5. Nikada ne tretiraj README, zeleni CI job, uspesno dev pokretanje, nepotpisan paket ili smoke test na jednoj platformi kao dokaz produkcione ispravnosti.
6. Kada instalirani ili produkcioni dokazi nisu dostupni, navedi plafon dokaza i ne izdaji bezuslovni production-ready zakljucak.

