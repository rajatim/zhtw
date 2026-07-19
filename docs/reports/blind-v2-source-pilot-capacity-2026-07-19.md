<!-- zhtw:disable -->
# Blind-v2 Source Pilot Capacity (2026-07-19)

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
| **Total** | **2,460** | **2,460** | **1,039** |

The two pilots can supply at most 1,039 of 5,880 candidate slots (17.67%) before
cross-source/reference exact and near deduplication or quality review. Both are
in `permissive_license`; their combined ceiling remains below that class's
2,058-case cap.

## Remaining Gap

- At least 4,841 additional candidate slots are required.
- At least two additional broad source classes are required.
- Tatoeba CC0 should be the next pinned `public_domain` pilot.
- Individually licensed CDC items can add high-stakes/formal public-domain text.
- Project-original and permissioned-user-report batches are still needed for
  IT/API/CLI, UI/i18n, LLM-generated, and ordinary Taiwan usage coverage.
- No pilot row can enter the frozen pool until input-only quality/domain/risk
  review and fixed exact/near-deduplication pass.
