# Precision and Language Capability Roadmap

> Status: 4.4.4 implementation and local release gate complete
> Recorded: 2026-08-09
> Completed: 2026-08-10
> Future version allocation synchronized: 2026-08-27
> Version scope source: https://rajatim.wiki/projects/zhtw/roadmap/
> Implementation detail: `docs/plans/2026-08-27-4-5-0-rule-foundation-plan.md`

## 1. Goal

Improve zhtw by making the default conversion path safer before expanding its
vocabulary. The target remains Taiwan Traditional Chinese. Broader capability
comes from additional source locales, domain profiles, complete Unicode
handling, and structured file adapters rather than one global set of risky
rules.

The guiding order is:

1. prevent wrong conversions;
2. make a second conversion produce the same result;
3. improve missing conversions with reviewed evidence;
4. add optional locale and domain coverage.

## 2. Review findings

### 2.1 Overlap coverage can hide an unselected suffix

The matcher currently marks every raw Aho-Corasick hit as covered, including a
hit that loses overlap selection. The character layer then skips those
positions. For example, a selected prefix term can leave the final `于` in
`应用于` unchanged instead of producing `應用於`.

The correct coverage is the union of:

- selected non-identity term spans; and
- effective identity-protection spans.

Unselected non-identity hits must not block character conversion.

### 2.2 Metadata is counted and exported as vocabulary

Keys such as `_comment_*` are documentation, but the runtime loader currently
accepts them as conversion rules. The CN data contains 176 such keys and the HK
data contains one. Runtime loading, statistics, and SDK export must exclude
reserved metadata consistently.

### 2.3 Bulk and reviewed rules have different trust levels

Most current CN coverage comes from the OpenCC-derived bulk file. It provides
useful breadth, but it also causes the known Blind-v2 second-pass changes and is
excluded from several quality gates. Raw rule count is therefore not a useful
quality target.

The long-term model should distinguish:

- `curated`: reviewed, low-risk rules enabled by default;
- `extended`: broad rules enabled explicitly until promoted by evidence.

The 4.4.4 patch strengthens measurement and safety without silently changing
the public default dictionary profile. A default profile change is reserved for
5.0.0.

### 2.4 Context and source coverage are still narrow

The context resolver has only a small set of balanced rules and protection
phrases. Runtime source selection supports CN and HK, while HK has little
reviewed coverage. Chinese detection and term import also exclude several CJK
extensions and valid mixed technical phrases.

### 2.5 Audits must measure the production pipeline

Some audit helpers reproduce older term-then-character logic instead of calling
the canonical converter. LLM term review also accepts incomplete or ambiguous
responses too easily. Quality tools must fail safely and use the same engine as
the public API.

## 3. Version 4.4.4 scope

### Matcher and SDK parity

- [x] Fix effective covered-position calculation in Python.
- [x] Add overlap-plus-character regression cases such as `应用于` and
  `两千万`.
- [x] Apply the same behavior to Java, TypeScript, Rust, Go, and .NET.
- [x] Export shared golden cases and verify byte-for-byte SDK parity.

### Dictionary and reporting safety

- [x] Filter underscore-prefixed metadata in wrapped and flat dictionary data.
- [x] Add loader and exporter regressions for metadata exclusion.
- [x] Report lexical terms separately from metadata and generated guards.
- [x] Replace the raw 30,000-rule assertion with checks that describe useful
  and reviewed coverage.

### Review and audit reliability

- [x] Make LLM term validation reject missing, invalid, or unclear verdicts.
- [x] Prevent negative wording such as `不正確` from being read as approval.
- [x] Route quality audit conversion through the canonical public engine.
- [x] Keep AI review advisory; no AI result becomes dictionary truth without a
  maintainer decision.

### Reproducibility and release robustness

- [x] Pin the Unicode/Unihan source version and checksum in charmap generation.
- [x] Record the pinned source in generated metadata.
- [x] Make subprocess tests use the active Python interpreter and project
  source tree.
- [x] Update the changelog and all mono-versioned artifacts to 4.4.4.

### Required gates

- [x] `zhtw validate`
- [x] `make version-check`
- [x] `make export-check`
- [x] complete Python test suite
- [x] complete Java, TypeScript, Rust, Go, and .NET test suites
- [x] release gate and public accuracy regression checks that are available
  locally
- [x] clean final diff with no tag, registry publication, or release action

### Completion evidence

- `make release-gate` passed on 2026-08-10.
- Python: 5,475 tests passed.
- Java: 159 tests passed.
- TypeScript: 162 tests passed and one optional test was skipped; type checking,
  build, and CommonJS/ESM package smoke tests passed.
- Rust/WASM, Go race tests, Go vet/lint, and .NET's 26 tests passed.
- Every effective CN/HK dictionary target is stable on a second conversion.
- Blind-v2 aggregate sentence idempotency improved from 1,915/1,960 (97.70%)
  to 1,925/1,960 (98.21%). No sealed row content was inspected or used for
  tuning.
- The public UD-GSD secondary diagnostic improved from 3,524/4,997 exact
  matches (70.52%) to 3,544/4,997 (70.92%), while idempotency improved from
  97.94% to 99.14%.
- No commit, tag, release action, or registry publication was made.

### Independent language advisory

The Codex first pass and a separate Gemini review run through `agy` agreed on
the low-risk public regression examples used in this release, including
`应用于` → `應用於` and `两千万` → `兩千萬`. The second review saw the inputs and
project safety rules, but not the Codex conclusions.

The reviewers disagreed about the existing protected phrase
`党太尉吃匾食`. Version 4.4.4 leaves that established rule unchanged and records
it for a later maintainer review. AI output remains advice rather than language
ground truth.

## 4. Allocated 4.x scope

The earlier candidate list is now assigned to explicit releases. The private
operator roadmap fixes version goals and acceptance criteria; the repository
implementation plan fixes files, APIs, migration steps, tests, and rollback.
Neither document may expand the other's scope independently.

### Version 4.5.0: explainable rule foundation

- rule schema v2 with stable ID, source locale, domain, trust level, priority,
  context, evidence source, and review status;
- Unicode 17.0 Han detection through Extension J and safe mixed
  Chinese/Latin/number candidate import as part of the v2 review workflow;
- report-only `explain` output for applied, protected, and rejected candidates;
- an explicit opt-in JSON value adapter that preserves every non-value input
  byte and never changes normal text conversion by default.

### Version 4.6.0: profiles and structured files

- separate `general`, `ui`, `it`, `formal`, `medical`, `legal`, and `social`
  profiles;
- opt-in XML/Android resources, gettext, Fluent, ICU message, Markdown, and
  HTML adapters with parser, placeholder, and round-trip structure gates.

### Version 4.7.0: regional source support

- stronger HK coverage;
- evidence-based Singapore and Macau source packs after the required native
  source-region and Taiwan-output reviews.

Every 4.x feature remains additive. Metadata, profiles, adapters, and regional
packs must not silently change the established default output.

## 5. Version 5.0.0 boundary

Use a major release only when changing established output behavior, including:

- making the reviewed dictionary the only default and moving broad bulk rules
  behind an explicit extended option;
- replacing simple leftmost-longest selection with a context-aware resolver;
- replacing the current source strings with a richer locale/profile API.

## 6. Accuracy evaluation order

Work first on semantic errors, over-conversion, wrong characters, and stable
second-pass output. Regional wording differences come later through profiles.
Sentence exact match must be reported together with changed-span precision,
recall, negative-corpus regressions, per-domain results, and second-pass
stability.

Do not tune against sealed Blind-v2 rows. Use approved public regressions for
development and run a fresh Blind-v3 evaluation after the implementation is
frozen.
