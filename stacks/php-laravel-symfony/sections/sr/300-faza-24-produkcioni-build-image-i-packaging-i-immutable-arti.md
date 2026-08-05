## Faza 24 - Produkcioni build, image-i, packaging i immutable artifact-i

### Cilj

Dokaži da pregledani source proizvodi jedan reproduktivan, minimalan, immutable, identifikovan i pokretljiv produkcioni artifact.

### Zahtevi audita

- Build-uj iz clean checkout-a sa pinovanim PHP-om, Composer-om, ekstenzijama, OS paketima, frontend toolchain-om i generation koracima.
- Instaliraj production zavisnosti uz sprovođenje lockfile-a, kontrolisane skripte i plugin-e, optimizovan autoloading i bez skrivenih development paketa.
- Generiši i proveri cache-eve, kompajlirane container-e, optimizovane rute, asset-e, prevode, proxy-je, metadata i frontend bundle-ove u kontrolisanoj fazi.
- Audituj container base image, FPM i web server konfiguraciju, non-root izvršavanje, filesystem permission-e, writable putanje, capability-je, health i signal handling.
- Ugradi ili izloži release identitet, dependency inventar, build metadata, schema kompatibilnost i artifact digest bez curenja tajni.
- Skeniraj, potpiši, attest-uj i sačuvaj tačan artifact; deploy-uj isti digest kroz okruženja bez rebuild-a.

### Obavezni dokazi

- Clean build transcript, lockfile verifikacija, artifact digest, SBOM, potpis i provenance.
- Inventar artifact-a koji dokazuje očekivani kod, zavisnosti, ekstenzije, config, cache-eve i odsustvo development alata ili tajni.
- Smoke i critical-flow rezultati iz packaged artifact-a, ne iz source checkout-a.

### Kriterijumi prihvatanja

- Jedan immutable digest je traceable do source-a, toolchain-a, zavisnosti, testova, deployment-a, telemetry-ja i rollback-a.
- Produkcija ne zavisi od mutable source mount-ova, runtime instalacije zavisnosti ili manuelnog generisanja cache-a.

