## Faza W - Cache, Sesija, Rate Limiting I Distribuirana Koordinacija

- Popisi Redis, Valkey, Memcached, Solid Cache, database cache, lokalnu memoriju i CDN cache-eve.
- Ukljuci tenant, user, role, locale, currency, permission, schema i release dimenzije u cache kljuceve gde je potrebno.
- Testiraj stampede, cold cache, delimicnu invalidaciju, stale autorizaciju, mismatch verzije serializacije i backend outage.
- Proveri session konzistentnost i revocation kroz replike, regione, rotaciju kljuceva i cache failover.
- Audituj rate-limit identitet, proxy trust, tenant fairness, distribuirane counter-e, fail-open ili fail-closed ponasanje i bypass-e.
- Koristi distributed lock samo sa expiry-jem, proverom vlasnistva i fencing-om gde stale holder moze napraviti stetu.

