<!-- zhtw:disable -->
# Benchmark Data Licenses

Every dataset manifest must reference a matching `notice_id` heading in this
file. A manifest is invalid when its attribution or output-license obligation
is missing.

## zhtw-project-original

- Source: Original zhtw benchmark and regression material.
- License: MIT unless a case records a more restrictive source license.
- Attribution: Copyright zhtw contributors.
- Modifications: Human annotation and Taiwan Traditional normalization.
- Output license: MIT.

## ud-gsd-v1

- Source: Universal Dependencies Chinese GSD commit
  `e0d85a020182e264d6384be2a59c0f4879a1cc35` and Chinese GSDSimp commit
  `7b61ed473f963e911788efdf1f478154bc1053e4` (tag `r2.18`).
- License: CC BY-SA 4.0
- Attribution: Universal Dependencies Chinese GSD contributors and Chinese GSDSimp contributors.
- Modifications: Extracted paired sentence text by sent_id, normalized JSON serialization, and added benchmark metadata; no linguistic content was corrected by zhtw.
- Output license: CC BY-SA 4.0
- Bias notice: GSDSimp was initially generated with OpenCC and later manually
  corrected. Results are secondary evidence and are not independent evidence
  against OpenCC-family converters.

## naer-terms-v1

- Source: Taiwan National Academy for Educational Research terminology data at
  the revision and retrieval date pinned by the future manifest.
- License: Taiwan Government Data Open License, version 1.0.
- Attribution: National Academy for Educational Research; no endorsement implied.
- Modifications: Field selection, context filtering, deduplication, and benchmark
  metadata enrichment.
- Output license: Taiwan Government Data Open License, version 1.0.

## sc-tc-regional-v1

- Source: SC-TC regional benchmark data, only after its repository data-file
  license is independently verified and pinned in a manifest.
- License: Pending verification; no derived data may be committed yet.
- Attribution: Pending verified upstream attribution.
- Modifications: None permitted before license verification.
- Output license: Pending verification.
