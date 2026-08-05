## Phase 20 - Uploads, Downloads, Archives, Media, Documents, and Filesystem Boundaries

### Objective

Prove authorization, parsing safety, storage integrity, isolation, and lifecycle for attacker-controlled files and generated artifacts.

### Audit Requirements

- Inventory uploads, direct-to-storage flows, imports, exports, archives, images, video, audio, PDF, office documents, CSV, temporary files, and generated downloads.
- Verify authentication, authorization, tenant namespace, size, count, filename, extension, MIME, magic bytes, parser limits, and quarantine before use.
- Audit traversal, symlink, race, overwrite, executable placement, public exposure, signed URL scope, response headers, content sniffing, and disposition.
- Test zip slip, decompression bombs, nested archives, malformed media, parser vulnerabilities, image metadata, macro content, and formula injection.
- Verify asynchronous scanning and processing state, duplicate callbacks, timeout, worker crash, partial files, cleanup, retention, deletion, and legal hold.
- Audit export authorization at generation and download time, snapshot consistency, row limits, sensitive fields, watermarking, expiry, and audit trail.

### Required Evidence

- File-flow matrix from ingress through scanning, processing, storage, delivery, retention, and deletion.
- Malicious-file, traversal, archive-bomb, parser-crash, duplicate-callback, and unauthorized-download tests.
- Cleanup, retention, deletion, restore, and legal-hold evidence.

### Acceptance Criteria

- Untrusted files cannot execute, escape their namespace, exhaust processing, or become publicly accessible by accident.
- Every generated or stored artifact has explicit authority, integrity, retention, and recovery behavior.

