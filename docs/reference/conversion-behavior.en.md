# Conversion behavior and limits

## Conservative conversion

ZHTW follows one main rule: it is better to convert less than to convert incorrectly. When context is weak, the tool may intentionally keep the input unchanged. This is a safety boundary, not proof that every unchanged character is a bug.

Processing follows this order:

1. Leftmost-longest matching selects the more complete term rule.
2. Identity rules protect text that is already correct or could be damaged by a shorter rule.
3. A small set of high-confidence ambiguous-character defaults is used only when the caller selects `balanced` mode.
4. Safe one-to-one character mappings are applied to the remaining positions.

## Source locales

- `cn`: Simplified Chinese, common Mainland Chinese terms, and their Taiwan forms.
- `hk`: Hong Kong Traditional Chinese terms converted to Taiwan usage.
- `cn,hk`: the CLI default, combining both sources in a fixed order.

`source` describes the input locale. It does not change the output locale, which is always Taiwan Traditional Chinese.

## Identity protection

An identity mapping has the same source and target. It occupies text that is already correct and prevents a shorter rule from changing part of it. It also helps keep conversion idempotent (可重複執行、結果不變).

## Known limits

- There is no sentence-understanding model. Text rules cannot understand every person name, place name, wordplay case, or specialist context.
- `strict` mode does not guess ambiguous characters without context. `balanced` still covers only a limited set.
- Custom dictionaries can override built-in rules. Callers must test the risk of incorrect conversion.
- Normal text mode processes the full text. Structured JSON requires the adapter to be enabled.
- A benchmark score only covers its stated version, data set, and scoring rules. It is not a guarantee for every real document.

To inspect one result, use `zhtw explain` and see the [Explain API](explain-api.md).
