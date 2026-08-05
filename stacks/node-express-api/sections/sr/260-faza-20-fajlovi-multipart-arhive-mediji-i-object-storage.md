## Faza 20 - Fajlovi, Multipart, Arhive, Mediji I Object Storage

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Definisi count, field, filename, path, size, total size, duration, dimension, archive-entry i decompression limite.
- Stream-uj upload i download gde je odgovarajuce i dokazi backpressure, abort, cleanup i partial-file ponasanje.
- Validiraj magic byte-ove, parser ponasanje, extension, MIME, encoding, archive putanje, symlink-e i nested sadrzaj.
- Spreci path traversal, zip slip, decompression bomb, parser bomb, image bomb, command injection i nebezbednu upotrebu temp fajlova.
- Koristi private storage po default-u i primeni tenant, owner, autorizaciju, expiry i disposition na svakom download-u.
- Proveri signed-URL scope, metod, objekat, expiry, header-e, revocation pretpostavke, CDN ponasanje, retention i orphan cleanup.

### Obavezni Dokazi

- Proizvedi i sacuvaj file-flow i storage-authorization matricu.
- Proizvedi i sacuvaj inventar parser-a, native alata i limita.
- Proizvedi i sacuvaj retention, cleanup i restore dokaz.

### Obavezni Failure I Acceptance Testovi

- Dokazi da archive traversal i decompression bomb-e su blokirani.
- Dokazi da prekinut upload ne ostavlja neautorizovan orphan.
- Dokazi da signed URL ne moze da predje tenant, object ili method scope.

