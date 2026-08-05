## 17. Konfiguracija, tajne, KMS i PKI

**Cilj:** Drzi konfiguraciju namernom, a tajne kratkotrajnim, ogranicenim, sifrovanim i oporavljivim.

### 17.1 Obavezne provere

1. Popisi izvore konfiguracije i tajni, putanje replikacije, environment overlay-e, default vrednosti, vlasnike, potrosace, refresh ponasanje i klasifikaciju podataka.
2. Detektuj tajne u Git istoriji, image-ima, manifestima, Helm values, Terraform state-u, planovima, CI promenljivama, cache-u, logovima, command line-u, anotacijama, support bundle-u i telemetriji.
3. Preferiraj spoljne secret manager-e, workload identity, dinamicke kredencijale, envelope encryption i kontrolisanu isporuku umesto staticnih Kubernetes Secret-a.
4. Proveri vlasnistvo KMS kljuceva, policy, rotaciju, zastitu od brisanja, regionalnu dostupnost, grant opseg, audit logove, alias-e i razdvajanje duznosti.
5. Proveri audience tajne, least privilege, TTL, mount dozvole, memory ili file izlozenost, refresh, application reload, preklapanje rotacije, opoziv i ponasanje pri otkazu.
6. Audituj PKI hijerarhiju, zastitu CA, izdavanje, odobrenje, SAN policy, algoritme kljuceva, obnovu, distribuciju poverenja, opoziv, hitnu zamenu i istek.
7. Testiraj rotaciju i opoziv najmanje jednog reprezentativnog neprodukcijskog kredencijala bez otkrivanja vrednosti.

### 17.2 Minimalni dokazi

- Mapa toka tajni i KMS ili PKI vlasnistva.
- Redigovan scan izlozenosti tajni i registar remedijacije.
- Dokaz testa rotacije, reload-a, preklapanja, opoziva i outage-a.

### 17.3 Kriterijumi izlaza

1. Nijedna potvrđena plaintext ili produkciona tajna bez vlasnika nije ostala u izvoru, artefaktima, logovima ili unmanaged storage-u.
2. Kriticni kredencijali se rotiraju i opozivaju bez nekontrolisanog outage-a ili zastarelog pristupa.
3. Pretpostavke KMS i PKI otkaza, brisanja, isteka i oporavka su razumljive i imaju vlasnika.

