## 35. Incident Response, Containment, Forensics, And Trusted Rebuild

### 35.1 Audit Scope

1. Define incident classes for malicious package or plugin, dependency compromise, credential theft, signing-key compromise, update-feed tampering, helper/service compromise, data corruption, and privacy breach.
2. Map evidence sources: repository, CI, package indexes, build logs, provenance, signatures, update metadata, installed files, process/module lists, logs, dumps, databases, and network telemetry.
3. Define containment controls: disable feed, revoke key or token, block package/version, pause rollout, disable plugin or feature, isolate host, stop writes, and preserve evidence.
4. Distinguish cleanup from trusted rebuild; a compromised interpreter, package, helper, updater, signing system, or host cannot be trusted merely because suspicious files were deleted.
5. Document credential rotation, certificate revocation, user notification, legal/privacy escalation, clean-room rebuild, restored data validation, and re-enrollment.
6. Define exit criteria, heightened monitoring, retrospective actions, owner, and verification that the original root cause and persistence mechanisms are removed.

### 35.2 Required Verification

1. Run a tabletop or technical exercise for at least the highest-impact applicable incident class.
2. Verify rapid identification of affected commits, dependencies, artifacts, signatures, channels, installed versions, users, data, and credentials.
3. Prove revocation, update disablement, kill switch, safe-mode startup, plugin quarantine, write freeze, and trusted replacement mechanisms.
4. Rebuild from known-good source and trusted toolchains on clean infrastructure; compare hashes, provenance, SBOM, signatures, and behavior.
5. Test recovery communication and operator runbooks without exposing sensitive forensic or personal data.

