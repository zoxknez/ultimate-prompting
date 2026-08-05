## 11. Baseline Commands And Reproducibility

Adapt commands to the repository and authorization boundary. Record command, environment, exit code, duration, and retained artifact.

```bash
git status --short --branch
flutter --version --machine
flutter doctor -v
dart --version
flutter pub get
flutter pub deps
flutter analyze
flutter test
# Run only applicable release builds in controlled environments:
flutter build apk --release
flutter build appbundle --release
flutter build ipa --release
flutter build web --release
flutter build windows --release
flutter build macos --release
flutter build linux --release
```

- Do not run `flutter clean`, broad regeneration, package upgrades, native dependency updates, signing, store submission, or destructive integration tests without understanding scope and preserving evidence.
- Use a clean checkout or isolated worktree to prove reproducibility and distinguish stale local state from repository defects.
- Separate analyzer, unit/widget, integration, release build, artifact inspection, install, launch, update, and production evidence in the report.
- Capture skipped targets and exact blockers; never convert unavailable platform tooling into a pass.

