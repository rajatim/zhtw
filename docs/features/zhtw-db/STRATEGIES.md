# 轉換策略指南

選擇正確的轉換策略是資料庫轉換最重要的決策。本文檔詳細說明每種策略的優缺點和適用場景。

---

## 策略總覽

| 策略 | 名稱 | 程式碼改動 | 設定改動 | 回滾 | 空間 | 適合場景 |
|------|------|-----------|---------|------|------|---------|
| A | 原地更新 | 無 | 無 | 無法 | 1x | 小型、可重建 |
| B | 新資料庫 | 無 | DB名 | 可 | 2x DB | 完整隔離 |
| C' | 反向影子 | 無 | 無 | 可 | 2x 表 | **推薦預設** |
| D | 版本欄位 | 要改 | 無 | 可 | 1.x | 漸進遷移 |
| E | 審計表 | 無 | 無 | 精確 | 1.x | 合規需求 |
| F | 新實例 | 無 | 連線 | 可 | 2x 實例 | 生產環境 |

---

## 策略 A：原地更新 (In-Place)

直接修改原表資料，最簡單但風險最高。

### 使用方式

```bash
zhtw db fix postgres://... --table users --strategy inplace --force
```

### SQL 範例

```sql
UPDATE users SET name = '使用者' WHERE id = 1;
```

### 優缺點

| 優點 | 缺點 |
|------|------|
| ✅ 最簡單、最直接 | ❌ 無法回滾（除非有備份）|
| ✅ 不需要額外空間 | ❌ 風險最高 |
| ✅ 無需程式碼改動 | ❌ 出錯難以恢復 |

### PostgreSQL 實作細節

```sql
BEGIN;
SET session_replication_role = 'replica';  -- 暫停觸發器

-- 分批更新（避免長事務）
UPDATE users SET name = '使用者'
WHERE id BETWEEN $1 AND $2
AND name = '用户';

COMMIT;
SET session_replication_role = 'origin';
VACUUM ANALYZE users;  -- 清理 dead tuples
```

| 項目 | 處理方式 |
|------|---------|
| 鎖定 | 分批處理（`--batch-size 1000`）|
| 觸發器 | `SET session_replication_role` 暫停 |
| MVCC | 完成後自動 `VACUUM ANALYZE` |
| WAL | 預估大小並警告 |
| 外鍵 CASCADE | 偵測並警告使用者 |

### MySQL 實作細節

```sql
SET SESSION foreign_key_checks = 0;
SET SESSION sql_log_bin = 0;  -- 可選

UPDATE users SET name = '使用者'
WHERE id BETWEEN ? AND ?
AND name = '用户';

SET SESSION foreign_key_checks = 1;
SET SESSION sql_log_bin = 1;
ANALYZE TABLE users;
```

### 適用場景

- 開發環境
- 可隨時重建的資料
- 小型資料集（< 10,000 筆）

---

## 策略 B：新資料庫 (New Database)

將轉換結果輸出到新的資料庫/檔案，原資料庫完全不動。

### 使用方式

```bash
# SQLite
zhtw db fix sqlite:///app.db --strategy newdb --output app_converted.db

# PostgreSQL
zhtw db fix postgres://localhost/mydb --strategy newdb --output mydb_tw
```

### 優缺點

| 優點 | 缺點 |
|------|------|
| ✅ 原資料庫完全不動 | ❌ 需要雙倍空間 |
| ✅ 可以慢慢驗證 | ❌ 需要切換連線字串 |
| ✅ 回滾 = 不切換 | |

### 實作細節

**PostgreSQL**
```bash
# 方式 1：pg_dump（邏輯備份）
pg_dump -Fc source_db | pg_restore -d target_db

# 方式 2：CREATE DATABASE TEMPLATE（物理複製）
CREATE DATABASE target_db TEMPLATE source_db;
```

**MySQL**
```bash
mysqldump source_db | mysql target_db
```

**SQLite**
```bash
cp source.db target.db
```

### 適用場景

- 一次性遷移
- 有足夠磁碟空間
- 不急著上線

---

## 策略 C'：反向影子 (Reverse Shadow) - **推薦**

備份原表，轉換後保持原表名稱，程式碼無需任何改動。

### 使用方式

```bash
zhtw db fix postgres://... --table users --strategy shadow
```

### 流程

```
  原始狀態                    轉換過程                      完成狀態

 ┌──────────┐              ┌──────────┐                  ┌──────────┐
 │  users   │    Step 1    │  users   │     Step 4      │  users   │
 │──────────│   ─────────> │──────────│    ─────────>   │──────────│
 │ id: 1    │   RENAME     │  (已改名為                  │ id: 1    │
 │ name:    │   TO backup  │  users_backup)              │ name:    │
 │ "用户"   │              │                             │ "使用者"  │
 └──────────┘              └──────────┘                  └──────────┘
                                 │                             ▲
                                 │ Step 2-3                    │
                                 │ CREATE + INSERT             │
                                 │ + RENAME                    │
                                 ▼                             │
                           ┌──────────┐                        │
                           │users_new │                        │
                           │──────────│                        │
                           │ "使用者" │ ───────────────────────┘
                           └──────────┘

  備份保留
 ┌────────────────┐
 │ users_backup_  │  (保留 7 天，可回滾)
 │ 20250101_1200  │
 └────────────────┘
```

### 優缺點

| 優點 | 缺點 |
|------|------|
| ✅ 程式不用改、設定不用改 | ❌ 需要處理外鍵 |
| ✅ 可隨時回滾（RENAME 回去）| ❌ 需要 2 倍表空間 |
| ✅ 原子切換 | ❌ RENAME 有短暫鎖定 |

### PostgreSQL 實作細節

```sql
BEGIN;

-- 1. 記錄外鍵約束
CREATE TEMP TABLE _fk_backup AS
SELECT conname, conrelid::regclass, confrelid::regclass, pg_get_constraintdef(oid)
FROM pg_constraint WHERE confrelid = 'users'::regclass;

-- 2. 移除指向本表的外鍵
DO $$
DECLARE r RECORD;
BEGIN
    FOR r IN SELECT conname, conrelid::regclass AS tbl FROM pg_constraint
             WHERE confrelid = 'users'::regclass
    LOOP
        EXECUTE 'ALTER TABLE ' || r.tbl || ' DROP CONSTRAINT ' || r.conname;
    END LOOP;
END $$;

-- 3. 重命名原表
ALTER TABLE users RENAME TO users_backup_20250101;

-- 4. 建立新表並轉換
CREATE TABLE users (LIKE users_backup_20250101 INCLUDING ALL);
INSERT INTO users SELECT
    id,
    CASE WHEN name = '用户' THEN '使用者' ELSE name END,
    ...
FROM users_backup_20250101;

-- 5. 修復序列
SELECT setval('users_id_seq', (SELECT MAX(id) FROM users));

-- 6. 重建外鍵

COMMIT;
```

### 各資料庫差異

| 項目 | PostgreSQL | MySQL | SQLite |
|------|-----------|-------|--------|
| 表重命名 | `ALTER TABLE RENAME` | `RENAME TABLE` | `ALTER TABLE RENAME` |
| 外鍵處理 | 需手動 DROP/CREATE | 需手動 DROP/CREATE | 無外鍵強制 |
| 序列處理 | `ALTER SEQUENCE` | `AUTO_INCREMENT` | `AUTOINCREMENT` |
| 索引 | 自動跟隨 | 自動跟隨 | 自動跟隨 |

### 適用場景

- **大多數情況的最佳選擇**
- 需要零程式碼改動
- 需要回滾能力

---

## 策略 E：審計模式 (Audit)

記錄所有變更到審計表，支援精確回滾，適合合規要求。

### 使用方式

```bash
zhtw db fix postgres://... --table users --strategy audit
```

### 審計表結構

```sql
CREATE TABLE zhtw_audit (
    id BIGSERIAL PRIMARY KEY,
    batch_id UUID NOT NULL,              -- 批次 ID
    table_schema VARCHAR(255) NOT NULL,
    table_name VARCHAR(255) NOT NULL,
    primary_key_columns JSONB NOT NULL,  -- {"id": 123}
    column_name VARCHAR(255) NOT NULL,
    old_value TEXT,
    new_value TEXT,
    converted_at TIMESTAMPTZ DEFAULT NOW(),
    converted_by VARCHAR(255),
    rollback_at TIMESTAMPTZ,
    rollback_by VARCHAR(255),

    INDEX idx_batch (batch_id),
    INDEX idx_table (table_schema, table_name),
    INDEX idx_converted_at (converted_at)
);
```

### 回滾流程

```sql
-- 精確回滾單筆
UPDATE users SET name = (
    SELECT old_value FROM zhtw_audit
    WHERE table_name = 'users'
    AND primary_key_columns->>'id' = '123'
    AND column_name = 'name'
)
WHERE id = 123;

-- 批次回滾
UPDATE zhtw_audit SET rollback_at = NOW()
WHERE batch_id = 'xxx' AND rollback_at IS NULL;
```

### 優缺點

| 優點 | 缺點 |
|------|------|
| ✅ 完整追蹤每筆變更 | ❌ 實作複雜 |
| ✅ 可精確回滾任一筆 | ❌ 審計表可能很大 |
| ✅ 符合合規要求 | ❌ 效能較低（雙倍寫入）|

### 適用場景

- 金融業（GDPR、個資法）
- 醫療業（HIPAA）
- 政府機關
- 上市公司
- 任何需要審計追蹤的場景

---

## 策略 F：新實例 (Instance Clone)

複製整個資料庫實例，轉換後切換連線字串。

### 使用方式

```bash
# 1. Clone 實例（使用雲端工具或我們的輔助指令）
zhtw db clone postgres://source postgres://target

# 2. 轉換新實例
zhtw db fix postgres://target --all-tables

# 3. 驗證
zhtw db diff postgres://source postgres://target

# 4. 切換（修改環境變數）
export DATABASE_URL=postgres://target
```

### 雲端 Clone 指令

| 雲端 | Clone 指令 | 耗時 |
|------|-----------|------|
| AWS RDS | `aws rds restore-db-instance-from-db-snapshot` | 分鐘級 |
| GCP Cloud SQL | `gcloud sql instances clone` | 分鐘級 |
| Azure | `az sql db copy` | 分鐘級 |
| DigitalOcean | `doctl databases fork` | 分鐘級 |

### 自建環境

| 資料庫 | Clone 方式 |
|--------|-----------|
| PostgreSQL | `pg_basebackup` 或 Logical Replication |
| MySQL | `xtrabackup` 或 `mysqldump` |
| MongoDB | `mongodump/mongorestore` 或 Replica Set |

### 優缺點

| 優點 | 缺點 |
|------|------|
| ✅ 完整隔離，零停機 | ❌ 需要雙倍資源 |
| ✅ 可充分測試後再切換 | ❌ 需要改連線字串 |
| ✅ 秒級回滾（切回舊連線）| ❌ 需要基礎設施存取權 |

### 適用場景

- 生產環境（24/7 服務）
- Blue-Green 部署
- 需要充分測試再上線

---

## 策略選擇決策樹

```
需要轉換資料庫
       │
       ▼
  是否為生產環境？
       │
  ┌────┴────┐
  否        是
  │         │
  ▼         ▼
可以接受    有維護窗口嗎？
資料遺失？      │
  │       ┌────┴────┐
┌─┴─┐     有        無
可以 不行   │         │
 │   │    ▼         ▼
 ▼   ▼  策略 C'   策略 F
策略 策略  反向影子   新實例
 A   C'
原地 反向
更新 影子


  有合規需求？
       │
  ┌────┴────┐
  有        無
  │         │
  ▼         ▼
策略 E    其他策略
審計模式
```

---

## 多專家角度評估

### DBA 視角

| 策略 | 鎖定影響 | 連線需求 | 效能衝擊 |
|------|---------|---------|---------|
| A | 高（行鎖） | 單一 | 中 |
| B | 無 | 雙重（讀+寫） | 高（I/O） |
| C' | 中（DDL 鎖） | 單一 | 中 |
| E | 高（雙表寫入） | 單一 | 高 |
| F | 無 | 雙重 | 取決於 Clone 方式 |

### Business Analyst 視角

| 業務情境 | 推薦策略 | 原因 |
|---------|---------|------|
| 24/7 線上服務 | F | 零停機 |
| 可維護窗口 | C' | 最乾淨 |
| 一次性遷移 | B | 最安全 |
| 漸進式遷移 | D | 最彈性 |
| 法規要求 | E | 完整追蹤 |

### 綜合評估矩陣

| 維度 | A 原地 | B 新庫 | C' 影子 | E 審計 | F 實例 |
|------|:-----:|:-----:|:------:|:-----:|:-----:|
| 實作複雜度 | ⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| 回滾能力 | ❌ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 空間需求 | ⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |
| 效能影響 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐ |
| 合規友善 | ❌ | ⭐ | ⭐ | ⭐⭐⭐ | ⭐⭐ |
| 零停機 | ❌ | ⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐⭐ |

---

*策略指南 v1.0 - 2025-12-31*
