# Explain API reference

> Available since 4.5.0. Shared fixtures verify the event shape in every SDK.

`explain` uses the same Aho-Corasick scan as the production matcher. It returns both the converted output and rule events. It does not run a second, simpler algorithm, so `explain(text).output` must always equal `convert(text)`.

## Python

```python
from zhtw import explain

result = explain("这个软件", sources=["cn"])
print(result.output)
# 這個軟體

for event in result.events:
    print(event.rule_id, event.reason_code, event.input_start, event.input_end)
```

Call `result.to_mapping()` for the shared JSON shape. All indexes are Unicode code-point indexes, and `end` is outside the span.

## CLI

```bash
zhtw explain "这个软件" --source cn
zhtw explain "这个软件" --source cn --json
echo "这个软件" | zhtw explain --source cn
```

Events normally contain only the matched `source`, `target`, and spans. They do not contain the complete input, file path, or nearby text. `--context` adds nearby text to each event. Do not enable it when processing customer data or other sensitive text.

## Event fields

| Field | Meaning |
|---|---|
| `rule_id` | Stable rule ID; character rules use `charmap:u...`, and balanced rules use `balanced:u...` |
| `layer` | `term`, `identity`, `balanced`, or `char` |
| `outcome` | `applied`, `protected`, or `skipped` |
| `input_start` / `input_end` | Code-point span in the original input |
| `output_start` / `output_end` | Code-point span in the converted output |
| `source` / `target` | Source and target stored in the rule |
| `reason_code` | Stable short code for program decisions |

## Reason codes

| Code | Meaning |
|---|---|
| `term_selected` | The longest matching term was selected |
| `identity_guard` | An identity rule protected this span |
| `identity_contained` | An identity candidate was fully inside a longer conversion |
| `overlap_loser` | A raw candidate was not selected because it overlapped another match |
| `protected_by_identity` | A conversion candidate overlapped an active identity guard |
| `loader_conflict_winner` | This approved definition won loader precedence |
| `loader_conflict_loser` | Another approved definition won loader precedence |
| `balanced_default` | Balanced mode handled an uncovered ambiguous character |
| `char_map` | A safe character mapping handled an uncovered character |

## Low-level API

Callers with a custom `Matcher` can use `explain_text`:

```python
from zhtw import Matcher, explain_text

matcher = Matcher({"软件": "軟體"})
result = explain_text("软件", matcher)
```

Pass `RuleRecord` values to `Matcher` to return custom rule IDs. Without them, ZHTW creates deterministic legacy custom IDs.
