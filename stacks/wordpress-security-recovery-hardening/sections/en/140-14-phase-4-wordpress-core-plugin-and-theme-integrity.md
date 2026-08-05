## 14. Phase 4 - WordPress Core, Plugin And Theme Integrity

1. Verify the detected WordPress version and locale.
2. Run core checksum verification as a signal, not a clean bill of health.
3. Use `--include-root` where appropriate to identify unexpected root files.
4. Compare core against a clean package from the official source.
5. Verify WordPress.org plugin checksums where available.
6. For premium, custom or removed plugins/themes:
   - establish provenance
   - obtain a known-good package from the vendor or repository
   - record version and download source
   - compare recursively
   - review build artifacts and vendor dependencies
7. Inspect inactive plugins/themes as well as active ones.
8. Inspect files outside the normal WordPress tree and neighboring sites under the same account.

### Checksum examples

```bash
wp core verify-checksums --path=/path/to/site --include-root --skip-plugins --skip-themes
wp plugin verify-checksums --all --strict --path=/path/to/site
wp core version --extra --path=/path/to/site --skip-plugins --skip-themes
wp plugin list --fields=name,status,version,update,update_version,auto_update --format=json --path=/path/to/site
wp theme list --fields=name,status,version,update,update_version,auto_update --format=json --path=/path/to/site
```

Do not use `--insecure`. If TLS validation fails, fix trust, networking or proxy configuration.

