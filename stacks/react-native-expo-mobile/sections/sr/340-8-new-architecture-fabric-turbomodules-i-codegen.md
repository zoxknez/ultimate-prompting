## 8. New Architecture, Fabric, TurboModules i Codegen

### 8.1 Stvarno stanje arhitekture
- Dokazi New Architecture iz generisanih projekata, build flag-ova, runtime ponasanja, ucitanih biblioteka, Codegen izlaza i release artefakta, a ne samo iz konfiguracione namere.
- Popisi legacy native module, legacy view manager, interop sloj, TurboModule, Fabric komponentu, Expo Module i direktan JSI binding.
- Klasifikuj svaku zavisnost kao potpuno podrzanu, zavisnu od compatibility sloja, delimicno podrzanu, forkovanu, patch-ovanu, neproverenu ili blokirajucu.
- Ne predlazi trajno iskljucivanje New Architecture kao popravku na linijama gde je arhitektura obavezna.
- Proveri brownfield host inicijalizaciju, vise surface-a, vise root-ova, vise React instanci i lifecycle ownership.
- Testiraj reprezentativni release build posle svake promene Codegen-a, registracije native modula, Fabric component scheme ili JSI koda.

### 8.2 Codegen ugovori
- Auditiraj vlasnistvo Codegen scheme, naming, nullability, optionality, enum evoluciju, oblik objekta, velicinu niza, numericki opseg i platformske razlike.
- Proveri da nameravani toolchain proizvodi generisani izlaz i da on nije stale, lokalno izmenjen, izostavljen iz artefakta ili neuskladjen izmedju platformi.
- Tretiraj TypeScript specifikacije kao interface ugovor, a ne runtime validaciju nepoverljivih vrednosti.
- Testiraj stari JavaScript sa novim native kodom i novi JavaScript sa starim native kodom samo gde release i OTA model dozvoljava takav overlap.
- Otkrij schema promene koje zahtevaju promenu runtimeVersion-a, native build, data migraciju, feature gate ili koordinisano backend izdanje.
- Sacuvaj generisanu schemu, kod, verzije alata i identitet artefakta kao pregledan dokaz.

### 8.3 Fabric komponente i native view
- Auditiraj konverziju prop-a, registraciju event-a, command dispatch, state update, layout measurement, recycling, mounting, unmounting i reuse native view-a.
- Proveri thread zahteve za UI rad, layout rad, background rad i callback ka JavaScript-u.
- Testiraj brzo mount-unmount ponavljanje, navigation replacement, list recycling, prekinutu animaciju, promenu orijentacije, fold/unfold i rekreiranje procesa.
- Otkrij zadrzani native view, delegate, listener, controller, fragment, activity, context i C++ objekat.
- Proveri da su event payload-i ograniceni, verzionisani gde je potrebno i bezbedni pri stale ili duploj isporuci.
- Koreliraj Fabric commit i mount timing sa korisniku vidljivim padom frame-a i pritiskom na native resurse.

