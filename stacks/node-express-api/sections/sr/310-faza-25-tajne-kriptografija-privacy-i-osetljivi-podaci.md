## Faza 25 - Tajne, Kriptografija, Privacy I Osetljivi Podaci

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi kredencijale, token-e, kljuceve, sertifikate, cookie-je, connection string-ove, signing material i osetljivu konfiguraciju po owner-u i scope-u.
- Spreci tajne u source-u, lockfile-u, image layer-ima, build logovima, test fixture-ima, source map-ama, dijagnostici, telemetry-ju i greskama.
- Koristi managed secret storage, short-lived identitet, least privilege, scoped injection, rotaciju, revocation i access audit.
- Koristi etablirane cryptographic biblioteke i dokumentuj algoritam, mode, key size, nonce, encoding i rotaciju.
- Klasifikuj licne i osetljive podatke i definisi collection, purpose, minimization, retention, export, deletion i legal hold.
- Redactuj osetljive vrednosti konzistentno kroz logove, trace-ove, metric-e, event-e, queue-ove, cache-eve, dijagnostiku i support alate.

### Obavezni Dokazi

- Proizvedi i sacuvaj inventar tajni, kljuceva i sertifikata.
- Proizvedi i sacuvaj data-classification i retention mapu.
- Proizvedi i sacuvaj rotation, revocation, deletion i restore dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da stari i novi kljucevi koegzistiraju samo u nameravanom periodu.
- Dokazi da opozvani kredencijali gube pristup u definisanom cilju.
- Dokazi da telemetry i dijagnostika ne sadrze raw tajne.

