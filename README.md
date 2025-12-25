# ZHTW

> 簡轉繁台灣用語轉換器 | Simplified to Traditional Chinese (Taiwan) Converter

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**rajatim 出品**

將程式碼和文件中的簡體中文轉換為台灣繁體中文用語。

## 特色

- **高效能** - Aho-Corasick 演算法，萬級術語秒級掃描
- **完全離線** - 不傳送任何資料到外部伺服器
- **可擴充詞庫** - JSON 格式，易於維護和貢獻
- **精準轉換** - 術語表優先，避免過度轉換
- **CI/CD 友善** - JSON 輸出，易於整合

## 安裝

```bash
pip install zhtw
```

或從原始碼安裝：

```bash
git clone https://github.com/rajatim/zhtw.git
cd zhtw
pip install -e .
```

## 快速開始

```bash
# 檢查模式（只報告，不修改）
zhtw check ./src

# 修正模式（自動修改檔案）
zhtw fix ./src

# JSON 輸出（CI/CD 整合）
zhtw check ./src --json

# 使用自訂詞庫
zhtw fix ./src --dict ./my-terms.json

# 排除目錄
zhtw check ./src --exclude node_modules,dist

# 只處理簡體
zhtw check ./src --source cn

# 只處理港式
zhtw check ./src --source hk

# 模擬執行（不實際修改）
zhtw fix ./src --dry-run
```

## 輸出範例

```
📁 掃描 ./src

📄 src/components/Header.tsx
   L12:5: "用户" → "使用者"
      ...顯示用户資訊...

📄 src/utils/api.ts
   L8:10: "网络" → "網路"
      ...檢查网络連線...

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  發現 2 處問題（2 個檔案）
   掃描: 150 個檔案 (跳過 45 個無中文檔案)
```

## 詞庫格式

```json
{
  "version": "1.0",
  "description": "自訂詞庫說明",
  "terms": {
    "文档": "文件",
    "代码": "程式碼",
    "软件": "軟體"
  }
}
```

## 內建詞庫

| 來源 | 類別 | 詞彙數 | 說明 |
|------|------|--------|------|
| CN | base | ~70 | 簡體基礎詞彙 |
| CN | it | ~55 | IT/程式術語 |
| CN | business | ~50 | 商業術語 |
| HK | base | ~50 | 港式基礎詞彙 |
| HK | tech | ~30 | 港式科技術語 |

## CI/CD 整合

### GitHub Actions

```yaml
- name: Check Traditional Chinese
  run: |
    pip install zhtw
    zhtw check ./src --json > result.json
    if [ $? -ne 0 ]; then
      echo "發現簡體中文用語，請修正"
      exit 1
    fi
```

### Jenkins

```groovy
stage('繁體中文檢查') {
    steps {
        sh 'pip install zhtw'
        sh 'zhtw check . --json > terminology-report.json'
    }
}
```

### JSON 輸出格式

```json
{
  "total_issues": 3,
  "files_with_issues": 2,
  "files_checked": 150,
  "files_modified": 0,
  "files_skipped": 45,
  "status": "fail",
  "issues": [
    {
      "file": "src/components/Header.tsx",
      "line": 12,
      "column": 5,
      "source": "用户",
      "target": "使用者"
    }
  ]
}
```

## 為什麼不用 OpenCC？

OpenCC 會過度轉換一些在台灣已經正確的詞彙：

| 原文 | OpenCC 結果 | 正確（台灣） |
|------|-------------|--------------|
| 權限 | 許可權 | 權限 |
| 設備 | 裝置 | 設備 |
| 視頻 | 視訊 | 影片 |

ZHTW 使用精確的術語表，只轉換明確定義的詞彙，避免這類問題。

## 開發

```bash
# 安裝開發依賴
pip install -e ".[dev]"

# 執行測試
pytest

# 執行 lint
ruff check .
```

## 路線圖

- [x] v1.0 - 基礎 CLI + 詞庫
- [ ] v1.5 - 分類詞庫 + 統計報告
- [ ] v2.0 - LLM 輔助詞彙探索
- [ ] v3.0 - 本地模型上下文感知

## License

MIT License

---

**rajatim 出品**
