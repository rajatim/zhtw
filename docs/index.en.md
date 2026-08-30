# ZHTW documentation

ZHTW is a conservative converter from Simplified Chinese and Hong Kong Traditional Chinese to Taiwan Traditional Chinese. It is designed for source code, locale files, documents, and automated checks.

The current stable version is **4.5.0**. One shared rule set supports the Python CLI, Python, Java, TypeScript, Rust, Go, .NET, and browser WebAssembly.

## Where to start

- New to ZHTW: read the [five-minute start](guides/getting-started.md).
- Scanning or fixing files: read [CLI and files](guides/cli-and-files.md).
- Integrating an app or browser: read [SDKs and Browser WASM](guides/sdk-and-browser.md).
- Finding why a term changed or stayed unchanged: read the [Explain API](reference/explain-api.md).
- Checking accuracy claims: read [Quality and evidence](testing/quality-and-evidence.md).

## Design principles

ZHTW does not use OpenCC as a runtime dependency. It also does not assume that every Simplified Chinese character has one safe Traditional Chinese answer. Conversion applies term rules, identity protection, optional balanced mode, and then safe one-to-one character mappings.

See [Conversion behavior and limits](reference/conversion-behavior.md) for the full boundary.

## Public and internal documentation

This site is the source of truth for product behavior, public APIs, quality evidence, and version information. Internal Jenkins job numbers, credentials, approvals, and recovery steps are not part of the public product contract.
