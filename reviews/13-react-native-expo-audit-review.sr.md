# Revizioni izvestaj 13 - React Native / Expo / Android / iOS

## Rezime

Postojeci EN/SR par je imao dobar osnovni paritet, ali je bio prekratak za dokaziv production audit. Nova verzija 2.0.0 uvodi formalni E0-E5 evidence model, P0-P3 severity, source-to-runtime identitet, obavezne matrice dokaza, adversarial scenarije i kompletan release, OTA, rollback, restore i incident ugovor.

## Najvaznije promene

- Generisani i rucno odrzavani native projekti vise se ne tretiraju isto.
- Expo Go, development build i store release imaju odvojene nivoe dokaza.
- New Architecture, Fabric, TurboModules, Codegen, Expo Modules i JSI imaju posebne thread, memory i ABI provere.
- EAS Update je razdvojen na runtime kompatibilnost, trust, signing, kanal, rollout, crash-loop recovery i rollback.
- Android i Apple imaju nezavisne build, artifact, signing, install, device, performance, accessibility i recovery matrice.
- Lokalni podaci, offline queue, background taskovi, push, deep linkovi, WebView, dozvole i native callback lifecycle imaju obavezne failure scenarije.
- CI/CD, provenance, SBOM, store submission, credential revocation i trusted rebuild su deo Definition of Done.

## Rezultat

Paket je spreman kao production-candidate master prompt. Konacna readiness tvrdnja za konkretnu aplikaciju i dalje zavisi od stvarnih E0-E5 dokaza.
