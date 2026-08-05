## Faza B - Inventar Projekta I Build Sistema

Mapiraj root/child Maven module, Gradle root/subproject/included build, source i test source setove, generated source, shared/domain/API/persistence/messaging/batch/infrastructure/test-fixture module, migracije, native hintove, Docker/Kubernetes/Terraform/Helm konfiguraciju i CI workflow. Prikazi smer zavisnosti i jasno oznaci cikluse, framework leakage u domenu, nejasno vlasnistvo, duplirane modele, rucno menjani generisani kod i neaktivne module.

Odredi jedan stvarni build tok. Ne pokreci Maven i Gradle nasumicno. Za Maven proveri wrapper, parent/BOM, `dependencyManagement`, profile, Enforcer, toolchain, compiler `release`, Surefire/Failsafe, resource filtering, pluginove, repozitorijume, snapshot-e, shading/repackage i generated sources. Kada je bezbedno, koristi `./mvnw --version`, `help:active-profiles`, ciljano `help:effective-pom`, `dependency:tree` i `dependency:analyze`. Globalni `mvn` koristi samo za eksplicitno poredjenje okruzenja.

Za Gradle proveri wrapper i checksum, pluginove, version catalog, constraints/platform, toolchain, source/target kompatibilnost, test suite/source setove, configuration/build cache, custom taskove, dependency locking/verification, repository content filtere, dynamic/changing verzije i annotation processing. Kada je bezbedno koristi `./gradlew --version`, `projects`, `tasks`, `javaToolchains`, `buildEnvironment`, `dependencies` i `properties`; `dependencyInsight` samo ciljano.

Klasifikuj dependency-je na Boot-managed, direktno verzionisane, tranzitivne, zastarele, konfliktne, nekoriscene, runtime/compile/annotation/test-only, native-nekompatibilne, CVE-potvrdjene, preview i nestandardne repository zavisnosti. Posebno proveri Spring Cloud/Boot mapiranje, Jackson, Hibernate/driver, Reactor/Netty, logging, Security, validation, cache/messaging klijente, APM/OpenTelemetry i test biblioteke. Ne menjaj pojedinacne Spring BOM-managed verzije bez dokumentovanog razloga.

