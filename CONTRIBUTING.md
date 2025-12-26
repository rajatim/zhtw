# Contributing to ZHTW

感謝你有興趣貢獻！

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
    "新词": "新詞"
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

## 回報問題

開 [Issue](https://github.com/rajatim/zhtw/issues)，請附上：

- 輸入文字
- 預期結果
- 實際結果

## 行為準則

- 保持友善
- 專注於技術討論
