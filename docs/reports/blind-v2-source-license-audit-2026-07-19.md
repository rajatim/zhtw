<!-- zhtw:disable -->
# Blind-v2 Candidate Source Audit (2026-07-19)

Status: fourteen source pilots imported; Tatoeba CC0 pilot rejected; classification ongoing

Updated: 2026-07-23 (three Ready.gov Simplified Chinese pilots added)

Issue: #43

This audit evaluates source and redistribution eligibility only. It does not run
zhtw, OpenCC, zhconv, or another converter, and it does not inspect expected or
engine output. Acceptance here does not authorize automatic inclusion: every
download still needs an immutable revision, raw SHA-256, parsing test, script
review, exact/near-deduplication audit, and domain/risk classification from the
input alone.

## Source Decisions

### NPS *Essential Acadia: Simplified Chinese*

- Official article: <https://www.nps.gov/articles/000/essential-acadia_simplified-chinese.htm>
- HTML SHA-256: `b3ba2eb004722ae23749ab20610f45ba0262fd3e94e0a20cc59e069e184885a0`.
- Rights: the NPS disclaimer states NPS-created website material is generally
  public domain unless otherwise indicated; this pilot extracts only article
  prose and excludes images, insignia, navigation, and linked content.
- Import result: 32 complete input-only sentences after conservative HTML
  container and sentence-boundary filtering.
- Decision: source accepted. Maintainer confirmed the Codex synthesis after
  Codex and Gemini review; 30 eligible inputs entered the collecting pool and
  2 malformed or context-dependent inputs were excluded.

### FTC *Scams and Your Small Business*, Simplified Chinese

- Official PDF author: Federal Trade Commission; publication date July 2023.
- PDF SHA-256: `c5bdddabd3570861a623134a768d253cc3a9200db683303d09624f3736c1b6a7`.
- Rights: FTC website policy states most FTC-created material is U.S. public
  domain; this pilot excludes graphics, seals, links, and third-party content.
- Import result: 81 complete input-only prose sentences after removing headings,
  page furniture, navigation URLs, phone instructions, and fragments.
- Decision: source accepted. Maintainer confirmed the Codex synthesis after
  Codex and Gemini classification review; 55 eligible inputs entered the
  collecting pool and 26 context-dependent inputs were excluded.

### Ready.gov Simplified Chinese disaster-preparedness pages

- Official pages: `earthquakes`, `floods`, and `hurricanes` under
  <https://www.ready.gov/zh-hans/>.
- HTML SHA-256 values: `d060c9b0cf07a88264c2288380fda65b662fd342392446918919a2059a44dfea`,
  `212da67b2ec70dfd32b7b88a5e546f3c551390d9f2ce7c8591deab7db3972e27`,
  and `b120d204b706d1c7eb716dbef206d42578fe8b0f283d8190120ce7dec4ad009e`.
- Rights: FEMA-authored federal-government prose is classified as U.S. public
  domain under 17 U.S.C. 105. The importer excludes navigation, URLs, phone
  instructions, images, insignia, and linked or third-party content.
- Import result: 48 earthquake, 53 flood, and 53 hurricane input-only cases;
  each page has a separate source ID, manifest, raw hash, and normalized hash.
- Decision: sources accepted. Classification batch 009 fixed a deterministic
  100-case selection. The maintainer confirmed the Codex/Gemini synthesis:
  86 were eligible and 14 were excluded. Dedupe promoted 85 inputs and removed
  one exact duplicate shared by the earthquake and flood pages.

### zhtw project-original IT/API/CLI v1

- Source: 100 Simplified Chinese engineering scenarios drafted by Codex on
  2026-07-23 and committed as an immutable input-only source snapshot.
- Raw SHA-256: `d41619cc854ce4d4d106717e35b9e511d1928b9a0935c48d8d1aab3fc68d488b`.
- License: MIT; source class `project_original`.
- Provenance: synthetic coverage for API, CLI, Git, databases, containers,
  CI/CD, packages, security, observability, messaging, and infrastructure.
- Restrictions: must be reported as Codex-drafted synthetic coverage, not
  organic market-frequency evidence. No converter output or expected text may
  influence source acceptance or source classification.
- Decision: accepted as an input-only pilot. Codex and Gemini advisories plus
  maintainer confirmation completed on 2026-07-23; all 100 eligible inputs
  passed the promotion dedupe gate.

### MASSIVE 1.0 `zh-CN`

- Repository: <https://github.com/alexa/massive>
- Dataset archive: <https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.0.tar.gz>
- Pinned repository revision: `f966f21846043aabef9b0f974fa7970027f43738`.
- Archive SHA-256: `7df623fd2d300a4d235d6ee5bd396c9a28258d3a0ccb29abdb054506eba153f8`.
- License: CC BY 4.0 for the dataset, stated in the archive LICENSE and official
  repository NOTICE.
- Source class: `permissive_license`.
- Script provenance: official `zh-CN` locale localized from the English SLURP
  seed corpus; no converter is used by zhtw.
- Raw capacity: 16,521 utterances; 15,619 unique after exact text dedupe.
- Privacy minimization: worker IDs and judgments are excluded from normalized
  output, together with intent and slot annotations.
- Known bias: translated/localized single-shot voice-assistant requests, many
  short commands and fragments, and recurring wake words.
- Decision: accepted for an input-only pilot and at most 588 final cases,
  subject to quality/domain/risk review and cross-source/reference dedupe.

### Tatoeba Mandarin CC0 export

- Source: <https://tatoeba.org/en/downloads>
- License: CC0 1.0 subset only.
- Source class: `public_domain`.
- Script provenance: contributor-authored Mandarin; do not use a generated
  transcription as the candidate input.
- Audited snapshot: 2026-07-18; SHA-256
  `72c6ac699497cbc9b75f6c021ef16dfaa91ab760fbb407217902b6b5388401c0`.
- Capacity: one Mandarin CC0 row.
- Quality result: the sole row contains the malformed year expression
  `2022/2972` and is not eligible.
- Decision: rejected for the current Blind-v2 pool. Do not substitute the
  general CC BY export or translations. Re-audit only if a future CC0 snapshot
  has materially more Mandarin originals.

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
- Imported items:
  - `cdc:111808`, *当您生病时*: 18 complete input-only sentences; PDF
    SHA-256 `af99f6f5dc63f2dbebd5d1ed0010dd492b27d9b742fd8416cff2f90b26f63b78`.
  - `cdc:120024`, *照顾好你的牙齿*: 22 complete input-only sentences; PDF
    SHA-256 `41a685b4c0ff1805b23afca4599d60583c6ffb5ccb892b391955956c9e365020`.
  - `cdc:116683`, *健康平等措施*: 22 complete input-only sentences; PDF
    SHA-256 `53fcf122e5009fecf2f7caa24cacbf7a43f55367a3b69ccdbcd69a90eae870a7`.
- Canonicalization note: the previously audited `cdc:154488` URL redirects to
  `cdc:120024`; only the canonical item ID and checksum are retained.
- Restrictions: each document is a separate source ID; retain corporate author,
  item URL, publication date, and document checksum. Include CDC attribution,
  no-endorsement language, free-source URL, and no substantive alteration.
- Known bias: health and government translation language; use mainly for the
  high-stakes/formal strata and keep within both source and source-class caps.
- Decision: the three listed items are individually accepted and pinned. A
  collection-wide assumption remains insufficient because CDC pages may include
  third-party material. All 62 rows still require input-only quality/domain/risk
  review before pool promotion.

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

The nine pinned pilots are not sufficient to freeze the pool. Under the
conservative 10% discordant-rate assumption, formal N is 1,960 and the minimum
candidate pool is 5,880. Each source may contribute at most 10% and each broad
source class at most 35%.

Before cross-source/reference near-deduplication and input-only quality review,
the pilot ceiling is:

| Source | Imported | Per-source cap | Maximum pool contribution |
|--------|---------:|---------------:|--------------------------:|
| FLORES-200 zho_Hans | 2,009 | 588 | 588 |
| UD Chinese-CFL | 451 | 588 | 451 |
| CDC Stacks cdc:111808 | 18 | 588 | 18 |
| CDC Stacks cdc:120024 | 22 | 588 | 22 |
| CDC Stacks cdc:116683 | 22 | 588 | 22 |
| MASSIVE 1.0 zh-CN | 15,619 | 588 | 588 |
| Project UI/i18n | 50 | 588 | 50 |
| Project LLM product | 50 | 588 | 50 |
| Project IT/API/CLI | 100 | 588 | 100 |
| FTC small-business fraud guide | 81 | 588 | 81 |
| NPS Essential Acadia | 32 | 588 | 32 |
| Ready.gov earthquakes | 48 | 588 | 48 |
| Ready.gov floods | 53 | 588 | 53 |
| Ready.gov hurricanes | 53 | 588 | 53 |
| **Total** | **18,608** | | **2,156 (36.67%)** |

FLORES, UD-CFL, and MASSIVE are `permissive_license`; the three CDC documents
and the FTC, NPS, and three Ready.gov pages are `public_domain`; the three
synthetic sources are `project_original`. All
class totals remain below the 2,058 class cap. The source-cap ceiling therefore
leaves at least 3,724 candidate slots unfilled. Actual usable
capacity can only decrease after input-only quality/strata review and the fixed
exact/near-deduplication audit. The final pool still needs at least:

- sustained coverage across the three broad source classes;
- continued publisher and source diversity beyond the ten-source floor;
- enough input-only cases in every domain/risk stratum to satisfy the fixed
  25/20/15/15/15/10 domain and 40/40/20 risk quotas;
- reserve cases in every stratum for deterministic replacement.

The 2026-07-18 Tatoeba CC0 snapshot added zero eligible capacity. The next source
work is to complete the Ready.gov human gate and add new public-domain or
permissioned sources to satisfy source-class and domain diversity.
Converter performance must not influence source or strata selection.
