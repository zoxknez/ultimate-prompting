## 9. Faza D - Arhitektura I Granice Modula

1. Mapiraj UI, presentation, domain, data, platform, network, storage, feature i shared slojeve.
2. Potvrdi dependency smer iz koda i Gradle-a, a ne iz package imena.
3. Preferiraj separation of concerns, single source of truth i unidirectional data flow tamo gde poboljsavaju ispravnost.
4. Ne uvodi domain layer ili Clean Architecture ceremoniju bez dokazane slozenosti ili ponovne upotrebe.
5. Proveri da UI komponente ne pristupaju direktno bazama, network client-ima, content provider-ima ili mutable singleton-ima bez opravdanog dizajna.
6. Proveri da repository-ji upravljaju koordinacijom data source-ova i izlozavaju eksplicitno ponasanje.
7. Proveri module boundaries zbog ciklusa, curenja implementation tipova, sirokih shared modula, duplih modela i nestabilnih public API-ja.
8. Proveri da DI scope-ovi odgovaraju Android lifetime-ovima i ne zadrzavaju pogresno activity-je, view-e, context-e, player-e ili naloge.
9. Identifikuj service locator-e, mutable global state, skrivene singleton cache-eve, static callback-e i process-wide state.
10. Proveri da feature granice podrzavaju testiranje, vlasnistvo, build performanse i release ponasanje, a ne samo estetiku direktorijuma.
11. Mapiraj kriticne state tranzicije i persistence granice.
12. Zabelezi arhitektonske izuzetke i obrazlozenje umesto forsiranja uniformnosti.

