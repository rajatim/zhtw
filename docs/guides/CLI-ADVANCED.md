# CLI 進階用法

> 完整的 `zhtw` CLI 引數、詞彙查詢、多編碼支援、忽略規則、自訂詞庫格式。

## 完整引數

```bash
# 單檔案模式（v2.8.0+）
zhtw check ./src/api.py    # 檢查單一檔案
zhtw fix ./src/api.py      # 修正單一檔案

# 使用自訂詞庫
zhtw fix ./src --dict ./my-terms.json

# 只處理簡體（跳過港式）  # zhtw:disable-line
zhtw check ./src --source cn

# 排除目錄
zhtw check ./src --exclude node_modules,dist

# 模擬執行（不實際修改）
zhtw fix ./src --dry-run

# 預覽修改（確認後才執行）
zhtw fix ./src --show-diff

# 備份後修改
zhtw fix ./src --backup

# 顯示詞庫統計
zhtw stats

# 驗證詞庫品質（檢查衝突和無效轉換）
zhtw validate

# 詳細輸出
zhtw check ./src --verbose
```

## 詞彙查詢 (v3.3.0+)

<!-- zhtw:disable -->
不確定某個詞會不會被轉？用 `lookup` 直接查：

```bash
# 查詢單詞
zhtw lookup 软件 服务器 数据库

# 查詢整句（自動拆解每個轉換點）
zhtw lookup "这个软件需要网络服务器"

# 詳細模式（顯示每個轉換由哪一層負責）
zhtw lookup -v 营养

# JSON 輸出（供程式使用）
zhtw lookup --json 结合

# stdin 管線
echo "心态" | zhtw lookup
```

**輸出範例：**
```
软件 → 軟體  (詞彙層: 软件→軟體)
服务器 → 伺服器  (詞彙層: 服务器→伺服器)
数据库 → 資料庫  (詞彙層: 数据库→資料庫)
```
<!-- zhtw:enable -->

## 多編碼支援 (v2.5.0+)

自動偵測並處理 Big5、GBK 等舊編碼檔案：

```bash
# 自動偵測編碼（預設）
zhtw fix ./legacy-code/

# 強制輸出為 UTF-8
zhtw fix ./big5-files/ --output-encoding utf-8

# 保留原編碼
zhtw fix ./mixed/ --output-encoding keep

# CI/CD 模式（無互動確認）
zhtw fix ./src/ --yes
# 或用環境變數
ZHTW_YES=1 zhtw fix ./src/
```

**支援編碼**：UTF-8 (含 BOM)、Big5、GBK、GB2312、GB18030

## .zhtwignore 忽略檔案

在專案根目錄建立 `.zhtwignore` 檔案，排除不需檢查的目錄或檔案：

```gitignore
# 測試目錄
tests/

# 詞庫檔案（本來就是簡體）
src/data/terms/

# 特定檔案
legacy-code.py
```

支援目錄模式（結尾 `/`）和檔案 glob 模式。

## 自訂詞庫格式

<!-- zhtw:disable -->
```json
{
  "version": "1.0",
  "description": "我的專案術語",
  "terms": {
    "自定义": "自訂"
  }
}
```
<!-- zhtw:enable -->

載入方式：

```bash
zhtw fix ./src --dict ./my-terms.json
```

自訂詞庫會覆蓋同名的內建詞條。

<!-- zhtw:disable -->
## 相關文件

- [README](../README.md) — 專案總覽、Quick Start、忽略特定程式碼 pragma
- [詞庫涵蓋範圍](DICTIONARY-COVERAGE.md) — 31,000+ 詞條分類、雙層架構細節
- [CI/CD 整合](CI-CD-INTEGRATION.md) — GitHub Actions / GitLab CI / pre-commit 完整設定
<!-- zhtw:enable -->
