## 7. Model Dokaza I Pouzdanosti

### Status dokaza

Koristi tačno jednu oznaku:

- `POTVRĐENO` - direktno podržano prikupljenim dokazom.
- `VEROVATNO` - više usklađenih indikatora, ali bez konačnog dokaza.
- `MOGUĆE` - razumno i delimično podržano.
- `NEPROVERENO` - nije testirano ili nema dovoljno dokaza.
- `OPOVRGNUTO` - dokaz protivreči hipotezi.

### Kvalitet dokaza

Oceni svaku važnu stavku:

- `E1` - direktan artefakt, pouzdan log, potvrđen hash ili reproduktivno opažanje.
- `E2` - jak prateći dokaz iz najmanje dva nezavisna izvora.
- `E3` - jedan indirektan indikator ili nepotpun artefakt.
- `E4` - nepotvrđena prijava, pretpostavka ili anegdota.

### Chain-of-custody zapis

```text
Evidence ID:
Prikupljeno u (ISO-8601 i vremenska zona):
Prikupio:
Izvorni host/nalog:
Originalna putanja/object ID:
Metod/komanda prikupljanja:
Originalna veličina:
SHA-256:
Vlasništvo i dozvole:
Originalni timestamp-ovi:
Lokacija čuvanja:
Istorija pristupa:
Napomene i redakcije:
```

Kada se kombinuju timestamp-ovi iz više sistema, koristi UTC i lokalnu vremensku zonu. Kada je moguće utvrdi clock drift.

