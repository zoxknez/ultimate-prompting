## 18. Installer, Store, Enterprise, Upgrade, And Uninstall Behavior

### 18.1 Installer Semantics

1. Identify installer technology, version, scope, elevation model, install path, data path, repair behavior, upgrade code/product code/bundle identity, custom actions, prerequisites, and rollback support.
2. Verify fresh install, same-version repair, patch/minor/major upgrade, downgrade rejection, side-by-side channels, per-user to per-machine transition, architecture transition, and uninstall.
3. Make custom actions minimal, deterministic, logged, retry-safe, and reversible. Never hide arbitrary network downloads or shell execution inside an installer.
4. Validate paths and permissions created by the installer. Prevent normal users from replacing executable files, DLLs, helpers, update components, or privileged configuration.
5. Preserve user data intentionally, migrate it explicitly, and remove it only according to documented user/enterprise choice.
6. Handle running application instances, tray processes, services, sidecars, locked files, antivirus, reboot-required state, and interrupted installation.
7. Verify registration and cleanup of protocols, file associations, shortcuts, startup entries, services, scheduled tasks, firewall rules, drivers, and store metadata.
8. Test installer logs and error messages for secret leakage and actionable recovery.

### 18.2 Stores And Enterprise Distribution

1. Map Microsoft Store, Mac App Store, Snap/Flatpak stores, package repositories, MDM, software-distribution tools, and direct-download channels separately.
2. Review sandbox, entitlement, API, payment, update, telemetry, privacy, age-rating, and content rules for each channel.
3. Use channel-specific configuration rather than runtime guessing. Verify bundle identity and data-path continuity between store and direct builds only when migration is supported.
4. Prevent a lower-trust channel from updating or replacing a higher-trust channel unintentionally.
5. Verify offline installers, proxy support, certificate deployment, WebView/runtime prerequisites, silent install switches, exit codes, logs, and detection rules for enterprise use.
6. Document ownership of store accounts, publisher organizations, recovery contacts, MFA, API keys, signing profiles, and emergency access.
7. Test store review/rejection fallback, phased release pause, package withdrawal, mandatory update constraints, and users stuck on old store versions.
8. Ensure release notes, privacy declarations, permissions, data safety, and screenshots match actual behavior.

