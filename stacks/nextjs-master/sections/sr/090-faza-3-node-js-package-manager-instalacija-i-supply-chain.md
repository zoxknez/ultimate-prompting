## Faza 3 - Node.js, package manager, instalacija i supply chain

Auditiraj izvrsnu dependency i installation putanju, a ne samo package.json deklaracije.

### Zahtevi audita

- Utvrdi stvarni Node binary, release liniju, arhitekturu, libc, OpenSSL/FIPS mode i native ABI lokalno, u CI-ju, preview-u i produkciji.
- Proveri vlasnika lockfile-a, verziju package manager-a, Corepack politiku, frozen install, workspace resolution, peer-e i hoisting.
- Pregledaj lifecycle skripte, binary download-e, generatore, patch-eve, Git/path zavisnosti i registry config.
- Detektuj dependency confusion, typosquatting, kompromitovane maintainere, neodrzavane pakete, duplikate i reachable ranjivosti.
- Proveri scope registry tokena, provenance, cache trust, offline politiku i odobrene advisory suppression-e.
- Tretiraj native addon-e, WASM, image procesore, database driver-e i browser binary-je kao platformski specificne ulaze.

### Obavezni dokazi

- Dokaz izvrsenih Node i package-manager verzija.
- Resolved dependency graph, advisory izvestaj, reachability obrazlozenje i suppression-i.
- Inventar lifecycle skripti i build-time mreznog pristupa.
- SBOM vezan za release ili ekvivalentan dependency inventar.

### Obavezni failure i acceptance testovi

- Frozen instalacija mora pasti na package.json i lockfile drift-u.
- Izgradi bez mreze nakon pripreme zavisnosti ili dokumentuj svaki izuzetak.
- Izgradi podrzane arhitekture native zavisnosti.
- Dokazi da nepoverljivi pull request-ovi ne mogu pristupiti release tokenima, produkcionim tajnama ili privilegovanim cache-evima.

