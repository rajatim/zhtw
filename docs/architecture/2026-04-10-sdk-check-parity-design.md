<!-- zhtw:disable -->
# SDK term-covered parity — convert/check/lookup 全面對齊 Python

**Date:** 2026-04-10
**Updated:** 2026-04-11 (scope expanded after Codex review)
**Status:** Ready for implementation

---

## Goal

修正 Java/TypeScript/Rust SDK 的 `convert()` / `check()` / `lookup()`，使 identity term 保護的位置不被 char layer 覆寫，與 Python 行為一致。

## 背景

### 問題 1：check() 不過濾 term-covered char matches

Python `converter.py` 的 `_find_char_matches()` 已加入 `covered_positions` 過濾（line 601）：term 匹配到的位置不再重複報告 char-level match。但三個 SDK 的 `check()` 仍然獨立報告所有 char-level matches，造成：

1. `golden-test.json`（由 Python 產生）與 SDK golden test 不一致（Java 目前 6 個 failure）
2. `check()` 報告的內容與 `convert()` 實際行為不符

### 問題 2：identity terms 不保護 convert()/lookup() 的 char layer

Python `matcher.get_covered_positions()` 用 `automaton.iter()` 收集**所有**命中位置，**含 identity terms**（source == target）。但三個 SDK：

- `findMatches()` / `find_term_matches()` 濾掉 identity terms 後才回傳
- `convert()` 用 `applyCharmap(replaceAll(text))`，char layer 跑在整段文字上，不做 covered 檢查
- `lookup()` 的 covered set 來自 `findMatches()` 結果，同樣不含 identity terms

這導致 9 組 identity terms（含有 `safe_chars` 裡的字元）在 SDK 會被 char layer 錯誤轉換：

| Identity term | SDK 錯誤輸出 | Python 正確輸出 | 被錯轉的字 |
|---|---|---|---|
| 尸位素餐 | 屍位素餐 | 尸位素餐 | 尸→屍 |
| 人云亦云 | 人雲亦雲 | 人云亦云 | 云→雲 ×2 |
| 急症 | 急癥 | 急症 | 症→癥 |
| 炎症 | 炎癥 | 炎症 | 症→癥 |
| 病症 | 病癥 | 病症 | 症→癥 |
| 癌症 | 癌癥 | 癌症 | 症→癥 |
| 于正升 | 於正升 | 于正升 | 于→於 |
| 周旋 | 周鏇 | 周旋 | 旋→鏇 |
| 党太尉吃匾食 | 黨太尉吃匾食 | 党太尉吃匾食 | 党→黨 |

## 設計原則

- **check() 是 convert() 的預覽** — 報告的 match 應精確反映 convert() 會做的轉換
- **直接改，不做向後相容** — 現有行為是 bug，不是 feature
- **每個 SDK 新增 `getCoveredPositions()` helper** — 走 raw automaton hits（含 identity），不沿用 `findMatches()` 結果
- **convert() 改為 covered-aware char layer** — 不能再用 `applyCharmap(replaceAll(text))` 的全量模式

## Python 參考實作

### `matcher.get_covered_positions()` (matcher.py:135-144)

```python
def get_covered_positions(self, text: str) -> set[int]:
    """Return source positions covered by any term hit, including identity terms."""
    covered: set[int] = set()
    for end_pos, (source, _target) in self.automaton.iter(text):
        start_pos = end_pos - len(source) + 1
        covered.update(range(start_pos, end_pos + 1))
    return covered
```

關鍵：用 `automaton.iter()`（raw hits），不是 `find_matches()`（filtered hits）。

### convert (fix=True) 流程 (converter.py:372-412)

```python
covered = matcher.get_covered_positions(text)   # 含 identity
matches = list(matcher.find_matches(text))       # 不含 identity
# 對每個 gap（matches 之間的文字），用 covered 決定是否跑 char layer
```

### check (fix=False) 流程 (converter.py:455-464)

```python
covered_positions = matcher.get_covered_positions(text)  # 含 identity
char_matches = _find_char_matches(text, char_table, ..., covered_positions=covered_positions)
# _find_char_matches 跳過 covered 位置
```

## 變更清單

### 1. 每個 SDK Matcher 新增 `getCoveredPositions()`

此方法遍歷 raw automaton hits（含 identity terms），收集所有命中位置。不做最長匹配或 overlap 過濾 — 所有 overlapping hits 的範圍都算 covered。這和 Python `automaton.iter()` 的行為一致。

#### Java (`sdk/java/src/main/java/com/rajatim/zhtw/AhoCorasickMatcher.java`)

新增方法：

```java
Set<Integer> getCoveredPositions(String text) {
    if (trie == null || text == null || text.isEmpty()) {
        return Collections.emptySet();
    }
    Set<Integer> covered = new HashSet<>();
    for (Emit emit : trie.parseText(text)) {
        for (int i = emit.getStart(); i <= emit.getEnd(); i++) {
            covered.add(i);
        }
    }
    return covered;
}
```

注意：`Emit.getEnd()` 是 inclusive，所以用 `<=`。

#### TypeScript (`sdk/typescript/src/core/matcher.ts`)

新增方法：

```typescript
getCoveredPositions(text: string): Set<number> {
    const covered = new Set<number>();
    for (const m of this.iterEmissions(text)) {
        for (let i = m.start; i < m.end; i++) {
            covered.add(i);
        }
    }
    return covered;
}
```

`iterEmissions()` 已經是 raw hits（含 identity），直接沿用。

#### Rust (`sdk/rust/zhtw/src/matcher.rs`)

新增 public function：

```rust
pub fn get_covered_positions(
    pma: &DoubleArrayAhoCorasick<u32>,
    pattern_table: &[(String, String)],
    text: &str,
) -> HashSet<usize> {
    let mut covered = HashSet::new();
    for m in pma.find_overlapping_iter(text) {
        let idx = m.value() as usize;
        let (ref src, _) = pattern_table[idx];
        for b in m.start()..m.end() {
            covered.insert(b);
        }
    }
    covered
}
```

### 2. 修改 `convert()`

現狀：`replaceAll(text)` → `applyCharmap(result)` — char layer 跑全部。

改為：先取 covered positions，term replace 後只對 uncovered 位置跑 char layer。

#### Java (`ZhtwConverter.java` lines 63-80)

```java
public String convert(String text) {
    if (text == null) return null;
    if (text.isEmpty()) return text;

    // Build covered positions from raw automaton hits (includes identity terms)
    Set<Integer> covered = matcher.getCoveredPositions(text);

    // Stage 1: Term-level replacement
    String result = matcher.replaceAll(text);

    // Stage 2: Char-level conversion, skipping covered positions
    if (charLayerEnabled) {
        result = applyCharmapWithCoverage(result, covered);
    }
    return result;
}
```

新增 `applyCharmapWithCoverage(String text, Set<Integer> covered)` — 與 `applyCharmap` 相同，但 skip covered UTF-16 positions。

注意：covered positions 是對原始 text 的，但 term replacement 可能改變字串長度。需要用 replaceAll 回傳的 position mapping，或改為 Python 模式（先 covered → 逐段處理）。**建議採用 Python 的 gap 模式**：

```java
public String convert(String text) {
    if (text == null) return null;
    if (text.isEmpty()) return text;

    Set<Integer> covered = matcher.getCoveredPositions(text);
    List<Match> matches = matcher.findMatches(text);

    if (matches.isEmpty()) {
        return charLayerEnabled ? applyCharmapSkipping(text, covered) : text;
    }

    StringBuilder sb = new StringBuilder();
    int lastEnd = 0;
    for (Match m : matches) {
        // Gap: apply char layer only on uncovered positions
        String gap = text.substring(lastEnd, m.getStart());
        sb.append(charLayerEnabled ? applyCharmapSkipping(gap, covered, lastEnd) : gap);
        // Term match: use target directly
        sb.append(m.getTarget());
        lastEnd = m.getEnd();
    }
    // Trailing gap
    String tail = text.substring(lastEnd);
    sb.append(charLayerEnabled ? applyCharmapSkipping(tail, covered, lastEnd) : tail);
    return sb.toString();
}

private String applyCharmapSkipping(String segment, Set<Integer> covered, int offset) {
    // For each char in segment, skip if (offset + i) is in covered
    ...
}
```

#### TypeScript (`converter.ts` lines 60-85)

同樣改為 gap 模式。參照 Java 的 pattern。

#### Rust (`converter.rs` lines 156-170)

同樣改為 gap 模式。用 `get_covered_positions()` + `find_term_matches()` 建構輸出。

### 3. 修改 `check()`

現狀：先收集 term matches，再獨立遍歷所有 codepoints 收集 char matches。

改為：用 `getCoveredPositions()` 過濾 char matches。

#### Java (`ZhtwConverter.java` lines 90-121)

```java
public List<Match> check(String text) {
    ...
    List<Match> result = new ArrayList<>();
    Set<Integer> coveredUtf16 = matcher.getCoveredPositions(text);

    // Term-level matches
    for (Match m : matcher.findMatches(text)) {
        int cpStart = Character.codePointCount(text, 0, m.getStart());
        int cpEnd = Character.codePointCount(text, 0, m.getEnd());
        result.add(new Match(cpStart, cpEnd, m.getSource(), m.getTarget()));
    }

    // Char-level matches: skip covered positions
    if (charLayerEnabled) {
        int cpIndex = 0;
        int i = 0;
        while (i < text.length()) {
            int cp = text.codePointAt(i);
            if (!coveredUtf16.contains(i)) {         // ← 新增
                String replacement = charmap.get(cp);
                String original = new String(Character.toChars(cp));
                if (replacement != null && !replacement.equals(original)) {
                    result.add(new Match(cpIndex, cpIndex + 1, original, replacement));
                }
            }                                          // ← 新增
            cpIndex++;
            i += Character.charCount(cp);
        }
    }
    return result;
}
```

#### TypeScript (`converter.ts` lines 90-117)

同樣加 covered check。刪除 line 105 的 `(Java semantics)` 註解。

#### Rust (`converter.rs` lines 173-210)

同樣加 covered_bytes check。

### 4. 修改 `lookup()`

現狀：covered set 來自 `findMatches()` 結果（不含 identity）。

改為：用 `getCoveredPositions()` 取代手動從 matches 建 covered set。

#### Java (`ZhtwConverter.java` lines 140-156)

```java
// Before:
Set<Integer> coveredUtf16 = new HashSet<>();
List<Match> termMatches = matcher.findMatches(word);
for (Match m : termMatches) {
    for (int i = m.getStart(); i < m.getEnd(); i++) {
        coveredUtf16.add(i);
    }
}

// After:
Set<Integer> coveredUtf16 = matcher.getCoveredPositions(word);
List<Match> termMatches = matcher.findMatches(word);
// (不再手動從 termMatches 建 covered set)
```

TypeScript 和 Rust 同理。

## 測試

### Golden test 補強

在 `src/zhtw/export.py` 的 golden cases 中新增 identity-protected cases：

**convert cases：**
```python
("尸位素餐", "尸位素餐"),      # identity term 保護 尸 不被轉為 屍
("人云亦云", "人云亦云"),      # identity term 保護 云 不被轉為 雲
("急症很严重", "急症很嚴重"),   # identity term 保護 症 不被轉為 癥 + char layer 轉 严→嚴 重→重
```

**check cases：**
```python
("尸位素餐", []),              # identity term: 不報告任何 match
("人云亦云", []),              # identity term: 不報告任何 match
```

**lookup cases：**
```python
("急症", {"output": "急症", "changed": false, "details": []}),
```

重新 `zhtw export` 後，golden-test.json 會包含這些 cases，各 SDK 的 golden test runner 從 fail → pass。

### 現有 golden test

`sdk/data/golden-test.json` 已反映 Python 的 check() filtered 行為。修完 check() 後，目前的 6 個 Java golden test failure 會從 fail → pass。

## 不做的事

- 不改 Python（已正確）
- 不加參數或新方法（直接改行為）
- 不升版（bug fix，下次版本一起帶）

## Commit message

```
fix: SDK convert/check/lookup 對齊 Python — identity term 保護 + covered positions

Java/TypeScript/Rust 的三個方法現在都使用 getCoveredPositions()
（含 identity terms）來決定 char layer 的作用範圍，與 Python 行為
及 golden-test.json 一致。

- 新增 getCoveredPositions(): 走 raw automaton hits 含 identity
- convert(): 改為 gap 模式，uncovered 位置才跑 char layer
- check(): 跳過 covered 位置的 char matches
- lookup(): covered set 改用 getCoveredPositions()
- golden-test.json: 補 identity-protected cases（尸位素餐、人云亦云、急症）
```
