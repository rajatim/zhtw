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

## flores-200-zho-hans-v1

- Source: FLORES-200 archive associated with `facebookresearch/flores` commit
  `a6c830c6e1051fb4ac1a44b32358f00463f332bd`; archive S3 version
  `KJZoZnGvyduN3osrx.67C_UQ7C9oNDic`.
- License: CC BY-SA 4.0
- Attribution: FLORES-200 contributors, Meta AI.
- Modifications: Extracted zho_Hans dev and devtest sentences, applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: CC BY-SA 4.0
- Bias notice: Professional web-article translations are not representative of
  ordinary Taiwan product traffic. Domain and risk remain pending input-only
  review.

## ud-chinese-cfl-v1

- Source: Universal Dependencies Chinese-CFL commit
  `ad71b068e4581343dab897ef2d54abf102580897` (tag `r2.18`).
- License: CC BY-SA 4.0
- Attribution: Universal Dependencies Chinese-CFL contributors.
- Modifications: Extracted sentence text from the pinned CoNLL-U file, applied Unicode NFC and whitespace normalization, removed exact within-source duplicates, and added input-only candidate metadata; no converter output or expected text was used.
- Output license: CC BY-SA 4.0
- Bias notice: Learner essays contain non-native wording and source errors.
  Domain and risk remain pending input-only review.

## naer-terms-v1

- Source: Government Data dataset 15275, `國家教育研究院-兩岸對照名詞-計算機學術名詞`;
  metadata updated 2024-07-08 10:11 Asia/Taipei and CSV Last-Modified
  2024-07-11T03:25:57Z.
- License: 政府資料開放授權條款-第1版 (Open Government Data License, version 1.0)
- Attribution: 國家教育研究院 2024 國家教育研究院-兩岸對照名詞-計算機學術名詞；不暗示國家教育研究院推薦、同意或為 zhtw 背書。
- Modifications: Selected and normalized source fields, preserved unresolved compound cells without delimiter splitting, classified conversion and identity candidates, excluded ambiguous bare terms, deduplicated evaluation cases, and added benchmark metadata; no records were imported into the zhtw product dictionaries.
- Output license: 政府資料開放授權條款-第1版 (Open Government Data License, version 1.0)

## sc-tc-regional-v1

- Source: SC-TC regional benchmark data, only after its repository data-file
  license is independently verified and pinned in a manifest.
- License: Pending verification; no derived data may be committed yet.
- Attribution: Pending verified upstream attribution.
- Modifications: None permitted before license verification.
- Output license: Pending verification.
