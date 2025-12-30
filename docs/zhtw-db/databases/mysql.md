# MySQL 指南

## 快速開始

```bash
# 安裝
pip install zhtw-db[mysql]

# 使用
export DATABASE_URL="mysql://user:pass@localhost:3306/mydb"
zhtw db check --table users
zhtw db fix --table users
```

---

## 驅動選擇

| 驅動 | 安裝方式 | 適用場景 |
|------|---------|---------|
| mysqlclient | `pip install zhtw-db[mysql]` | 生產環境（需編譯）|
| PyMySQL | `pip install zhtw-db[mysql-pure]` | 開發環境（純 Python）|

---

## 支援版本

- MySQL 5.7, 8.0
- MariaDB 10.x

---

## 字元集注意事項

### utf8 vs utf8mb4

MySQL 的 `utf8` 只支援 3 bytes，無法儲存某些中文字（如 emoji）。建議使用 `utf8mb4`。

```sql
-- 檢查資料庫字元集
SHOW VARIABLES LIKE 'character_set%';

-- 檢查表字元集
SHOW CREATE TABLE users;
```

### 自動轉換

zhtw-db 會自動偵測並警告 utf8 表：

```
⚠️  users 表使用 utf8 編碼，建議升級至 utf8mb4
```

---

## 策略實作細節

### 策略 A：原地更新

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

**處理項目**：
- 引擎：偵測 MyISAM 並警告（表鎖）
- Binlog：`--skip-binlog` 選項
- 複製延遲：`--check-replica-lag` 選項
- 字元集：強制檢查 utf8mb4

### 策略 C'：反向影子

```sql
-- MySQL 支援原子 RENAME
RENAME TABLE
    users TO users_backup_20250101,
    users_new TO users;
```

---

## 引擎差異

| 引擎 | 鎖定 | 建議 |
|------|------|------|
| InnoDB | 行鎖 | 推薦 |
| MyISAM | 表鎖 | 警告使用者 |

---

## 權限需求

| 操作 | 權限 |
|------|------|
| check | `SELECT` |
| fix | `SELECT`, `UPDATE`, `CREATE`, `DROP`, `ALTER` |

---

## 常見問題

### 連線編碼問題

```bash
# 確保連線使用 utf8mb4
mysql://user:pass@localhost/mydb?charset=utf8mb4
```

### AUTO_INCREMENT 重設

策略 C' 會自動處理：

```sql
SELECT MAX(id) + 1 FROM users_backup;
ALTER TABLE users AUTO_INCREMENT = {value};
```
