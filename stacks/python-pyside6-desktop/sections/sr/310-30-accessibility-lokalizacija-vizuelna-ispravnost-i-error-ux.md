## 30. Accessibility, lokalizacija, vizuelna ispravnost i error UX

### 30.1 Obim audita

1. Inventariši podržane jezike, pisma, locale-e, vremenske zone, kalendare, brojanje, valute, jedinice, plural pravila, input metode, teme, contrast režime i motion preference.
2. Pregledaj accessible nazive, uloge, stanja, opise, odnose, live update-e, redosled fokusa, keyboard rad, shortcut-e, mnemonic-e i screen-reader izlaz.
3. Proceni skaliranje teksta, high DPI, fractional scaling, duge prevode, right-to-left layout, bidirectional tekst, emoji, combining mark-ove, truncation i font fallback.
4. Pregledaj kontrast boja, indikatore koji nisu samo boja, vidljivost fokusa, target size, reduced motion, flashing, cancellation animacija i grafičke alternative.
5. Mapiraj user-visible error stanja za validaciju, permission denial, offline, timeout, partial failure, cancellation, korumpirane podatke, update kvar i recovery.
6. Obezbedi da su greške actionable bez izlaganja tajni, stack trace-a, internih putanja, identifikatora ili lažnih success stanja.

### 30.2 Obavezna verifikacija

1. Testiraj kritične tokove samo tastaturom, screen reader-ima, high contrast-om, 200 procenata ili policy-required skaliranjem teksta, RTL-om, dugim prevodima i reduced motion-om.
2. Pokreni zapakovane build-ove na svakoj platformi jer se native accessibility bridge-evi, fontovi, meniji, dialogi i shortcut-i razlikuju od source testova.
3. Verifikuj fokus i announcement-e tokom asinhronog progress-a, validation kvara, modalnih dialoga, notifikacija, zamene stranice i recovery-ja od greške.
4. Testiraj promene locale-a i vremenske zone, dvosmislene datume, daylight-saving tranzicije, Unicode imena fajlova i mixed-script unos.
5. Zahtevaj screenshot-ove ili snimke za vizuelne regresije i accessibility dokaze gde automatizacija nije dovoljna.

