<!-- zhtw:disable -->
# Blind-v3 Fresh Accuracy Benchmark Plan

Date: 2026-08-01

Status: `ready_for_private_collection`

Tracking issue: [#53](https://github.com/rajatim/zhtw/issues/53)

## 1. Goal

Blind-v3 will provide fresh evidence for a future zhtw release after 4.4.3. It
must measure generalization on inputs that were not used to build, review, or tune
the converter.

Blind-v2 remains a published monitoring set. Its 5,896-case candidate pool, 1,960
frozen inputs, expected values, misses, and post-result review artifacts must not
be reused in Blind-v3.

## 2. Private-by-default storage

All pre-run Blind-v3 material stays under `benchmarks/accuracy/private/`:

```text
benchmarks/accuracy/private/blind-v3/
  candidate-pool.json
  inputs.json
  expected.json
  annotation-ledger.jsonl
  evaluation-ledger.jsonl
  detailed-output/
```

The repository may publish schemas, process documentation, source manifests,
license records, preregistration hashes, and aggregate final reports. It must not
publish candidate text, frozen input text, expected values, acceptable variants,
case IDs linked to results, converter output, or detailed misses before the formal
one-shot run is complete.

Repository ignore rules and tests reject accidental top-level Blind-v3 artifacts.
Before every push, `scripts/audit_benchmark_publication.py` remains mandatory.

## 3. Source collection

Build at least `max(3 × N, 1,800)` new input candidates. Every source must be one
of the following:

- new public-domain text collected after the Blind-v2 freeze;
- newly pinned permissive-license corpora that Blind-v2 did not use;
- newly created project-original text written without converter output;
- private, permissioned user text with a recorded right to use and publish only
  aggregate results.

Do not select text because zhtw, OpenCC, zhconv, or an LLM converts it well or
badly. Do not use search queries based on known Blind-v2 misses. Record source
class, license, citation, retrieval date, immutable revision, and content hash.

Use the Blind-v2 domain and risk quotas as the starting distribution. Recalculate
the formal sample size with paired power analysis before freezing. Exact and
near-duplicate checks must cover Blind-v1, Blind-v2, all public regression cases,
all public benchmark inputs, dictionary source and target phrases, and the new
candidate pool itself.

## 4. Annotation and review

For each frozen case:

1. Codex prepares the first expected-value proposal, acceptable variants, risk,
   and reason without seeing converter output.
2. Agy performs an independent review with only the input and annotation rules.
3. Codex compares both reviews and lists disagreements, high-risk cases, and low
   confidence cases.
4. The maintainer reviews the complete packet and makes the final human decision.
5. Metadata records `single_human_with_ai_advisory`; AI output is never ground
   truth.

Review packets and expected values remain private. Public artifacts contain only
coverage totals, hashes, reviewer roles, and approval dates.

## 5. Freeze and one-shot run

Before evaluation, commit a public preregistration containing:

- source manifest hashes and license summary;
- frozen input and expected hashes;
- selected zhtw commit and version;
- locked competitor versions and container digest;
- normalization and accepted-output rules;
- primary endpoint, risk metrics, idempotency metric, ranking policy, and power
  result;
- random seed and deterministic replacement policy.

Run the formal comparison once on a controlled local or self-hosted machine. Do
not upload private artifacts or detailed logs. Only aggregate results may be read
first. Any interrupted rerun must use identical hashes and be written to the
private evaluation ledger.

After the first score is visible, Blind-v3 is no longer fresh for a converter
changed in response to that score. Such changes require Blind-v4 for a new fresh
claim.

## 6. Required outputs

- private candidate pool, frozen inputs, expected values, annotation ledger, and
  evaluation ledger;
- public source and license manifest;
- public preregistration with immutable hashes;
- aggregate market report with confidence intervals and paired tests;
- current-version idempotency result;
- publication audit result;
- optional independent reproduction package that contains no private data.

## 7. Completion gates

- [ ] New candidate pool reaches the required size and source quotas.
- [ ] No Blind-v1, Blind-v2, public benchmark, regression, or dictionary leakage.
- [ ] Every case has a maintainer decision after Codex and independent Agy advice.
- [ ] Power analysis fixes the final N before sampling.
- [ ] Inputs, expected values, competitor locks, code, and protocol are frozen.
- [ ] The one-shot ledger proves no post-score tuning occurred.
- [ ] Aggregate report passes publication and license audits.
- [ ] README claims name the evaluated zhtw version and Blind-v3 result.

## 8. Execution order

1. Create schemas and private directory templates outside git.
2. Collect and license-check new sources.
3. Normalize, classify, and deduplicate the candidate pool.
4. Run power analysis and freeze the deterministic sample.
5. Complete Codex, Agy, and maintainer annotation.
6. Commit preregistration hashes.
7. Run the one-shot comparison.
8. Publish the aggregate report and update product claims.

Blind-v3 work must not start by copying the public Blind-v2 candidate pool.
