<!-- section:STACK-NEXTJS-OVERLAY-FOCUS -->
# Next.js Master Overlay Stack-a

## Obavezne Oblasti Audita

1. **App Router & Server Komponente / Akcije**:
   - Proveriti autorizaciju na strani servera na svim Server Akcijama i Route Handler-ima.
   - Auditovati `use cache`, `cacheTag` i pravila revalidacije za curenje podataka između zahteva.
   - Pregledati Proxy / Middleware granicu i osigurati da ne zamenjuje AuthZ u sloju podataka.

2. **Core Web Vitals & Performanse**:
   - Auditovati LCP, INP, CLS optimizaciju, učitavanje fontova, strategiju skripti i optimizaciju slika.
   - Pregledati veličinu bundle-a, dinamičke uvoze i režijski trošak RSC payload serijalizacije.

3. **Bezbednost & Granice Podataka**:
   - Proveriti CSRF, CORS, CSP zaglavlja, dangerouslySetInnerHTML i rizike neslaganja hidracije.
   - Pregledati izloženost promenljivih okruženja (`NEXT_PUBLIC_` vs server-only tajne).
