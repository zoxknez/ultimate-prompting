## 23. Faza R - Legacy, Migracije I Interoperabilnost

1. Identifikuj deprecated Android API-je, support biblioteke, Kotlin synthetics, AsyncTask, Loader, legacy storage, legacy permission, stari billing, stari media i obsolete Gradle API.
2. Klasifikuj svaki legacy element kao safe, supported, risky, blocking ili migration candidate.
3. Ne migriraj samo zbog mode. Vezi migraciju za support, security, correctness, performance, policy ili maintainability.
4. Planiraj framework i toolchain upgrade u compatibility-bounded koracima.
5. Sacuvaj ponasanje characterization testovima pre velikih refactor-a.
6. Tokom migracije testiraj database, storage, auth, navigation, notification, background, media i signing kontinuitet.
7. Proveri Java i Kotlin nullability, SAM, exception, generic, annotation i threading interoperabilnost.
8. Proveri da KMP ili shared modul ne skriva platform lifecycle, security ili storage zahteve.
9. Ukloni obsolete compatibility kod tek nakon potvrde supported device i version policy-ja.
10. Dokumentuj privremene bridge-eve i rokove da ne postanu trajna skrivena arhitektura.

