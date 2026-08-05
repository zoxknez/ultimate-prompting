## Istrazivacki Baseline - 5. avgust 2026.

Ovaj baseline je polazna tacka, ne zamena za proveru pri svakom izvrsavanju. Agent mora ponovo proveriti aktuelne izvore pre preporuke ili izmene:

| Komponenta | Stanje 5. avgusta 2026. | Obavezna provera pri auditu |
| --- | --- | --- |
| Java | Java 25 je aktuelni LTS; Java 26 je najnoviji GA feature release. | OpenJDK/Oracle roadmap, JDK distributer, patch i production runtime. |
| Spring Boot | Stabilna linija je 4.1.0; zahteva Java 17-26, Spring Framework 7.0.8+, Tomcat 11/Servlet 6.1 ili Jetty 12.1; GraalVM 25+ za native image. | Projektnu verziju, podrzanu minor liniju, Spring portfolio i migration guide. |
| Spring Boot 4 prelazak | Jakarta EE 11, Servlet 6.1 i Spring Framework 7; uklonjeni deprecated API-ji zahtevaju proveru kompatibilnosti. Za starije projekte prvo dovedi Boot 3 na poslednji 3.5.x patch. | Breaking changes, Spring Cloud release train, pluginove, agente i rollback. |
| Spring Boot podrska | Major verzija najmanje tri godine, ali samo podrzana minor linija; minor najmanje 12 meseci OSS podrske. | Zvanicni support policy i eventualni komercijalni support. |
| Maven | Maven 3.9.16 je preporucena stabilna verzija; Maven 3.10.0-rc-1 i 4.0.0-rc-6 su preview i nisu production izbor. | Wrapper, checksum, JDK build alata i aktivne profile. |
| Gradle | Gradle 9.6.1 je aktuelna stabilna verzija. | Wrapper, checksum, plugin kompatibilnost i toolchain. |
| Observability | Spring Boot koristi Micrometer Observation za metrike i tracing, uz OpenTelemetry integraciju; Actuator daje produkcione endpointe. | Stvarnu instrumentaciju, kardinalnost, propagaciju i izlozenost endpointa. |
| Artefakti | Spring Boot podrzava Dockerfile, Cloud Native Buildpacks, graceful shutdown i GraalVM native/AOT tokove. | Artefakt koji se stvarno deployuje, image, shutdown i native ogranicenja. |

