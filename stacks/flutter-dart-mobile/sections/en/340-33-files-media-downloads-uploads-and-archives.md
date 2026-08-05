## 33. Files, Media, Downloads, Uploads, And Archives

Treat every external file as untrusted and every local path as platform-specific.

- Inventory document pickers, camera/gallery, drag/drop, share intents, clipboard, imports, exports, archives, media decode, thumbnails, downloads, uploads, and temporary files.
- Validate type from content where possible, size, dimensions, duration, count, encoding, filename, extension, path, archive structure, and parser limits.
- Prevent path traversal, symlink/reparse abuse, zip slip, decompression bombs, overwrite, executable content, malicious metadata, parser crashes, and unsafe external opening.
- Use scoped or user-selected storage appropriately; verify platform bookmarks/permissions, revocation, sandbox paths, removable media, cloud files, and file-provider semantics.
- Define upload and download resume, integrity hash, content length, partial file, cancellation, retry, quota, duplicate, overwrite, cleanup, and low-disk behavior.
- Do not expose private local paths, signed URLs, tokens, tenant identifiers, EXIF/GPS data, or user content in logs and analytics.
- Test malformed, truncated, huge, encrypted, nested, renamed, zero-byte, duplicate, unsupported, and slow-stream files.
- Verify cleanup after success, failure, cancellation, process death, logout, account deletion, app update, and uninstall according to policy.

