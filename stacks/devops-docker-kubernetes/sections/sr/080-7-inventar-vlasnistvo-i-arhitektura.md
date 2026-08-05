## 7. Inventar, vlasnistvo i arhitektura

**Cilj:** Izgradi potvrđenu mapu sistema i ukloni nepoznato vlasnistvo.

### 7.1 Obavezne provere

1. Otkrij sve repozitorijume, servise, job-ove, redove, baze, object store-ove, cache-eve, registre, klastere, namespace-ove, naloge, javne endpoint-e i third-party zavisnosti.
2. Mapiraj request, event, batch, administrativne, deployment, secret i recovery tokove podataka preko trust boundary-ja.
3. Identifikuj tier, kriticnost, klasifikaciju podataka, korisnicki uticaj, SLO, RPO, RTO, vlasnika, on-call rotaciju i runbook za svaku kriticnu komponentu.
4. Uporedi dijagrame i kataloge sa live DNS-om, cloud inventarom, cluster API-jima, registrima, CI sistemima i telemetrijom.
5. Identifikuj napustene, duplirane, shadow, unmanaged, end-of-life i internet-exposed resurse.
6. Dokumentuj deljene zavisnosti i korelisane failure domain-e, ukljucujuci identity, DNS, KMS, registry, CI, control plane i observability.

### 7.2 Minimalni dokazi

- Dijagram arhitekture i trust boundary-ja vezan za live dokaze.
- Masinski citljiv inventar resursa i vlasnistva.
- Lista nepoznatih, napustenih, deljenih i kriticnih zavisnosti.

### 7.3 Kriterijumi izlaza

1. Kriticni servisi imaju potvrđene vlasnike, zavisnosti, SLO, RPO, RTO i escalation putanje.
2. Live arhitektura se materijalno podudara sa dokumentovanom namerom ili je drift registrovan.
3. Nijedan internet-exposed ili privileged nepoznat resurs nije ostao bez trijaze.

