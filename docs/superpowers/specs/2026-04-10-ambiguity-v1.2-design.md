<!-- zhtw:disable -->
# 歧義字擴充 v1.2 設計規格

**Date:** 2026-04-10
**Author:** rajatim + Claude (brainstorming session)
**Status:** Approved — ready for implementation plan

---

## Goal

將 15 個「假歧義字」從 `ambiguous_excluded` 升級到 `safe_chars`，使 strict mode 也能轉換它們。另外為 5 個真歧義字擴充 `balanced_defaults`。

## 核心洞察

119 個歧義字中，有一批被錯誤歸類：它們的替代繁體形式是死語、異體字、或極罕古字，不構成真正的語義歧義。這些字應該待在 safe_chars（字元層），而非 balanced_defaults（歧義層）。

**設計原則：** `strict = stable contract`、`balanced = evolving contract`。零風險的一對一字不該汙染 balanced 的語義。

---

## §1 · 路線 A：升級 safe_chars（15 字）

### 機制

修改 `scripts/generate_charmap.py` 的覆寫清單，然後重新跑生成腳本：

1. 從 `FORCE_EXCLUDE` 移除 3 字（Unihan 說一對一，人工錯誤標記為歧義）
2. 加入 `FORCE_INCLUDE` 12 字（Unihan 說一對多，但替代形是異體字/死語）

### 字表

#### FORCE_EXCLUDE → 移除（3 字）

| 簡 | → 繁 | 原排除理由 | 為什麼可以升級 |
|---|---|---|---|
| 仆 | 僕 | 仆(fall forward) vs 僕(servant) | 「前仆後繼」由詞庫 identity 保護；裸字幾乎只有「僕」義 |
| 尸 | 屍 | 尸(preside) vs 屍(corpse) | 「尸位素餐」是極古語，現代文本中裸字「尸」= 屍 |
| 帘 | 簾 | 帘(wine shop sign) vs 簾(curtain) | 酒帘是死語，現代裸字「帘」= 簾 |

#### Unihan 一對多 → FORCE_INCLUDE（12 字）

| 簡 | → 繁 | Unihan 替代形 | 為什麼可以覆寫 |
|---|---|---|---|
| 凫 | 鳧 | 鳬 | 鳬 是鳧的異體字 |
| 坝 | 壩 | 垻 | 垻 極罕 |
| 竖 | 豎 | 竪 | 竪 是豎的異體字 |
| 绣 | 繡 | 鏽 | 鏽=rust 是完全不同的字，不構成歧義 |
| 绷 | 繃 | — | 無真實替代 |
| 蕴 | 蘊 | 縕/緼 | 古字，現代不用 |
| 谣 | 謠 | 諑 | 諑 是極罕異體 |
| 赃 | 贓 | — | 無真實替代 |
| 酝 | 醞 | — | 無真實替代 |
| 锈 | 鏽 | 銹 | 銹 是鏽的異體，台灣標準用鏽 |
| 颓 | 頹 | 穨 | 穨 是頹的古字 |
| 鳄 | 鱷 | — | 無真實替代 |

### 效果

- `safe_chars` 從 6345 → **6360**（+15）
- `ambiguous_excluded` 從 119 → **104**（-15）
- strict mode 受益：這 15 字不需要 balanced mode 就能轉

### 驗證

```bash
# 重新生成 safe_chars.json
python scripts/generate_charmap.py --report

# 驗證映射數量
python -c "import json; d=json.load(open('src/zhtw/data/charmap/safe_chars.json')); print(len(d['chars']), len(d['ambiguous_excluded']))"
# 期望: 6360 104

# 跑測試
pytest
```

---

## §2 · 路線 B：擴充 balanced_defaults（5 字）

### 前提

路線 A 完成後再做。這 5 字有真實的替代繁體字，屬於真歧義，但主流義 >95%。

### 字表

| 簡 | 預設 | 替代 | 替代用法 | 詞庫保護 |
|---|---|---|---|---|
| 卤 | 滷 | 鹵 | 鹵素(halogen) | 需加 identity: 鹵素→鹵素 |
| 坛 | 壇 | 罈 | 酒罈/醬罈 | 需加詞條: 酒坛→酒罈 |
| 弥 | 彌 | 瀰 | 瀰漫 | 需加詞條: 弥漫→瀰漫 |
| 摆 | 擺 | 襬 | 下襬/衣襬 | 需加詞條: 下摆→下襬 |
| 纤 | 纖 | 縴 | 縴夫 | 已有詞條: 纤夫→縴夫 ✅ |

### 機制

1. 先補齊詞庫保護詞條（4 個新詞條）
2. 再加入 `balanced_defaults.json`（5 字）
3. `zhtw export` 重新產生 `zhtw-data.json`

### 效果

- `balanced_defaults` 從 3 → **8**（+5）
- 僅 balanced mode 受益

---

## §3 · 不做的事

- ❌ 不動複雜多義字（后/里/面/干/台/系/制/复…）— 這些需要 v2 語義消歧
- ❌ 不動罕用字（CJK ext）— 使用價值低、驗證成本高
- ❌ 不動 identity 字（了/出/千/秋/朱/累/致…）— 轉不轉都一樣
- ❌ 路線 B 不一次全吞 — 小批進，每次驗證

## §4 · 測試策略

| 測試 | 內容 |
|------|------|
| **路線 A 回歸** | 15 字在 strict mode 下正確轉換 |
| **路線 A 不變性** | 現有 729 個測試全通過 |
| **ambiguous_excluded 數量** | 斷言從 119 → 104 |
| **safe_chars 數量** | 斷言從 6345 → 6360 |
| **路線 B 正向** | 5 字在 balanced mode 轉換 |
| **路線 B 詞庫保護** | 弥漫→瀰漫、下摆→下襬 等不被 balanced 覆寫 |
| **路線 B strict 不變** | 5 字在 strict mode 不轉換 |

## §5 · 119 字完整分類（供後續參考）

| 分類 | 數量 | 處置 | 字 |
|------|------|------|---|
| v1 balanced_defaults | 3 | 維持 | 几丰杰 |
| → safe_chars (本次) | 15 | 路線 A | 仆凫坝尸帘竖绣绷蕴谣赃酝锈颓鳄 |
| → balanced_defaults (本次) | 5 | 路線 B | 卤坛弥摆纤 |
| 已被嚴格模式覆蓋 | 15 | 不需處理 | 众伪启团奖并汇锐闲阅颜鸡钩钵咸 |
| Identity（繁簡同形） | ~18 | 不需處理 | 了出千秋朱累致御卜蒙栗回向同合困借冬曲 |
| 複雜多義 | ~20 | v2 語義消歧 | 后里面干台系制复采表冲准征只卷斗别划丑余折才志朴松胡舍谷辟注克么家奸 |
| 罕用字 | ~20 | 未來低優先 | 䴘妫悫沩瘘硷谫赍赝辒鲞鳁鿭𩙧𫇭𮲸𮷷𰷭镋镌莼绦绱缊 |
