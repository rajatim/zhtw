# JSON adapter reference

> Available since 4.5.0. The caller must explicitly enable the adapter. Normal text conversion is unchanged.

## Purpose

The JSON adapter converts string values only. It does not convert object keys. This is useful for configuration files, locale files, and API fixtures where content must change without changing the structure or unrelated formatting.

```json
{
  "软件 key": "这个软件",
  "number": 1.00e+02
}
```

Only the value changes:

```json
{
  "软件 key": "這個軟體",
  "number": 1.00e+02
}
```

## Python API

```python
from zhtw import convert_json

output = convert_json('{"软件":"这个软件","number":1}', sources=["cn"])
assert output == '{"软件":"這個軟體","number":1}'
```

`convert_json()` accepts a complete JSON string and returns a converted JSON string. Invalid input or duplicate object keys raise `JsonAdapterError`; no partial result is returned.

## CLI

```bash
zhtw check ./locales --adapter json --source cn
zhtw fix ./locales --adapter json --source cn --show-diff
```

Directory mode processes `.json` files only. Single-file mode also requires a `.json` extension. `--adapter json` controls input parsing, while `--json` only controls the CLI report format.

## Byte preservation

- The full document is validated with a JSON parser before token spans are scanned.
- Object keys, whitespace, indentation, line endings, number forms, booleans, `null`, structure, and array order stay unchanged.
- Unchanged string values keep their original escapes and bytes.
- Only a changed string value is emitted again. It uses compact JSON escaping, keeps Unicode characters directly, and escapes required quotes, backslashes, and control characters.
- The output is parsed again to confirm that keys and non-string values did not change.
- Duplicate keys fail closed (安全失敗), including keys that become equal after escape decoding, such as `key` and `\u006bey`.
- `NaN`, `Infinity`, trailing commas, and other invalid JSON are rejected.

## Write safety

During CLI fixes, ZHTW creates a temporary file in the source directory. It completes encoding, flush, and `fsync` before an atomic replacement. If parsing, conversion, encoding, verification, or writing fails, the command exits with a non-zero status and leaves the original file unchanged. Read-only files are rejected.

Exact-byte cross-SDK cases are stored in `sdk/data/json-adapter-golden.json`. Every implementation uses the same input and expected output.
