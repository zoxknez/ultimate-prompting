## 26. Zabranjene Precice

Ne radi sledece:

1. Ne proglasavaj aplikaciju production-ready zato sto `assembleDebug` prolazi.
2. Ne iskljucuj R8, resource shrinking, lint, testove, TLS validation, signing provere ili dozvole da bi build prosao.
3. Ne koristi debug signing ili debug endpoint-e u produkciji.
4. Ne dodaj siroka keep pravila bez dokaza zasto su potrebna.
5. Ne koristi `GlobalScope`, unmanaged executor-e, stvarne sleep-ove ili swallowed exception kao popravke.
6. Ne menjaj transaction, idempotency ili autorizaciju samo UI disable-ovanjem dugmeta.
7. Ne cuvaj tajne u source-u, resursima, BuildConfig-u, assets, native string-u ili reverzibilnoj obfuscation i ne nazivaj ih bezbednim.
8. Ne prihvataj sve sertifikate, ne iskljucuj hostname verification i ne dozvoljavaj cleartext globalno.
9. Ne proglasavaj exported komponentu, deep link, WebView ili file provider bezbednim bez testiranja hostile input-a.
10. Ne koristi destructive Room migration fallback za korisnicke podatke bez eksplicitnog odobrenja i recovery-ja.
11. Ne tvrdi 16 KB podrsku samo zato sto se aplikacija instalira na normalnom emulatoru.
12. Ne tretiraj emulator-only uspeh kao dokaz za codec, DRM, camera, Bluetooth, TV, OEM ili thermal ponasanje.
13. Ne izmisljaj command output, test rezultat, profiler metriku, Play Console stanje, policy eligibility ili citate izvora.
14. Ne radi nepovezan mass upgrade ili rewrite dok popravljas jedan problem.
15. Ne proglasavaj kriticnu oblast bezbednom zato sto pristup ili dokaz nedostaje.
16. Ne ignorisi release-only, minified, offline, low-memory, process-death ili account-switching ponasanje.

