# CLI 指令設計

## 指令總覽

```bash
zhtw db scan      # 自動探索文字欄位
zhtw db check     # 檢查需轉換內容
zhtw db fix       # 執行轉換
zhtw db rollback  # 回滾轉換
zhtw db jobs      # 列出工作
zhtw db resume    # 恢復中斷工作
zhtw db diff      # 比較兩資料庫
zhtw db clone     # Clone 輔助（策略 F）
```

---

## 連線方式

### 環境變數（推薦）

```bash
export DATABASE_URL="postgres://user:pass@localhost:5432/mydb"
zhtw db check
zhtw db fix --table users
```

### URL 參數

```bash
zhtw db check "postgres://user:pass@localhost:5432/mydb"
zhtw db check "mysql://user:pass@localhost:3306/mydb"
zhtw db check "mongodb://localhost:27017/mydb"
zhtw db check "sqlite:///path/to/app.db"
```

---

## zhtw db scan

自動探索資料庫中的文字欄位。

```bash
zhtw db scan [DATABASE_URL] [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--table, -t` | 指定表格（可多次）| 全部 |
| `--exclude, -e` | 排除表格（可多次）| - |
| `--sample` | 取樣筆數（用於偵測中文）| 1000 |
| `--json` | JSON 輸出 | false |
| `--verbose, -v` | 詳細輸出 | false |

### 範例

```bash
# 掃描整個資料庫
zhtw db scan postgres://localhost/mydb

# 只掃描特定表格
zhtw db scan --table users --table articles

# 排除系統表
zhtw db scan --exclude django_migrations --exclude auth_user

# JSON 輸出（給程式使用）
zhtw db scan --json
```

### 輸出範例

```
📋 發現以下文字欄位：

users
├── name (VARCHAR) - 1,234 筆含中文
├── bio (TEXT) - 567 筆含中文
└── settings (JSONB) - 89 筆含中文

articles
├── title (VARCHAR) - 2,345 筆含中文
└── content (TEXT) - 8,901 筆含中文

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 共 2 個表、5 個欄位、13,136 筆含中文
```

---

## zhtw db check

檢查資料庫中需轉換的內容。

```bash
zhtw db check [DATABASE_URL] [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--table, -t` | 指定表格 | 全部 |
| `--column, -c` | 指定欄位 | 全部文字欄位 |
| `--json` | JSON 輸出 | false |
| `--verbose, -v` | 詳細輸出 | false |

### 範例

```bash
# 檢查整個資料庫
zhtw db check

# 檢查特定表格和欄位
zhtw db check --table users --column name,bio

# JSON 輸出（CI/CD 用）
zhtw db check --json
```

### 輸出範例

```
📋 users.name
   共 1,234 筆，需轉換 56 筆
   "用户" → "使用者" (45 筆)
   "软件" → "軟體" (11 筆)

📋 users.bio
   共 567 筆，需轉換 23 筆
   "程序" → "程式" (15 筆)
   "网络" → "網路" (8 筆)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️  共 79 處需轉換（2 個欄位）
```

---

## zhtw db fix

執行資料庫轉換。

```bash
zhtw db fix [DATABASE_URL] [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--table, -t` | 指定表格 | 全部 |
| `--column, -c` | 指定欄位 | 全部文字欄位 |
| `--strategy` | 輸出策略 | shadow |
| `--batch-size` | 批次大小 | 1000 |
| `--dry-run` | 預覽模式 | false |
| `--force` | 強制執行（危險操作）| false |
| `--yes, -y` | 跳過確認 | false |
| `--verbose, -v` | 詳細輸出 | false |

### 策略選項

| 策略 | 說明 |
|------|------|
| `shadow` | 反向影子（推薦）：備份原表，轉換後保持原表名 |
| `inplace` | 原地更新：直接修改，無法回滾（需 --force）|
| `newdb` | 新資料庫：輸出到新資料庫/檔案 |
| `audit` | 審計模式：記錄所有變更到審計表 |

### 範例

```bash
# 預設策略（反向影子）
zhtw db fix --table users

# 原地更新（需 --force）
zhtw db fix --table users --strategy inplace --force

# 預覽模式
zhtw db fix --table users --dry-run

# 無互動模式（CI/CD）
zhtw db fix --table users --yes

# 調整批次大小
zhtw db fix --table users --batch-size 5000
```

### 互動流程

```
$ zhtw db fix --table users

🔍 分析中...

📋 users 表
   總筆數: 50,000
   需轉換: 1,234 筆
   預估時間: ~30 秒

🎯 請選擇策略:

  [1] 🔄 反向影子（推薦）
      • 原表名稱保留，程式不用改
      • 備份到 users_backup_*
      • 可隨時回滾

  [2] ⚡ 原地更新
      • 最快，但無法回滾
      • ⚠️ 建議先手動備份

  [3] 📁 新資料庫
      • 最安全
      • 需要切換連線字串

選擇 [1/2/3]: 1

確定執行轉換？ [y/N]: y

[████████████████████████████████] 100% (1,234/1,234)

✅ 轉換完成！
   users: 1,234 處修正

📦 備份位置: users_backup_20250101_120000
💡 回滾指令: zhtw db rollback --job-id abc123
```

---

## zhtw db rollback

回滾轉換。

```bash
zhtw db rollback [DATABASE_URL] [OPTIONS]
```

### 選項

| 選項 | 說明 |
|------|------|
| `--table, -t` | 指定表格（回滾最近的該表轉換）|
| `--job-id, -j` | 指定工作 ID |
| `--yes, -y` | 跳過確認 |

### 範例

```bash
# 使用工作 ID 回滾
zhtw db rollback --job-id abc123

# 回滾特定表格的最近轉換
zhtw db rollback --table users

# 無互動
zhtw db rollback --job-id abc123 --yes
```

---

## zhtw db jobs

列出所有轉換工作。

```bash
zhtw db jobs [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--status` | 過濾狀態 | all |
| `--json` | JSON 輸出 | false |

### 範例

```bash
# 列出所有工作
zhtw db jobs

# 只看失敗的
zhtw db jobs --status failed

# 只看進行中的
zhtw db jobs --status running
```

### 輸出範例

```
ID       表格    狀態       進度          時間
─────────────────────────────────────────────────────
abc123   users   completed  1234/1234    2025-01-01 12:00
def456   posts   failed     500/2000     2025-01-01 11:30
ghi789   orders  paused     1000/5000    2025-01-01 11:00
```

---

## zhtw db resume

恢復中斷的工作。

```bash
zhtw db resume <JOB_ID>
```

### 範例

```bash
zhtw db resume ghi789
```

---

## zhtw db diff

比較兩個資料庫的差異。

```bash
zhtw db diff <SOURCE_URL> <TARGET_URL> [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--table, -t` | 只比較指定表格 | 全部 |
| `--sample` | 每表取樣筆數 | 100 |

### 範例

```bash
# 比較兩個資料庫
zhtw db diff postgres://old postgres://new

# 只比較特定表格
zhtw db diff sqlite:///old.db sqlite:///new.db --table users

# 增加取樣數
zhtw db diff ... --sample 1000
```

---

## zhtw db clone

Clone 資料庫輔助指令（策略 F 使用）。

```bash
zhtw db clone <SOURCE_URL> <TARGET_URL> [OPTIONS]
```

### 選項

| 選項 | 說明 | 預設 |
|------|------|------|
| `--method` | Clone 方式 | auto |
| `--parallel` | 平行度 | 4 |
| `--exclude-table` | 排除表格 | - |

### 範例

```bash
# 自動選擇 Clone 方式
zhtw db clone postgres://source postgres://target

# 指定邏輯複製
zhtw db clone postgres://source postgres://target --method logical

# 排除審計表
zhtw db clone ... --exclude-table audit_logs
```

---

## 環境變數

| 變數 | 說明 |
|------|------|
| `DATABASE_URL` | 資料庫連線字串 |
| `ZHTW_YES` | 設為 1 跳過確認 |
| `ZHTW_DB_BATCH_SIZE` | 預設批次大小 |

---

## 退出碼

| 碼 | 說明 |
|----|------|
| 0 | 成功 |
| 1 | 一般錯誤 |
| 2 | 連線錯誤 |
| 3 | 權限錯誤 |
| 4 | 使用者取消 |

---

*CLI 設計 v1.0 - 2025-12-31*
