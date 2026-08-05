## Faza 1 - Topologija sistema, ulazne tačke i trust boundary-ji

### Cilj

Mapiraj stvarnu application, process, data, identity i network topologiju pre procene kontrola.

### Zahtevi audita

- Popiši HTTP front controller-e, CLI komande, queue consumer-e, scheduler taskove, migracije, realtime servere i webhook receiver-e.
- Mapiraj CDN, WAF, load balancer, ingress, reverse proxy, web server, FPM socket, application proces, bazu, broker, cache i storage hop-ove.
- Identifikuj aktere, service identity-je, tenant-e, administratore, support korisnike, provajdere i machine-to-machine pozivaoce.
- Klasifikuj autoritativne store-ove, replike, cache, index-e, izvedene projekcije, fajlove i spoljne system-of-record sisteme.
- Označi trust prelaze za header-e, cookie-je, tokene, message metadata, tenant identifikatore, imena fajlova, URL-ove, serialized payload-e i environment promenljive.
- Dodeli ownership i escalation putanje za svaki executable, data store, integraciju, tajnu i recovery proceduru.

### Obavezni dokazi

- Dijagram arhitekture i trust boundary-ja povezan sa stvarnom konfiguracijom i deployment dokazom.
- Inventar ulaznih tačaka i vlasnika sa runtime-om, identitetom, pristupom podacima i side effect-ima.
- Mapa kritičnih putanja i zavisnosti koja uključuje degraded i failure putanje.

### Kriterijumi prihvatanja

- Nijedna spolja dostupna ili privilegovana ulazna tačka nije ostala nemapirana.
- Svaka kritična invarijanta ima autoritativnog vlasnika i enforcement sloj.

