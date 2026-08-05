## 14. Network, Local Services, Proxies, And Certificates

### 14.1 Remote Network Calls

1. Inventory frontend, main/Rust, plugin, sidecar, updater, telemetry, crash, licensing, payment, and installer network clients.
2. Define connect, TLS, header, body, idle, stream, total, and retry deadlines. Propagate cancellation and distinguish user cancellation from network failure.
3. Retry only safe or idempotent operations with bounded attempts, exponential backoff, jitter, retry budgets, and respect for server rate-limit signals.
4. Validate redirects, final origin, content type, size, certificate, proxy behavior, and DNS changes for privileged downloads and update metadata.
5. Protect against SSRF where user-controlled URLs can reach localhost, private ranges, metadata services, Unix sockets, named pipes, or privileged local endpoints.
6. Do not disable TLS verification globally. If certificate pinning or custom roots are used, define rotation, expiry, backup trust, proxy compatibility, and recovery.
7. Redact authorization headers, cookies, tokens, device identifiers, license data, personal content, and query secrets from logs and crash reports.
8. Test offline, captive portal, DNS failure, proxy auth, TLS interception, expired certificate, clock skew, slowloris, partial response, oversized response, and retry storm.

### 14.2 Local HTTP, Socket, Pipe, And Service Interfaces

1. Inventory every localhost listener, Unix socket, named pipe, loopback WebSocket, custom URI broker, privileged service, browser callback server, and developer port.
2. Bind to the narrowest interface and use OS permissions, random unguessable endpoints, authentication, origin checks, request schemas, rate limits, and lifetime controls.
3. Do not assume localhost is trusted. Browsers, other users, sandboxed apps, malware, and local network exposure can reach incorrectly bound services.
4. Protect against DNS rebinding, browser cross-origin requests, CSRF-like local requests, port prediction, stale socket files, named-pipe squatting, and service impersonation.
5. Validate peer identity for privileged service or helper communication. Bind requests to the current app instance, user, session, version, and intended operation.
6. Define startup races, port conflicts, service upgrade order, version handshake, reconnect, graceful shutdown, and orphan cleanup.
7. Never expose generic shell, filesystem, database, update, or credential functions over a local endpoint without strong authentication and narrow authorization.
8. Test unauthenticated local requests, cross-origin browser requests, another OS user, stale client, wrong version, replay, oversized payload, slow client, and process crash.

