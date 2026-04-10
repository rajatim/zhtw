<!-- zhtw:disable -->
# 歧義字擴充 v1.3 設計規格

**Date:** 2026-04-10
**Status:** Ready for implementation

---

## Goal

將 5 個字從 `ambiguous_excluded` 升級到 `safe_chars`。其中 2 字需要先補詞庫 identity 保護，3 字可直接升級。

## 前置背景

- v1.2 已完成：13 字升級 safe_chars + 5 字擴充 balanced_defaults
- 當前狀態：safe_chars=6356，ambiguous_excluded=106，balanced_defaults=8
- 本次目標：safe_chars +5，ambiguous_excluded -5

---

## 變更清單

### Step 1：補詞庫 identity 保護（2 個詞條）

在 `src/zhtw/data/terms/cn/chars.json` 的 `terms` 中新增：

```json
"前仆后继": "前仆後繼",
"尸位素餐": "尸位素餐"
```

**理由：**
- `仆` 升級為 safe_chars 後，strict mode 會把所有裸字「仆」轉成「僕」
- `前仆后继` 的「仆」是「仆倒」義（不是「僕人」），繁體應保留為「仆」
- 加入 identity mapping `前仆后继→前仆後繼` 讓詞庫層保護這個成語
- `尸位素餐` 的「尸」是「尸位」義（佔著位置不做事），繁體也保留為「尸」
- 加入 identity mapping `尸位素餐→尸位素餐` 讓詞庫層保護

**注意：** 先加詞條，跑 `pytest` 確認無衝突，再做 Step 2。

### Step 2：修改 generate_charmap.py

#### 從 FORCE_EXCLUDE 移除 2 字

```python
# 移除這兩行：
"仆",  # 僕(servant) vs 仆(fall forward)
"尸",  # 屍(corpse) vs 尸(preside over)
```

#### 在 FORCE_INCLUDE 新增 5 字

```python
"仆": "僕",  # 仆倒(前仆後繼) 由詞庫 identity 保護
"尸": "屍",  # 尸位素餐 由詞庫 identity 保護
"赝": "贗",  # 贗品(counterfeit)，無真實替代
"镋": "鎲",  # 罕用兵器字，無真實替代
"镌": "鐫",  # 鐫刻(engrave)，無真實替代
```

### Step 3：重新生成 safe_chars.json

**不要手動改 safe_chars.json。** 執行：

```bash
python scripts/generate_charmap.py
```

這會從 Unihan 下載最新資料並套用 FORCE_EXCLUDE / FORCE_INCLUDE 覆寫，自動產出正確的 safe_chars.json。

生成後驗證：
- `safe_chars` 數量應比當前 +5
- `ambiguous_excluded` 數量應比當前 -5
- `仆尸赝镋镌` 都在 `chars` 中，不在 `ambiguous_excluded` 中
- stats metadata 與實際內容一致

### Step 4：重新 export

```bash
.venv/bin/python -m zhtw export
cp sdk/data/zhtw-data.json sdk/rust/zhtw/data/zhtw-data.json
```

### Step 5：更新測試

#### tests/test_charconv.py

- `test_v12_promoted_safe_chars`：擴充或新增測試，涵蓋 v1.3 的 5 字（仆→僕、尸→屍、赝→贗、镋→鎲、镌→鐫）
- `test_v12_true_ambiguous_chars_remain_excluded`：從檢查清單中移除 `仆`、`尸`（它們不再是 ambiguous）

#### tests/test_ambiguous_chars.py

- `test_v12_promotions_and_deferred_chars`：把 `仆`、`尸` 從 `still_ambiguous` 移到 `promoted_to_safe`

#### tests/test_ambiguous_balanced.py

- `test_bare_ambiguous_unchanged_in_strict`：從清單移除 `仆`、`尸`（它們現在在 strict 會被轉換）

#### 新增測試

在 `tests/test_charconv.py` 或適當位置新增：

```python
def test_v13_identity_protection():
    """v1.3 詞庫 identity 保護成語不被字元層覆寫。"""
    # 前仆后继 的 仆 應保留（仆倒義），不應轉成 僕
    assert convert("前仆后继", ambiguity_mode="strict") == "前仆後繼"
    # 尸位素餐 的 尸 應保留（尸位義），不應轉成 屍
    assert convert("尸位素餐", ambiguity_mode="strict") == "尸位素餐"

def test_v13_bare_chars_convert_in_strict():
    """v1.3 升級的字在 strict mode 裸字應被轉換。"""
    from zhtw.charconv import char_convert, get_translate_table
    table = get_translate_table()
    assert char_convert("仆", table) == "僕"
    assert char_convert("尸", table) == "屍"
    assert char_convert("赝", table) == "贗"
    assert char_convert("镋", table) == "鎲"
    assert char_convert("镌", table) == "鐫"
```

### Step 6：驗證

```bash
# 全部測試通過
pytest

# version check
make version-check
```

---

## 不做的事

- 不動 balanced_defaults（本次純 safe_chars 升級）
- 不動複雜多義字
- 不動罕用古字（除了 赝/镋/镌 這 3 個有明確一對一映射的）
- 不改版本號（資料修正，不是功能變更）

## Commit message

```
feat: 歧義字擴充 v1.3 — 5 字升級 safe_chars（仆尸赝镋镌）

- 新增詞庫 identity 保護：前仆后继→前仆後繼、尸位素餐→尸位素餐
- FORCE_EXCLUDE 移除 仆、尸
- FORCE_INCLUDE 新增 仆→僕、尸→屍、赝→贗、镋→鎲、镌→鐫
- 重新生成 safe_chars.json（+5 safe，-5 ambiguous）
```
