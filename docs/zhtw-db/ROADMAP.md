# 產品路線圖

## 版本規劃總覽

```
v3.0 ─────► v3.1 ─────► v3.2 ─────► v3.3 ─────► v3.4+
SQLite     PostgreSQL   MySQL       MongoDB     企業級
```

---

## Phase 1: SQLite (v3.0)

**目標**：驗證核心架構，快速獲得使用者回饋

### 版本明細

| 版本 | 功能 | 策略支援 |
|------|------|---------|
| v3.0.0 | `zhtw db check` / `zhtw db scan` | - |
| v3.0.1 | `zhtw db fix` 反向影子 | C'（預設）|
| v3.0.2 | `zhtw db fix --strategy inplace` | A |
| v3.0.3 | `zhtw db fix --strategy newdb` | B |
| v3.0.4 | `zhtw db rollback` | C' 回滾 |
| v3.0.5 | `zhtw db diff` | 驗證工具 |

### 為什麼 SQLite 優先

- 零配置（不需要帳密）
- 單檔案（容易測試和展示）
- 最多獨立開發者使用
- Django/Flask/Rails 開發環境標配

---

## Phase 2: PostgreSQL (v3.1)

**目標**：進入正式生產環境

### 版本明細

| 版本 | 功能 |
|------|------|
| v3.1.0 | 連線 + check（psycopg2/psycopg3 支援）|
| v3.1.1 | fix 所有策略（A/B/C'/E）|
| v3.1.2 | Instance Clone 輔助（F）|
| v3.1.3 | JSONB 欄位處理 |
| v3.1.4 | 分批 + 進度條 + Checkpoint |
| v3.1.5 | 外鍵/觸發器/權限自動處理 |

### PostgreSQL 專屬考量

```python
# 需要處理的特殊情況
- JSONB 欄位內的中文
- TEXT[] 陣列欄位
- 觸發器暫停/恢復
- 外鍵約束處理
- VACUUM ANALYZE
```

### 支援版本

- PostgreSQL 12, 13, 14, 15, 16

---

## Phase 3: MySQL/MariaDB (v3.2)

**目標**：覆蓋傳統應用

### 版本明細

| 版本 | 功能 |
|------|------|
| v3.2.0 | 連線 + check（mysqlclient/PyMySQL 支援）|
| v3.2.1 | fix 所有策略 |
| v3.2.2 | utf8mb4 自動處理 |
| v3.2.3 | MariaDB 相容性 |
| v3.2.4 | 分區表支援 |

### MySQL 專屬考量

```python
# MySQL 特有問題
- utf8 vs utf8mb4（歷史包袱）
- ENUM 類型處理
- FULLTEXT 索引重建
- 分區表支援
- InnoDB vs MyISAM 偵測
```

### 支援版本

- MySQL 5.7, 8.0
- MariaDB 10.x

---

## Phase 4: MongoDB (v3.3)

**目標**：NoSQL 市場

### 版本明細

| 版本 | 功能 |
|------|------|
| v3.3.0 | 連線 + check |
| v3.3.1 | fix（Collection 備份 ≈ C'）|
| v3.3.2 | 巢狀文件遞迴處理 |
| v3.3.3 | Sharded Cluster 支援 |

### MongoDB 策略調整

```javascript
// MongoDB 沒有 RENAME TABLE，改用：
// 1. 建立 users_backup collection
// 2. 複製所有文件
// 3. 在原 collection 更新
```

### 支援版本

- MongoDB 5.0, 6.0, 7.0

---

## Phase 5: 企業級 (v3.4+)

**目標**：企業市場

| 版本 | 資料庫 | 備註 |
|------|--------|------|
| v3.4 | SQL Server | 企業 Windows 環境 |
| v3.5 | Oracle | 大型企業、政府 |
| v3.6 | 雲端整合 | RDS Clone、Cloud SQL Clone |

---

## 資料庫驅動版本策略

### 問題

不同環境使用不同的資料庫驅動：

```
PostgreSQL: psycopg2 vs psycopg2-binary vs psycopg(v3) vs asyncpg
MySQL: mysqlclient vs mysql-connector vs PyMySQL vs aiomysql
MongoDB: pymongo vs motor
```

### 解決方案：SQLAlchemy 抽象 + 使用者自選

```bash
# 方案 1：使用者已有驅動（企業環境常見）
pip install zhtw-db
# 自動偵測已安裝的驅動

# 方案 2：我們提供預設（新使用者）
pip install zhtw-db[postgres]    # 預設 psycopg2-binary
pip install zhtw-db[mysql]       # 預設 mysqlclient
pip install zhtw-db[mongodb]     # 預設 pymongo

# 方案 3：指定特定驅動
pip install zhtw-db[postgres-v3]    # psycopg v3
pip install zhtw-db[mysql-pure]     # PyMySQL（無需編譯）
```

### pyproject.toml 設計

```toml
[project.optional-dependencies]
postgres = ["psycopg2-binary>=2.9"]
postgres-source = ["psycopg2>=2.9"]       # 生產推薦
postgres-v3 = ["psycopg[binary]>=3.0"]    # 新版
mysql = ["mysqlclient>=2.0"]
mysql-pure = ["PyMySQL>=1.0"]             # 無需編譯
mongodb = ["pymongo>=4.0"]
all = ["psycopg2-binary", "mysqlclient", "pymongo"]
```

### 驅動偵測優先順序

```python
DRIVER_PRIORITY = {
    "postgresql": ["psycopg", "psycopg2", "pg8000"],
    "mysql": ["mysqlclient", "pymysql", "mysql-connector"],
    "mongodb": ["pymongo"],
}
```

---

## 功能優先級

### P0 - MVP 必要

- [ ] SQLite 支援
- [ ] check / fix 指令
- [ ] 策略 A（原地）+ C'（反向影子）
- [ ] Checkpoint 斷點續傳
- [ ] 進度條

### P1 - 生產必要

- [ ] PostgreSQL 支援
- [ ] MySQL 支援
- [ ] rollback 指令
- [ ] 策略 E（審計）
- [ ] JSON/JSONB 欄位處理

### P2 - 進階功能

- [ ] MongoDB 支援
- [ ] 策略 F（新實例）
- [ ] 陣列欄位處理
- [ ] 雲端 Clone 整合

### P3 - 企業功能

- [ ] SQL Server 支援
- [ ] Oracle 支援
- [ ] 完整審計報表

---

*路線圖 v1.0 - 2025-12-31*
