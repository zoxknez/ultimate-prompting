## Phase F - RubyGems, Bundler And Supply Chain

```text
bundle check
bundle platform
bundle list
bundle outdated --strict
bundle doctor
bundle config list
gem env
```

- Audit sources, mirrors, credentials, Git gems, path gems, floating branches, prereleases, broad constraints, platforms, groups and conditional dependencies.
- Verify lockfile platforms, Ruby version, Bundler version, checksums where supported and deterministic deployment mode.
- Treat gem installation hooks, extensions, executables, plugins, code generators and Rake tasks as executable supply-chain inputs.
- Review yanked releases, advisories, provenance, MFA ownership signals, licenses and transitive native libraries.
- Use targeted updates and preserve a reviewed dependency diff. Never solve drift by deleting the lockfile.

