## Faza 4 - TypeScript, JavaScript, ESM, CJS I Build Semantika

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi svaki tsconfig, project reference, target, lib, module, moduleResolution, strictness override i path alias.
- Dokazi koji compiler ili transpiler obradjuje production kod, testove, worker-e, migracije, skripte i generisane source-e.
- Detektuj transpile-only, noCheck, skipLibCheck, stale deklaracije, decorator i source-map rizike.
- Audituj ESM i CJS granice, extension resolution, exports, conditional exports, dynamic import, require hook-ove i dual-package hazard-e.
- Proveri da build output sadrzi nameravane fajlove i nema nenamernih tajni, fixture-a, source-a ili test podataka.
- Tretiraj tipove samo kao developer dokaz; nezavisno validiraj sav runtime input i eksterni output.

### Obavezni Dokazi

- Proizvedi i sacuvaj compiler, transpiler i module-resolution matricu.
- Proizvedi i sacuvaj generated-code i artifact-content dokaz.
- Proizvedi i sacuvaj rezultate kompatibilnosti old i new klijenata i deployment-a.

### Obavezni Failure I Acceptance Testovi

- Dokazi da production build izvrsava nameravane type provere.
- Dokazi da ESM i CJS entrypoint-i se ucitavaju u ciljnom runtime-u.
- Dokazi da runtime validacija odbija podatke koji samo izgledaju type-correct.

