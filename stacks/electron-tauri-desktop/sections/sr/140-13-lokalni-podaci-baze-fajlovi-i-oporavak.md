## 13. Lokalni podaci, baze, fajlovi i oporavak

### 13.1 Inventar i klasifikacija podataka

1. Popisi svaku persistent lokaciju: app data, user data, config, cache, logove, crash dump-ove, temp, download-e, baze, browser profile-e, cookie-je, secure storage, OS kredencijale, keychain, registry/plist, shared container-e i removable/network storage.
2. Klasifikuj podatke po vlasniku, nalogu/tenant-u, osetljivosti, retention-u, backup-u, sinhronizaciji, prenosivosti, brisanju i zakonskim zahtevima.
3. Odvoji tajne od preferences, cache od durable stanja, izvedene podatke od source-of-truth podataka i account-specific podatke od device-wide podataka.
4. Dokumentuj putanje po platformi, tipu paketa, portable rezimu, store sandbox-u, enterprise redirection-u, roaming profilu i vise instaliranih kanala.
5. Verifikuj directory i file dozvole posle ciste instalacije, upgrade-a, repair-a, downgrade-a, promene naloga i migracije.
6. Spreci jednog lokalnog OS korisnika, app kanal, nalog, tenant ili prethodnu instalaciju da cita podatke drugog osim kada je eksplicitno dizajnirano.
7. Definisi sta prezivljava uninstall, sta se uklanja, sta zahteva potvrdu korisnika i kako se obradjuju enterprise-managed podaci.
8. Testiraj malo slobodnog diska, read-only media, kvotu, duzinu putanje, Unicode, case razlike, antivirus lock, concurrent pristup i nagli nestanak napajanja.

### 13.2 Baze, migracije, konkurentnost i integritet

1. Identifikuj svaki embedded ili lokalni database engine, tacnu verziju, extension-e, encryption sloj, journal mode, locking model, busy timeout, schema verziju i backup metod.
2. Pregledaj schema constraint-e, foreign key-eve, uniqueness, check-ove, index-e, transaction boundary-je, isolation, conflict handling i recovery.
3. Nikada se ne oslanjaj samo na application validaciju za durable invarijante. Dodaj database constraint-e gde su podrzani i kompatibilni.
4. Dizajniraj migracije za crash safety, idempotency, forward compatibility, rollback ili forward repair, zahteve prostora i preklapanje stare/nove aplikacije.
5. Napravi backup ili snapshot pre destruktivnih migracija. Verifikuj citljivost backup-a i restore u izolovanom okruzenju.
6. Testiraj dva prozora/procesa, background job-ove, sidecar-e, sync engine-e i stare/nove verzije koje pristupaju istim podacima gde je to moguce.
7. Spreci duple eksterne side effect-e oko lokalnih transakcija pomocu idempotency kljuceva, outbox/inbox obrazaca, durable state machine-a ili compensating action-a.
8. Eksplicitno obradi korupciju: detekciju, read-only safe mode, export, granice repair-a, restore, telemetriju, komunikaciju korisniku i zabranu tihog reset-a.
9. Verifikuj cuvanje encrypted database kljuca, rotaciju, recovery, promenu naloga, migraciju uredjaja i ponasanje kada secure storage nije dostupan.
10. Testiraj prekid migracije na svakom durable koraku, downgrade posle migracije, concurrent startup, lock contention, pun disk i korumpiran journal/WAL.

### 13.3 Fajlovi, import, export, arhive i korisnicki sadrzaj

1. Tretiraj svaki importovan, otvoren, prevucen, nalepljen, sinhronizovan ili preuzet fajl kao nepoverljiv bez obzira na ekstenziju.
2. Validiraj format parser-om i sadrzajem, ne samo ekstenzijom ili MIME-om. Ogranici velicinu, dimenzije, broj entry-ja, compression ratio, nesting, parse vreme, memoriju i output.
3. Koristi robustan parser u ogranicenom procesu kada je moguce. Audituj native codec-e i document biblioteke zbog memory-safety i command-execution rizika.
4. Spreci path traversal, apsolutne putanje, symlink extraction, hard-link zloupotrebu, device fajlove, alternate stream-ove, overwrite, nasledjivanje dozvola i archive bomb-e.
5. Kreiraj export atomski sa bezbednim dozvolama i eksplicitnim overwrite ponasanjem. Izbegni curenje tajni, skrivenih kolona, obrisanih zapisa, internih ID-jeva ili podataka nepovezanog naloga.
6. Sanitizuj imena fajlova za svaku platformu bez kreiranja kolizija ili gubitka mogucnosti mapiranja na izvor.
7. Oznaci ili karantiniraj preuzete/generisane fajlove gde platform expectations to zahtevaju i ne otvaraj automatski executable ili active content.
8. Testiraj malformed, truncated, oversized, polyglot, password-protected, nested, malicious-name i concurrently modified fajlove.

