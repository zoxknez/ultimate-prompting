## Faza 5 - Next.js konfiguracija, build graph i izlaz

Auditiraj efektivnu Next.js konfiguraciju i emitovani route/runtime graph za tacnu verziju i cilj.

### Zahtevi audita

- Pregledaj next.config grane, plugin-e, compiler opcije, experimental flag-ove, output, basePath, assetPrefix, images, redirect-e, rewrite-e, header-e i cache podesavanja.
- Proveri Turbopack ili alternativno bundler ponasanje, loader/plugin kompatibilnost, source map-e, minifikaciju i tree shaking.
- Zabelezi static, dynamic, partially prerendered, edge, Node, client i handler odluke iz build izlaza.
- Detektuj ignorisane build greske, warning-as-success, type/lint bypass, nedostajucu env validaciju i route konflikte.
- Proveri output tracing, standalone pakovanje, serverExternalPackages, native module i runtime fajlove.
- Uporedi lokalni, CI, preview, staging i production build i objasni svaku razliku.

### Obavezni dokazi

- Efektivni next.config po klasi okruzenja.
- Build izlaz i inventar route/runtime manifest-a.
- Bundle i traced-file dokaz za kriticne rute.
- Lista upozorenja, suppression-a, experimental flag-ova i deployment grana.

### Obavezni failure i acceptance testovi

- Pokreni production artefakt samo sa dokumentovanim runtime fajlovima.
- Obori build na nedostajucoj ili malformed obaveznoj environment promenljivoj.
- Izvrsi svaku runtime klasu i detektuj nepodrzane Edge API-je.
- Proveri source-map upload i access control bez izlaganja source-a ili tajni.

