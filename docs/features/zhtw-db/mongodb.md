# MongoDB 指南

## 快速開始

```bash
# 安裝
pip install zhtw-db[mongodb]

# 使用
export DATABASE_URL="mongodb://localhost:27017/mydb"
zhtw db check --collection users
zhtw db fix --collection users
```

---

## 驅動

| 驅動 | 安裝方式 |
|------|---------|
| pymongo | `pip install zhtw-db[mongodb]` |

---

## 支援版本

- MongoDB 5.0, 6.0, 7.0

---

## 術語對應

| SQL | MongoDB |
|-----|---------|
| 表 (Table) | 集合 (Collection) |
| 列 (Row) | 文件 (Document) |
| 欄位 (Column) | 欄位 (Field) |

---

## 策略實作

### 備份策略（類似 C'）

MongoDB 沒有 `RENAME COLLECTION`，改用：

```javascript
// 1. 建立備份集合
db.users.aggregate([
    { $match: {} },
    { $out: "users_backup_20250101" }
]);

// 2. 更新原集合
db.users.bulkWrite([
    {
        updateOne: {
            filter: { _id: ObjectId("...") },
            update: { $set: { name: "使用者" } }
        }
    },
    // ...
]);
```

---

## 巢狀文件處理

MongoDB 文件可以有任意深度的巢狀結構：

```javascript
// 原始文件
{
    "_id": ObjectId("..."),
    "profile": {
        "name": "用户",
        "settings": {
            "language": "简体",
            "notifications": {
                "email": "软件通知"
            }
        }
    },
    "tags": ["软件", "程序", "网络"]
}

// 轉換後
{
    "_id": ObjectId("..."),
    "profile": {
        "name": "使用者",
        "settings": {
            "language": "繁體",
            "notifications": {
                "email": "軟體通知"
            }
        }
    },
    "tags": ["軟體", "程式", "網路"]
}
```

zhtw-db 會遞迴處理所有巢狀結構。

---

## Sharded Cluster

對於分片集群：

```bash
# 指定 mongos 路由
mongodb://mongos1:27017,mongos2:27017/mydb

# 確保所有分片都可存取
```

---

## Replica Set

```bash
# 連線到 Primary
mongodb://primary:27017,secondary1:27017,secondary2:27017/mydb?replicaSet=rs0

# 可以從 Secondary 讀取加速掃描
mongodb://...?readPreference=secondaryPreferred
```

---

## 常見問題

### 連線逾時

```bash
# 增加逾時
mongodb://localhost:27017/mydb?connectTimeoutMS=30000
```

### 認證

```bash
# 帶認證
mongodb://user:pass@localhost:27017/mydb?authSource=admin
```

### 大量更新效能

使用 bulkWrite 批次處理，避免單筆更新：

```javascript
db.users.bulkWrite([
    { updateOne: { ... } },
    { updateOne: { ... } },
    // ...
], { ordered: false });
```
