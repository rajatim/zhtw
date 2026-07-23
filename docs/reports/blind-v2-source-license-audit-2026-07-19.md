<!-- zhtw:disable -->
# Blind-v2 Candidate Source Audit (2026-07-19)

Status: twenty-four source pilots imported; Tatoeba CC0 pilot rejected; classification ongoing

Updated: 2026-07-24 (AOSP framework Simplified Chinese pilot added)

Issue: #43

This audit evaluates source and redistribution eligibility only. It does not run
zhtw, OpenCC, zhconv, or another converter, and it does not inspect expected or
engine output. Acceptance here does not authorize automatic inclusion: every
download still needs an immutable revision, raw SHA-256, parsing test, script
review, exact/near-deduplication audit, and domain/risk classification from the
input alone.

## Source Decisions

### FTC *Heads Up: Stop. Think. Connect.*, Simplified Chinese

- Official resource index: <https://consumer.ftc.gov/resources-simplified-chinese>.
- PDF SHA-256:
  `fd48b428794f5a70b32da3d56f264149963b68d8b9382a8fedf1c434d3a01112`.
- Rights: FTC-authored material is U.S. public domain under the FTC website
  policy; the pilot excludes graphics, seals, links, English parallel text, and
  third-party content.
- Import result: 117 complete input-only sentences from the 15-page booklet
  after removing headings, page furniture, URLs, and incomplete fragments.
- Known bias: youth online-safety translation concentrating social media,
  privacy, account security, cyberbullying, and device safety.
- Decision: source accepted. Classification batch 012 fixes a deterministic
  100-case selection. Codex and Gemini independent advisories plus Codex
  synthesis are complete. The maintainer confirmed all 100 as eligible and
  explicitly classified `优惠卷 → 優惠券` as a candidate gap. All 100 passed
  exact/near dedupe and entered the collecting pool.

### VS Code Simplified Chinese localization pack

- Repository: <https://github.com/microsoft/vscode-loc>.
- Pinned revision: `da6509eed60b550e0e785d0d78ac05be46d5e982` (2026-07-20).
- Source JSON SHA-256:
  `dd07fd811a728567b1360c4d48f55f5717bf4145df1e7245412bd846c6e14517`.
- License: MIT; pinned license SHA-256:
  `d8428ce0697ff754457dbebb25ff82da1a7f95b281f4fef4cc0cd2fa4586a144`.
- Source class: `permissive_license`.
- Import result: 18,290 prefiltered message values, 2,672 exact within-source
  duplicates removed, and 15,618 unique input-only candidates retained.
- Known bias: Microsoft-managed product localization dominated by VS Code UI,
  developer-tool terminology, short labels, placeholders, and translated text;
  it is not independent organic market-frequency evidence.
- Decision: accepted as an input-only pilot and at most 588 final cases.
  Classification batch 011 fixes a deterministic 100-case first selection;
  Codex and Gemini advisories plus Codex synthesis are complete. The maintainer
  confirmed all 100 as eligible, including four explicit eligibility/risk
  adjustments. All 100 passed exact/near dedupe and entered the collecting pool.

### AOSP framework Simplified Chinese resources

- Repository: <https://android.googlesource.com/platform/frameworks/base/>;
  mirrored at <https://github.com/aosp-mirror/platform_frameworks_base>.
- Pinned revision: `1cdfff555f4a21f71ccc978290e2e212e2f8b168`.
- Source XML SHA-256:
  `71e241287957d068dcf6df1df1f8279109bd79f68e69b7de9137b60d4ff8d915`.
- License: Apache License 2.0, stated directly in the pinned `strings.xml`
  header. Source class: `permissive_license`.
- Import result: 1,835 structurally eligible `<string>` resources before
  within-source dedupe; 138 exact duplicates removed and 1,697 unique
  input-only candidates retained. Escaped multiline values, URLs, email
  addresses, and short non-prose values are excluded before selection.
- Known bias: Android platform localization is dominated by system UI,
  telephony, security, device management, and formatting placeholders; it is
  not independently authored organic market-frequency evidence.
- Decision: accepted as an input-only pilot and at most 588 final cases.
  Classification batch 014 fixes a deterministic first 100-case selection.
  Codex and Gemini independent advisories plus Codex synthesis are complete;
  maintainer confirmation and promotion remain pending.

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

### zhtw project-original formal/LLM semantic v1

- Source: 100 Simplified Chinese scenarios drafted by Codex on 2026-07-24 and
  committed as an immutable input-only source snapshot: 50 formal-writing and
  50 LLM semantic-preservation contexts.
- Raw SHA-256: `4b4950f9e1cb1d567948cf958a0220a722f9c28d036f4fcd65dc54824741c91f`.
- Normalized SHA-256:
  `c41e7b21fd813543f05c370756c77ebd15c8caae6292010ee64b258875bcd890`.
- License: MIT; source class `project_original`.
- Restrictions: synthetic quota coverage only, not organic market-frequency
  evidence. No converter output or expected text influenced drafting or source
  acceptance. Domain and risk were assigned only through input-only review.
- Decision: accepted as an input-only pilot. Codex and Gemini via Antigravity
  CLI independently classified all 100 inputs; maintainer `tim` confirmed the
  Codex synthesis on 2026-07-24. All 100 passed the promotion dedupe gate and
  entered the collecting pool.

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

## OSHA Simplified Chinese Publications

- Publication index: <https://www.osha.gov/publications/bylanguage/chinese-simplified>
- Reuse policy: <https://www.dol.gov/general/aboutdol/copyright>
- Source class: `public_domain` for OSHA-authored federal-government text;
  third-party material is excluded and no endorsement is implied.
- Pinned inputs:

| Source ID | Cases | Raw PDF SHA-256 |
|-----------|------:|----------------|
| `osha-electrical-safety-simplified-v1` | 14 | `073a474bfa93e92f2e8dbc4c4fd36688bee6a81b5e4005e1679bd538f33ec6a6` |
| `osha-chainsaw-safety-simplified-v1` | 20 | `10e48e358ac6aa74e718919dacac8968a1791d1a2cd4414b7cef3bd58ba99751` |
| `osha-work-zone-traffic-simplified-v1` | 16 | `b9c3cf515de9b0bbb8e74b0857bdc01afe1fd408475f0a07912856071dd1f502` |
| `osha-disaster-falls-simplified-v1` | 14 | `f2683f14e4ca64f01679e91dd43f0422e7f13721f0cf16a2c2f6cdea714079f3` |
| `osha-small-business-consultation-simplified-v1` | 22 | `cdcedd100ce05013968026e640079d7044deb913178496424f71b89481a5567e` |
| `osha-disaster-cleanup-simplified-v1` | 76 | `3cf0356ce7fc80af1c560c6ba6be3b01ae2968ef155f164f2bb8b2b1afb58670` |
| `osha-fallen-workers-family-simplified-v1` | 23 | `9af69756e3640e385f51a13825bce70110faa340b5e8f163e779d582a3f2c213` |

- Restrictions: validate each PDF's page count, title, and OSHA corporate-author
  metadata; extract only configured Simplified Chinese pages. Exclude English
  pages, URLs, telephone instructions, page furniture, images, logos, and named
  third-party testimonials. Keep each publication as an independent source ID.
- Known bias: U.S. occupational-safety and administrative language is not
  representative of ordinary Taiwan traffic and concentrates high-stakes text.
- Decision: all seven source snapshots are accepted as input-only pilots. The
  maintainer confirmed the 100-case classification batch on 2026-07-24; all 85
  eligible inputs passed exact/near deduplication and entered the collecting pool.

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

The current pinned pilots are not sufficient to freeze the pool. Under the
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
| Project formal/LLM semantic | 100 | 588 | 100 |
| FTC small-business fraud guide | 81 | 588 | 81 |
| NPS Essential Acadia | 32 | 588 | 32 |
| Ready.gov earthquakes | 48 | 588 | 48 |
| Ready.gov floods | 53 | 588 | 53 |
| Ready.gov hurricanes | 53 | 588 | 53 |
| OSHA electrical safety | 14 | 588 | 14 |
| OSHA chainsaw safety | 20 | 588 | 20 |
| OSHA work-zone traffic | 16 | 588 | 16 |
| OSHA disaster falls | 14 | 588 | 14 |
| OSHA small-business consultation | 22 | 588 | 22 |
| OSHA disaster cleanup | 76 | 588 | 76 |
| OSHA fallen-workers family guide | 23 | 588 | 23 |
| VS Code zh-hans localization | 15,618 | 588 | 588 |
| AOSP framework zh-rCN | 1,697 | 588 | 588 |
| FTC Heads Up online safety | 117 | 588 | 117 |
| **Source-cap total** | **36,325** | | **3,734 (63.50%)** |
| **Class-adjusted total** | | | **2,989 (50.83%)** |

FLORES, UD-CFL, MASSIVE, VS Code localization, and AOSP are `permissive_license`;
the three CDC documents, two FTC publications, NPS, three Ready.gov pages, and seven OSHA publications are
`public_domain`; the four synthetic sources are `project_original`. All
permissive source caps total 2,215, so that class is limited to 2,058 by the
35% class cap. Public-domain and project-original totals remain below their
class caps. The class-adjusted ceiling therefore leaves at least 2,891 candidate
slots unfilled. Actual usable
capacity can only decrease after input-only quality/strata review and the fixed
exact/near-deduplication audit. The final pool still needs at least:

- sustained coverage across the three broad source classes;
- continued publisher and source diversity beyond the ten-source floor;
- enough input-only cases in every domain/risk stratum to satisfy the fixed
  25/20/15/15/15/10 domain and 40/40/20 risk quotas;
- reserve cases in every stratum for deterministic replacement.

The 2026-07-18 Tatoeba CC0 snapshot added zero eligible capacity. Additional
permissive sources cannot increase the class-adjusted ceiling until the pool
grows in other classes. The next source work is therefore to add new
public-domain or permissioned sources while preserving domain diversity.
Converter performance must not influence source or strata selection.
