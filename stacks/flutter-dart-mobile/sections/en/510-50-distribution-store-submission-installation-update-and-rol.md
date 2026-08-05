## 50. Distribution, Store Submission, Installation, Update, And Rollback

Release success means users can safely obtain, install, run, update, and recover the intended artifact.

- Inventory Google Play, App Store/TestFlight, web/CDN, Microsoft Store/MSIX, direct Windows installers, Mac App Store/Developer ID, Linux stores/packages, enterprise, and internal channels.
- Verify identity continuity, version/build monotonicity, signing, metadata, screenshots, privacy disclosures, content ratings, export compliance, subscriptions, account deletion, and review requirements.
- Test clean install, upgrade from every supported prior version, skipped-version upgrade, reinstall, restore, channel switch, architecture change, interrupted install, low disk, offline launch, and uninstall.
- Verify user data, secure storage, database, files, permissions, notifications, deep links, background tasks, app links, and associations survive or reset according to policy.
- Define staged rollout cohorts, telemetry gates, acceptance thresholds, abort triggers, freeze authority, rollback owner, support communication, and store-specific rollback limits.
- Web deployments must prevent mixed asset versions, stale HTML/service worker traps, incompatible API changes, missing source maps, and cache-poisoned rollback.
- Mobile store rollback may require a forward-fix build; preserve old/new compatibility, remote disable controls, backend mitigations, and recovery communications.
- Desktop updaters/installers must verify signature, metadata, channel, architecture, atomic replacement, running process, downgrade policy, rollback, and key rotation.
- Do not call rollout successful until operational evidence covers intended cohorts, critical journeys, migrations, crashes, performance, support signals, and rollback readiness.

