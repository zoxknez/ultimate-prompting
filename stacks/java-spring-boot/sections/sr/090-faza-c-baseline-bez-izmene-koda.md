## Faza C - Baseline Bez Izmene Koda

Prvo proveri dependency resolution, main/test compilation, unit/integration testove, static analysis, style/format, packaging, startup, health, native/AOT ako projekat zvanicno podrzava, container image i smoke test stvarnog deploy artefakta. Za Maven prilagodi `./mvnw -B -ntp compile`, `test`, `verify` i `package`; za Gradle `./gradlew compileJava`, `test`, `check` i `build`. Ne koristi `-DskipTests` kao dokaz da build prolazi i razdvoji preskoceno izvrsavanje, kompilaciju testova, disabled testove i neaktivne integration profile.

Za svaki neuspeh sacuvaj prvu relevantnu gresku i trazi osnovni uzrok: JDK/toolchain mismatch, repository/certifikat, profil, tajna, port, locale/timezone, test-order, lokalna baza ili Docker runtime. Startup pokreci samo sa bezbednom lokalnom/test konfiguracijom koja ne salje email, ne koristi production queue/payment/service discovery i ne menja produkcione podatke.

