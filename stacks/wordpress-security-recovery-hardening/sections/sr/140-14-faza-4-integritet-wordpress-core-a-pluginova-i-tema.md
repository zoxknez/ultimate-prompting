## 14. Faza 4 - Integritet WordPress Core-a, Pluginova I Tema

1. Potvrdi detektovanu WordPress verziju i locale.
2. Pokreni core checksum proveru kao signal, a ne kao potvrdu da je sve čisto.
3. Koristi `--include-root` kada je primenljivo da pronađeš neočekivane root fajlove.
4. Uporedi core sa čistim paketom iz zvaničnog izvora.
5. Proveri checksum pluginova iz WordPress.org repozitorijuma kada je dostupan.
6. Za premium, custom ili uklonjene pluginove/teme:
   - utvrdi poreklo
   - nabavi known-good paket od vendora ili iz repozitorijuma
   - zabeleži verziju i izvor preuzimanja
   - uradi rekurzivni diff
   - pregledaj build artefakte i vendor zavisnosti
7. Pregledaj neaktivne pluginove i teme, ne samo aktivne.
8. Pregledaj fajlove van normalnog WordPress stabla i susedne sajtove pod istim nalogom.

### Primeri checksum provere

```bash
wp core verify-checksums --path=/putanja/do/sajta --include-root --skip-plugins --skip-themes
wp plugin verify-checksums --all --strict --path=/putanja/do/sajta
wp core version --extra --path=/putanja/do/sajta --skip-plugins --skip-themes
wp plugin list --fields=name,status,version,update,update_version,auto_update --format=json --path=/putanja/do/sajta
wp theme list --fields=name,status,version,update,update_version,auto_update --format=json --path=/putanja/do/sajta
```

Ne koristi `--insecure`. Ako TLS validacija ne prolazi, popravi trust, network ili proxy konfiguraciju.

