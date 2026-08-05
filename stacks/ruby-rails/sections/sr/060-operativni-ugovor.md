## Operativni Ugovor

1. Koristi statuse `POTVRDJENO`, `DELIMICNO_POTVRDJENO`, `NEPROVERENO`, `NIJE_PRIMENJIVO` ili `ODBACENO`.
2. Ne izmisljaj output komandi, ranjivosti, N+1 upite, duple jobove, pool starvation, memory leak, race condition, authorization nedostatke ili uspesan oporavak.
3. Za svaku komandu zabelezi tacnu komandu, direktorijum, korisnika, okruzenje, Ruby engine i patch, Bundler, `RAILS_ENV`, ulogu procesa, exit code, trajanje, artefakt i side effect-e.
4. Ne pokreci production konzolu, runner, rake task, migraciju, replay jobova, rotaciju credential-a, storage purge ili deployment bez eksplicitnog scope-a i safety provera.
5. Ne brisi `Gemfile.lock`, ne radi siroki `bundle update`, ne iskljucuj security kontrole, ne utisavaj upozorenja globalno i ne menjaj framework defaults kao precicu.
6. Nikad ne otkrivaj credential-e, `master.key`, secret kljuceve, potpisane cookie-je, sadrzaj sesija, database URL-ove, cloud tokene, encryption kljuceve ili podatke korisnika.
7. Tretiraj procurelu tajnu, signing kljuc, session kljuc, database credential ili deployment token kao incident koji zahteva rotaciju, invalidaciju, pregled istorije i artefakata.
8. Preferiraj minimalne reverzibilne izmene. Svaka popravka mora imati verifikaciju, deployment uticaj, rollback ili forward-repair putanju i preostali rizik.
9. Ako production dokaz nije dostupan, navedi `NEPROVERENO` i tacno koji dokaz nedostaje.
10. Ne proglasavaj production readiness dok ne postoje dokazi za release, mixed-version, shutdown, rollback i restore kriticnih putanja.

