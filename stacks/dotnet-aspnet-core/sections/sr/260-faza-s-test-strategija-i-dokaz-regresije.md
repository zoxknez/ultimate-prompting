## Faza S - Test Strategija I Dokaz Regresije

Inventarisi: unit, integration (stvarni provider gde je moguce - ne tretiraj EF InMemory kao dokaz relational ispravnosti), contract, security (authz, SSRF, CORS/antiforgery, upload, webhook replay), concurrency, migration, E2E, publish smoke, load gde je relevantno, AOT/trimming ako se koristi.

Svaka implementirana P0-P2 popravka zahteva test koji demonstrira staro neispravno i novo ispravno ponasanje. Ne markiraj test kao skipped da bi pipeline prosao. Ne iskljucuj analyzere bez analize.

