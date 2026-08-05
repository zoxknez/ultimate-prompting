## Faza 2 - Runtime, Toolchain, Artefakt I Identitet Procesa

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Odredi stvarni Node binary, verziju, release liniju, arhitekturu, libc, OpenSSL, ICU, V8 i native-module ABI.
- Uporedi local, editor, CI, test, build, container, serverless, migration, worker i production runtime-e.
- Proveri engines, packageManager, Corepack politiku, version fajlove, Docker base image, platform runtime i process-manager konfiguraciju.
- Dokazi koji commit i dependency graph su proizveli svaki artefakt i koji digest je proizveo svaku deployment reviziju.
- Korelisi build ID, image digest, deployment ID, config reviziju, schema verziju i pokrenuti PID ili function reviziju.
- Pregledaj native addon-e, prebuilt binary-je, WASM i preuzete alate radi platform i ABI kompatibilnosti.

### Obavezni Dokazi

- Proizvedi i sacuvaj runtime i ABI matricu.
- Proizvedi i sacuvaj artifact provenance lanac.
- Proizvedi i sacuvaj deployment-to-process korelacioni dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da CI i produkcija prijavljuju nameravani runtime.
- Dokazi da native modul pogresne arhitekture otkazuje pre traffic-a.
- Dokazi da pokrenuti proces se moze povezati sa immutable artefaktom.

