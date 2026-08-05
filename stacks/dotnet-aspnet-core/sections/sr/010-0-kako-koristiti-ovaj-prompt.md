## 0. Kako Koristiti Ovaj Prompt

### 0.1 Obavezni Ulazi

| Polje | Vrednost |
| --- | --- |
| Repozitorijum, solution i relevantne putanje | `[PUTANJE / URL-OVI]` |
| Poslovna namena i kriticni tokovi | `[TOKOVI / INVARIJANTE]` |
| Okruzenja i deployment jedinice | `[LOCAL / TEST / STAGE / PROD / DR]` |
| Hosting i operativni sistemi | `[IIS / KESTREL / CONTAINER / KUBERNETES / AZURE / DRUGO]` |
| Baze, brokeri, cache i object storage | `[SISTEMI / VLASNICI]` |
| Identity provider-i i trust boundary-ji | `[OIDC / COOKIE / JWT / MTLS / API KEY / DRUGO]` |
| Javni i interni ugovori | `[HTTP / GRPC / SIGNALR / EVENTI / FAJLOVI]` |
| Dostupnost, latencija, RPO i RTO ciljevi | `[SLO / RPO / RTO]` |
| Uskladjenost, privatnost i data residency | `[PRAVILA / REGIONI]` |
| Poznati incidenti, defekti i planirane migracije | `[KONTEKST]` |
| Production pristup i ovlascenje za izmene | `[READ / WRITE / ODOBRAVACI]` |
| Rezim rada | `[AUDIT_ONLY / AUDIT_AND_SAFE_FIX / FULL_IMPLEMENTATION / FIX_CONFIRMED_ISSUES / MIGRATION_AUDIT / INCIDENT_MODE]` |

### 0.2 Pravilo Za Nedostajuce Informacije

1. Nastavi bezbedno istrazivanje kada ulazi nisu potpuni; ne blokiraj ceo audit.
2. Zakljucuj samo iz repozitorijuma, project fajlova, razresenih buildova, runtime stanja, deployment artefakata, telemetrije, metadata baze i autoritativne dokumentacije.
3. Nerazresene pretpostavke oznaci kao `NEPROVERENO` i navedi tacan dokaz ili pristup potreban za njihovu proveru.
4. Trazi samo pristup, odobrenje, kredencijale ili poslovnu odluku koja stvarno blokira potvrdu ili bezbednu popravku.
5. Nikada ne tretiraj README, arhitektonski dijagram, zeleni pipeline, uspesan health odgovor ili generisani OpenAPI dokument kao dokaz potpune production ispravnosti.
6. Kada production dokaz nije dostupan, navedi granicu dokaza i ne izdaj bezuslovan production-ready zakljucak.

