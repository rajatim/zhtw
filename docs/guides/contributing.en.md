# Contributing

ZHTW welcomes code, documentation, terms, and real text that you have the right to publish. The repository [contribution guide](https://github.com/rajatim/zhtw/blob/main/CONTRIBUTING.md) is the full development guide.

## Report an incorrect or missing conversion

Open a [GitHub Issue](https://github.com/rajatim/zhtw/issues) with:

1. The zhtw version, source, and ambiguity mode.
2. The shortest complete input that keeps the needed context.
3. The actual result and your suggested Taiwan Traditional result.
4. A reason or public source for the Taiwan usage.
5. A counterexample that a new rule might damage.

Do not submit one ambiguous term without context. Report security problems privately through the [Security Policy](https://github.com/rajatim/zhtw/blob/main/SECURITY.md).

## Change a dictionary

Converting less is better than converting incorrectly. A broad term needs Taiwan-context evidence. Add an identity mapping and a regression test when a rule could damage a correct substring.

```bash
uv sync --extra dev
uv run zhtw validate
uv run pytest
make docs-build
```

If a version changes, use `make bump VERSION=X.Y.Z` to update every SDK. Never update only one package by hand.

## AI and human decisions

AI can organize candidates, find counterexamples, and give advice. The maintainer must make the final decision for benchmark expected values, annotations, and accepted terms. Do not use AI output directly as ground truth.

Contributions must not contain credentials, customer data, private expected values, or third-party text that you cannot publish.
