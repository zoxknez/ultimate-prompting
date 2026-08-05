## 19. Networking, TLS, Authentication, Retries, And Streaming

### 19.1 Audit Scope

1. Inventory QNetworkAccessManager instances, Python HTTP clients, WebSocket/SSE/gRPC clients, proxy configuration, DNS, certificate stores, and custom transports.
2. Record connection, TLS, request, read, write, total, idle, and pool-acquisition timeouts plus cancellation and deadline propagation.
3. Review certificate validation, hostname verification, redirects, proxy authentication, client certificates, pinning where justified, and rotation behavior.
4. Assess token acquisition, refresh serialization, expiry, revocation, logout, account switching, MFA/passkey flows, and secure browser handoff.
5. Check retry classification, idempotency, jitter, budget, circuit breaking, offline queueing, reconnect, resume, duplicate delivery, and replay.
6. For streaming and large transfers, review backpressure, partial files, checksums, disk limits, sparse files, cancellation, resume metadata, and cleanup.

### 19.2 Required Verification

1. Test slow DNS, TLS failure, certificate rotation, proxy changes, captive portal, offline transition, packet loss, partial response, malformed response, and server throttling.
2. Run concurrent expiry and refresh scenarios to prove one safe refresh path and correct failure propagation.
3. Verify that retries do not duplicate purchases, writes, uploads, downloads, device commands, or local state transitions.
4. Measure queue growth, memory, disk, UI responsiveness, and recovery during long-running or stalled transfers.
5. Confirm secrets and sensitive payloads are absent from URLs, proxy logs, debug traces, crash reports, telemetry, and support bundles.

