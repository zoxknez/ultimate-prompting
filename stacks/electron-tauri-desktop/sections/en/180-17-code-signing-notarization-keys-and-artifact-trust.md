## 17. Code Signing, Notarization, Keys, And Artifact Trust

### 17.1 Signing Architecture

1. Inventory every signing identity and purpose: Windows executable/installer, macOS application/installer, Apple notarization credentials, Linux packages, Tauri updater, store upload, mobile targets, and internal enterprise signing.
2. Use separate keys where threat model or tooling requires separation. Document which compromise affects which channel and how trust can be recovered.
3. Keep private keys in hardware-backed or managed signing systems where practical. Restrict export, interactive use, CI access, roles, approvals, IP/network, repository, branch, and environment.
4. Use timestamping where platform policy supports it so valid releases survive certificate expiry. Verify timestamp authority and failure behavior.
5. Record certificate subject, issuer, serial/thumbprint, validity, key algorithm, timestamp, entitlements, hardened-runtime state, notarization result, and exact artifact hash without exposing private material.
6. Verify signatures after all packaging, fuse, resource, installer, and update transformations. Never modify a signed artifact silently.
7. Define certificate renewal overlap, revocation, lost-key response, expired certificate behavior, publisher identity continuity, and emergency release procedures.
8. Separate signing from publishing so a signed artifact still requires reviewed promotion to a channel.
9. Audit who can submit arbitrary bytes to the signing service. A protected key is insufficient if untrusted jobs can request signatures.
10. Verify local signature checking and store/platform verification on clean machines, not only inside CI.

### 17.2 macOS Signing, Hardened Runtime, Entitlements, And Notarization

1. Verify bundle identifier, team ID, certificate type, designated requirement, nested-code signatures, frameworks, helpers, login items, XPC/services, sidecars, and installer images.
2. Use the minimum entitlements. Justify JIT, unsigned executable memory, disabled library validation, automation, camera, microphone, screen recording, files, network, keychain groups, and sandbox exceptions.
3. Ensure every nested executable and framework is signed in the correct order with compatible entitlements before the outer bundle.
4. Run strict signature verification and assess Gatekeeper behavior on a clean downloaded artifact with quarantine metadata.
5. Submit the exact release artifact for notarization, verify success, staple where applicable, and confirm offline/online Gatekeeper behavior.
6. Test direct download, DMG/PKG, App Store build where applicable, update replacement, helper launch, first run, permission prompts, and OS-version differences.
7. Define behavior when notarization is unavailable, delayed, rejected, or later invalidated. Do not release an unverified substitute.
8. Preserve notarization logs and submission IDs tied to artifact hashes for incident response.

### 17.3 Windows Signing And Reputation

1. Verify Authenticode signatures on executables, DLLs, installers, update packages, drivers/helpers, and catalog files where applicable.
2. Use the intended publisher identity consistently across releases to preserve upgrade trust and reputation. Document certificate renewal and organization changes.
3. Timestamp signatures and verify both signature and timestamp chain on clean supported Windows versions.
4. Audit EV/standard certificate or managed-signing workflow, HSM/Key Vault access, sign-command arguments, digest algorithm, dual-signing needs, and cross-signing assumptions.
5. Verify SmartScreen/Mark-of-the-Web behavior for direct downloads and how reputation is monitored without weakening user protection.
6. Ensure unsigned or differently signed child binaries cannot be loaded from writable directories or bundled accidentally.
7. Test install, repair, update, rollback, uninstall, side-by-side channels, per-user/per-machine scope, UAC, locked files, antivirus, and enterprise policy.
8. Define response to compromised publisher credentials, revoked certificate, false-positive malware classification, and store suspension.

### 17.4 Linux Package Signing And Repository Trust

1. Identify each distribution format and trust model: AppImage, Debian, RPM, Flatpak, Snap, AUR/source package, tarball, or managed enterprise repository.
2. Verify package/repository signatures, metadata expiry, key distribution, rotation, revocation, mirror trust, and update ownership.
3. Audit desktop files, MIME handlers, icons, AppStream metadata, sandbox permissions, portals, systemd units, polkit rules, post-install scripts, and uninstall scripts.
4. Do not treat a signed package as universally trusted across distributions. Test the exact repository, store, or direct-download path.
5. Verify library dependencies and minimum distribution versions on clean supported environments, including WebKitGTK and system runtime requirements for Tauri.
6. Test install, upgrade, downgrade, rollback, package-manager conflict, read-only filesystem, sandbox portals, missing dependencies, and offline enterprise mirrors.
7. Define how direct-download users receive security updates when no built-in updater exists or when distribution policies own updates.
8. Document key compromise and repository takeover response.

