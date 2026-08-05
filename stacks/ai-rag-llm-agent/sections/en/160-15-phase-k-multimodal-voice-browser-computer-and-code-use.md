## 15. Phase K - Multimodal, Voice, Browser, Computer And Code Use

1. Treat text, images, PDFs, audio, video, OCR, metadata, captions, DOM, accessibility trees, and screenshots as untrusted inputs.
2. Test hidden and visually embedded instructions, adversarial overlays, steganographic or metadata-based content where relevant, and cross-modal conflicts.
3. Verify browser navigation, downloads, uploads, clipboard, login state, cookies, local files, and external links follow least privilege.
4. Apply exact destination and URL controls for automatic navigation or retrieval where possible.
5. Isolate code execution with resource, filesystem, process, package, secret, and network controls.
6. Validate generated code before execution and never run it with unnecessary host or production privileges.
7. For voice, verify consent, recording indicators, transcription retention, speaker ambiguity, interruption, accidental activation, and high-impact verbal confirmation.
8. For computer use, require visible confirmation for high-impact actions and test UI ambiguity, layout changes, malicious pages, and stale screenshots.
9. Verify downloaded artifacts are scanned, typed, size-limited, and stored safely.

