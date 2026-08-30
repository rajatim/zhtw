# CLI and files

## Main commands

| Command | Purpose | Changes data |
|---|---|---|
| `zhtw check PATH` | Scan one file or a directory and report differences | No |
| `zhtw fix PATH` | Convert and write files | Yes |
| `zhtw lookup TEXT` | Inspect term conversion and its source | No |
| `zhtw explain TEXT` | Return output and rule events | No |
| `zhtw stats` | Show rule and character-map counts | No |
| `zhtw validate` | Validate the maintained dictionaries | No |

Run `zhtw COMMAND --help` for the complete options in your installed version. This site does not copy the full help text because that would create a second source that could become stale.

## Common safety options

```bash
zhtw check ./src --source cn --json
zhtw fix ./src --source cn --dry-run
zhtw fix ./src --source cn --show-diff
zhtw fix ./src --source cn --backup
zhtw check ./src --exclude node_modules,dist
```

- `--source cn` handles Simplified Chinese input only; `hk` handles Hong Kong Traditional Chinese. The default is `cn,hk`.
- `--ambiguity-mode strict` is the conservative default. `balanced` applies defaults for a small set of high-confidence ambiguous characters.
- `--no-char-convert` disables the character layer and keeps term rules active.
- `--json` changes the CLI report format. It does not enable structured JSON processing.

## JSON files

Normal `check` and `fix` commands treat a file as text. To keep keys, number forms, and formatting unchanged while converting string values, explicitly add `--adapter json`:

```bash
zhtw check ./locales --adapter json --source cn
zhtw fix ./locales --adapter json --source cn --show-diff
```

See the [JSON adapter](../reference/json-adapter.md) for failure and write-safety rules.

## Ignoring content

A `.zhtwignore` file at the project root supports directory and glob rules similar to `.gitignore`. In source files, `zhtw:disable-next`, `zhtw:disable`, and `zhtw:enable` can protect blocks that must stay unchanged.

The existing [advanced CLI guide](https://github.com/rajatim/zhtw/blob/main/docs/guides/CLI-ADVANCED.md) covers Big5, GBK, GB2312, GB18030, UTF-8, and custom dictionaries. Its English replacement is planned, so it is not part of the stable bilingual navigation yet.
