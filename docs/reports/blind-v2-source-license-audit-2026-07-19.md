<!-- zhtw:disable -->
# Blind-v2 Candidate Source Audit (2026-07-19)

Status: two source pilots pinned and imported; classification remains pending

Issue: #43

This audit evaluates source and redistribution eligibility only. It does not run
zhtw, OpenCC, zhconv, or another converter, and it does not inspect expected or
engine output. Acceptance here does not authorize automatic inclusion: every
download still needs an immutable revision, raw SHA-256, parsing test, script
review, exact/near-deduplication audit, and domain/risk classification from the
input alone.

## Accepted Pending Pinning

### Tatoeba Mandarin CC0 export

- Source: <https://tatoeba.org/en/downloads>
- License: CC0 1.0 subset only.
- Source class: `public_domain`.
- Script provenance: contributor-authored Mandarin; do not use a generated
  transcription as the candidate input.
- Restrictions: use only rows present in the dedicated CC0 export. Preserve the
  Tatoeba sentence ID and weekly dump date. Reject mixed/Traditional-script rows
  during input-only human script review, without consulting converter output.
- Decision: conditionally accepted. The mutable weekly URL must be downloaded
  once, hashed, and recorded before extraction.

Tatoeba states that general sentence exports are CC BY 2.0 FR and that a
separate download contains all CC0 sentences. Its CC0 policy limits CC0 to
original sentences, not translations.

### FLORES-200 `zho_Hans`

- Repository: <https://github.com/facebookresearch/flores>
- Audited revision: `a6c830c6e1051fb4ac1a44b32358f00463f332bd`.
- License: CC BY-SA 4.0.
- Source class: `permissive_license`.
- Script provenance: human translation in the declared Simplified Chinese
  script variant, not a conversion generated for this project.
- Known bias: 3,001 professional translations from 842 web articles; translation
  and article-domain language is not representative of ordinary Taiwan product
  traffic.
- Pinned archive: S3 version `KJZoZnGvyduN3osrx.67C_UQ7C9oNDic`, SHA-256
  `b8b0b76783024b85797e5cc75064eb83fc5288b41e9654dabc7be6ae944011f6`.
- Pilot result: 2,009 unique public dev/devtest inputs imported; all domain and
  risk fields remain unset pending input-only review.
- Decision: accepted for at most 588 cases under the current global
  single-source cap.

The official repository lists FLORES-200 as CC BY-SA 4.0 and describes the
translation and verification workflow.

### UD Chinese-CFL

- Source: <https://universaldependencies.org/treebanks/zh_cfl/>
- Pinned revision: UD release 2.18, commit
  `ad71b068e4581343dab897ef2d54abf102580897`; CoNLL-U SHA-256
  `5eb666265585bc1cd1a04ea5ca2d94f2ddc6f00b782ae7dfe815e08504879923`.
- License: CC BY-SA 4.0.
- Source class: `permissive_license`.
- Script provenance: the official treebank page explicitly states that the data
  is in Simplified Chinese.
- Known bias: learner essays contain non-native wording and annotation-source
  errors; this is useful challenge material but must not dominate a domain.
- Pilot result: 451 unique inputs imported; all domain and risk fields remain
  unset pending input-only review.
- Decision: accepted, subject to sentence-level quality filtering performed
  without converter output.

### CDC Stacks Simplified Chinese public-domain items

- Collection: <https://stacks.cdc.gov/>
- Reuse policy: <https://www.cdc.gov/other/agencymaterials.html>
- Source class: `public_domain`.
- Script provenance: only item records explicitly labelled Simplified Chinese
  and Public Domain may be used.
- Candidate examples:
  - <https://stacks.cdc.gov/view/cdc/111808>
  - <https://stacks.cdc.gov/view/cdc/154488>
  - <https://stacks.cdc.gov/view/cdc/116683>
- Restrictions: each document is a separate source ID; retain corporate author,
  item URL, publication date, and document checksum. Include CDC attribution,
  no-endorsement language, free-source URL, and no substantive alteration.
- Known bias: health and government translation language; use mainly for the
  high-stakes/formal strata and keep within both source and source-class caps.
- Decision: conditionally accepted per item. A collection-wide assumption is
  insufficient because CDC pages may include third-party material.

## Rejected

### UD Chinese-GSDSimp

- Source: <https://universaldependencies.org/treebanks/zh_gsdsimp/>
- Reason: the official description says the Simplified text was initially
  generated from Traditional GSD with OpenCC and then manually corrected.
- Decision: rejected. Using it would violate the rule against converter-derived
  candidate inputs and would create direct OpenCC source bias.

### UD Chinese-PUD

- Source: <https://universaldependencies.org/treebanks/zh_pud/>
- License: CC BY-SA 3.0.
- Reason: the current Chinese treebank text is Traditional Chinese. Creating a
  Simplified candidate version would require a converter and violate the input
  provenance rule.
- Decision: rejected for Blind-v2 candidate generation. It may remain suitable
  for unrelated public compatibility work.

### Mozilla Common Voice Scripted Speech 26.0, Chinese (China)

- Dataset listing: <https://commonvoice.mozilla.org/datasets>
- Consumer terms: <https://mozilladatacollective.com/terms/consumers>
- Stated dataset license: CC0 1.0.
- Reason: current Mozilla Data Collective download terms shown during dataset
  access prohibit re-hosting or re-sharing the downloaded dataset. Committing
  extracted candidate sentences would therefore create avoidable redistribution
  ambiguity despite the CC0 label.
- Decision: rejected unless Mozilla provides terms that explicitly permit the
  intended redistribution path or written clarification is retained.

## Capacity Assessment

The two pinned pilots are not sufficient to freeze the pool. Under the
conservative 10% discordant-rate assumption, formal N is 1,960 and the minimum
candidate pool is 5,880. Each source may contribute at most 10% and each broad
source class at most 35%.

Before cross-source/reference near-deduplication and input-only quality review,
the pilot ceiling is:

| Source | Imported | Per-source cap | Maximum pool contribution |
|--------|---------:|---------------:|--------------------------:|
| FLORES-200 zho_Hans | 2,009 | 588 | 588 |
| UD Chinese-CFL | 451 | 588 | 451 |
| **Total** | **2,460** | | **1,039 (17.67%)** |

Both pilots are `permissive_license`, whose class cap is 2,058. The pilot
ceiling therefore leaves at least 4,841 candidate slots unfilled. Actual usable
capacity can only decrease after input-only quality/strata review and the fixed
exact/near-deduplication audit. The final pool still needs at least:

- three broad source classes;
- ten independently identified sources overall;
- enough input-only cases in every domain/risk stratum to satisfy the fixed
  25/20/15/15/15/10 domain and 40/40/20 risk quotas;
- reserve cases in every stratum for deterministic replacement.

The next source work is to classify the two pilots from input alone, then pin a
Tatoeba CC0 snapshot and individually verified CDC Stacks documents. Additional
project-original and permissioned-user-report sources are required to satisfy
source-class diversity. Converter performance must not influence source or
strata selection.
