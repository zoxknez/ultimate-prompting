## 0. Kako koristiti ovaj prompt

### 0.1 Obavezni ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, arhiva i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Tip aplikacije i UI stek | `[WIDGETS / QML / MESOVITO / WEBENGINE / NEPOZNATO]` |
| Poslovna svrha i kritični tokovi | `[TOKOVI / INVARIJANTE]` |
| Podržani OS i arhitekture | `[WINDOWS / MACOS / LINUX / X64 / ARM64 / DRUGO]` |
| Python, Qt, PySide6 i packaging ciljevi | `[VERZIJE / ABI / ALATI]` |
| Formati i kanali distribucije | `[INSTALLER / STORE / PORTABLE / ENTERPRISE / AUTO-UPDATE]` |
| Lokalna skladišta, fajlovi, cache i tajne | `[LOKACIJE / FORMATI / VLASNICI]` |
| Udaljeni servisi i mrežno poverenje | `[API-JI / PROXY-JI / SERTIFIKATI]` |
| Native biblioteke, uređaji i privilegovani helper-i | `[DLL / DYLIB / SO / UREDJAJI / SERVISI]` |
| Signing, notarizacija i update infrastruktura | `[KLJUCEVI / PROVAJDERI / FEED-OVI / KANALI]` |
| Ciljevi dostupnosti, startovanja, latencije i resursa | `[SLO / BUDZETI]` |
| Produkcioni pristup i ovlašćenje za izmene | `[READ / WRITE / ODOBRAVACI]` |
| Režim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / INCIDENT_MODE]` |

### 0.2 Politika za informacije koje nedostaju

1. Nastavi sa bezbednim otkrivanjem kada su ulazi nepotpuni; ne blokiraj ceo audit.
2. Zaključuj samo iz sadržaja repozitorijuma, lock fajlova, razrešenih okruženja, build izlaza, zapakovanih artefakata, potpisa, instaliranog stanja, runtime dokaza, telemetrije i autoritativne dokumentacije.
3. Označi nerazrešene pretpostavke kao `UNVERIFIED` i navedi tačan dokaz, platformu, credential, odobrenje, uređaj ili korisnički tok potreban za razrešenje.
4. Traži samo pristup, odobrenje, credential-e, poslovne odluke, hardver ili distributivne naloge koji materijalno blokiraju potvrdu ili bezbednu popravku.
5. Nikada ne tretiraj README, zeleni CI job, uspešno pokretanje iz source-a, nepotpisan paket ili smoke test na jednoj platformi kao dokaz produkcione ispravnosti.
6. Kada instalirani ili produkcioni dokaz nije dostupan, navedi plafon dokaza i ne izdaji bezuslovan production-ready zaključak.

