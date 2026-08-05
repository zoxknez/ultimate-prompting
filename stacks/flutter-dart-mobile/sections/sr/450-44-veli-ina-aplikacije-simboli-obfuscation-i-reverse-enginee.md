## 44. Veličina aplikacije, simboli, obfuscation i reverse engineering

Smanji veličinu i izloženost informacija bez žrtvovanja dijagnostike ili pretvaranja da klijent može čuvati tajne.

- Meri release veličinu po platformi, download veličinu, instaliranu veličinu, split veličinu, web transfer veličinu, native biblioteke, fontove, asset-e, lokalizaciju i duple resurse.
- Koristi size analizu i diff po izdanju; dodeli vlasništvo i budžet za značajan rast.
- Proveri tree shaking, deferred loading gde je prikladno, asset varijante, image formate, font subsetting, native stripping, isključenje debug artefakata i package-level doprinose.
- Ako se koristi Dart obfuscation, sačuvaj tačne symbol map-e po artefaktu i proveri crash deobfuscation i retention.
- Sačuvaj Android mapping/native simbole, Apple dSYM, Windows PDB, macOS/Linux simbole, web source map-e i native plugin simbole uz kontrolu pristupa.
- Ne tvrdi da obfuscation štiti API tajne, authorization logiku, encryption ključeve, poslovna pravila ili lične podatke.
- Pregledaj runtime stringove, logove, error poruke, manifest metapodatke, endpoint-e, feature flag-ove, test kredencijale, sertifikate i asset-e radi nenamernog otkrivanja.
- Testiraj upload simbola, dekodiranje crash-a, privatnost source map-a, retention, pristup, dostupnost tokom incidenta i artifact-to-symbol identitet.

