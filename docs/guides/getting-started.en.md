# Five-minute start

## Install the CLI

Python 3.10 or later is required:

```bash
python3 -m pip install zhtw
zhtw --version
```

## Convert your first text

```bash
echo "这个软件需要网络连接" | zhtw explain --source cn
```

`explain` shows the converted output and the rules that were involved. When you only need the result in code, use the Python API:

```python
from zhtw import convert

assert convert("这个软件", sources=["cn"]) == "這個軟體"
```

## Check before changing files

```bash
zhtw check ./locales --source cn
zhtw fix ./locales --source cn --dry-run
zhtw fix ./locales --source cn --show-diff
```

`check` never changes files. `fix --dry-run` simulates a write, while `--show-diff` displays the changes before asking. Keep source files in version control or back them up before automated writes.

## Choose a runtime

| Need | Recommended option |
|---|---|
| Scan a repository or locale directory | Python CLI |
| Convert inside a Python program | `zhtw` Python package |
| Java, Node.js, Rust, Go, or .NET | Native SDK |
| Keep browser text off a backend | `zhtw-wasm` Browser WebAssembly |
| Process JSON locale files | Explicitly enable the [JSON adapter](../reference/json-adapter.md) |

Continue with [CLI and files](cli-and-files.md) or [SDKs and Browser WASM](sdk-and-browser.md).
