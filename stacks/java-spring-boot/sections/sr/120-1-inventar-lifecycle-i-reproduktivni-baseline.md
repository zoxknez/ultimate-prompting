## 1. Inventar, Lifecycle I Reproduktivni Baseline

Mapiraj Maven/Gradle wrapper i verzije, Java toolchain, `pom.xml`/`build.gradle`, dependency management, repozitorijume, lock fajlove, profile, compiler flagove, annotation procesore, test suiteove, Spring Boot/Framework/Security verzije, MVC naspram WebFlux-a, entry point, auto-configuration exclusions, beanove, filter chainove, controllere/rute, DTO validaciju, JPA context-e i migracije, jobove/schedulere, queue-ove, cache, autentikaciju, konfiguraciju, Actuator, deployment, CI/CD i testove.

Proveri tacne Java i Spring Boot verzije prema aktuelnom lifecycleu i poslednjem patchu. U vreme audita proveri stvarne system requirements umesto hardkodovanja; na primer Spring Boot 4.1 zahteva Java 17 ili visu. Razdvoji JVM JAR, WAR, container i GraalVM native-image pakovanje, pa validiraj njihove razlicite runtime, reflection, resource, observability, memory i startup granice.

Napravi mapu toka `client -> CDN/load balancer/reverse proxy -> servlet/reactive server -> filter chain -> controller/router -> authentication -> authorization -> validation -> service -> transaction -> database/cache/queue/external dependency -> response`.

Pokreni deterministicko dependency razresavanje, kompilaciju, static analysis, proveru formatiranja gde je konfigurisana, unit/integration/security/contract testove, startup paketovanog artefakta, status migracija, health/readiness probe, dependency vulnerability/SBOM provere i graceful-shutdown test gde je podrzan. Zabelezi komande, tool/JDK verzije, exit kodove, pocetni neuspeh i da li je uzrok kod, konfiguracija, tajna, spoljna zavisnost ili lokalno okruzenje.

