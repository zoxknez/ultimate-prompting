## Phase M - Shared Security Analysis

Trust boundaries: public API, internal API, admin, worker, DB, broker, filesystem, cloud metadata, FFI.

AuthN/AuthZ: token/session validation, object-level authorization, tenant isolation, service-to-service auth. Test BOLA/IDOR.

Input: injection (SQL/command/path), SSRF, deserialization bombs, path traversal, zip-slip, XSS if HTML exists, header injection.

Command execution: allowlists, avoid shell where possible, env scrubbing.

Filesystem: root confinement, permissions, symlinks, temp files.

TLS/crypto: chain verification, min version, ciphers, certificate pinning where needed, key storage; never disable TLS verify on production paths.

Secrets: not in source/log/image/artifact; rotation; incident if compromised (without displaying full values).

Debug: pprof, metrics, admin, reflection — not public without protection.

