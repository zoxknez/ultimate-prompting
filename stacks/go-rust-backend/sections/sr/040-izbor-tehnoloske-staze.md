## Izbor Tehnoloske Staze

Na pocetku utvrdi jednu od:

| Staza | Kada |
| --- | --- |
| `GO` | Samo Go moduli/paketi/executable. |
| `RUST` | Samo Rust crate/workspace/executable. |
| `MIXED_GO_RUST` | Oba jezika u istom sistemu. |
| `UNKNOWN` | Nedovoljno dokaza; prvo inventar, ne nagadjaj. |

Za `MIXED_GO_RUST`:

- zajednicka analiza sistema;
- puna Go staza za Go module;
- puna Rust staza za Rust crate/workspace;
- posebna analiza FFI, IPC, mreznih i podatkovnih granica izmedju njih.

Ne primenjuj Go preporuke na Rust deo niti Rust preporuke na Go deo bez jasne tehnoloske granice.

