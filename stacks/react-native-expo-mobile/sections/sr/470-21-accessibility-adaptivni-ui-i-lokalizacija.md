## 21. Accessibility, adaptivni UI i lokalizacija

### 21.1 Accessibility
- Testiraj screen reader, focus redosled, label, role, state, hint, live region, grouping, heading, modal, gresku i custom gesture.
- Testiraj tastaturu, switch control, external input, D-pad, pointer, TV focus i hardware-key navigaciju gde je podrzano.
- Proveri veliki tekst, font scaling, Dynamic Type, bold text, display zoom, kontrast, nezavisnost od boje, reduced motion, transparency i animation settings.
- Testiraj loading, empty, offline, permission-denied, validation, partial failure, destructive confirmation i success stanje.
- Obezbedi da custom Fabric view, native view, chart, mapa, media kontrola i WebView izloze upotrebljivu accessibility semantiku.
- Koristi automatizovane provere kao dopunu manuelnom testiranju asistivne tehnologije na obe platforme.

### 21.2 Adaptivni layout i lokalizacija
- Testiraj podrzane telefone, tablete, foldable, resizable prozore, split screen, orijentaciju, safe area, tastaturu, cutout i external display.
- Koristi merene adaptivne breakpoint-e i prioritete sadrzaja umesto pretpostavki po nazivu uredjaja.
- Testiraj LTR i RTL layout, bidirectional tekst, promenu locale-a, dug prevod, plural pravila, gramaticke varijante i fallback locale.
- Auditiraj datum, vreme, kalendar, time zone, broj, valutu, decimalnu preciznost, rounding, jedinicu, broj telefona, adresu i sortiranje.
- Proveri da su persistirane vrednosti locale-independent i da migracije ne reinterpretiraju formatirane display stringove kao kanonske podatke.
- Testiraj promenu locale-a i time zone-a dok je aplikacija instalirana, u background-u, offline ili izvrsava dugu operaciju.

