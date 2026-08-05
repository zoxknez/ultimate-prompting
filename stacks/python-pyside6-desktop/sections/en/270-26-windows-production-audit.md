## 26. Windows Production Audit

### 26.1 Audit Scope

1. Review supported Windows versions, x64/ARM64, MSVC runtime, Universal CRT, WebView/graphics dependencies, DPI awareness, and code-page assumptions.
2. Inspect PE imports, manifests, Authenticode, timestamp, catalog/signature chain, DLL search order, side-by-side assemblies, and packaged Qt platform plugins.
3. Assess MSI/MSIX/EXE/portable installer behavior, per-user versus per-machine scope, UAC, registry, services, scheduled tasks, firewall, file associations, and repair.
4. Review DPAPI, Credential Manager, ACLs, junctions, reparse points, named pipes, AppData/ProgramData/Program Files locations, and multi-user isolation.
5. Test high DPI, multiple monitors, Remote Desktop, session lock, fast user switching, sleep/resume, dark mode, input methods, and accessibility tools.
6. Define SmartScreen reputation, certificate renewal, enterprise deployment, antivirus/EDR interaction, update, rollback, and uninstall support.

### 26.2 Required Verification

1. Verify the final installed executable and every shipped DLL/plugin with trusted inspection tools and signature-chain validation.
2. Launch from adversarial working directories and with modified PATH to detect DLL or executable hijacking.
3. Test standard-user install/use/update/uninstall, elevation boundaries, another OS user, roaming/non-roaming profiles, and locked files.
4. Exercise display scaling combinations, monitor removal, RDP reconnect, graphics fallback, accessibility, locale, and IME scenarios.
5. Validate update and rollback across certificate renewal, reboot-required files, running helper processes, and enterprise security software.

