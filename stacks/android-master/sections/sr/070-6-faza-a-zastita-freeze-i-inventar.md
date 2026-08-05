## 6. Faza A - Zastita, Freeze I Inventar

1. Zabelezi `git status --short --branch`, trenutni revision, branch-eve, submodule-e, worktree-e, untracked fajlove i lokalne izmene.
2. Identifikuj root repozitorijuma i svaki included build, composite build, convention plugin, `buildSrc`, version catalog i custom Gradle plugin.
3. Mapiraj application, library, dynamic-feature, benchmark, test-fixture, baseline-profile, Wear, TV, Auto i KMP module.
4. Mapiraj source set-ove, varijante, flavor-e, signing konfiguracije, manifest overlay-e, generisane source fajlove, native source set-ove, assets, resurse i packaging options.
5. Pronadji CI workflow-e, release skripte, Fastlane, Play Publisher, Firebase App Distribution, artifact repository-je i environment konfiguraciju.
6. Inventarisi reference ka keystore-ovima i putanje tajni bez ispisivanja vrednosti.
7. Inventarisi application ID-jeve, namespace-ove, logiku version code i version name, deep-link hostove, content authority-je, service-e, receiver-e, provider-e, activity-je, dozvole, feature-e i queries.
8. Inventarisi native biblioteke i third-party SDK-ove iz source konfiguracije i buildovanih artefakata.
9. Identifikuj kriticne user journey-e, destruktivne operacije, regulisane podatke, offline zahteve i device-specific ponasanje.
10. Uspostavi no-change baseline pre popravki.

Minimalne bezbedne komande, prilagodjene projektu:

```text
git status --short --branch
git rev-parse HEAD
./gradlew --version
./gradlew projects
./gradlew tasks --all
```

