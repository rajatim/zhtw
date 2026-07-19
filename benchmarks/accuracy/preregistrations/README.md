<!-- zhtw:disable -->
# Benchmark Preregistrations

Formal benchmark runs require a frozen preregistration conforming to
`../preregistration.schema.json`. It binds the dataset, inputs, private expected
hash, zhtw commit, competitor lock, normalization, ranking policy, and power
analysis before any score is read.

Preregistration files must not contain a private expected path or case-level
content. The first Blind-v2 preregistration is created by Issue #43.

Before creating that preregistration:

1. Freeze and validate the candidate pool.
2. Rebuild the input-only sample from the frozen pool, seed, and formal N.
3. Complete Codex and Gemini advisory packets without converter output.
4. Record maintainer decisions covering N/N case IDs.
5. Seal the gitignored expected file and bind only its SHA-256 here.
6. Confirm the private evaluation ledger has no prior `score_exposed` event for
   this preregistration.

The formal runner must eventually append `run_started` before invoking any
engine and either `run_interrupted` or `score_exposed` afterward. Once a score is
exposed, the same preregistration cannot be used for another fresh claim.
