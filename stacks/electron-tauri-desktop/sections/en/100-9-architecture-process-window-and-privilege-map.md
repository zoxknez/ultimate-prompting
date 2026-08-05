## 9. Architecture, Process, Window, And Privilege Map

### 9.1 Mandatory Architecture Map

1. Draw the process tree: bootstrap, Electron main or Tauri Rust core, renderer/webview processes, GPU, utility/worker processes, sidecars, local daemons, helpers, crash reporter, updater, installer, and spawned children.
2. Map every window and webview by stable label or identifier, content origin, lifecycle, owner, user role, data sensitivity, navigation policy, permission set, and exposed bridge.
3. Map every trust boundary between untrusted remote content, local packaged UI, privileged bridge, native core, local files, operating-system APIs, devices, and remote services.
4. Map all IPC mechanisms: Electron IPC, MessagePort, postMessage, webview messaging, Tauri invoke/events/channels, local sockets, named pipes, HTTP, WebSocket, stdin/stdout, files, and custom protocols.
5. Map authentication and authorization decisions at the layer that performs privileged work. UI hiding is not authorization.
6. Map state ownership: renderer memory, main/Rust state, local database, files, secure storage, cloud service, updater, and installer.
7. Map startup, shutdown, crash restart, sleep/wake, session lock/unlock, network transition, update restart, and OS sign-out/shutdown paths.
8. Mark every path that can execute code, launch a process, open an external URL, write a file, access credentials, use a device, change settings, install an update, or delete data.

### 9.2 Privilege-Minimization Questions

1. Can a renderer or webview do less? Remove broad bridges and expose narrow operations with explicit schemas.
2. Can a privileged operation move to a dedicated process, scoped command, OS service, or broker with a smaller attack surface?
3. Can a window receive a unique capability or session instead of inheriting a global permission set?
4. Can a file, URL, executable, device, or credential scope be restricted to an allowlisted subset?
5. Can network content be rendered without local privileges and without sharing cookies, storage, permissions, or service workers with trusted content?
6. Can the updater, installer, or release job run with temporary credentials and separate approval?
7. Can administrative behavior be separated from the normal user process and made auditable?
8. Can a compromised renderer be contained without reaching code execution, secrets, user files, update controls, or another tenant/account?

