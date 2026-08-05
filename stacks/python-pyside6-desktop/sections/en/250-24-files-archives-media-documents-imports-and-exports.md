## 24. Files, Archives, Media, Documents, Imports, And Exports

### 24.1 Audit Scope

1. Inventory every accepted and produced file format, parser, codec, archive, image, media, PDF, office, CSV, database, project, backup, and export path.
2. Record trust source, maximum size, expansion ratio, recursion depth, path rules, temporary storage, validation, sanitization, and cleanup.
3. Review path traversal, zip slip, symlink/hardlink abuse, alternate streams, special files, device paths, filename normalization, extension confusion, and overwrite behavior.
4. Assess parser memory/CPU limits, decompression bombs, malformed metadata, external references, macros, formulas, embedded content, and native codec vulnerabilities.
5. Validate atomic export, partial output, disk full, cancellation, existing files, permissions, network shares, removable media, and concurrent access.
6. Distinguish preview, validation, import, conversion, execution, external-open, and trusted-project semantics.

### 24.2 Required Verification

1. Use a malicious corpus and fuzz representative parsers in isolated environments; include oversized, recursive, truncated, polyglot, and path-manipulating samples.
2. Test import/export cancellation and crash at every write boundary; verify no misleading successful output or corrupted original remains.
3. Confirm temporary files use safe locations, restrictive permissions, unpredictable names, atomic replacement, and deterministic cleanup.
4. Verify external tools and codecs are resolved from trusted signed locations and receive safely quoted arguments and constrained resources.
5. Ensure user warnings describe actual risk and do not become the only control for executable or active content.

