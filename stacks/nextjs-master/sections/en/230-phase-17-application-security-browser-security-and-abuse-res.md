## Phase 17 - Application Security, Browser Security, And Abuse Resistance

Verify actual response and runtime behavior, not configuration intent.

### Audit Requirements

- Verify CSP, nonce/hash strategy, HSTS, frame protection, Referrer-Policy, Permissions-Policy, COOP, COEP, CORP, and MIME protections.
- Inventory HTML, Markdown, rich text, MDX, embeds, SVG, URL rendering, and every dangerous HTML sink.
- Validate and canonicalize URLs, redirects, hosts, protocols, paths, filenames, object keys, and outbound destinations.
- Prevent SSRF with destination policy, DNS/IP checks, redirect revalidation, private-network controls, protocol limits, and egress controls.
- Review CSRF for cookie-auth mutations, CORS, host/origin validation, same-site assumptions, and alternate clients.
- Protect login, reset, invitation, verification, actions, APIs, search, upload, export, expensive rendering, and third-party spend.

### Required Evidence

- Observed security headers and CSP violation evidence.
- Input/output/URL/file/outbound trust-boundary inventory.
- Rate-limit key, scope, storage, bypass, failure, and capacity evidence.
- Reachability and patch evidence for relevant advisories.

### Mandatory Failure And Acceptance Tests

- Inject script, URL, SVG, Markdown, rich-text, header, and template payloads.
- Test SSRF through IPs, redirects, encoded hosts, protocols, and metadata targets in isolation.
- Test rate-limit bypass by account, tenant, IP, session, alias, region, and distributed concurrency.
- Run regressions derived from current Next.js, React, RSC, auth, parser, and platform advisories.

