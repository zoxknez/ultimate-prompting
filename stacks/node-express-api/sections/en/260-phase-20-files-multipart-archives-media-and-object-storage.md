## Phase 20 - Files, Multipart, Archives, Media, And Object Storage

Audit the effective behavior in source, resolved configuration, built artifact, target deployment, and failure paths. Mark unavailable evidence explicitly instead of filling gaps with assumptions.

### Audit Requirements

- Define count, field, filename, path, size, total size, duration, dimension, archive-entry, and decompression limits.
- Stream uploads and downloads where appropriate and prove backpressure, abort, cleanup, and partial-file behavior.
- Validate magic bytes, parser behavior, extension, MIME, encoding, archive paths, symlinks, and nested content.
- Prevent path traversal, zip slip, decompression bomb, parser bomb, image bomb, command injection, and unsafe temp-file use.
- Use private storage by default and enforce tenant, owner, authorization, expiry, and disposition on every download.
- Verify signed-URL scope, method, object, expiry, headers, revocation assumptions, CDN behavior, retention, and orphan cleanup.

### Required Evidence

- Produce and preserve the file-flow and storage-authorization matrix.
- Produce and preserve the parser, native-tool, and limit inventory.
- Produce and preserve retention, cleanup, and restore evidence.

### Mandatory Failure And Acceptance Tests

- Prove that archive traversal and decompression bombs are blocked.
- Prove that an aborted upload leaves no unauthorized orphan.
- Prove that a signed URL cannot cross tenant, object, or method scope.

