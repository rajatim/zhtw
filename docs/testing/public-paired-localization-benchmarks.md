<!-- zhtw:disable -->
# Public Paired Localization Benchmarks

## Purpose

This package lets the project test zhtw against public Simplified/Traditional
localization maintained by AOSP, Microsoft, and Mozilla. It adds external
evidence without waiting for an outside reviewer.

It is project-run evidence. It must not be described as independent third-party
validation.

## Sources

| Track | Input | Reference | Cases | License | Known overlap |
|---|---|---|---:|---|---|
| AOSP framework UI | `zh-rCN` | `zh-rTW` | 1,968 | Apache-2.0 | Blind-v2 source pool |
| VS Code UI | `zh-hans` | `zh-hant` | 17,133 | MIT | Blind-v2 source pool |
| Firefox browser UI | `zh-CN` | `zh-TW` | 1,264 | MPL-2.0 | None known |

Every manifest pins an exact upstream commit, raw SHA-256 values, attribution,
license, normalized dataset hash, and known bias.

## Pairing Rules

The importer uses structured parsers instead of text matching:

- Android XML pairs `string` resources by name and product variant.
- VS Code JSON pairs string leaves by full module/message path.
- Firefox Fluent uses `fluent.syntax` and pairs plain-text messages and
  attributes by file and identifier.

A case is excluded when a key is missing on either side, placeholders differ,
the value is multiline, the structure contains unsupported rich expressions,
the input has no Han text, or the same input/reference pair already exists.

## Reproduction

Verify that current upstream downloads still match the pinned hashes and that
normalization is deterministic:

```bash
make benchmark-paired-import-check
```

Run zhtw-only aggregate diagnostics:

```bash
make benchmark-paired-report DATE=2026-07-31
```

Run a locked comparison against the primary OpenCC and zhconv family
representatives:

```bash
image="zhtw-benchmark-competitors:$(jq -r '.environment.environment_sha256' \
  benchmarks/accuracy/competitors.lock.json | cut -c1-12)"

for id in aosp-framework-paired-ui-v1 vscode-paired-ui-v1 firefox-paired-ui-v1; do
  uv run python scripts/run_paired_localization_benchmark.py \
    --manifest "benchmarks/accuracy/manifests/$id.json" \
    --engines zhtw,opencc-s2twp,zhconv-zh-tw \
    --container-image "$image" \
    --generated-date 2026-07-31 \
    --output-prefix "docs/reports/$id-benchmark-2026-07-31"
done
```

## Interpretation

Exact match is intentionally strict. A miss can mean a converter error, a valid
Taiwan variant, or a vendor rewrite that is outside normal script conversion.
Changed-span scores help show partial agreement, but they do not turn the vendor
translation into ground truth.

The tracks can strengthen or challenge a broad claim. They cannot change the
frozen Blind-v2 ranking, and they cannot prove normal-traffic accuracy. AOSP and
VS Code are especially limited as fresh evidence because their Simplified
sources were represented in the Blind-v2 source pool.
