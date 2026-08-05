## 7. Errors, Timeouts, Real-Time, And Shutdown

Verify inbound/header/body limits, database statement timeout, external deadline, job timeout, stream idle timeout, retry budget, and shutdown deadline. Propagate cancellation/interrupt signals appropriately; never swallow interrupts. A disconnected client should cancel unnecessary safe work, and a timeout must not leave untracked side effects.

Use a stable error taxonomy: validation, unauthenticated, forbidden, not found, conflict, rate limited, dependency unavailable, timeout, and internal failure. Each error needs a safe message, stable code, correct HTTP/gRPC status, retryability, correlation ID, and safe optional details. Preserve causes for diagnostics without repeated error logging at every layer.

For WebSocket, SSE, and gRPC streaming validate connection and per-message authorization, origin/tenant scope, reconnect, heartbeat, idle timeout, message/connection limits, backpressure, cleanup, replay/sequence IDs, missed-event recovery, slow consumers, and deployment behavior. Initial connection authorization is not sufficient for every message/resource.

Test platform shutdown. The application should become unready, reject new traffic, drain or safely cancel in-flight work, stop claiming jobs, close streams, flush telemetry/logs, release database/cache/broker resources, and finish before an explicit platform deadline. Test shutdown during long reads, critical writes, jobs, uploads, streams, and migration deployment.

