## 42. Adaptivni dizajn, accessibility, lokalizacija i inkluzivan UX

Accessibility i adaptacija su zahtevi ispravnosti, ne završno ulepšavanje.

- Definiši podržane klase prozora, breakpoint-e, orijentaciju, posture, input režime, navigacione obrasce, gustinu informacija i feature parity po platformi.
- Testiraj text scaling iznad uobičajenih default-a, bold text, display zoom, high contrast, color filter-e, dark mode, reduced motion, reduced transparency i promene sistemskog fonta.
- Proveri semantic label-e, uloge, vrednosti, stanja, akcije, traversal redosled, live region-e, heading-e, grupisanje, povezivanje greške i skriven dekorativni sadržaj.
- Testiraj TalkBack, VoiceOver, browser screen reader-e, Narrator, VoiceOver na macOS-u i podržane Linux accessibility alate kroz kritične tokove.
- Proveri keyboard-only i switch access, vidljiv fokus, focus trapping, restoration, shortcut-e, escape/back semantiku, veličinu touch target-a, alternative gestovima i produženje timeout-a.
- Audituj kontrast, non-color signale, bljeskanje, animaciju, autoplay, caption-e, transkript, audio description, haptiku i oporavak od greške.
- Proveri razrešavanje locale-a, fallback, plural/gender pravila, RTL, bidirectional tekst, datum/vreme, vremensku zonu, brojeve, valutu, imena, adrese, sortiranje, pretragu i Unicode normalizaciju.
- Otkrij hard-coded korisnički tekst, spojene prevode, odsečene stringove, nedostajuće ključeve, zastarele generisane lokalizacije, nepreveden native UI i nebezbedan serverski tekst.
- Zahtevaj automatizovane semantics provere plus ručno assistive-technology i locale matrix testiranje kritičnih tokova.

