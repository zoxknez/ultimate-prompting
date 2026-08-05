## 16. Network, DNS, TLS, Ingress, Gateway And Mesh

**Objective:** Constrain traffic, authenticate endpoints, and make failure behavior explicit.

### 16.1 Required Checks

1. Map north-south, east-west, control-plane, node, registry, identity, telemetry, backup, and third-party traffic with protocols, ports, identities, and data classes.
2. Audit VPC or VNet routes, firewalls, security groups, load balancers, private endpoints, NAT, egress gateways, proxies, VPN, peering, transit, and cross-account paths.
3. Verify default-deny network policy behavior for ingress and egress, namespace selectors, pod selectors, IP blocks, DNS requirements, host-network pods, and CNI limitations.
4. Audit DNS ownership, delegation, split horizon, wildcard records, TTL, DNSSEC where applicable, stale records, takeover risk, resolver dependencies, and change rollback.
5. Verify TLS versions, cipher policy, certificate chain, SANs, hostname verification, mTLS identities, trust-store distribution, automated renewal, revocation assumptions, and expiry alerts.
6. Audit Ingress or Gateway API routing, host and path conflicts, default backend, redirects, headers, request size, timeouts, retries, buffering, WebSocket or gRPC, source IP, and admin endpoints.
7. For service mesh, verify identity issuance, policy scope, fail-open behavior, sidecar or ambient mode, egress control, retries, circuit breaking, telemetry cost, and upgrade compatibility.
8. Test certificate expiry, DNS failure, dependency timeout, partial packet loss, route conflict, unavailable zone, and retry amplification.

### 16.2 Minimum Evidence

- Traffic and trust map with effective network controls.
- TLS, certificate, DNS, ingress or gateway, and policy test results.
- Failure test evidence for DNS, certificates, dependencies, and retries.

### 16.3 Exit Criteria

1. Critical traffic is explicitly allowed, unnecessary traffic is denied, and control limitations are known.
2. Certificates renew and fail safely before expiry, with actionable alerts and ownership.
3. Routing, timeout, and retry behavior does not cause silent exposure or cascading failure.

