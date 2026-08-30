# Current version

Current version: **4.5.0** (2026-08-30).

## 4.5.0 highlights

- Added an explicitly enabled JSON string-value adapter that preserves object keys, structure, and unchanged content.
- Added the `explain` CLI and cross-SDK APIs with stable rule IDs, spans, layers, outcomes, and reason codes.
- Added rule schema v2 metadata, stable IDs, and a human review lifecycle.
- Extended Unicode 17.0 Han validation and safe mixed Chinese, English, and number term imports.
- Strengthened Jenkins-only candidates, verification, supply-chain audits, package smoke tests, and interrupted-release recovery.

See the [4.5.0 CHANGELOG](https://github.com/rajatim/zhtw/blob/main/CHANGELOG.md#450---2026-08-30) for all fixes and security updates.

## Compatibility

- Python: 3.10 to 3.13.
- Java: 11 or later; candidates are tested on 11, 17, and 21.
- Node.js: 20 or later; candidates are tested on 20 and 22.
- Rust: minimum supported toolchain 1.80.1, plus stable.
- .NET: `netstandard2.0` and `net8.0`.
- See each package README for Go and Browser WASM requirements.

All SDKs use one version. Do not mix runtime and shared-data versions during an upgrade.

## Public release evidence

Public registries, the GitHub tag, release notes, and checksums must point to the same candidate content. Registry versions are never reused or overwritten. A content fix requires a new patch version.

Internal Jenkins receipts and credential operations are not part of the public API. Users can verify releases through [GitHub Releases](https://github.com/rajatim/zhtw/releases) and each package registry.
