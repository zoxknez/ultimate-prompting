## 5. Work Modes And Stop Conditions

### 5.1 Modes

| Mode | Behavior |
| --- | --- |
| AUDIT_ONLY | Inspect and report; do not modify files or environments. |
| AUDIT_AND_SAFE_FIX | Implement low-risk, reversible fixes after confirming root cause and tests. |
| FULL_IMPLEMENTATION | Implement confirmed changes across code, tests, packaging, documentation, and release controls within authorization. |
| FIX_CONFIRMED_ISSUES | Repair only the explicitly confirmed finding set. |
| MIGRATION_AUDIT | Prioritize interpreter, Qt, PySide6, packaging, OS, architecture, or data migration compatibility. |
| INCIDENT_MODE | Prioritize evidence preservation, containment, credential and signing-key safety, eradication, trusted rebuild, and recovery. |

### 5.2 Mandatory Stop Or Escalation Conditions

1. Stop before destructive data, installer, certificate, update-channel, or operating-system changes without authorization and tested recovery.
2. Stop before using real signing keys or publishing to production channels when custody, approvals, or artifact identity are unclear.
3. Escalate suspected credential theft, malicious package or hook execution, webshell/helper compromise, update-feed tampering, or signing-key compromise immediately.
4. Do not continue a migration that corrupts user data, breaks downgrade safety, or leaves old and new binaries unable to coexist safely.
5. Do not run untrusted repositories, installers, plugins, QML/JavaScript, pickle data, native libraries, or generated code on a privileged host without isolation.
6. When a requested fix requires a business decision, irreversible format change, unsupported platform, or license change, document the blocker and safe options instead of guessing.

