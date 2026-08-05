## 21. Observability, crash reporting, privatnost i forenzika

1. Definisi structured logove, metrike, trace-ove, crash report-ove, update event-e, installer event-e, security event-e i user-visible diagnostic export.
2. Ukljuci verziju, kanal, commit/artifact identitet, platformu, arhitekturu, OS verziju, relevantnu WebView/Chromium/Node/Rust verziju, tip procesa, window label-u, correlation ID i operation stanje gde je bezbedno.
3. Rediguj tajne, tokene, cookie-je, authorization header-e, sadrzaj fajlova, licne putanje, korisnicka imena, nazive dokumenata, database zapise, clipboard podatke i osetljive URL-ove.
4. Koristi sampling i rate limit-e da sprecis telemetry storm, prekomerno prikupljanje privatnih podataka, pun disk i recursive crash-reporting otkaz.
5. Upload-uj simbole i source map-e vezane za tacne hash-eve artefakta. Ogranici pristup i retention.
6. Razlikuj renderer/webview, main/Rust core, GPU, utility, sidecar, installer, updater i native izvore crash-a.
7. Prati startup uspeh, crash-free session-e, adoption/failure update-a, rollback, migration failure, permission denial, IPC/command denial, queue saturation i resource budget-e.
8. Obezbedi privacy-preserving lokalni diagnostic bundle sa eksplicitnim korisnickim pregledom i pristankom gde je primereno.
9. Sacuvaj chain of custody za incident artefakte i izbegni menjanje kompromitovanih sistema pre snimanja dokaza.
10. Svaki produkcioni alert mora imati vlasnika, obrazlozenje praga, dashboard/kontekst, runbook i tumacenje uticaja na korisnika.

