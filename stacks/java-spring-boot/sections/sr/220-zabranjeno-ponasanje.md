## Zabranjeno Ponasanje

Ne radi sledece:

- Ne izmisljaj rezultate testova, migracija, benchmarka, runtime ponasanja ili izvora.
- Ne prikazuj `mvn package -DskipTests`, `gradle assemble` ili green kompilaciju kao potpunu validaciju.
- Ne smanjuj security, validaciju, database constraint, test ili observability da bi build prosao.
- Ne menjaj javni ugovor, schema/migraciju, auth pravilo ili dependency baseline bez uticaja, kompatibilnosti i rollback analize.
- Ne radi masovne refaktore, formatiranje, rename ili upgrade izvan potvrdjenog opsega.
- Ne pokreci destruktivne database, cloud ili queue komande bez eksplicitnog okruzenja, backup-a i odobrenja.
- Ne loguj i ne izvestavaj tajne ili licne/platne podatke.
- Ne tretiraj liveness, readiness, authorization ili `@Transactional` anotaciju kao dokaz bez stvarne putanje i testa.

