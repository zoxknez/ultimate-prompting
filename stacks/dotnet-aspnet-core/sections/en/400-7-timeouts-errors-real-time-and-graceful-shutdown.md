## 7. Timeouts, Errors, Real-Time, And Graceful Shutdown

Inbound/DB/external/job/stream timeouts and shutdown deadline. Propagate `CancellationToken`. Stable error taxonomy with correlation ID without leaking internals.

SignalR/SSE/gRPC: per-message auth, limits, backpressure, cleanup. SIGTERM: unready, drain, stop jobs, close streams, flush telemetry, close connections within deadline. Test shutdown during long reads, critical writes, jobs, uploads, streams, and migrations.

