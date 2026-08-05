## 25. Incident Mode

1. Preserve volatile evidence before cleanup: running processes, executable paths, loaded modules, command lines, network connections, open files, updater state, installer logs, signatures, hashes, browser/WebView storage, and relevant memory/crash artifacts.
2. Isolate affected release channels, signing/publishing credentials, update endpoints, stores, CDN objects, local services, and administrative access according to the containment plan.
3. Determine whether compromise is in renderer content, privileged bridge, native core, dependency, build system, signing system, update metadata, distribution channel, installer, local data, or external service.
4. Do not destroy evidence by reinstalling, auto-updating, deleting cache, rotating all keys blindly, or running unreviewed cleanup tools before collection.
5. Revoke or disable the smallest affected trust path first, but assume broader impact until evidence narrows it.
6. Build replacement artifacts from a verified commit in a trusted clean environment with reviewed dependencies, new or verified credentials, SBOM, provenance, signatures, and package inspection.
7. Test clean install, in-place recovery, compromised-version update, data preservation, credential reset, key rotation, and rollback before release.
8. Communicate affected versions, platforms, channels, indicators, user actions, data impact, and recovery status accurately without speculation.
9. Preserve a timeline of source, build, signing, publishing, distribution, install, execution, detection, containment, eradication, recovery, and follow-up.
10. Produce root cause, control failure, detection gap, blast radius, recovery evidence, residual risk, and prevention actions with owners and deadlines.

