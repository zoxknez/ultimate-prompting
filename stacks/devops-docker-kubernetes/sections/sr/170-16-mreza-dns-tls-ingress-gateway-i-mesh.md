## 16. Mreza, DNS, TLS, ingress, gateway i mesh

**Cilj:** Ogranici saobracaj, autentikuj endpoint-e i ucini ponasanje pri otkazu eksplicitnim.

### 16.1 Obavezne provere

1. Mapiraj north-south, east-west, control-plane, node, registry, identity, telemetrijski, backup i third-party saobracaj sa protokolima, portovima, identitetima i klasama podataka.
2. Audituj VPC ili VNet rute, firewall-e, security group-e, load balancer-e, private endpoint-e, NAT, egress gateway-e, proxy-je, VPN, peering, transit i cross-account putanje.
3. Proveri default-deny network policy ponasanje za ingress i egress, namespace selector-e, pod selector-e, IP block-ove, DNS potrebe, host-network podove i CNI ogranicenja.
4. Audituj DNS vlasnistvo, delegaciju, split horizon, wildcard record-e, TTL, DNSSEC gde je primenljivo, zastarele record-e, takeover rizik, resolver zavisnosti i rollback izmene.
5. Proveri TLS verzije, cipher policy, lanac sertifikata, SAN, hostname verifikaciju, mTLS identitete, distribuciju trust store-a, automatsko obnavljanje, pretpostavke opoziva i expiry alarme.
6. Audituj Ingress ili Gateway API routing, konflikte host-a i putanje, default backend, redirect-e, header-e, request size, timeout-e, retry, buffering, WebSocket ili gRPC, source IP i admin endpoint-e.
7. Za service mesh proveri izdavanje identiteta, policy opseg, fail-open ponasanje, sidecar ili ambient mode, egress kontrolu, retry, circuit breaking, cenu telemetrije i upgrade kompatibilnost.
8. Testiraj istek sertifikata, DNS otkaz, dependency timeout, delimican gubitak paketa, konflikt ruta, nedostupnu zonu i retry amplifikaciju.

### 16.2 Minimalni dokazi

- Mapa saobracaja i poverenja sa efektivnim mreznim kontrolama.
- Rezultati TLS, certificate, DNS, ingress ili gateway i policy testova.
- Dokaz failure testova za DNS, sertifikate, zavisnosti i retry.

### 16.3 Kriterijumi izlaza

1. Kriticni saobracaj je eksplicitno dozvoljen, nepotreban je odbijen, a ogranicenja kontrola su poznata.
2. Sertifikati se obnavljaju i bezbedno otkazuju pre isteka, sa akcionim alarmima i vlasnistvom.
3. Routing, timeout i retry ponasanje ne izazivaju tihu izlozenost ili kaskadni otkaz.

