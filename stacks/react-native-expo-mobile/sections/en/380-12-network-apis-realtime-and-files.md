## 12. Network, APIs, Realtime, And Files

### 12.1 Network Contract
- Inventory every base URL, protocol, client, interceptor, proxy, certificate policy, redirect rule, timeout, retry, cache, and offline behavior.
- Define connect, TLS, write, read, total, idle, upload, download, and background-transfer timeouts.
- Use bounded retries only for classified transient failures and account for idempotency, retry budgets, jitter, deadlines, and server overload.
- Audit redirect handling, hostname validation, proxy configuration, certificate pinning lifecycle, custom trust stores, and debug exceptions.
- Validate response schema, content type, size, compression, encoding, pagination, cursor, error contract, and partial-response behavior.
- Test captive portal, DNS failure, TLS rotation, slow network, network handoff, airplane mode, metered connection, and server version skew.

### 12.2 Upload, Download, Import, And Export
- Validate source, path, URI scheme, MIME type, extension, magic bytes, size, count, filename, and permission for every file operation.
- Use streaming and bounded buffers for large files; audit temporary files, partial files, cleanup, resumability, integrity, and disk-full behavior.
- Test content URI, security-scoped URL, cloud-provider file, removable storage, shared storage, revoked permission, and stale bookmark scenarios.
- Treat image, media, PDF, archive, document, CSV, font, and native codec parsers as hostile-input boundaries.
- Protect against path traversal, zip slip, decompression bomb, oversized dimensions, parser hang, malformed metadata, and executable content.
- Verify server-side authorization, malware scanning where required, integrity confirmation, reconciliation, and user-visible final status.

