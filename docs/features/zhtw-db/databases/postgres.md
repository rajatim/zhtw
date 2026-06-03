# PostgreSQL 指南

## 快速開始

```bash
# 安裝
pip install zhtw-db[postgres]

# 使用
export DATABASE_URL="postgres://user:pass@localhost:5432/mydb"
zhtw db check --table users
zhtw db fix --table users
```

---

## 驅動選擇

| 驅動 | 安裝方式 | 適用場景 |
|------|---------|---------|
| psycopg2-binary | `pip install zhtw-db[postgres]` | 開發環境（預設）|
| psycopg2 | `pip install zhtw-db[postgres-source]` | 生產環境（需編譯）|
| psycopg3 | `pip install zhtw-db[postgres-v3]` | 新專案（async 支援）|

---

## 支援版本

- PostgreSQL 12, 13, 14, 15, 16

---

## 策略實作細節

### 策略 A：原地更新

```sql
BEGIN;
SET session_replication_role = 'replica';  -- 暫停觸發器

UPDATE users SET name = '使用者'
WHERE id BETWEEN $1 AND $2
AND name = '用户';

COMMIT;
SET session_replication_role = 'origin';
VACUUM ANALYZE users;
```

**處理項目**：
- 鎖定：分批處理（`--batch-size 1000`）
- 觸發器：`SET session_replication_role` 暫停
- MVCC：完成後自動 `VACUUM ANALYZE`
- WAL：預估大小並警告
- 外鍵 CASCADE：偵測並警告

### 策略 C'：反向影子

```sql
BEGIN;

-- 1. 記錄外鍵約束
CREATE TEMP TABLE _fk_backup AS
SELECT conname, pg_get_constraintdef(oid)
FROM pg_constraint WHERE confrelid = 'users'::regclass;

-- 2. 移除外鍵
ALTER TABLE orders DROP CONSTRAINT orders_user_id_fkey;

-- 3. 重命名
ALTER TABLE users RENAME TO users_backup_20250101;

-- 4. 建立新表並轉換
CREATE TABLE users (LIKE users_backup_20250101 INCLUDING ALL);
INSERT INTO users SELECT ... FROM users_backup_20250101;

-- 5. 重建外鍵
ALTER TABLE orders ADD CONSTRAINT orders_user_id_fkey
FOREIGN KEY (user_id) REFERENCES users(id);

COMMIT;
```

**處理項目**：
- 外鍵：自動 DROP/CREATE
- 序列：自動轉移 OWNED BY
- 索引：自動跟隨
- 權限：自動複製

---

## 特殊欄位處理

### JSONB

```python
# 遞迴處理 JSONB 內的中文
{
    "user": {
        "name": "用户",  # → "使用者"
        "settings": {
            "language": "简体"  # → "繁體"
        }
    }
}
```

### TEXT[]

```python
# 陣列每個元素都處理
["用户", "软件", "程序"]
# → ["使用者", "軟體", "程式"]
```

---

## 權限需求

| 操作 | 權限 |
|------|------|
| check | `SELECT` |
| fix (A) | `SELECT`, `UPDATE` |
| fix (C') | `SELECT`, `INSERT`, `CREATE`, `DROP`, `ALTER` |
| fix (E) | 上述 + 審計表權限 |

---

## 效能建議

1. **分批處理**：大表使用 `--batch-size 5000`
2. **低峰期執行**：避免影響線上服務
3. **監控 WAL**：預留足夠磁碟空間
4. **VACUUM**：完成後考慮手動 `VACUUM FULL`

---

## 常見問題

### 連線被拒絕

```bash
# 檢查 pg_hba.conf
# 確認允許連線來源
```

### 權限不足

```sql
GRANT SELECT, UPDATE ON users TO your_user;
```

### 外鍵衝突

```bash
# 使用策略 C' 自動處理
zhtw db fix --strategy shadow
```
