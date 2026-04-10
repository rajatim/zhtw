<!-- zhtw:disable -->
# SDK check() parity — 跳過 term-covered char matches

**Date:** 2026-04-10
**Status:** Ready for implementation

---

## Goal

修正 Java/TypeScript/Rust SDK 的 `check()` 方法，使其跳過已被 term-level match 覆蓋的 char-level matches，與 Python 行為一致。

## 背景

Python `converter.py` 的 `_find_char_matches()` 已加入 `covered_positions` 過濾（line 601）：term 匹配到的位置不再重複報告 char-level match。但三個 SDK 的 `check()` 仍然獨立報告所有 char-level matches，造成：

1. `golden-test.json`（由 Python 產生）與 SDK golden test 不一致
2. `check()` 報告的內容與 `fix()` 實際行為不符
3. 每個 SDK 自身的 `check()` 與 `lookup()` 行為不一致（lookup 已有過濾）

## 設計原則

- **check() 是 fix() 的預覽** — 報告的 match 應精確反映 fix() 會做的轉換
- **直接改，不做向後相容** — 現有行為是 bug，不是 feature
- **複用各 SDK 自己 lookup() 的 covered positions 模式** — 不引入新概念

## 變更清單

### Java (`sdk/java/src/main/java/com/rajatim/zhtw/ZhtwConverter.java`)

**現狀（lines 90-121）：** `check()` 先收集 term matches，再獨立遍歷所有 codepoints 收集 char matches。

**修改：**
1. 第一趟收集 term matches 時，同時記錄 covered UTF-16 positions（`Set<Integer>`），模式同 `lookup()` lines 142-155
2. 第二趟 char-level 迴圈中，檢查 `if (coveredUtf16.contains(i)) continue;`

### TypeScript (`sdk/typescript/src/core/converter.ts`)

**現狀（lines 90-117）：** `check()` 先收集 term matches，再遍歷所有 codepoints 收集 char matches。Line 105 註解：`// Char layer: walk codepoints regardless of term coverage (Java semantics).`

**修改：**
1. 第一趟收集 term matches 時，同時記錄 covered codepoint positions（`Set<number>`）
2. 第二趟 char-level 迴圈中，檢查 `if (covered.has(cp)) continue;`
3. 刪除 line 105 的 `(Java semantics)` 註解

### Rust (`sdk/rust/zhtw/src/converter.rs`)

**現狀（lines 173-210）：** `check()` 先收集 term matches，再遍歷所有 chars 收集 char matches。

**修改：**
1. 第一趟收集 term matches 時，同時記錄 covered byte positions（`HashSet<usize>`），模式同 `lookup()` lines 228-233
2. 第二趟 char-level 迴圈中，檢查 `if covered_bytes.contains(&byte_idx) { continue; }`

## 測試

- `sdk/data/golden-test.json` 已反映正確行為（Python re-export），不需修改
- 各 SDK 的 golden test runner 應從 fail → pass：
  - `sdk/java/src/test/java/com/rajatim/zhtw/GoldenTest.java`
  - `sdk/typescript/tests/golden.test.ts`
  - Rust integration tests
- 不需新增測試 — golden test 即驗證

## 不做的事

- 不改 Python（已正確）
- 不改 `lookup()` / `fix()`（已正確）
- 不加參數或新方法（直接改行為）
- 不升版（bug fix，下次版本一起帶）

## Commit message

```
fix: SDK check() 對齊 Python — 跳過 term-covered char matches

Java/TypeScript/Rust 的 check() 現在跳過已被 term match 覆蓋的
char-level matches，與 Python 行為及 golden-test.json 一致。
```
