## 27. Mandatory Adversarial And Failure Scenarios
1. S1 - Two rapid user actions initiate the same privileged or financial mutation.
2. S2 - A response completes after navigation, logout, tenant switch, item replacement, or view destruction.
3. S3 - The app dies before request send, during transfer, after server commit, and before local acknowledgement.
4. S4 - Old binary receives new JavaScript, new binary starts with old embedded JavaScript, and rollback follows local migration.
5. S5 - OTA download is interrupted, corrupted, out of storage, signature-invalid, channel-mismatched, or crash-looping.
6. S6 - Account or tenant switches while cached data, offline commands, streams, notifications, and background work remain active.
7. S7 - Deep link or notification targets a removed, unauthorized, stale, cross-tenant, or malformed resource.
8. S8 - Token refresh, logout, revocation, key rollover, network retry, and multiple parallel requests race.
9. S9 - Native callback arrives after React instance reload, activity recreation, view-controller replacement, or Fabric view recycling.
10. S10 - JSI or native code receives malformed, oversized, misaligned, stale, duplicated, or concurrently accessed data.
11. S11 - Background task, push action, media event, or location event executes with old code, expired credentials, or changed schema.
12. S12 - Network is slow, captive, metered, switching, offline, TLS-rotated, partially failing, or returning incompatible data.
13. S13 - Local database migration is interrupted, storage is full, data is corrupted, backup is restored, or two app versions access the state.
14. S14 - Permission changes in settings, is limited, becomes permanently denied, or is revoked while a resource is active.
15. S15 - App is backgrounded, suspended, killed, restored, upgraded, or rebooted during each critical operation.
16. S16 - Low memory, thermal pressure, low battery, low storage, slow device, long list, large image, and repeated navigation coincide.
17. S17 - Malicious file, archive, image, media, PDF, URL, WebView page, bridge message, or native intent is processed.
18. S18 - Signing credential, update key, CI runner, dependency, config plugin, native SDK, or build image is compromised.
19. S19 - Store rollout, OTA rollout, backend rollout, local migration, and feature flag overlap in incompatible order.
20. S20 - Production rollback and isolated restore are executed after real data, queue, update, and schema changes.

