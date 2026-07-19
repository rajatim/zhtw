<!-- zhtw:disable -->
# Accuracy Regression Datasets

This directory stores public regression datasets for zhtw accuracy work. Inputs
stay Simplified Chinese; expected values are manually curated Taiwan Traditional
Chinese from `zhtw-test-corpus`, approved annotation backlog promotions, and
holdout cases explicitly removed from sealed status before tuning, plus
maintainer-approved public reproduction promotions.

## Benchmark v2 governance

- `manifest.schema.json` defines source revision, licensing, attribution,
  importer, bias, and artifact-hash requirements for every new track.
- `LICENSES.md` is the required notice registry referenced by manifests.
- `ranking-policy-v1.json` freezes the primary market-ranking policy.
- `preregistration.schema.json` binds artifacts, commit, ranking policy, and
  power analysis before a formal score is read.
- `scripts/validate_benchmark_assets.py` fails closed on missing metadata,
  notices, files, or mismatched hashes.
- `scripts/benchmark_metrics.py` provides deterministic alignment, changed-span
  metrics, paired bootstrap/McNemar comparison, and paired power analysis.

Validation:

```bash
make benchmark-validate
```

Formal execution additionally requires explicit frozen assets and refuses a
dirty or mismatched zhtw commit:

```bash
uv run python scripts/run_accuracy_benchmark.py \
  --formal \
  --manifest benchmarks/accuracy/manifests/blind-v2.json \
  --preregistration benchmarks/accuracy/preregistrations/blind-v2-run-1.json \
  --inputs benchmarks/accuracy/blind-v2.inputs.json \
  --expected /private/path/blind-v2.expected.json
```

An unavailable engine invalidates a formal run. A per-case exception or empty
output stays in the denominator as a miss and is counted by error category.

## regression-v1

`regression-v1.json` is the first M1 public regression dataset.

Source:

- `docs/reports/competitor-diffs-full-2026-07-03.json`
- `docs/reports/annotation-promotion-gate-2026-07-07.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch11-semantic-reaudit-2026-07-14.json`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.json`
- `docs/reports/public-reproduction-promotion-gate-after-batch10-remaining-signal-2026-07-13.json`
- source expected: curated corpus `expected`
- promoted expected: approved annotation backlog `review.expected`
- holdout promoted expected:
  `benchmarks/accuracy/holdout-regression-candidates-v1.json`
- public reproduction promoted expected:
  `docs/reports/public-reproduction-maintainer-final-decision-after-batch10-remaining-signal-2026-07-13.json`
- competitor classification: from the full discovery report when available

Selection rule:

1. Include all curated corpus cases with human expected output.
2. Require zhtw to match every expected output.
3. Preserve discovery classification from the full competitor report.
4. Mark `zhtw_advantage` rows as `over_conversion_guard`.
5. Mark `all_match` rows as `baseline_guard`.
6. Append promotion-ready approved annotation cases after promotion gate passes.
7. Append holdout cases only after they are removed from sealed status, made
   public, fixed, and pass their promotion gate.
8. Append public reproduction cases only after maintainer final decision and a
   strict zhtw primary-expected match promotion gate.

Current size: 1,229 cases.

Distribution:

| Domain | Cases |
|--------|-------|
| formal | 128 |
| high_risk | 13 |
| it | 280 |
| llm | 19 |
| mixed | 25 |
| news | 100 |
| regressions | 100 |
| social | 192 |
| tech | 100 |
| ui | 172 |
| wiki | 100 |

Risk:

| Risk | Cases |
|------|-------|
| baseline_guard | 308 |
| candidate_gap | 465 |
| over_conversion_guard | 478 |

Classification:

| Classification | Cases |
|----------------|-------|
| all_match | 192 |
| annotation_promoted | 500 |
| holdout_regression_promoted | 219 |
| public_reproduction_promoted | 32 |
| zhtw_advantage | 308 |

Competitor miss count:

| Missed competitors | Cases |
|--------------------|-------|
| 0 | 943 |
| 1 | 167 |
| 2 | 141 |

This dataset is public regression, not sealed holdout. It prevents known-good
zhtw behavior from regressing; it must not be used as proof of a new blind
accuracy claim.

## blind-v1

`blind-v1` is a **published evaluation benchmark**, not a fresh or sealed
holdout. Its expected values and detailed rows appeared in tracked reports, and
its misses were reviewed during development. Keep it for historical and
like-for-like comparison only; new generalization or market claims require
`blind-v2` or a later preregistered one-shot benchmark.

The historical notes below describe the workflow when blind-v1 was still
treated as sealed. They do not override its current `published_evaluation`
classification.

Current files:

- `blind-v1.inputs.json`: public input-only seed pool.
- `blind-v1.inputs.schema.json`: input-only schema. Case objects must not contain
  `expected`, `acceptable`, `review`, or `annotation`.
- `blind-v1.expected.schema.json`: private expected schema for human-reviewed
  ground truth.
- `holdout-regression-candidates-v1.json`: public regression candidates removed
  from sealed holdout before tuning.
- `holdout-regression-candidates-v1.schema.json`: schema for those removed
  public candidates.
- `docs/reports/holdout-input-pool-expansion-blind-v1-2026-07-09.*`:
  aggregate-only audit for the 127 input-only cases added after the second
  promotion.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.*`:
  aggregate-only audit for the next 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch5-100-cases-2026-07-09.*`:
  aggregate-only audit for the batch5 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.*`:
  aggregate-only audit for the batch6 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.*`:
  aggregate-only audit for the batch7 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.*`:
  aggregate-only audit for the batch8 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.*`:
  aggregate-only audit for the batch9 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.*`:
  aggregate-only audit for the batch10 100 input-only cases.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch11-100-cases-2026-07-13.*`:
  aggregate-only audit for the latest 100 input-only cases; maintainer expected
  confirmation completed on 2026-07-14.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch12-100-cases-2026-07-14.*`:
  aggregate-only audit for 100 fresh input-only cases; maintainer expected
  confirmation completed on 2026-07-14.
- `docs/reports/holdout-input-pool-expansion-blind-v1-batch13-100-cases-2026-07-14.*`:
  aggregate-only audit for the latest 100 input-only cases; Codex and independent
  Gemini advisory, maintainer confirmation, and the first blind benchmark are complete.
- `competitors.lock.json`: draft adapter lockfile for reproducible benchmark
  runs.
- `scripts/create_holdout_annotation_packet.py`: reviewer packet generator that
  shows inputs and empty annotation fields only.
- `scripts/run_accuracy_benchmark.py`: benchmark runner; aggregate-only is the
  default, while detailed output must use a private ignored path.

Current input pool:

| Domain | Cases |
|--------|-------|
| formal | 164 |
| high_risk | 128 |
| it | 189 |
| llm | 159 |
| social | 180 |
| ui | 188 |

Total collected: 1,008 / 2,000 in the current input-only pool. The reviewed
private expected file covers all 1,008 cases after Batch13 miss review.

Through 2026-07-14, 219 cases total were removed from sealed holdout and converted
into public regression candidates before tuning. Batch1/batch2 removed 27
cases before expansion; batch3 removed 39 cases from the 200-case sanity pass;
batch4 recheck removed 5 cases from the 261-case sanity pass; remaining-40
final review removed and promoted 18 additional public candidates; the 338-case
miss review removed and promoted 12 additional public candidates and confirmed
3 acceptable variants that stayed sealed; the batch6 miss review removed and
promoted 11 additional public candidates and confirmed 2 acceptable variants
that stayed sealed; the batch7 miss review removed and promoted 17 additional
public candidates and confirmed 7 acceptable variants that stayed sealed; the
batch8 miss review removed and promoted 15 additional public candidates,
confirmed 4 acceptable variants that stayed sealed, and kept 30 remaining misses
as private holdout signal; the batch9 miss review removed and promoted 16
additional public candidates, confirmed 6 acceptable variants that stayed sealed,
and kept 31 remaining misses as private holdout signal; the batch10 miss review
removed and promoted 16 additional public candidates, confirmed 4 acceptable
variants that stayed sealed, and kept 32 remaining misses as private holdout
signal; the batch11 semantic re-audit removed and promoted 10 additional public
candidates, confirmed 4 acceptable variants, and retained 11 strict private
signals; the batch12 miss review removed and promoted 11 additional public
candidates, confirmed 4 acceptable variants, and retained no new strict private
signals.
The audit reports are
`docs/reports/holdout-sealed-pool-update-blind-v1-2026-07-09.md` and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch2-2026-07-09.md`, plus
`docs/reports/holdout-sealed-pool-update-blind-v1-batch3-2026-07-09.md` and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch4-recheck-2026-07-09.md`,
and
`docs/reports/holdout-sealed-pool-update-blind-v1-remaining-40-final-review-2026-07-09.md`,
and
`docs/reports/holdout-sealed-pool-update-blind-v1-338-miss-review-2026-07-09.md`,
and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch6-miss-review-2026-07-10.md`,
and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch7-miss-review-2026-07-10.md`,
and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.md`, and
`docs/reports/holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.md`.
After batch1/batch2, 127 new public input-only cases were added to continue
building the sealed pool toward the 2,000-case target. Those new cases were
reviewed under the maintainer-approved single-human + AI advisory cadence and
the private expected file was rebuilt; after batch3 the sealed pool had 161
reviewed input cases. Batch4 added 100 public input-only cases and those cases
were reviewed under the same cadence; follow-up recheck confirmed 9 acceptable
variants, removed 5 cases to public regression, and left 256 current sealed
cases. Remaining-40 final review then confirmed 3 acceptable variants, removed
18 public regression candidates, and left 238 reviewed sealed cases. Batch5
then added 100 new public input-only cases and was reviewed under the same
cadence. The 338-case miss review confirmed 3 acceptable variants, removed 12
public regression candidates, and left 326 reviewed sealed cases. Batch6 then
added 100 new public input-only cases; Codex/Gemini advisory reviews, diff
review, maintainer confirmation packet, and maintainer final decision are
complete. The batch6 miss review then confirmed 2 acceptable variants, removed
11 public regression candidates, and left 415 reviewed sealed cases. The local
private expected file now covers those 415 reviewed sealed cases. Batch7 then
added 100 public input-only cases; Codex first-pass advisory, Gemini CLI
advisory, Codex/Gemini diff review, and maintainer confirmation packet are
complete. Maintainer final decision accepted the 65-case review queue and 35
no-immediate-question cases, so the local private expected file covered 515
reviewed sealed cases before miss review. The batch7 miss review then confirmed
7 acceptable variants, removed 17 public regression candidates, and left 498
reviewed sealed cases. Batch8 then added 100 new public input-only cases; Codex
first-pass advisory, Gemini CLI advisory, Codex/Gemini diff review, and
maintainer confirmation packet are complete. Maintainer final decision accepted
the 66-case review queue and 34 no-immediate-question cases, so the then-current
input pool and local private expected file are aligned at 598 reviewed sealed
cases before miss review. The batch8 miss review then confirmed 4 acceptable
variants, removed 15 public regression candidates, and left 583 reviewed sealed
cases. Batch9 then added 100 new public input-only cases; Codex first-pass
advisory, Gemini CLI advisory, Codex/Gemini diff review, and maintainer
confirmation packet are complete. Maintainer final decision accepted the 69-case
review queue and 31 no-immediate-question cases, so the current input pool and
local private expected file were aligned at 683 reviewed sealed cases before miss
review. The batch9 miss review then confirmed 6 acceptable variants, removed 16
public regression candidates, and left 667 reviewed sealed cases. Batch10 then
added 100 new public input-only cases; Codex first-pass advisory, Gemini CLI
advisory, Codex/Gemini diff review, and maintainer confirmation packet are
complete. Maintainer final decision accepted the 44-case review queue and 56
no-immediate-question cases, so the then-current input pool and local private
expected file were aligned at 767 reviewed sealed cases before miss review. The
batch10 miss review then confirmed 4 acceptable variants, removed 16 public
regression candidates, and left 751 reviewed sealed cases. Batch11 later added
100 cases; its semantic re-audit removed 10 public candidates and left 841
reviewed sealed cases. Batch12 then added 100 cases; its miss review confirmed
4 acceptable variants, removed and promoted 11 public candidates, and left the
current 930 reviewed sealed cases. The
aggregate-only expansion audits are
`docs/reports/holdout-input-pool-expansion-blind-v1-2026-07-09.md` and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.md`,
plus
`docs/reports/holdout-input-pool-expansion-blind-v1-batch5-100-cases-2026-07-09.md`,
and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch6-100-cases-2026-07-09.md`,
and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.md`,
and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.md`,
and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.md`,
and
`docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.md`.

Expected values are intentionally not committed yet. `blind-v1.expected.json` is
ignored by git until the benchmark is ready to publish. The historical batch7
final decision covered 515 reviewed sealed cases; the historical batch8 final
decision covered 598 reviewed sealed cases; the historical batch8 miss review
left 583 reviewed sealed cases; the historical batch9 final decision covered
683 reviewed sealed cases before miss review; the historical batch10 final
decision covered 767 reviewed sealed cases before miss review; the current
local private expected file covers 751 reviewed sealed cases after the batch10
miss review.
Expected must
be produced by human review only:

1. Codex creates the first expected-output recommendation with rationale.
2. Gemini reviews independently from the input-only packet.
3. Codex compares Codex/Gemini outputs and separates exact matches from
   disagreements or low-confidence cases.
4. Maintainer confirmation/adjudication is the human decision.
5. zhtw, OpenCC, zhconv, competitor majority vote, and unreviewed LLM output are
   forbidden expected sources.

This accelerated cadence is recorded as `single_human_with_ai_advisory`. A
strict sealed benchmark claim still needs a second human reviewer or explicit
disclosure that one human maintainer made the final decision with AI advisory.

Latest private sanity after batch10 miss review:

- Aggregate-only report:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch10-miss-review-2026-07-13.md`
- Full private benchmark rows:
  `/tmp/zhtw-blind-v1-private-benchmark-after-batch10-miss-review-2026-07-13.json`
  and intentionally not stored in repo.
- zhtw accepted: 719 / 751.
- Misses: 32.
- Accepted accuracy: 0.9574.
- Miss mix: 1 baseline guard, 2 candidate gap, 29 over-conversion guard.
- Sanitized miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-767-cases-2026-07-12.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-767-cases-2026-07-12.md`
- Maintainer miss-classification review queue:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-miss-classification-2026-07-12.md`
- Miss classification result: 32 kept as private holdout signal, 16
  recommended as public regression candidates after sealed removal, 4 require
  expected/acceptable recheck. Gemini recommended 0 classification changes.
- Batch10 miss final decision:
  `docs/reports/holdout-maintainer-final-decision-batch10-miss-classification-blind-v1-2026-07-13.md`
- Batch10 miss sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch10-miss-review-2026-07-13.md`
- Batch10 miss promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.md`
- Remaining 32 signal summary:
  `docs/reports/holdout-remaining-signal-summary-blind-v1-after-batch10-miss-review-2026-07-13.md`
- Remaining signal result: 32 kept as private holdout signals, 0 public
  candidates, 0 expected recheck cases, and 0 maintainer review cases. No
  converter, dictionary, or private expected changes were made from these
  remaining sealed signals; any future tuning must first use independent public
  reproduction inputs.
- Gemini remaining-signal policy review:
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-after-batch10-miss-review-2026-07-13.md`
- Gemini remaining-signal review status: completed with Gemini CLI Vertex AI
  auth using `gemini-2.5-pro`; policy passed, 0 blocking findings, and 0
  changes recommended.
- Independent public reproduction seeds:
  `benchmarks/accuracy/public-reproduction-seeds-v1.json`
- Public reproduction report:
  `docs/reports/holdout-independent-public-reproduction-seeds-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction status: 32 original input-only cases created from
  sanitized metadata themes only. The seed file intentionally still contains no
  expected values; human-confirmed expected values now live in the maintainer
  final decision and are not regression/tuning data until a separate promotion
  gate passes.
- Public reproduction Codex first-pass advisory:
  `docs/reports/public-reproduction-codex-first-pass-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction Gemini independent advisory:
  `docs/reports/public-reproduction-gemini-advisory-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction Codex/Gemini diff:
  `docs/reports/public-reproduction-codex-gemini-diff-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction maintainer packet:
  `docs/reports/public-reproduction-maintainer-confirmation-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction maintainer final decision:
  `docs/reports/public-reproduction-maintainer-final-decision-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction review result: maintainer review OK confirmed all 32
  public reproduction cases under `single_human_with_ai_advisory`: 26
  Codex/Gemini primary exact matches, 6 primary differences, 17 review-packet
  cases, and 15 no-immediate-question cases. No converter, dictionary, seed
  input, or public regression dataset changes were made in this step.
- Public reproduction promotion gate:
  `docs/reports/public-reproduction-promotion-gate-after-batch10-remaining-signal-2026-07-13.md`
- Public reproduction promotion result: after conservative full-sentence
  mappings, all 32 cases matched the final primary expected and were promoted
  into `regression-v1.json`; 0 cases remain withheld.
- Batch10 final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.md`
- Batch10 maintainer confirmation:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.md`
- Batch10 review result: 44 review-queue cases and 56 no-immediate-question
  cases accepted into private expected; 17 batch10 cases are
  `human_adjudication`, 83 are `human_first_pass`.

Historical private sanity after batch9 miss review:

- Aggregate-only report:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch9-miss-review-2026-07-12.md`
- Full private benchmark rows:
  `/tmp/zhtw-blind-v1-private-benchmark-after-batch9-miss-review-2026-07-12.json`
  and intentionally not stored in repo.
- zhtw accepted: 636 / 667.
- Misses: 31.
- Accepted accuracy: 0.9535.
- Miss mix: 1 baseline guard, 2 candidate gap, 28 over-conversion guard.
- Sanitized miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-683-cases-2026-07-12.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.md`
- Maintainer miss-classification review queue:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-miss-classification-2026-07-12.md`
- Miss classification result: 31 kept as private holdout signal, 16 recommended
  as public regression candidates after sealed removal, 6 require
  expected/acceptable recheck.
- Batch9 expansion final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 maintainer confirmation:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 miss-classification final decision:
  `docs/reports/holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.md`
- Batch9 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch9 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch9 Gemini public promotion policy review:
  `docs/reports/holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.md`
- Historical batch8 final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.md`
- Historical batch8 final decision sanity:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch8-2026-07-10.md`
- Batch8 miss review final decision:
  `docs/reports/holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.md`
- Sanitized miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-598-cases-2026-07-10.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.md`
- Maintainer review queue:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-miss-classification-2026-07-10.md`
- Sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.md`
- Public promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.md`
- Gemini public promotion policy review:
  `docs/reports/holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.md`
- Miss review result: 30 kept as private holdout signal, 15 moved to public
  regression candidates and promoted, 4 accepted as private acceptable variants.
- Miss mix after miss review: 1 baseline guard, 2 candidate gap, 27
  over-conversion guard.

Batch10 review artifacts:

- Input expansion audit:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch10-100-cases-2026-07-12.md`
- Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch10-100-cases-2026-07-12.md`
- Gemini CLI advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch10-100-cases-2026-07-12.md`
- Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch10-100-cases-2026-07-12.md`
- Maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch10-100-cases-2026-07-12.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch10-100-cases-2026-07-12.md`

Before batch11, the 751-case input pool was aligned with the local 751-case
private expected file after the batch10 miss review. The 767-case batch10 final decision,
667-case batch9 miss-review sanity report, 683-case batch9 final decision,
583-case batch8 miss review, 598-case batch8 final decision, 498-case batch7
miss review, 515-case batch7 final decision, and 415-case batch6 miss review
sanity reports remain historical snapshots only.

Batch11 review artifacts:

- Input expansion audit:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch11-100-cases-2026-07-13.md`
- Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch11-100-cases-2026-07-13.md`
- Gemini CLI independent advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch11-100-cases-2026-07-14.md`
- Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch11-100-cases-2026-07-14.md`
- Maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-100-cases-2026-07-14.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch11-100-cases-2026-07-14.md`
- Private benchmark sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch11-2026-07-14.md`

Batch11 has 79 exact Codex/Gemini matches and 21 differences. The 50-case
maintainer packet contains those 21 differences plus 29 exact matches requiring
policy review; the other 50 cases have no immediate question. Private expected
was updated after maintainer review OK. No unreviewed acceptable variants were
added. The strict post-review sanity result is 791/851 accepted with 60 misses
(about 92.95% accepted accuracy); private rows remain outside the repository.

The 60 post-batch11 misses completed Codex classification and Gemini
sanitized policy review. The 32 previously confirmed holdout signals remain
unchanged. The current recommendation is 35 private holdout signals, 14 public
regression candidates, and 11 expected/acceptable rechecks. Gemini passed the
policy review with zero classification changes; the resulting 25-case packet
was superseded by the semantic re-audit below:

- `docs/reports/holdout-miss-classification-blind-v1-851-cases-2026-07-14.md`
- `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-851-cases-2026-07-14.md`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-miss-classification-2026-07-14.md`

After the maintainer identified possible overcorrection, the 25 review cases
were re-audited under a semantic-correctness rule. Gemini independently reviewed
input-only cases without seeing Codex, current expected values, or zhtw output.
The revised recommendation is 4 acceptable variants, 10 true public regression
candidates, and 11 strict private holdout signals that must not drive tuning.
Nineteen cases were covered by explicit maintainer preferences, and the final 6
were confirmed review OK. The final decision added 4 private acceptable variants,
removed and promoted 10 public regression candidates, and retained 11 strict
private signals. The current private sanity is 795/841 accepted with 46 misses
(about 94.53%); this change includes both semantic acceptable variants and a
smaller sealed denominator:

- `docs/reports/holdout-codex-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.md`
- `docs/reports/holdout-gemini-independent-semantic-reaudit-blind-v1-batch11-25-cases-2026-07-14.md`
- `docs/reports/holdout-semantic-reaudit-diff-blind-v1-batch11-25-cases-2026-07-14.md`
- `docs/reports/holdout-maintainer-confirmation-blind-v1-batch11-semantic-reaudit-6-cases-2026-07-14.md`
- `docs/reports/holdout-maintainer-final-decision-blind-v1-batch11-semantic-reaudit-2026-07-14.md`
- `docs/reports/holdout-regression-promotion-gate-blind-v1-batch11-semantic-reaudit-2026-07-14.md`
- `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch11-semantic-reaudit-2026-07-14.md`

Do not promote blind misses directly into `regression-v1.json`. If a blind case
is used to tune zhtw before publication, remove it from sealed holdout first and
turn it into a public regression candidate with a clear audit note.

Create the first human annotation packet:

```bash
make accuracy-holdout-annotation-packet DATE=2026-07-07
uv run python scripts/create_holdout_annotation_packet.py \
  --inputs benchmarks/accuracy/blind-v1.inputs.json \
  --generated-date 2026-07-07 \
  --reviewer-stage first_human_review \
  --output docs/reports/holdout-annotation-packet-blind-v1-first_human_review-2026-07-07.md
```

The packet must stay input-only. Do not add zhtw, Gemini, OpenCC, zhconv, or
other converter output to the reviewer packet.

Default review cadence for the maintainer loop:

1. Codex creates the first expected-output recommendation with rationale.
2. Gemini reviews independently from the input-only packet.
3. Codex compares Codex/Gemini outputs and separates exact matches from
   disagreements or low-confidence cases.
4. Only disagreements, high-risk cases, and low-confidence cases are shown to
   the maintainer for confirmation.
5. Maintainer confirmation is the human decision. Codex/Gemini output remains
   advisory and must not be treated as ground truth by itself.

If this accelerated cadence is used, record it as
`single_human_with_ai_advisory`. A strict sealed benchmark claim still needs a
second human reviewer or an explicit disclosure that only one human maintainer
made the final decision with AI advisory.

Latest Codex first-pass advisory:

- Markdown:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch12-100-cases-2026-07-14.md`
- JSON:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch12-100-cases-2026-07-14.json`
- Cases: 100
- Confidence: 79 high, 21 medium
- Review-needed cases before independent review: 21
- Status: advisory only; not ground truth; not promotion-ready

Latest Gemini independent advisory:

- Markdown:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch12-100-cases-2026-07-14.md`
- JSON:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch12-100-cases-2026-07-14.json`
- Cases: 100
- Confidence: 100 high
- Review-needed cases before Codex/Gemini diff review: 0
- Model observed: `gemini-2.5-pro`; tool calls: 0
- CLI auth note: API-key env vars were unset for this run
- Status: advisory only; not ground truth; not promotion-ready

Latest Codex/Gemini difference review:

- Markdown:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch12-100-cases-2026-07-14.md`
- JSON:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch12-100-cases-2026-07-14.json`
- Exact matches: 87
- Differences: 13
- Exact but policy-review cases: 31
- No immediate-question cases: 56
- Maintainer queue total: 44
- Difference recommendations: 7 Codex, 6 Gemini
- Maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch12-100-cases-2026-07-14.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch12-100-cases-2026-07-14.md`
- Private benchmark sanity:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch12-2026-07-14.md`
- Historical status immediately after expected review: private expected covered
  941/941 cases
- Fresh Batch12 result: 85/100 accepted, 15 misses
- Historical aggregate result before miss review: 880/941 accepted, about 93.52%
- Batch12 miss semantic review: Codex first classified 7 acceptable variants and
  8 public candidates; Gemini then reviewed the 15 inputs independently with no
  Codex/private/zhtw values and zero tool calls. The combined recommendation is
  9 acceptable variants and 6 public candidates. Maintainer feedback rejected
  two rare orthographic forms for contemporary Taiwan usage. Maintainer final
  review classified 4 cases as acceptable variants and 11 as public regression
  candidates, with no new strict private signal:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch12-miss-review-8-cases-2026-07-14.md`
- Batch12 miss final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch12-miss-review-2026-07-14.md`
- Batch12 miss promotion gate, 11/11 passed:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.md`
- Current private sanity: 884/930 accepted, 46 misses, about 95.05%:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch12-miss-review-2026-07-14.md`
- Interpretation: the denominator changed because 11 cases were removed before
  tuning and 4 acceptable variants were added. This is not a pure capability-gain
  comparison with the historical 880/941 result.

Batch13 review status:

- Input-only expansion:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch13-100-cases-2026-07-14.md`
- Codex first pass: 78 high confidence, 22 medium confidence:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch13-100-cases-2026-07-14.md`
- Independent Gemini CLI advisory: `gemini-2.5-pro`, 100/100 cases, zero tool
  calls and zero quality flags:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch13-100-cases-2026-07-14.md`
- Difference review: 66 exact matches, 34 differences, 19 exact policy-review
  cases, 47 no-immediate-question cases, and 53 cases in the maintainer queue:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch13-100-cases-2026-07-14.md`
- Maintainer review OK accepted all 100 cases; 35 are recorded as human
  adjudication and 65 as human first pass. Private expected now covers 1,030 cases:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch13-100-cases-2026-07-14.md`
- Fresh Batch13 result before tuning: 66/100 accepted, 34 misses. Aggregate:
  950/1,030 accepted, about 92.23%. The fresh misses are IT 10, UI 8, LLM 6,
  high-risk 5, social 3, and formal 2:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch13-2026-07-14.md`
- This fresh-batch result is a valid generalization signal under
  `single_human_with_ai_advisory`; it does not support a market-best claim.
- The 34 fresh misses have completed Codex first-pass classification and an
  independent Gemini `gemini-2.5-pro` input-only review with zero tool calls.
  Codex/Gemini agree on 19 classifications and differ on 15. The synthesized
  recommendation is 5 acceptable variants, 22 public regression candidates,
  and 7 strict private signals; 19 cases require maintainer confirmation. No
  private expected, sealed pool, or dictionary change has occurred:
  `docs/reports/holdout-codex-gemini-miss-review-diff-blind-v1-batch13-34-cases-2026-07-14.md`

Latest expansion advisory for the 127 newly added input-only cases:

- Codex first-pass:
  `docs/reports/holdout-codex-first-pass-blind-v1-expansion-127-cases-2026-07-09.md`
- Gemini aggregate:
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-expansion-127-cases-2026-07-09.md`
- Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.md`
- Cases: 127
- Codex confidence: 87 high, 40 medium
- Gemini exact matches with Codex: 79
- Differences from Codex: 48
- Maintainer queue after policy filters: 81
- Difference recommendations: 39 Codex, 7 Gemini, 2 third value
- Status: advisory only by itself; final expected values require maintainer
  decision before being written to private expected

Latest expansion maintainer confirmation packet:

- Markdown:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.md`
- JSON:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-differences-2026-07-09.json`
- Scope: 48 Codex/Gemini difference cases only
- Deferred policy-review cases: 33
- Difference recommendations: 39 Codex, 7 Gemini, 2 third value
- Status: confirmation packet only; not ground truth by itself

Latest expansion differences maintainer decision summary:

- Markdown:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-differences-2026-07-09.md`
- JSON:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-differences-2026-07-09.json`
- Scope: 48 Codex/Gemini difference cases only
- Maintainer decision: accepted all recommended expected values unchanged
- Would-be expected source: 48 `human_adjudication`
- Private expected update: not yet; the current input file has 200 cases, and
  the benchmark runner requires full expected/input alignment
- Remaining expansion review at that step: 33 exact-match policy-review cases

Latest expansion policy-review confirmation packet:

- Markdown:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.md`
- JSON:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json`
- Scope: 33 Codex/Gemini exact-match policy-review cases
- Recommendation: 33 Codex/Gemini match
- Difference cases: 0
- Status: confirmation packet only; not ground truth by itself

Latest expansion policy-review maintainer decision summary:

- Markdown:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.md`
- JSON:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-policy-review-2026-07-09.json`
- Scope: 33 Codex/Gemini exact-match policy-review cases
- Maintainer decision: accepted all recommended expected values unchanged
- Would-be expected source: 33 `human_first_pass`
- Private expected update: recorded by the full 127-case expansion decision
  summary

Latest expansion final decision summary:

- Markdown:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-127-cases-2026-07-09.md`
- JSON:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-expansion-127-cases-2026-07-09.json`
- Scope: all 127 expansion cases
- Expansion expected source: 79 `human_first_pass`, 48 `human_adjudication`
- Total private expected source after rebuild: 135 `human_first_pass`, 65
  `human_adjudication`
- Private expected status: rebuilt to 200 cases, `sealed_private`, gitignored
- The public summary intentionally omits expected values.

Latest maintainer confirmation packet:

- Markdown:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.md`
- JSON:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-0001-0100-2026-07-08.json`
- Cases needing maintainer confirmation: 59
- Difference cases: 30
- Exact but policy-review cases: 29
- No immediate-question cases: 41
- Status: confirmation packet only; not ground truth; not promotion-ready

Latest maintainer final decision summary:

- Markdown:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.md`
- JSON:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-0001-0100-2026-07-08.json`
- Private expected:
  `benchmarks/accuracy/blind-v1.expected.json`
- Private expected status: `sealed_private`
- Approval policy: `single_human_with_ai_advisory`
- Expected source: 70 `human_first_pass`, 30 `human_adjudication`
- The public summary intentionally omits expected values.

Latest private benchmark sanity summary for the 256-case private expected:

- Markdown:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.md`
- JSON:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-2026-07-09.json`
- Engine: `zhtw`
- Accepted: 216 / 256
- Accepted accuracy: 0.8438
- Primary exact accuracy: 0.7188
- Idempotency rate: 0.9883
- Domain accuracy: formal 34/41, high_risk 24/26, it 41/50, llm 38/43,
  social 35/44, ui 44/52.
- Rows and expected values are intentionally omitted from the repo summary.

Latest 261-case private miss classification:

- Codex classification:
  `docs/reports/holdout-miss-classification-blind-v1-261-cases-2026-07-09.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-261-cases-2026-07-09.md`
- Misses classified: 54
- Move to public regression candidate before tuning: 18
- Requires expected/acceptable recheck: 16
- Keep as sealed holdout signal: 20
- Codex revised 7 high-risk / over-conversion guard cases to
  `requires_expected_recheck` after Gemini policy findings.
- Final Gemini review saw sanitized metadata only and reported policy consistent
  with 0 follow-up findings. It did not receive inputs, expected values,
  acceptable variants, zhtw outputs, or benchmark rows.

Latest 261-case requires-expected recheck:

- Codex recheck summary:
  `docs/reports/holdout-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`
- Private maintainer packet:
  `/tmp/zhtw-holdout-261-case-recheck-maintainer-review-packet-2026-07-09.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-requires-expected-recheck-blind-v1-261-cases-2026-07-09.md`
- Recheck cases: 16
- Confirmed acceptable variants: 9
- Moved to public regression candidate: 5
- Kept strict primary expected: 2
- Updated private sanity after final decision: 216 / 256 accepted.
- Gemini reviewed sanitized metadata only and reported policy consistent with 0
  follow-up findings.

Latest batch4 input expansion and advisory:

- Input expansion:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch4-100-cases-2026-07-09.md`
- Codex first pass:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch4-100-cases-2026-07-09.md`
- Gemini advisory:
  `docs/reports/holdout-gemini-vertex-advisory-blind-v1-batch4-100-cases-2026-07-09.md`
- Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch4-100-cases-2026-07-09.md`
- Maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch4-100-cases-2026-07-09.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch4-100-cases-2026-07-09.md`
- Cases added: 100
- Codex/Gemini exact matches: 74
- Differences: 26
- Maintainer queue: 64
- No immediate question: 36
- Private expected status at initial batch4 close: updated to 261 cases,
  `sealed_private`, gitignored. Later batch4 recheck removed 5 cases from sealed.
- Batch4 expected source: 74 `human_first_pass`, 26 `human_adjudication`.

Latest 200-case private miss classification:

- Codex classification:
  `docs/reports/holdout-miss-classification-blind-v1-200-cases-2026-07-09.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-200-cases-2026-07-09.md`
- Misses classified: 56
- Move to public regression candidate before tuning: 39
- Requires expected/acceptable recheck: 11
- Keep as sealed holdout signal: 6
- Gemini reviewed sanitized metadata only and reported policy consistent with 0
  follow-up findings. It did not receive inputs, expected values, acceptable
  variants, zhtw outputs, or benchmark rows.

Latest post-batch3 miss recheck:

- Codex recheck:
  `docs/reports/holdout-post-batch3-miss-recheck-blind-v1-2026-07-09.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-post-batch3-recheck-blind-v1-2026-07-09.md`
- First-pass sealed misses reviewed: 17
- Maintainer review required: 11
- Recommended acceptable variant candidates: 11
- Keep as sealed holdout signal: 6
- Private maintainer packet:
  `/tmp/zhtw-holdout-post-batch3-maintainer-review-packet-2026-07-09.md`
- Maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-post-batch3-recheck-blind-v1-2026-07-09.md`
- Gemini reviewed sanitized metadata only and reported policy consistent with 0
  follow-up findings.
- Maintainer confirmed all 11 acceptable variant recommendations. Private
  expected was updated locally; primary expected values were unchanged.
- Current sealed misses after final decision: 6

Latest remaining signal summary:

- Codex summary:
  `docs/reports/holdout-remaining-signal-summary-blind-v1-2026-07-09.md`
- Gemini sanitized policy review:
  `docs/reports/holdout-gemini-policy-review-remaining-signal-blind-v1-2026-07-09.md`
- Remaining signal cases: 6
- Signal categories: 5 graph-variant over-conversion signals, 1 strict UI
  wording signal
- Policy: keep sealed; do not use for converter or dictionary tuning unless a
  future step first removes the case from sealed holdout and creates a public
  regression candidate artifact.

Latest private miss classification:

- Markdown:
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.md`
- JSON:
  `docs/reports/holdout-miss-classification-blind-v1-2026-07-08.json`
- Misses classified: 43
- Move to public regression candidate: 22
- Keep as sealed holdout signal: 7
- Requires expected recheck: 14
- Non-idempotent misses needing follow-up: 5
- Expected values, converter outputs, input text, and full benchmark rows are
  intentionally omitted from the repo report.

Latest expected/acceptable recheck:

- Markdown:
  `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.md`
- JSON:
  `docs/reports/holdout-expected-recheck-blind-v1-2026-07-09.json`
- Recheck cases: 14
- Private acceptable variants added: 12
- Strict primary expected kept: 2
- Moved to public regression in this step: 0
- After recheck: accepted 69 / 78, misses 9
- Expected values, acceptable variants, input text, converter outputs, and full
  benchmark rows are intentionally omitted from the repo report.

Latest remaining miss classification:

- Markdown:
  `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.md`
- JSON:
  `docs/reports/holdout-remaining-miss-classification-blind-v1-2026-07-09.json`
- Remaining sealed misses classified: 9
- Move to public regression candidate: 5
- Keep as sealed holdout signal: 4
- Idempotency follow-up cases: 1
- Strict after expected recheck: 2
- Expected values, acceptable variants, input text, converter outputs, and full
  benchmark rows are intentionally omitted from the repo report.

Latest holdout-to-regression promotion:

- Candidate dataset:
  `benchmarks/accuracy/holdout-regression-candidates-v1.json`
- First sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-2026-07-09.md`
- First promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-2026-07-09.md`
- Batch2 sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch2-2026-07-09.md`
- Batch2 promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch2-2026-07-09.md`
- Batch3 sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch3-2026-07-09.md`
- Batch3 promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch3-2026-07-09.md`
- Batch4 recheck sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch4-recheck-2026-07-09.md`
- Batch4 recheck promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch4-recheck-2026-07-09.md`
- Remaining-40 final review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-remaining-40-final-review-2026-07-09.md`
- Remaining-40 final review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-remaining-40-final-review-2026-07-09.md`
- 338-case miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-338-miss-review-2026-07-09.md`
- 338-case miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-338-miss-review-2026-07-09.md`
- Batch6 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch6-miss-review-2026-07-10.md`
- Batch6 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch6-miss-review-2026-07-10.md`
- Batch7 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch7-miss-review-2026-07-10.md`
- Batch7 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.md`
- Batch8 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.md`
- Batch8 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.md`
- Batch9 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch9 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch10 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch10-miss-review-2026-07-13.md`
- Batch10 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch10-miss-review-2026-07-13.md`
- Batch12 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch12-miss-review-2026-07-14.md`
- Batch12 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch12-miss-review-2026-07-14.md`
- Batch13 miss review final decision: 5 acceptable variants, 22 public regression
  candidates, and 7 strict private signals.
- Batch13 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch13-miss-review-2026-07-14.md`
- Removed from sealed holdout: 219
- Promotion-ready after conservative full-sentence mappings: 219
- Promoted into `regression-v1.json`: 219
- Sealed pool after batch10 miss review: 751
- Current input-only seed pool after batch13 miss review: 1,008
- Reviewed sealed subset currently covered by private expected: 1,008
- Batch13 inputs confirmed into private expected: 100
- Batch12 inputs confirmed into private expected: 100
- Batch11 inputs confirmed into private expected: 100
- Newly added inputs confirmed into private expected before batch3 removal: 127
- Newly added inputs confirmed into private expected in batch4: 100
- Newly added inputs confirmed into private expected in batch5: 100
- Newly added inputs confirmed into private expected in batch6: 100
- Newly added inputs confirmed into private expected in batch7: 100
- Newly added inputs confirmed into private expected in batch8: 100
- Newly added inputs confirmed into private expected in batch9: 100
- Batch7 input-only expansion audit:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 Gemini CLI independent advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 private sanity:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch7-2026-07-10.md`
- Batch7 review queue: 65 cases total; 28 Codex/Gemini differences, 37 exact
  matches requiring policy review, 35 no immediate question.
- Batch6 Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch6-100-cases-2026-07-10.md`
- Batch6 Gemini CLI independent advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch6-100-cases-2026-07-10.md`
- Batch6 Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch6-100-cases-2026-07-10.md`
- Batch6 maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-100-cases-2026-07-10.md`
- Batch6 maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch6-100-cases-2026-07-10.md`
- Batch6 private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch6-2026-07-10.md`
- Batch6 miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-426-cases-2026-07-10.md`
- Batch6 miss classification maintainer packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch6-miss-classification-2026-07-10.md`
- Batch6 miss classification final decision:
  `docs/reports/holdout-maintainer-final-decision-batch6-miss-classification-blind-v1-2026-07-10.md`
- Batch6 miss review private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch6-miss-review-2026-07-10.md`
- Batch7 maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch7-100-cases-2026-07-10.md`
- Batch7 private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch7-2026-07-10.md`
- Batch7 miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-515-cases-2026-07-10.md`
- Batch7 Gemini miss classification policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-515-cases-2026-07-10.md`
- Batch7 miss classification maintainer packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch7-miss-classification-2026-07-10.md`
- Batch7 miss classification final decision:
  `docs/reports/holdout-maintainer-final-decision-batch7-miss-classification-blind-v1-2026-07-10.md`
- Batch7 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch7-miss-review-2026-07-10.md`
- Batch7 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch7-miss-review-2026-07-10.md`
- Batch7 Gemini public promotion policy review:
  `docs/reports/holdout-gemini-policy-review-batch7-miss-public-promotion-2026-07-10.md`
- Batch7 miss review private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch7-miss-review-2026-07-10.md`
- Batch8 input-only expansion audit:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 Gemini CLI independent advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 maintainer final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch8-100-cases-2026-07-10.md`
- Batch8 private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch8-2026-07-10.md`
- Batch8 miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-598-cases-2026-07-10.md`
- Batch8 Gemini miss classification policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-598-cases-2026-07-10.md`
- Batch8 miss classification maintainer packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch8-miss-classification-2026-07-10.md`
- Batch8 miss classification final decision:
  `docs/reports/holdout-maintainer-final-decision-batch8-miss-classification-blind-v1-2026-07-11.md`
- Batch8 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch8-miss-review-2026-07-11.md`
- Batch8 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch8-miss-review-2026-07-11.md`
- Batch8 Gemini public promotion policy review:
  `docs/reports/holdout-gemini-policy-review-batch8-miss-public-promotion-2026-07-11.md`
- Batch8 miss review private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch8-miss-review-2026-07-11.md`
- Batch8 miss classification queue: 19 cases total; 15 public regression
  candidates, 4 expected recheck cases, 30 no immediate question.
- Batch9 input-only expansion audit:
  `docs/reports/holdout-input-pool-expansion-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 Codex first-pass advisory:
  `docs/reports/holdout-codex-first-pass-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 Gemini CLI independent advisory:
  `docs/reports/holdout-gemini-cli-advisory-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 Codex/Gemini diff review:
  `docs/reports/holdout-codex-gemini-diff-review-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 maintainer confirmation packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 final decision:
  `docs/reports/holdout-maintainer-final-decision-blind-v1-batch9-100-cases-2026-07-12.md`
- Batch9 private sanity aggregate:
  `docs/reports/holdout-private-benchmark-sanity-blind-v1-after-batch9-miss-review-2026-07-12.md`
- Batch9 review queue: 69 cases total; 30 Codex/Gemini differences, 39 exact
  matches requiring policy review, 31 no immediate question.
- Batch9 miss classification:
  `docs/reports/holdout-miss-classification-blind-v1-683-cases-2026-07-12.md`
- Batch9 Gemini miss-classification policy review:
  `docs/reports/holdout-gemini-policy-review-miss-classification-blind-v1-683-cases-2026-07-12.md`
- Batch9 miss-classification maintainer packet:
  `docs/reports/holdout-maintainer-confirmation-blind-v1-batch9-miss-classification-2026-07-12.md`
- Batch9 miss-classification queue: 22 cases total; 16 public regression
  candidates, 6 expected recheck cases, 31 no immediate question.
- Batch9 miss-classification final decision:
  `docs/reports/holdout-maintainer-final-decision-batch9-miss-classification-blind-v1-2026-07-12.md`
- Batch9 miss review sealed pool update:
  `docs/reports/holdout-sealed-pool-update-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch9 miss review promotion gate:
  `docs/reports/holdout-regression-promotion-gate-blind-v1-batch9-miss-review-2026-07-12.md`
- Batch9 Gemini public promotion policy review:
  `docs/reports/holdout-gemini-policy-review-batch9-miss-public-promotion-2026-07-12.md`

## Path To 1,000 Cases

`regression-v1` covers all 500 currently available curated corpus cases, 500
approved annotation promotions, 219 cases removed from sealed holdout before
tuning, and 32 public reproduction promotions. The M1 target of 1,000 public
regression cases is complete; current public regression coverage is 1,251. Do
not synthesize expected outputs from zhtw or competitors.

Recommended gap:

| Area | Uncollected Cases |
|------|-------------------|
| IT/API/CLI | 0 |
| UI/i18n | 0 |
| Formal/news/legal/finance/medical | 0 |
| Social/daily | 0 |
| Ambiguous mixed-context regressions | 0 |

The gap is tracked in:

- `annotation-backlog-v1.json`
- `annotation-backlog-v1.schema.json`
- `scripts/accuracy_annotation_status.py`
- `scripts/check_accuracy_backlog.py`
- `scripts/promote_accuracy_backlog.py`

Current backlog progress:

| Batch | Collected | Needs maintainer review | Approved | Target |
|-------|-----------|-------------------------|----------|--------|
| it-api-cli | 175 | 0 | 175 | 175 |
| ui-i18n | 125 | 0 | 125 | 125 |
| formal-high-risk | 100 | 0 | 100 | 100 |
| social-daily | 75 | 0 | 75 | 75 |
| mixed-ambiguity | 25 | 0 | 25 | 25 |

The first `it-api-cli` batch includes `ai_draft` suggestions copied from
`docs/reports/annotation-first-pass-ai-draft-2026-07-05.md`. These are reference
notes only. Reviewer `tim` has completed first pass by writing `review.expected`
from the draft after review.

The first batch was then checked against Gemini Vertex advisory output. Maintainer
`tim` accepted the Gemini advisory decision on 2026-07-05:

- 11 cases matched the first pass exactly and remain `human_first_pass`.
- 14 cases differed and were updated to the Gemini advisory version as
  `human_adjudication`.
- Gemini is recorded under `review.ai_advisory`; it is not recorded as a human
  `blind_reviewer`.
- All 25 cases are now `approved` and promotion-ready under the
  `single_human_with_ai_advisory_or_independent_blind_review` policy.

The second `it-api-cli` batch contains 50 candidate inputs:

- IDs: `it-api-cli-0026` through `it-api-cli-0075`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0026-0075-2026-07-05.md`
- Gemini Vertex advisory report:
  `docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.md`
- Current status: `approved`
- Gemini matched the Codex draft on 25 cases and differed on 25 cases.
- Maintainer `tim` accepted the Gemini version for all 25 differing cases on
  2026-07-05. The matching 25 cases remain `human_first_pass`; the differing 25
  cases are recorded as `human_adjudication`.

The third `it-api-cli` batch contains 50 candidate inputs:

- IDs: `it-api-cli-0076` through `it-api-cli-0125`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0076-0125-2026-07-06.md`
- Gemini Vertex advisory report:
  `docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.md`
- Current status: `approved`
- Gemini matched the Codex draft on 24 cases and differed on 26 cases.
- Maintainer `tim` accepted the Codex version for all 26 differing cases on
  2026-07-06. The matching 24 cases remain `human_first_pass`; the differing 26
  cases are recorded as `human_adjudication` with Gemini advisory rejected.

The fourth `it-api-cli` batch contains 50 candidate inputs:

- IDs: `it-api-cli-0126` through `it-api-cli-0175`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-it-api-cli-0126-0175-2026-07-06.md`
- Gemini Vertex advisory report:
  `docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.md`
- Current status: `approved`
- Gemini matched the Codex draft on 34 cases and differed on 16 cases.
- Maintainer `tim` accepted the Gemini version for all 16 differing cases on
  2026-07-06. The matching 34 cases remain `human_first_pass`; the differing 16
  cases are recorded as `human_adjudication`.
- These 50 cases are now `approved` and promotion-ready.

The first `ui-i18n` work unit contains 100 candidate inputs:

- IDs: `ui-i18n-0001` through `ui-i18n-0100`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-ui-i18n-0001-0100-2026-07-06.md`
- Gemini Vertex advisory reports:
  - `docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0001-0050-2026-07-06.md`
  - `docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0051-0100-2026-07-06.md`
- Codex difference review:
  `docs/reports/annotation-codex-review-ui-i18n-0001-0100-2026-07-06.md`
- Current status: `approved`
- Gemini matched the Codex draft on 72 cases and differed on 28 cases.
- Maintainer `tim` accepted the Codex recommendation on 2026-07-06:
  72 exact-match cases use the shared Codex/Gemini expected output as
  `human_first_pass`; 4 differing cases use the Gemini advisory expected output;
  24 differing cases use the Codex expected output with Gemini advisory rejected.
- These 100 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

The second `ui-i18n` work unit contains 25 candidate inputs:

- IDs: `ui-i18n-0101` through `ui-i18n-0125`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-ui-i18n-0101-0125-2026-07-06.md`
- Gemini Vertex advisory report:
  `docs/reports/annotation-gemini-vertex-advisory-ui-i18n-0101-0125-2026-07-06.md`
- Codex difference review:
  `docs/reports/annotation-codex-review-ui-i18n-0101-0125-2026-07-06.md`
- Current status: `approved`
- Gemini matched the Codex draft on 18 cases and differed on 7 cases.
- Maintainer `tim` accepted the Codex recommendation on 2026-07-06:
  18 exact-match cases use the shared Codex/Gemini expected output as
  `human_first_pass`; 1 differing case uses the Gemini advisory expected output;
  6 differing cases use the Codex expected output with Gemini advisory rejected.
- These 25 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

The first `formal-high-risk` work unit contains 100 candidate inputs:

- IDs: `formal-high-risk-0001` through `formal-high-risk-0100`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-formal-high-risk-0001-0100-2026-07-06.md`
- Gemini Vertex advisory reports:
  - `docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.md`
  - `docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.md`
- Codex difference review:
  `docs/reports/annotation-codex-review-formal-high-risk-0001-0100-2026-07-06.md`
- Current status: `approved`
- Gemini matched the Codex draft on 91 cases and differed on 9 cases.
- Maintainer `tim` accepted final expected values on 2026-07-07:
  91 exact-match cases use the shared Codex/Gemini expected output as
  `human_first_pass`; 7 differing cases use the Gemini advisory expected output;
  2 differing cases use the Codex expected output with Gemini advisory rejected.
- These 100 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

The first `social-daily` work unit contains 75 candidate inputs:

- IDs: `social-daily-0001` through `social-daily-0075`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-social-daily-0001-0075-2026-07-07.md`
- Gemini Vertex advisory reports:
  - `docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.md`
  - `docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.md`
- Codex difference review:
  `docs/reports/annotation-codex-review-social-daily-mixed-0001-0100-2026-07-07.md`
- Current status: `approved`
- Gemini matched the Codex draft on 60 cases and differed on 15 cases.
- Maintainer `tim` accepted final expected values on 2026-07-07:
  60 exact-match cases use the shared Codex/Gemini expected output as
  `human_first_pass`; 2 differing cases use the Gemini advisory expected output;
  13 differing cases use the Codex expected output with Gemini advisory rejected.
- These 75 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

The first `mixed-ambiguity` work unit contains 25 candidate inputs:

- IDs: `mixed-ambiguity-0001` through `mixed-ambiguity-0025`
- Codex AI draft report:
  `docs/reports/annotation-first-pass-ai-draft-mixed-ambiguity-0001-0025-2026-07-07.md`
- Gemini Vertex advisory report:
  `docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.md`
- Codex difference review:
  `docs/reports/annotation-codex-review-social-daily-mixed-0001-0100-2026-07-07.md`
- Current status: `approved`
- Gemini matched the Codex draft on 18 cases and differed on 7 cases.
- Maintainer `tim` accepted final expected values on 2026-07-07:
  18 exact-match cases use the shared Codex/Gemini expected output as
  `human_first_pass`; 1 differing case uses the Gemini advisory expected output;
  6 differing cases use the Codex expected output with Gemini advisory rejected.
- These 25 cases are now `approved`, promotion-ready, and promoted into
  `regression-v1.json`.

Check progress:

```bash
make accuracy-annotation-status
uv run python scripts/accuracy_annotation_status.py --format json
```

Check approved cases against the current zhtw converter before promotion:

```bash
make accuracy-promotion-gate DATE=2026-07-07
uv run python scripts/check_accuracy_backlog.py \
  --generated-date 2026-07-07 \
  --fail-on-mismatch
```

Latest gate result for the approved annotation cases:

- Report: `docs/reports/annotation-promotion-gate-2026-07-07.md`
- Approved checked: 500
- Skipped not promotion-ready: 0
- Promotion ready now: 500
- Needs zhtw fix before promotion: 0
- Expected idempotent: 500
- Promoted into `regression-v1.json`: 500

Do not promote failing cases into `regression-v1.json` until zhtw output matches
their approved expected value.

Create a blind review packet that hides first-pass expected output:

```bash
make accuracy-blind-review-packet BATCH=it-api-cli DATE=2026-07-05
uv run python scripts/create_blind_review_packet.py \
  --batch it-api-cli \
  --generated-date 2026-07-05 \
  --output docs/reports/annotation-blind-review-packet-it-api-cli-2026-07-05.md
```

Promotion rule:

1. Collect candidate inputs without expected generated from zhtw or competitors.
2. Codex may write `ai_draft` as the first advisory pass. This is not ground
   truth and must not populate `review.expected`.
3. Gemini runs an independent advisory pass from the input only. Pending output
   is recorded as `review.ai_advisory_draft` and the case moves to
   `needs_maintainer_review`.
4. Maintainer final review chooses the Taiwan Traditional expected value and
   writes `review.expected`.
5. If the maintainer accepts an unchanged advisory value, use
   `expected_source = "human_first_pass"`. If the maintainer resolves a Codex vs
   Gemini difference or writes a third version, use
   `expected_source = "human_adjudication"` and set `adjudicator`.
6. Gemini output must be recorded under `review.ai_advisory`, not as a human
   `blind_reviewer`. If maintainer accepts Gemini, use
   `decision = "accepted"`; if maintainer rejects Gemini during adjudication,
   use `decision = "rejected"` and keep `expected_source = "human_adjudication"`.
7. `approved` counts as promotion-ready only when `expected` is non-empty,
   `expected_source` is `human_first_pass` or `human_adjudication`, and the case
   has either a different human blind reviewer or a recorded `review.ai_advisory`.
8. Disagreement or `human_adjudication` cases require a non-empty `adjudicator`.
9. Only promotion-ready `approved` cases can be promoted into `regression-v1.json`.
10. After promotion, run `uv run python -m pytest tests/test_accuracy_regression.py -q`.
