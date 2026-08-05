## 10. Generated Code, Assets, And Build Inputs

Generated output is part of the product and must be reproducible and reviewed.

- Inventory `build_runner`, Freezed, json serialization, Retrofit, GraphQL, protobuf, localization, route, DI, asset, icon, splash, Pigeon, and custom generators.
- Verify generator versions, inputs, options, output ownership, clean rebuild behavior, and whether generated files are committed intentionally.
- Regenerate in an isolated clean tree and compare output; investigate drift instead of accepting bulk diffs blindly.
- Review generated serialization, platform bindings, routes, registrants, permissions, API clients, and database schemas for security and compatibility.
- Audit asset declarations, wildcard inclusion, secrets accidentally packaged as assets, duplicate media, font licensing, locale coverage, and platform packaging.
- Inspect compile-time constants and `--dart-define` values for environment confusion, secret leakage, dead-code assumptions, and reproducibility.
- Verify icon, splash, manifest, Info.plist, entitlement, desktop metadata, web manifest, and service-worker output in final artifacts.
- Fail CI on unexplained generated drift, missing source inputs, non-reproducible output, or unreviewed privilege changes.

