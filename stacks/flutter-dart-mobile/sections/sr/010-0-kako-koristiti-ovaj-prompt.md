## 0. Kako koristiti ovaj prompt

### 0.1 Obavezni ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, arhiva i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Poslovna svrha i kritični tokovi | `[TOKOVI / INVARIJANTE]` |
| Tip Flutter aplikacije | `[MOBILE / WEB / DESKTOP / ADD-TO-APP / EMBEDDED / MIXED]` |
| Podržane platforme i arhitekture | `[ANDROID / IOS / IPADOS / WEB / WINDOWS / MACOS / LINUX / ARHITEKTURE]` |
| Minimalne i ciljne verzije platformi | `[API / OS / BROWSER MATRICA]` |
| Identitet, plaćanja, licenciranje i privilegovane operacije | `[SISTEMI / VLASNICI]` |
| Backend API-ji, realtime, push i eksterni servisi | `[SERVISI / UGOVORI]` |
| Lokalna skladišta, fajlovi, keš i osetljivi podaci | `[LOKACIJE / FORMATI / VLASNICI]` |
| Flavor-i, okruženja, tenant-i i release kanali | `[MATRICA]` |
| Potpisivanje, store-ovi, installer-i i update infrastruktura | `[KLJUČEVI / PROVAJDERI / KANALI]` |
| Ciljevi dostupnosti, startovanja, latencije, memorije i veličine | `[SLO / BUDŽETI]` |
| Privatnost, accessibility, usklađenost i rezidentnost podataka | `[PRAVILA / REGIONI]` |
| Poznati incidenti, greške, dug i planirane migracije | `[KONTEKST]` |
| Production pristup i ovlašćenje za izmene | `[READ / WRITE / ODOBRAVAOCI]` |
| Režim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Pravilo za nedostajuće informacije

1. Nastavi bezbedno otkrivanje kada ulazi nisu potpuni; ne blokiraj ceo audit.
2. Zaključuj samo iz sadržaja repozitorijuma, lock fajlova, razrešenih dependency grafova, generisanog izlaza, build artefakata, instaliranog stanja, runtime dokaza, telemetrije i autoritativne dokumentacije.
3. Označi nerešene pretpostavke kao `UNVERIFIED` i navedi tačan dokaz, platformu, kredencijal, odobrenje, hardver, store pristup ili okruženje potrebno za razrešenje.
4. Traži samo pristup, odobrenje, kredencijale, poslovne odluke ili fizičke uređaje koji stvarno blokiraju potvrdu ili bezbednu popravku.
5. Nikada ne tretiraj README, uspešan analyzer, debug pokretanje, test samo na emulatoru, nepotpisan artefakt ili smoke test jedne platforme kao dokaz production ispravnosti.
6. Kada release, store, device, browser ili production dokazi nisu dostupni, navedi granicu dokaza i ne izdaji bezuslovnu production-ready ocenu.

