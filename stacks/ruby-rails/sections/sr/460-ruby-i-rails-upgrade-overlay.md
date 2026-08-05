## Ruby I Rails Upgrade Overlay

1. Prvo patchuj trenutne podrzane Ruby i Rails linije kada postoje hitne security popravke.
2. Nadogradi Ruby odvojeno od Rails-a gde je moguce i uporedi interpreter, native-gem, GC, YJIT i performance ponasanje.
3. Ukloni deprecation-e i blokirajuce gemove pre promene Rails minor ili major linije.
4. Pokreni `app:update` u pregledanoj grani i pregledaj svaku config i default izmenu.
5. Namerno pregledaj `config.load_defaults`; ne kopiraj konfiguraciju nove aplikacije slepo.
6. Testiraj framework komponente odvojeno: Active Record, Active Job, Action Cable, Active Storage, Action Mailer, Hotwire i asset-e.
7. Dokazi mixed-version deployment, database kompatibilnost, queued payload kompatibilnost i rollback pre production cutover-a.
8. Napreduj jedan podrzani korak odjednom i sacuvaj izmeren pre i posle baseline.

