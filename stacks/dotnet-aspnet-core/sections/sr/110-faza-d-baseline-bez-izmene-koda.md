## Faza D - Baseline Bez Izmene Koda

Uspostavi baseline pre menjanja koda:

1. `dotnet restore` (i `--locked-mode` kada se ocekuje);
2. Debug i Release `dotnet build`;
3. analyzere / `dotnet format` gde je konfigurisano;
4. `dotnet test` (unit, integration, security, contract);
5. `dotnet publish --configuration Release` (i RID/self-contained profil ako se stvarno deployuje);
6. production-like startup sa bezbednom lokalnom/test konfiguracijom;
7. status migracija, health/readiness, graceful shutdown gde je podrzano.

Za svaki neuspeh sacuvaj prvu relevantnu gresku i trazi osnovni uzrok: SDK mismatch, restore, tajna, port, baza, test-order ili lokalno okruzenje. Startup ne sme slati email, koristiti production queue/payment niti menjati produkcione podatke.

