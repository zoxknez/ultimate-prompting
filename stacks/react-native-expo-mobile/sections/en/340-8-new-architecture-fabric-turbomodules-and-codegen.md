## 8. New Architecture, Fabric, TurboModules, And Codegen

### 8.1 Architecture Reality
- Prove New Architecture from generated projects, build flags, runtime behavior, loaded libraries, Codegen output, and release artifact rather than configuration intent alone.
- Inventory legacy native modules, legacy view managers, interop layers, TurboModules, Fabric components, Expo Modules, and direct JSI bindings.
- Classify each dependency as fully supported, compatibility-layer dependent, partially supported, forked, patched, unverified, or blocking.
- Do not propose disabling the New Architecture as a permanent fix on lines where the architecture is mandatory.
- Verify brownfield host initialization, multiple surfaces, multiple roots, multiple React instances, and lifecycle ownership.
- Test representative release builds after every change to Codegen, native module registration, Fabric component schema, or JSI code.

### 8.2 Codegen Contracts
- Audit Codegen schema ownership, naming, nullability, optionality, enum evolution, object shape, array size, numeric range, and platform differences.
- Verify generated output is produced by the intended toolchain and is not stale, locally modified, missing from the artifact, or inconsistent across platforms.
- Treat TypeScript specifications as an interface contract, not runtime validation for untrusted values.
- Test old JavaScript with new native code and new JavaScript with old native code only where the release and OTA model permits such overlap.
- Detect schema changes that require a runtimeVersion change, native build, data migration, feature gate, or coordinated backend release.
- Retain generated schema, code, tool versions, and artifact identity as reviewable evidence.

### 8.3 Fabric Components And Native Views
- Audit prop conversion, event registration, command dispatch, state updates, layout measurement, recycling, mounting, unmounting, and native view reuse.
- Verify thread requirements for UI work, layout work, background work, and callbacks into JavaScript.
- Test rapid mount-unmount, navigation replacement, list recycling, interrupted animation, orientation change, fold/unfold, and process recreation.
- Detect retained native views, delegates, listeners, controllers, fragments, activities, contexts, and C++ objects.
- Verify event payloads are bounded, versioned where necessary, and safe under stale or duplicated delivery.
- Correlate Fabric commit and mount timing with user-visible frame drops and native resource pressure.

