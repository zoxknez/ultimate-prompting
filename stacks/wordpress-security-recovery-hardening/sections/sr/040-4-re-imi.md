## 4. Režimi

Izaberi režim iz prosleđenog konteksta. Ako režim nije naveden, koristi `CONTAIN_AND_RECOVER`.

### AUDIT_ONLY

- Obavi pregled bezbedan po dokaze.
- Ne menjaj fajlove, database zapise, korisnike, DNS, CDN, kredencijale ili konfiguraciju.
- Navedi tačne preporučene akcije i sledeće korake rangirane po riziku.

### CONTAIN_AND_RECOVER

- Obavi čuvanje dokaza, containment, eradication, recovery, rotaciju kredencijala, hardening i verifikaciju.
- Pre svake destruktivne akcije ili akcije koja utiče na dostupnost navedi uticaj i rollback putanju.

### HARDEN_ONLY

- Potvrdi da u pregledanom scope-u nema poznatih aktivnih indikatora kompromitacije.
- Poboljšaj konfiguraciju, kontrolu pristupa, patching, backup, monitoring i operativne kontrole.
- Ako se pojave indikatori kompromitacije, zaustavi hardening-only rad i pređi na incident-response trijažu.

### FORENSICS_ONLY

- Sačuvaj i analiziraj dokaze bez remediation-a.
- Održavaj strogi chain-of-custody i napravi reproduktivnu vremensku liniju.

