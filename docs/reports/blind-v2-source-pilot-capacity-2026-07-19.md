<!-- zhtw:disable -->
# Blind-v2 Source Pilot Capacity (2026-07-19)

Updated: 2026-07-23 (FTC Simplified Chinese public-domain pilot)

Report mode: `aggregate`

Issue: #43

This report contains aggregate source capacity only. The importers did not run
zhtw or any competitor, and the pilot artifacts contain no expected text,
acceptable alternatives, annotations, or converter output.

## Fixed Design

- Formal N: 1,960, from the preregistered conservative power assumption.
- Minimum candidate pool: 5,880 (`3 × N`).
- Maximum single-source contribution: 588 (10%).
- Maximum broad source-class contribution: 2,058 (35%).
- Domain/risk classification: pending input-only review for every imported row.

## Gross Capacity

| Source | Raw | Unique input-only | Source-cap ceiling |
|--------|----:|------------------:|-------------------:|
| FLORES-200 zho_Hans dev/devtest | 2,009 | 2,009 | 588 |
| UD Chinese-CFL r2.18 | 451 | 451 | 451 |
| CDC Stacks cdc:111808 | 18 | 18 | 18 |
| CDC Stacks cdc:120024 | 22 | 22 | 22 |
| CDC Stacks cdc:116683 | 22 | 22 | 22 |
| MASSIVE 1.0 zh-CN | 16,521 | 15,619 | 588 |
| FTC small-business fraud guide | 81 | 81 | 81 |
| NPS Essential Acadia | 32 | 32 | 32 |
| **Total** | **19,156** | **18,254** | **1,802** |

The eight external pilots can supply at most 1,802 of 5,880 candidate slots
(30.65%) before cross-source/reference exact and near deduplication or quality
review. FLORES, UD-CFL, and MASSIVE are `permissive_license`; the three CDC
documents and the FTC and NPS guides are `public_domain`. Both source-class totals remain
below the 2,058-case cap.

## Remaining Gap

- At least 4,078 additional candidate slots are required from these external
  pilots alone. The confirmed project-original cases reduce the live collecting
  pool gap separately, but do not change this gross external-source audit.
- At least one additional broad source class is required.
- The ten-source floor has been reached when the three separately manifested
  project-original sources are counted, but source diversity and class-balance
  gates remain unsatisfied.
- Further CDC items may add high-stakes/formal public-domain text only after
  item-level authorship, rights, canonical URL, and checksum verification.
- Project-original and permissioned-user-report batches are still needed for
  IT/API/CLI, UI/i18n, LLM-generated, and ordinary Taiwan usage coverage.
- No pilot row can enter the frozen pool until input-only quality/domain/risk
  review and fixed exact/near-deduplication pass.

## Promotion Update (2026-07-22)

CDC classification batch 003 completed 62/62 maintainer decisions. One malformed
input was excluded and all 61 eligible inputs passed tracked-reference exact and
character 5-gram Jaccard 0.85 near-deduplication. They are now in the
`collecting` pool with this distribution:

- Source: 18 / 21 / 22 across the three CDC documents.
- Domain: 52 high-stakes, 8 social/daily, 1 formal/news.
- Risk: 21 candidate-gap, 4 over-conversion guard, 36 baseline guard.
- Source class: 61 public-domain.

This does not reduce the gross sourcing requirement: the final pool still needs
at least 5,880 cases and must satisfy the 10% per-source, 35% per-source-class,
and fixed domain/risk strata gates before freezing or expected annotation.

Classification batches 001 and 002 were subsequently promoted through the same
hash-verified path. The combined batches 001-003 collecting pool contains 228
cases after cross-batch/reference dedupe, with zero dedupe exclusions:

- Source class: 167 permissive-license and 61 public-domain.
- Domain: 59 formal/news, 60 high-stakes, 7 IT/API/CLI, 102 social/daily.
- Missing domains: UI/i18n and LLM-generated.
- Risk: 70 candidate-gap, 58 over-conversion guard, 100 baseline guard.

On 2026-07-23, classification batch 004 added 100 maintainer-confirmed
project-original inputs after Codex/Gemini review and Codex synthesis. The
combined batches 001-004 collecting pool contains 328 cases with zero dedupe
exclusions:

- Source class: 167 permissive-license, 100 project-original, and 61 public-domain.
- Domain: 59 formal/news, 60 high-stakes, 9 IT/API/CLI, 102 social/daily,
  50 UI/i18n, and 48 LLM-generated.
- Missing domains: none.
- Risk: 151 candidate-gap, 66 over-conversion guard, 111 baseline guard.
- Remaining minimum-pool gap: 5,552.

The project-original inputs are synthetic coverage material and must not be
reported as organic market-frequency evidence.

## MASSIVE Review Update (2026-07-23)

The checksum-pinned MASSIVE 1.0 archive supplied 16,521 zh-CN rows and 15,619
unique normalized utterances. The importer retained only ID, partition,
utterance, and provenance; intent, slot, worker, judgment, converter output, and
expected fields were not imported.

Classification batch 005 deterministically sampled the first 100-case MASSIVE
selection round. Codex and Gemini completed independent input-only advisories;
they match on 35 cases and differ on 65. Codex synthesis recommends 98 eligible
and 2 excluded cases. Maintainer `tim` confirmed the full synthesis on
2026-07-23. All 98 eligible cases passed the normal exact/near-dedupe promotion
gate, bringing the collecting pool to 426 cases with a remaining gap of 5,454.

## Project IT/API/CLI Update (2026-07-23)

Classification batch 006 added 100 Codex-drafted project-original IT/API/CLI
inputs. Gemini independently reviewed all IDs with zero tool calls or API
errors; maintainer `tim` confirmed the second Codex synthesis containing 82
candidate-gap, 8 over-conversion guard, and 10 baseline cases. All 100 passed
exact/reference and near-deduplication, bringing the collecting pool to 526
cases with a remaining minimum-pool gap of 5,354.

## FTC Review Update (2026-07-23)

The checksum-pinned FTC Simplified Chinese PDF supplied 81 complete input-only
sentences. Classification batch 007 completed Codex first-pass review, Gemini
independent review, and Codex synthesis. The synthesis recommends 55 eligible
and 26 excluded cases. Maintainer `tim` confirmed the synthesis on 2026-07-23;
all 55 eligible inputs passed exact/reference and near-deduplication. The
collecting pool now contains 581 cases with a remaining minimum-pool gap of
5,299.

## NPS Acadia Review Update (2026-07-23)

The checksum-pinned NPS article supplied 32 complete input-only travel, park-rule,
and outdoor-safety sentences. Batch 008 completed Codex first-pass review,
Gemini independent review, and Codex synthesis. The synthesis recommends 30
eligible and 2 excluded cases. Maintainer `tim` confirmed the synthesis on
2026-07-23; all 30 eligible inputs passed exact/reference and near-deduplication.
The collecting pool now contains 611 cases with a remaining minimum-pool gap
of 5,269.
