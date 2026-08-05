## 15. Identitet, RBAC i workload identity

**Cilj:** Primeni least privilege na ljude, masine, workload-e i hitni pristup.

### 15.1 Obavezne provere

1. Mapiraj ljudski SSO, MFA, grupe, cloud IAM, Kubernetes autentikaciju, service account-e, workload identity, CI identitete, automatizaciju i break-glass putanje.
2. Popisi efektivni RBAC, ukljucujuci agregaciju, impersonation, bind, escalate, citanje tokena i tajni, pods exec ili attach, port-forward, nodes proxy, CSR approval, webhook i CRD kontrolu.
3. Odbaci siroke wildcard-e, rutinski cluster-admin, deljene identitete, dugotrajne service-account tokene, ugrađene kubeconfig fajlove i reuse identiteta kroz okruzenja.
4. Koristi kratkotrajne federisane kredencijale i audience-bound workload identity gde je podrzano. Proveri issuer, subject, audience, claim-ove, trust policy i trajanje sesije.
5. Razdvoji odgovornosti citanja, deployment-a, promocije, odobrenja, secret-admin-a, cluster-admin-a, billing-a i break-glass-a.
6. Testiraj pristup pomocu impersonation-a ili ekvivalentne bezbedne metode, ukljucujuci odbijene putanje, opozvano clanstvo, istekle sesije i pretpostavke kompromitovanog workload-a.
7. Zahtevaj logovan, vremenski ogranicen, odobren i pregledan hitni pristup sa testiranim opozivom.

### 15.2 Minimalni dokazi

- Graf efektivnih ljudskih i masinskih dozvola.
- Dokaz federation i workload-identity trust policy-ja.
- Rezultat vezbe aktiviranja i opoziva break-glass pristupa.

### 15.3 Kriterijumi izlaza

1. Kriticne privilegije su pripisive, minimalne, vremenski ogranicene gde je moguce i razdvojene po duznosti.
2. Nijedan deljeni kredencijal bez vlasnika ili rutinska cluster-admin putanja nije ostala.
3. Ponasanje opoziva i hitnog pristupa je potvrđeno.

