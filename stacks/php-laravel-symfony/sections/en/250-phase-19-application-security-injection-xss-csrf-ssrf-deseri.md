## Phase 19 - Application Security, Injection, XSS, CSRF, SSRF, Deserialization, and Abuse

### Objective

Identify and verify controls for attacker-controlled data, dangerous interpreters, privilege boundaries, and resource abuse.

### Audit Requirements

- Map untrusted data into SQL, shell, template, HTML, URL, header, log, file path, regex, expression language, LDAP, XML, YAML, CSV, and mail contexts.
- Verify parameterization, contextual encoding, autoescape boundaries, trusted HTML handling, CSP, sanitization, header safety, and formula-injection controls.
- Audit CSRF for browser-authenticated mutations, SameSite assumptions, CORS, origin checks, login CSRF, logout CSRF, and token lifecycle.
- Audit SSRF through URL fetchers, previews, webhooks, importers, redirects, DNS rebinding, alternate IP syntax, metadata services, and internal protocols.
- Reject unsafe native deserialization, object injection, PHAR metadata abuse, untrusted YAML tags, XML entities, dynamic class resolution, and gadget chains.
- Test resource abuse through expensive regex, deep structures, large collections, decompression, image processing, exports, search, pagination, and concurrent requests.
- Review debug routes, profiler, Telescope, Horizon, Pulse, Ignition, Symfony profiler, phpinfo, stack traces, source maps, and secret exposure.

### Required Evidence

- Untrusted-source-to-dangerous-sink matrix with control and test evidence.
- Exploit-oriented negative tests for injection, XSS, CSRF, SSRF, deserialization, traversal, and resource exhaustion.
- Production evidence that debug and diagnostic surfaces are inaccessible or appropriately protected.

### Acceptance Criteria

- No attacker-controlled value reaches an interpreter, privileged sink, or internal network target without a verified control.
- Malformed or intentionally expensive input is rejected within bounded CPU, memory, time, and downstream cost.

