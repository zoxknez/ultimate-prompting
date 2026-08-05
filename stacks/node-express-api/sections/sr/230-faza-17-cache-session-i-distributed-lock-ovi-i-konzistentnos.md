## Faza 17 - Cache, Session-i, Distributed Lock-ovi I Konzistentnost

Audituj efektivno ponasanje u source-u, resolved konfiguraciji, izgradjenom artefaktu, ciljnom deployment-u i failure putanjama. Eksplicitno oznaci nedostupan dokaz umesto popunjavanja praznina pretpostavkama.

### Audit Zahtevi

- Inventarisi local, shared, response, object, session, authorization i CDN cache-eve.
- Definisi kljuceve sa tenant, user, role, locale, permission, version i feature dimenzijama gde je potrebno.
- Klasifikuj podatke kao public, tenant-shared, user-private, request-private ili zabranjene za cache.
- Dokumentuj TTL, stale tolerance, redosled invalidacije, outage ponasanje i stampede zastitu.
- Za distributed lock-ove definisi owner-a, lease, renewal, expiry, fencing token, clock pretpostavke i side-effect guard.
- Proveri session i authorization invalidaciju posle logout-a, promene tenant-a, promene prava i revocation-a kredencijala.

### Obavezni Dokazi

- Proizvedi i sacuvaj cache-classification i key matricu.
- Proizvedi i sacuvaj invalidation, outage i stampede tabelu.
- Proizvedi i sacuvaj lock, lease i fencing protocol.

### Obavezni Failure I Acceptance Testovi

- Dokazi da cross-tenant cache read nije moguc.
- Dokazi da stale prava ne mogu da sacuvaju opozvan pristup.
- Dokazi da istekli lock holder ne moze da commit-uje zasticeni side effect.

