# SQLite 指南

## 快速開始

```bash
# 安裝（SQLite 驅動內建，不需額外安裝）
pip install zhtw-db

# 使用
zhtw db check sqlite:///app.db
zhtw db fix sqlite:///app.db --table users
```

---

## 連線格式

```bash
# 相對路徑
sqlite:///app.db
sqlite:///./data/app.db

# 絕對路徑
sqlite:////Users/name/app.db
sqlite:///C:/Users/name/app.db  # Windows
```

---

## 特性

| 特性 | 說明 |
|------|------|
| 驅動 | 內建 sqlite3（不需額外安裝）|
| 鎖定 | 檔案級鎖定 |
| 外鍵 | 預設關閉（需手動啟用）|
| 備份 | 簡單（複製檔案即可）|

---

## 策略差異

### 策略 B：新資料庫

對 SQLite 來說最簡單：

```bash
# 複製檔案
cp app.db app_converted.db

# 轉換新檔案
zhtw db fix sqlite:///app_converted.db
```

### 策略 C'：反向影子

```sql
-- SQLite 支援 ALTER TABLE RENAME
ALTER TABLE users RENAME TO users_backup_20250101;

-- 建立新表
CREATE TABLE users AS SELECT
    id,
    CASE WHEN name = '用户' THEN '使用者' ELSE name END AS name,
    ...
FROM users_backup_20250101;
```

---

## 備份建議

SQLite 備份極為簡單：

```bash
# 修改前先備份
cp app.db app.db.bak

# 或使用 SQLite 內建備份
sqlite3 app.db ".backup app.db.bak"
```

---

## 常見問題

### 檔案鎖定

```
sqlite3.OperationalError: database is locked
```

確保沒有其他程式正在存取資料庫。

### 外鍵約束

```sql
-- 啟用外鍵（預設關閉）
PRAGMA foreign_keys = ON;
```

### 大檔案效能

大型 SQLite 檔案（> 1GB）建議：
- 使用較大的 `--batch-size`
- 確保磁碟空間充足（策略 C' 需要 2 倍空間）
