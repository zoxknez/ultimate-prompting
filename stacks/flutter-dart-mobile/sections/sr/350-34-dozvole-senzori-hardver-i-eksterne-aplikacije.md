## 34. Dozvole, senzori, hardver i eksterne aplikacije

Traži minimalnu capability u trenutku potrebe i preživi odbijanje ili opoziv.

- Popiši kameru, mikrofon, fotografije, medije, kontakte, kalendar, lokaciju, Bluetooth, nearby devices, notifikacije, local network, USB, serial, NFC, biometriju, health, senzore i screen capture.
- Mapiraj runtime zahteve na manifest/Info.plist/entitlement/desktop deklaracije, purpose tekst, store disclosure-e, privacy manifest-e i stvarne code path-ove.
- Obradi not determined, denied, permanently denied, restricted, limited, approximate, one-time, while-in-use, background i revoked stanja tačno.
- Ne dosađuj ponovljenim zahtevima, ne zaobilazi platformski UI, ne otvaraj settings bez konteksta i ne tvrdi capability koju OS nije odobrio.
- Proveri odsustvo hardvera, zauzet uređaj, prekid, promenu rute, lifecycle tranziciju, multi-window upotrebu, promenu dozvole i cleanup plugin greške.
- Validiraj intent-e eksternih aplikacija, URL-ove, file handoff, povratne vrednosti, spoofed callback-ove, nedostajuće handler-e i izlaganje osetljivih podataka.
- Testiraj fizičke uređaje i relevantne OS verzije; emulator/simulator podrška nije dovoljna za kameru, Bluetooth, background lokaciju, NFC, biometriju, medije i USB.
- Meri uticaj kontinuiranog sensing-a ili skeniranja na bateriju, termiku, radio, CPU, memoriju i privatnost.

