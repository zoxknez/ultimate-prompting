## 11. Baseline komande i reproduktivnost

Prilagodi komande repozitorijumu i granici ovlašćenja. Zabeleži komandu, okruženje, exit code, trajanje i sačuvan artefakt.

```bash
git status --short --branch
flutter --version --machine
flutter doctor -v
dart --version
flutter pub get
flutter pub deps
flutter analyze
flutter test
# Pokreni samo primenljive release build-ove u kontrolisanim okruženjima:
flutter build apk --release
flutter build appbundle --release
flutter build ipa --release
flutter build web --release
flutter build windows --release
flutter build macos --release
flutter build linux --release
```

- Ne pokreći `flutter clean`, široku regeneraciju, nadogradnju paketa, update native zavisnosti, potpisivanje, store submission ili destruktivne integration testove bez razumevanja scope-a i čuvanja dokaza.
- Koristi clean checkout ili izolovan worktree da dokažeš reproduktivnost i razlikuješ zastarelo lokalno stanje od problema repozitorijuma.
- Odvoji analyzer, unit/widget, integration, release build, artifact inspection, install, launch, update i production dokaze u izveštaju.
- Sačuvaj preskočene ciljeve i tačne blokere; nikada ne pretvaraj nedostupan platformski tooling u prolaz.

