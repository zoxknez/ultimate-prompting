## 5. Faza 0 - zastiti workspace i utvrdi opseg

### 5.1 Snapshot pre izmene

1. Zabelezi root repozitorijuma, trenutnu granu, commit, remote-e, submodule-e, worktree-je, ignorisane/generisane direktorijume, stanje package manager-a, stanje Rust toolchain-a i necommit-ovane izmene.
2. Zabelezi host operativni sistem, arhitekturu, shell, locale, vremensku zonu, tip fajl sistema, security softver i da li je okruzenje lokalno, VM, CI, container ili remote builder.
3. Popisi postojece installer-e, release artefakte, signing izlaze, notarization logove, update manifeste, store pakete i crash simbole pre generisanja zamena.
4. Hash-uj ili na drugi nacin identifikuj svaki artefakt koriscen kao audit dokaz. Sacuvaj timestamp-e i originalna imena fajlova.
5. Identifikuj direktorijume sa stvarnim korisnickim podacima, produkcionim tajnama, signing kljucevima, sertifikatima, hardware kredencijalima, browser profilima ili stanjem release kanala; iskljuci ih iz destruktivnih testova.
6. Napravi uzak plan izmena i eksplicitne stop uslove pre editovanja.

### 5.2 Pocetni log komandi

```text
Za svaku komandu zabelezi:
- tacnu komandu i argumente;
- radni direktorijum;
- promenljive okruzenja koje uticu na ponasanje, sa redigovanim tajnim vrednostima;
- verzije framework-a, Node-a, package manager-a, Rust-a, Cargo-a, linker-a, compiler-a, packaging i signing alata;
- platformu i arhitekturu;
- exit code;
- sazet stdout/stderr;
- generisane ili izmenjene fajlove;
- nivo dokaza i zakljucak;
- razlog ako komanda nije pokrenuta.
```

