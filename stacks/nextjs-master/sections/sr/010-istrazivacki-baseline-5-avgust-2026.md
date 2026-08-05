## Istrazivacki baseline - 5. avgust 2026.

Ovo je datirana pocetna tacka. Pre svake lifecycle, migration, security ili compatibility odluke ponovo proveri primarne izvore, instalirane pakete, lockfile, platform image i pokrenuti proces.

| Komponenta | Baseline | Obavezna provera |
| --- | --- | --- |
| Next.js | 16.3.x je najnovija stabilna feature linija; 16.2.11 Active LTS i 15.5.21 Maintenance LTS posle bezbednosnog izdanja iz jula 2026. | Tacan patch, maintained linija, canary upotreba, router mode, platformska podrska i advisory-ji |
| React | 19.2.x je stabilan; React Compiler 1.0 je stabilan, ali opcion | Uskladjenost react/react-dom, RSC patch-evi, compiler konfiguracija i kompatibilnost biblioteka |
| TypeScript | 7.0 je stabilan; 6.0 ostaje transition i compatibility linija | Compiler koji koriste editor, CI, Next build, testovi, generatori i monorepo zadaci |
| Node.js | 24 LTS i 22 LTS su podrzani; 26 je Current | Build/runtime image, arhitektura, libc, native ABI i platformska podrska |
| Routing | Next.js 16 je preimenovao Middleware u Proxy | Stvarni fajl, matcher-i, semantika, runtime, rewrite, redirect, header i bypass putanje |
| Caching | Cache Components i use cache/private/remote su version-specific | Efektivni flag-ovi, cache kljucevi, scope, invalidacija, CDN ponasanje i izolacija privatnih podataka |

### Politika primarnih izvora

- Koristi zvanicnu Next.js, React, Node.js, TypeScript, hosting-platform, ORM, database, auth-provider i standards dokumentaciju.
- Zabelezi URL, datum pristupa, tacnu tvrdnju, izabranu verziju i da li je repository i runtime dokaz potvrdjuje.
- Ne zamenjuj zvanicne lifecycle, security ili migration smernice rezimeima, objavama na mrezama, snippet-ima ili popularnoscu paketa.
- Kada se izvori ne slazu, prikazi konflikt i zadrzi odluku uslovnom dok se tacna komponenta i runtime ne provere.

