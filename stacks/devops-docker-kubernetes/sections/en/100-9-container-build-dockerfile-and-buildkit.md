## 9. Container Build, Dockerfile And BuildKit

**Objective:** Produce minimal, reproducible, non-secret-bearing, multi-platform-ready OCI artifacts.

### 9.1 Required Checks

1. Inspect build context, `.dockerignore`, stages, base images, digest pinning policy, package installation, cache usage, generated files, ownership, timestamps, and reproducibility.
2. Use BuildKit secret or SSH mounts for build-time credentials. Reject secrets in `ARG`, `ENV`, copied files, layers, cache exports, logs, or image history.
3. Verify multi-stage boundaries prevent compilers, package managers, source, tests, credentials, and debug tooling from leaking into runtime images.
4. Run as a deliberate non-root UID and GID, with correct file ownership, writable paths, signals, init behavior, locale, certificates, timezone assumptions, and shutdown semantics.
5. Verify architecture support, native libraries, emulation risks, 32-bit or 64-bit assumptions, and manifest-list correctness for required platforms.
6. Generate SBOM and provenance at build time and bind them to the immutable image digest.
7. Measure compressed size, unpacked size, layer reuse, startup impact, vulnerability exposure, and operational debuggability rather than optimizing size blindly.

### 9.2 Minimum Evidence

- Reproducible build command, builder version, platform matrix, and image digests.
- Image history and layer inspection with secret checks.
- SBOM, provenance, signature, scan, and runtime smoke evidence tied to digest.

### 9.3 Exit Criteria

1. No credential is present in context, layers, history, metadata, logs, or exported cache.
2. Runtime image contains only justified components and runs correctly as non-root on required architectures.
3. Artifact identity, SBOM, provenance, signature, and test results are immutable and mutually traceable.

