<!-- section:CORE-PRODUCTION-READINESS-DOD -->
# Jezgro — Definicija Završenosti Spremnosti za Produkciju (DoD)

Označiti svaku primenljivu stavku sa `POTVRDJENO` / `NEVERIFIKOVANO` / `NIJE_PRIMENLJIVO` uz dokaze.

## Minimum (svi stack-ovi)

1. Radni prostor zaštićen; nekomitovan rad zabeležen
2. Stvarni stack/runtime/toolchain identifikovan
3. Životni ciklus/EOL proveren u odnosu na **trenutne** primarne izvore
4. Graf zavisnosti + integritet lockfile-a pregledan
5. Osnovni status instalacije/build-a/testa zabeležen sa stvarnim komandama
6. Kritični korisnički/poslovni tokovi mapirani
7. Autentifikacija/Autorizacija (ili N/A) sa pozitivnim i negativnim slučajevima
8. Tajne nisu procurele u kodu, logovima ili izveštaju
9. P0/P1 popravljen ili izolovan sa tokom oporavka
10. P0–P2 popravke imaju regresione testove gde je izvodljivo
11. Strategija puštanja/vraćanja (ili pakovanja/ažuriranja) dokumentovana
12. Opservabilnost dovoljna za dijagnostiku incidenata (ili naveden jaz)
13. Neverifikovane oblasti eksplicitne
14. Završni diff bez nebitnog šuma
15. Bez tvrdnje o spremnosti za produkciju bez dokaza

Stack overlay-i dodaju specifične stavke DoD-a.
