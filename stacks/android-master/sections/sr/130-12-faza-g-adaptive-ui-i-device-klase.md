## 12. Faza G - Adaptive UI I Device Klase

### 12.1 Telefoni, Tableti, Foldable I Desktop-Like Rezimi

1. Testiraj compact, medium i expanded window size, a ne samo imena uredjaja ili orijentaciju.
2. Proveri resize, split-screen, freeform, multi-window, fold posture, hinge, desktop mode, tastaturu, misa, trackpad i stylus gde su podrzani.
3. Izbegavaj orientation lock i resizability ogranicenja osim ako use case i policy to opravdavaju.
4. Proveri da se list-detail, navigation, dialog, sheet, grid, media i forme prilagodjavaju bez slepog rastezanja phone UI-ja.
5. Testiraj cutout-e, inset-e, edge-to-edge, status i navigation bar, IME, gesture navigation i display density.
6. Proveri focus order, keyboard navigation, hover, context menu, shortcut-e i selection za vece uredjaje.
7. Testiraj kontinuitet state-a pri resize-u ili prebacivanju izmedju display-a.
8. Proveri screenshot i sensitive content ponasanje u recents i na eksternim display-ima.

### 12.2 Android TV I D-Pad

1. Mapiraj focus traversal za svaki ekran, rail, row, dialog, overlay, player, search i empty ili error state.
2. Proveri vidljiv focused state, deterministicki initial focus, focus restoration i odsustvo focus trap-a.
3. Testiraj D-pad, back, play, pause, seek, channel, menu, long press i varijacije daljinskih upravljaca proizvodjaca.
4. Proveri overscan-safe layout, citljivost sa distance, target size, contrast i motion.
5. Proveri da lazy liste pravilno cuvaju focus kada se podaci promene, stranice ucitavaju, filter promeni ili item nestane.
6. Proveri player controls, active audio, multiview, buffering, retry, parental gate i screen-on ponasanje.
7. Testiraj TV launcher intent, banner-e, recommendations, preview channel-e, media session i background playback gde je primenjivo.
8. Proveri da su touch-only pretpostavke uklonjene iz TV tokova.
9. Testiraj low-memory TV uredjaje i sporiji storage ili network uslove.

### 12.3 Wear OS, Automotive I Druge Device Povrsine

1. Primeni samo ako postoje i koristi aktuelne platform-specific quality smernice.
2. Proveri rotary input, ambient mode, tile-ove, complication-e, small-screen navigaciju i battery ogranicenja za Wear OS.
3. Proveri driver-distraction, parked naspram driving state-a, template-e, media, messaging i manifest deklaracije za Android Auto ili Automotive.
4. Proveri companion-device association, cross-device state, dozvole i disconnect recovery.
5. Razdvoji device-specific kod i policy bez nepotrebnog dupliranja core business logike.

