# Contributing to ZHTW

感謝你有興趣貢獻！

## 黃金規則

```
1. 寧可少轉，不要錯轉
2. 不用 OpenCC（會過度轉換）
3. 詞庫修改要謹慎（確認臺灣不用該詞）
4. 修改後跑 pytest
5. 子字串加 identity mapping
```

## 新增詞彙

這是最常見的貢獻方式。

### 1. 找到對應的詞庫檔案

```
src/zhtw/data/terms/
├── cn/          # 簡體 → 台灣繁體
│   ├── base.json
│   ├── it.json
│   └── business.json
└── hk/          # 港式 → 台灣繁體
    ├── base.json
    └── tech.json
```

### 2. 新增詞彙

```json
{
  "terms": {
    "新詞": "新詞"
  }
}
```

### 3. 確認轉換正確

> 寧可少轉，不要錯轉

- 確認這個詞在台灣用語中**確實需要轉換**
- 如果不確定，先開 Issue 討論

### 4. 提交 PR

```bash
git checkout -b add-term-xxx
git add .
git commit -m "feat: 新增詞彙 xxx"
git push origin add-term-xxx
```

## 開發

```bash
# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest

# 執行 lint
ruff check .
```

## 提供真實簡體中文用例

我們正在為 Blind-v2 公開 benchmark 收集具明確授權的真實簡體中文 input。請使用
[專用 issue form](https://github.com/rajatim/zhtw/issues/new?template=permissioned-user-report.yml)
每次提供 1 至 10 個由你原創或有權提供的完整句子；目前進度與完成條件記錄在
[issue #47](https://github.com/rajatim/zhtw/issues/47)。

請勿提供繁體 expected、轉換器輸出、個資、客戶資料、憑證或未公開內容。提交前必須
閱讀並接受
[Permissioned User Report Consent v1](docs/benchmark/PERMISSIONED-USER-REPORT-CONSENT.md)。

## 回報問題

開 [Issue](https://github.com/rajatim/zhtw/issues)，請附上：

- 輸入文字
- 預期結果
- 實際結果

## 行為準則

- 保持友善
- 專注於技術討論

## AI 輔助開發

本專案支援 [Claude Code](https://claude.ai/claude-code)。專案根目錄的 `CLAUDE.md` 包含開發指南，可以幫助 AI 更好地協助你貢獻。
