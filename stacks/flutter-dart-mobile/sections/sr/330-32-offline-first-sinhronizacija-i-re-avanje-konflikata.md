## 32. Offline-first, sinhronizacija i rešavanje konflikata

Offline ponašanje mora definisati autoritet, redosled, identitet i conflict semantiku.

- Dokumentuj koji read i write tokovi su dozvoljeni offline, njihovo obećanje korisniku, trajnost, istek, cancellation i uslove serverskog prihvatanja.
- Dodeli stabilne operation ID-jeve i idempotency key-eve; persistiraj queue stanje transakciono sa verzijom payload-a, actor-om, tenant-om, zavisnošću, retry brojem i statusom.
- Definiši redosled, zavisnost, compaction, deduplikaciju, retry, backoff, istek, poison operaciju, cancellation i ručnu intervenciju.
- Izaberi conflict politiku po entitetu i polju: server authority, client authority, version check, merge, append-only, CRDT ili eksplicitno korisničko rešavanje.
- Spreči zastarele offline operacije da deluju posle logout-a, promene uloge, tenant-a, brisanja, promene kvote, cene ili poslovnog pravila.
- Testiraj duge offline periode, clock skew, promenjen redosled operacija, duplirane operacije, parcijalnu sinhronizaciju, reset servera, promenu šeme, istek tokena i više uređaja.
- Obezbedi istinit UI za pending, synced, conflicted, failed, canceled, expired i rejected operacije.
- Meri starost queue-a, stopu konflikata, retry broj, poison stopu, potiskivanje duplikata, reconciliation lag i korisniku vidljiv gubitak podataka.

