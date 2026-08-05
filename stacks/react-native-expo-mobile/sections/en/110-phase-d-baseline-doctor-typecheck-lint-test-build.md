## Phase D - Baseline Doctor / Typecheck / Lint / Test / Build

```text
npx tsc --noEmit
# lint/jest per project
# Android:
npx react-native run-android --mode=release   # or eas build --profile ...
# iOS:
# archive / eas build
```

Record the first failure. No EAS submit/update to prod.

