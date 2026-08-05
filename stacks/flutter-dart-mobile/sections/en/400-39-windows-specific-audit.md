## 39. Windows-Specific Audit

Verify the Win32 host, package, signing identity, installation, protocol handling, and update path.

- Audit CMake, Visual Studio workload, MSVC/runtime, Windows SDK, architecture, runner code, plugins, generated registrant, native DLLs, and build configuration.
- Verify application identity, package family, publisher, AppUserModelID, MSIX or installer metadata, install scope, elevation, per-user/per-machine behavior, and repair/uninstall.
- Audit Authenticode certificate, timestamp, nested binaries, DLL search, side-loading, SmartScreen reputation, certificate renewal, revocation, and key custody.
- Verify protocol/file associations, command-line arguments, single-instance behavior, multiple windows, toast activation, startup tasks, drag/drop, clipboard, and external processes.
- Test DPI scaling, multiple monitors, remote desktop, high contrast, screen readers, keyboard, IME, touch, tablet mode, sleep/resume, lock/unlock, and fast user switching.
- Audit local files, registry, credential storage, ACLs, temporary paths, symlinks/reparse points, roaming data, backup, and enterprise policy.
- Inspect update atomicity, running-file replacement, reboot requirement, downgrade, channel switch, rollback, old shortcut cleanup, and user-data preservation.
- Test Windows versions, architectures, clean install, upgrade, repair, uninstall, restricted user, offline install, antivirus interaction, and low disk.

