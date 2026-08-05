## 5. Dokazi, Nalazi I Severity

### 5.1 Sema Nalaza

Za svaki nalaz zabelezi:

```text
ID
severity: P0 | P1 | P2 | P3
status: OPEN | FIXED | CONTAINED | ACCEPTED | REJECTED | UNVERIFIED
komponenta i modul
build type, flavor i okruzenje
uredjaj, API level, ABI i form factor
entry point i user journey
preduslovi i trigger
koraci reprodukcije
ocekivani rezultat
stvarni rezultat
evidence status
lokacija dokaza
root cause
uticaj i blast radius
preporucena popravka
implementirana izmena, ako postoji
verifikacija i regression test
rollback ili containment
preostali rizik
owner i rok, ako su poznati
```

### 5.2 Android-Specific Severity Model

Koristi zajednicki severity model, uz sledeca minimalna tumacenja:

- `P0`: curenje produkcionog kredencijala ili signing kljuca; potvrdjen auth ili tenant bypass; destruktivna ili nepovratna korupcija podataka; release crash loop; remote code execution; iskoristiva exported komponenta sa kriticnim uticajem; pokvaren production update put; potpuni prekid kriticnog playback-a ili poslovnog toka.
- `P1`: cest crash ili ANR; prakticna zloupotreba deep link-a ili intent-a; race koji izaziva duple ili nekonzistentne upise; neuspesna migracija sa rizikom gubitka korisnickih podataka; nekontrolisan foreground service ili battery drain; kritican TV focus trap; nebezbedan WebView ili izlaganje fajlova; release-only kvar; ozbiljan permission, privacy ili policy problem.
- `P2`: merljiva slabost u jank-u, startup-u, memoriji, energiji, lifecycle-u, accessibility-ju, offline radu, error state-u, observability-ju, testabilnosti ili odrzavanju sa stvarnim korisnickim ili operativnim uticajem.
- `P3`: low-impact ciscenje, naming, dokumentacija, neblokirajuca konzistentnost ili opciona modernizacija.

Severity zavisi od uticaja, dostupnosti napada ili kvara, ucestalosti, oporavka i dokaza, a ne od broja prekrsenih style pravila.

### 5.3 Dnevnik Komandi, Build-a I Uredjaja

Za svaku izvrsenu komandu, test, benchmark ili device sesiju zabelezi:

```text
run ID
revision repozitorijuma i dirty stanje
komanda ili akcija
working directory
Android Studio / AGP / Gradle / JDK / Kotlin / SDK / NDK verzije
varijanta, flavor, build type i task
model emulatora ili fizickog uredjaja
Android verzija, API level, ABI, page size i form factor
vreme pocetka i kraja
exit status
upozorenja i greske
sazetak rezultata
lokacija artefakta, izvestaja, trace-a, screenshot-a ili loga
okruzenje izvrsavanja: local | container | CI | device-lab | staging | production-read-only
```

Ne predstavljaj crveni build kao zelen zato sto je jedan nepovezan task prosao.

