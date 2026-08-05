## Faza 20 - Upload, download, arhive, mediji, dokumenti i filesystem granice

### Cilj

Dokaži autorizaciju, parsing bezbednost, storage integritet, izolaciju i lifecycle za attacker-controlled fajlove i generisane artifact-e.

### Zahtevi audita

- Inventariši upload-e, direct-to-storage tokove, import-e, export-e, arhive, slike, video, audio, PDF, office dokumente, CSV, privremene fajlove i generisane download-e.
- Proveri autentikaciju, autorizaciju, tenant namespace, veličinu, broj, filename, ekstenziju, MIME, magic bytes, parser limite i quarantine pre korišćenja.
- Audituj traversal, symlink, race, overwrite, smeštanje executable-a, javno izlaganje, signed URL scope, response header-e, content sniffing i disposition.
- Testiraj zip slip, decompression bomb-e, nested arhive, malformed medije, parser ranjivosti, image metadata, macro sadržaj i formula injection.
- Proveri asinhrono scanning i processing stanje, duplicate callback-ove, timeout, worker crash, parcijalne fajlove, cleanup, retention, brisanje i legal hold.
- Audituj export autorizaciju u trenutku generisanja i download-a, snapshot konzistentnost, row limite, osetljiva polja, watermarking, expiry i audit trail.

### Obavezni dokazi

- Matrica file toka od ingress-a kroz scanning, processing, storage, delivery, retention i brisanje.
- Malicious-file, traversal, archive-bomb, parser-crash, duplicate-callback i unauthorized-download testovi.
- Dokaz cleanup-a, retention-a, brisanja, restore-a i legal hold-a.

### Kriterijumi prihvatanja

- Nepoverljivi fajlovi ne mogu da se izvrše, izađu iz svog namespace-a, iscrpe processing ili slučajno postanu javno dostupni.
- Svaki generisani ili skladišteni artifact ima eksplicitno authority, integrity, retention i recovery ponašanje.

