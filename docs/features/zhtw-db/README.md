# zhtw-db 資料庫轉換支援

> **狀態**: 📐 架構設計完成，待實作

將 zhtw 的簡繁轉換功能擴充套件到資料庫，支援掃描和轉換資料庫中的中文內容。

---

## 快速開始

```bash
# 安裝
pip install zhtw-db
# 或指定資料庫驅動
pip install zhtw-db[postgres]
pip install zhtw-db[mysql]
pip install zhtw-db[mongodb]

# 使用
export DATABASE_URL="postgres://user:pass@localhost/mydb"
zhtw db scan                    # 自動探索文字欄位
zhtw db check --table users     # 檢查需轉換內容
zhtw db fix --table users       # 執行轉換
```

---

## 檔案索引

| 檔案 | 說明 |
|------|------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | 專案架構設計 |
| [STRATEGIES.md](./STRATEGIES.md) | 轉換策略指南（A-F 策略詳解）|
| [ROADMAP.md](./ROADMAP.md) | 產品路線圖 |
| [CLI.md](./CLI.md) | CLI 指令設計 |
| [JENKINS.md](./JENKINS.md) | Jenkins CI/CD 需求規格 |
| [databases/](./databases/) | 資料庫專屬指南 |

---

## 支援的資料庫

| 資料庫 | 驅動 | 狀態 | 版本 |
|--------|------|------|------|
| SQLite | 內建 sqlite3 | 📋 v3.0 | - |
| PostgreSQL | psycopg2/psycopg3 | 📋 v3.1 | 12-16 |
| MySQL/MariaDB | mysqlclient/PyMySQL | 📋 v3.2 | 5.7-8.0 |
| MongoDB | pymongo | 📋 v3.3 | 5.0-7.0 |
| SQL Server | - | 📋 v3.4 | - |
| Oracle | - | 📋 v3.5 | - |

---

## 核心功能

### 1. 自動探索 (scan)

```bash
zhtw db scan postgres://localhost/mydb

# 輸出
📋 發現以下文字欄位：
   users.name (VARCHAR) - 1,234 筆含中文
   users.bio (TEXT) - 567 筆含中文
   articles.title (VARCHAR) - 2,345 筆含中文
```

### 2. 檢查 (check)

```bash
zhtw db check --table users --column name

# 輸出
📋 users.name
   共 1,234 筆，需轉換 56 筆
   "使用者" → "使用者" (45 筆)
   "軟體" → "軟體" (11 筆)
```

### 3. 轉換 (fix)

```bash
# 預設策略：反向影子（安全）
zhtw db fix --table users

# 選擇策略
zhtw db fix --table users --strategy shadow    # 反向影子
zhtw db fix --table users --strategy inplace   # 原地更新
zhtw db fix --table users --strategy audit     # 審計模式
```

### 4. 回滾 (rollback)

```bash
zhtw db rollback --job-id abc123
zhtw db rollback --table users
```

---

## 設計原則

1. **使用者零改動** — 轉換後程式碼不需修改，保持原表名稱
2. **可回滾** — 預設策略支援完整回滾
3. **斷點續傳** — 大表轉換中斷可恢復
4. **多策略** — 根據場景選擇最適合的策略

---

## 相關 Issue

- [#10 - feat: 資料庫內容轉換支援](https://github.com/rajatim/zhtw/issues/10)

---

*zhtw-db 是 zhtw 的獨立外掛程式套件*
