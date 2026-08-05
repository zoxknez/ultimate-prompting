<!-- section:STACK-NEXTJS-OVERLAY-FOCUS -->
# Next.js Master Stack Overlay

## Mandatory Audit Domains

1. **App Router & Server Components / Actions**:
   - Verify server-side authorization on all Server Actions and Route Handlers.
   - Audit `use cache`, `cacheTag`, and revalidation rules for data leakage across requests.
   - Inspect Proxy / Middleware boundary to ensure it does not replace data-layer AuthZ.

2. **Core Web Vitals & Performance**:
   - Audit LCP, INP, CLS optimization, font loading, script strategy, and image optimization.
   - Inspect bundle size, dynamic imports, and RSC payload serialization overhead.

3. **Security & Data Boundaries**:
   - Check CSRF, CORS, CSP headers, dangerouslySetInnerHTML, and hydration mismatch risks.
   - Inspect environment variable exposure (`NEXT_PUBLIC_` vs server-only secrets).
