# zhtw-db 架構設計

## 確認的決策

| 項目 | 決策 |
|------|------|
| MVP 範圍 | 完整 MVP（SQLite + 策略 A/C' + Checkpoint + 進度條）|
| 資料類型 | 全部類型（TEXT/JSON/陣列/ENUM）|
| 自動探索 | 提供 `zhtw db scan` 指令 |
| 測試策略 | 混合模式（單元 Mock + 整合 testcontainers）|
| CI/CD | Jenkins |

---

## 專案結構

```
zhtw-db/
├── src/zhtw_db/
│   ├── __init__.py              # 版本號、匯出
│   ├── cli.py                   # CLI 入口（擴展 zhtw）
│   │
│   ├── core/                    # 核心模組
│   │   ├── __init__.py
│   │   ├── scanner.py           # Schema 自動探索
│   │   ├── converter.py         # 轉換引擎
│   │   ├── checkpoint.py        # 進度檢查點
│   │   └── progress.py          # 進度條/ETA
│   │
│   ├── strategies/              # 輸出策略（Strategy Pattern）
│   │   ├── __init__.py
│   │   ├── base.py              # 抽象基類
│   │   ├── inplace.py           # A - 原地更新
│   │   ├── shadow.py            # C' - 反向影子
│   │   ├── newdb.py             # B - 新資料庫
│   │   ├── audit.py             # E - 審計模式
│   │   └── instance.py          # F - 新實例
│   │
│   ├── drivers/                 # 資料庫驅動抽象
│   │   ├── __init__.py
│   │   ├── base.py              # 抽象基類
│   │   ├── sqlite.py            # SQLite 實作
│   │   ├── postgres.py          # PostgreSQL 實作
│   │   ├── mysql.py             # MySQL 實作
│   │   └── mongodb.py           # MongoDB 實作
│   │
│   ├── types/                   # 資料類型處理
│   │   ├── __init__.py
│   │   ├── text.py              # TEXT/VARCHAR
│   │   ├── json.py              # JSON/JSONB
│   │   ├── array.py             # 陣列類型
│   │   └── enum.py              # ENUM 類型
│   │
│   └── utils/                   # 工具
│       ├── __init__.py
│       ├── connection.py        # 連線管理
│       ├── security.py          # 密碼處理、SSL
│       └── logger.py            # 日誌
│
├── tests/
│   ├── unit/                    # 單元測試（Mock）
│   │   ├── test_scanner.py
│   │   ├── test_converter.py
│   │   ├── test_checkpoint.py
│   │   └── test_strategies.py
│   │
│   ├── integration/             # 整合測試（testcontainers）
│   │   ├── conftest.py          # 容器 fixtures
│   │   ├── test_sqlite.py
│   │   ├── test_postgres.py
│   │   ├── test_mysql.py
│   │   └── test_mongodb.py
│   │
│   └── fixtures/                # 測試資料
│       ├── sample_data.sql
│       └── sample_data.json
│
├── docs/
│   ├── quickstart.md
│   ├── strategies.md
│   └── databases/
│
├── pyproject.toml
├── README.md
├── CHANGELOG.md
├── Jenkinsfile
└── docker-compose.test.yml
```

---

## 整體架構圖

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                  CLI Layer                                   │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌─────────┐ ┌──────────┐  │
│  │  scan   │ │  check  │ │   fix   │ │ rollback │ │  jobs   │ │  resume  │  │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬─────┘ └────┬────┘ └────┬─────┘  │
└───────┼──────────┼──────────┼───────────┼───────────┼───────────┼──────────┘
        │          │          │           │           │           │
        ▼          ▼          ▼           ▼           ▼           ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                                Core Layer                                    │
│                                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────────┐ │
│  │   Scanner    │  │  Converter   │  │  Checkpoint  │  │     Progress     │ │
│  │              │  │              │  │   Manager    │  │    (進度條/ETA)   │ │
│  │ • 探索表格    │  │ • 載入詞庫    │  │              │  │                  │ │
│  │ • 偵測欄位    │  │ • 比對轉換    │  │ • 建立檢查點  │  │ • TTY 偵測       │ │
│  │ • 取樣分析    │  │ • 批次處理    │  │ • 更新進度    │  │ • 進度計算       │ │
│  └──────┬───────┘  └──────┬───────┘  │ • 恢復工作    │  │ • ETA 估算       │ │
│         │                 │          └──────┬───────┘  └────────┬─────────┘ │
└─────────┼─────────────────┼─────────────────┼───────────────────┼───────────┘
          │                 │                 │                   │
          ▼                 ▼                 ▼                   ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             Strategy Layer                                   │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                      OutputStrategy (Abstract)                       │    │
│  │  • validate()  • prepare()  • execute()  • finalize()  • rollback() │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│         ▲              ▲              ▲              ▲              ▲       │
│         │              │              │              │              │       │
│  ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ │
│  │  Inplace   │ │   Shadow   │ │   NewDB    │ │   Audit    │ │  Instance  │ │
│  │    (A)     │ │    (C')    │ │    (B)     │ │    (E)     │ │    (F)     │ │
│  │            │ │            │ │            │ │            │ │            │ │
│  │ UPDATE直接 │ │ 備份→轉換  │ │ 輸出新庫   │ │ 審計記錄   │ │ Clone實例  │ │
│  │ 無法回滾   │ │ 可RENAME回 │ │ 切換連線   │ │ 精確回滾   │ │ 切換連線   │ │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘ └────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Type Layer                                      │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                       TypeHandler (Abstract)                         │    │
│  │              • extract_text()       • replace_text()                 │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│         ▲              ▲              ▲              ▲                      │
│         │              │              │              │                      │
│  ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐               │
│  │    Text    │ │    JSON    │ │   Array    │ │    Enum    │               │
│  │            │ │            │ │            │ │            │               │
│  │ TEXT       │ │ JSON       │ │ TEXT[]     │ │ ENUM       │               │
│  │ VARCHAR    │ │ JSONB      │ │ VARCHAR[]  │ │ (警告模式) │               │
│  │ CHAR       │ │ (遞迴解析) │ │ ARRAY      │ │            │               │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘               │
└─────────────────────────────────────────────────────────────────────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                             Driver Layer                                     │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │                     DatabaseDriver (Abstract)                        │    │
│  │  • connect()      • list_tables()     • scan_column()               │    │
│  │  • disconnect()   • get_table_info()  • batch_update()              │    │
│  │  • begin/commit/rollback              • rename_table()              │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│         ▲              ▲              ▲              ▲                      │
│         │              │              │              │                      │
│  ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐ ┌──────┴─────┐               │
│  │   SQLite   │ │ PostgreSQL │ │   MySQL    │ │  MongoDB   │               │
│  │            │ │            │ │            │ │            │               │
│  │ sqlite3    │ │ psycopg2   │ │ mysqlclient│ │ pymongo    │               │
│  │ (內建)     │ │ psycopg3   │ │ PyMySQL    │ │            │               │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘               │
└─────────────────────────────────────────────────────────────────────────────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                            Database Layer                                    │
│                                                                              │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐         │
│    │  SQLite  │     │PostgreSQL│     │  MySQL   │     │ MongoDB  │         │
│    │  *.db    │     │ :5432    │     │  :3306   │     │  :27017  │         │
│    └──────────┘     └──────────┘     └──────────┘     └──────────┘         │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 核心類別設計

### 1. DatabaseDriver（資料庫驅動抽象）

```python
# src/zhtw_db/drivers/base.py
from abc import ABC, abstractmethod
from typing import Iterator, Any
from dataclasses import dataclass

@dataclass
class ColumnInfo:
    name: str
    data_type: str          # TEXT, VARCHAR, JSON, etc.
    is_nullable: bool
    max_length: int | None
    has_chinese: bool       # 掃描結果

@dataclass
class TableInfo:
    schema: str
    name: str
    primary_key: list[str]
    columns: list[ColumnInfo]
    row_count: int

class DatabaseDriver(ABC):
    """資料庫驅動抽象基類"""

    @abstractmethod
    def connect(self, url: str) -> None:
        """建立連線"""
        pass

    @abstractmethod
    def disconnect(self) -> None:
        """關閉連線"""
        pass

    @abstractmethod
    def list_tables(self) -> list[str]:
        """列出所有表"""
        pass

    @abstractmethod
    def get_table_info(self, table: str) -> TableInfo:
        """取得表結構資訊"""
        pass

    @abstractmethod
    def scan_column(self, table: str, column: str) -> Iterator[tuple[Any, str]]:
        """串流掃描欄位內容，yield (pk_value, content)"""
        pass

    @abstractmethod
    def update_row(self, table: str, pk: Any, column: str, value: str) -> None:
        """更新單筆資料"""
        pass

    @abstractmethod
    def batch_update(self, table: str, updates: list[tuple[Any, str, str]]) -> int:
        """批次更新，回傳成功筆數"""
        pass

    @abstractmethod
    def begin_transaction(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

    # 策略 C' 需要的方法
    @abstractmethod
    def rename_table(self, old_name: str, new_name: str) -> None:
        pass

    @abstractmethod
    def create_table_like(self, source: str, target: str) -> None:
        pass

    @abstractmethod
    def copy_table_data(self, source: str, target: str) -> int:
        pass

    @abstractmethod
    def get_foreign_keys_to(self, table: str) -> list[dict]:
        """取得指向此表的外鍵"""
        pass

    @abstractmethod
    def drop_constraint(self, table: str, constraint: str) -> None:
        pass

    @abstractmethod
    def create_constraint(self, table: str, constraint_def: str) -> None:
        pass
```

### 2. OutputStrategy（輸出策略抽象）

```python
# src/zhtw_db/strategies/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Iterator, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from ..drivers.base import DatabaseDriver

@dataclass
class ConversionPlan:
    """轉換計畫"""
    table: str
    column: str
    total_rows: int
    affected_rows: int
    estimated_time: float   # 秒
    space_required: int     # bytes
    warnings: list[str]
    can_rollback: bool

@dataclass
class ConversionResult:
    """轉換結果"""
    table: str
    column: str
    success_count: int
    error_count: int
    duration: float
    backup_location: str | None
    rollback_command: str | None

class OutputStrategy(ABC):
    """輸出策略抽象基類"""

    name: str
    description: str
    requires_extra_space: bool
    supports_rollback: bool
    danger_level: int  # 1-5, 5 最危險

    @abstractmethod
    def validate(self, driver: "DatabaseDriver", table: str) -> list[str]:
        """驗證此策略是否可用，回傳警告訊息"""
        pass

    @abstractmethod
    def estimate(self, driver: "DatabaseDriver", table: str, column: str) -> ConversionPlan:
        """預估轉換計畫"""
        pass

    @abstractmethod
    def prepare(self, driver: "DatabaseDriver", table: str) -> None:
        """準備工作（如建立備份表）"""
        pass

    @abstractmethod
    def execute(
        self,
        driver: "DatabaseDriver",
        table: str,
        column: str,
        conversions: Iterator[tuple[Any, str, str]],  # (pk, old, new)
        batch_size: int,
        on_progress: Callable[[int, int], None]
    ) -> ConversionResult:
        """執行轉換"""
        pass

    @abstractmethod
    def finalize(self, driver: "DatabaseDriver", table: str) -> None:
        """完成工作（如 VACUUM、切換表名）"""
        pass

    @abstractmethod
    def rollback(self, driver: "DatabaseDriver", table: str, backup_location: str) -> None:
        """回滾"""
        pass
```

### 3. CheckpointManager（斷點續傳）

```python
# src/zhtw_db/core/checkpoint.py
from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
from typing import Any
import json
import uuid

@dataclass
class CheckpointData:
    job_id: str
    database_url_hash: str  # URL 的 hash（不存密碼）
    table: str
    column: str
    strategy: str
    total_rows: int
    processed_rows: int
    last_pk: Any
    status: str             # running, paused, completed, failed
    started_at: str         # ISO format
    updated_at: str
    error: str | None
    backup_location: str | None

class CheckpointManager:
    """檢查點管理器"""

    CHECKPOINT_DIR = Path.home() / ".zhtw" / "checkpoints"

    def __init__(self, checkpoint_dir: Path = None):
        self.checkpoint_dir = checkpoint_dir or self.CHECKPOINT_DIR
        self.checkpoint_dir.mkdir(parents=True, exist_ok=True)

    def create(self, database_url: str, table: str, column: str,
               strategy: str, total_rows: int) -> str:
        """建立新檢查點，回傳 job_id"""
        ...

    def update(self, job_id: str, processed: int, last_pk: Any) -> None:
        """更新進度（每批次呼叫）"""
        ...

    def complete(self, job_id: str, backup_location: str = None) -> None:
        """標記完成"""
        ...

    def fail(self, job_id: str, error: str) -> None:
        """標記失敗"""
        ...

    def pause(self, job_id: str) -> None:
        """暫停（可恢復）"""
        ...

    def load(self, job_id: str) -> CheckpointData | None:
        """載入檢查點"""
        ...

    def list_incomplete(self) -> list[CheckpointData]:
        """列出未完成的工作"""
        ...
```

### 4. TypeHandler（資料類型處理）

```python
# src/zhtw_db/types/json.py
class JsonTypeHandler(TypeHandler):
    """JSON/JSONB 類型處理器"""

    supported_types = ["JSON", "JSONB", "json", "jsonb"]

    def extract_text(self, value: Any) -> list[tuple[str, str]]:
        """遞迴提取 JSON 中所有字串"""
        texts = []

        def recurse(obj, path="$"):
            if isinstance(obj, str):
                texts.append((path, obj))
            elif isinstance(obj, dict):
                for k, v in obj.items():
                    recurse(v, f"{path}.{k}")
            elif isinstance(obj, list):
                for i, item in enumerate(obj):
                    recurse(item, f"{path}[{i}]")

        recurse(value)
        return texts

    def replace_text(self, value: Any, replacements: dict[str, str]) -> Any:
        """遞迴替換 JSON 中的字串"""
        ...
```

---

## 資料流程圖

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            zhtw db fix 流程                                  │
└─────────────────────────────────────────────────────────────────────────────┘

     使用者                     zhtw-db                        資料庫
        │                          │                              │
        │  zhtw db fix postgres:// │                              │
        │─────────────────────────>│                              │
        │                          │                              │
        │                          │  1. 連線                     │
        │                          │─────────────────────────────>│
        │                          │                              │
        │                          │  2. 取得表結構               │
        │                          │─────────────────────────────>│
        │                          │<─────────────────────────────│
        │                          │                              │
        │                          │  3. 掃描欄位內容             │
        │                          │─────────────────────────────>│
        │                          │<─────────────────────────────│
        │                          │                              │
        │  顯示轉換計畫            │                              │
        │<─────────────────────────│                              │
        │                          │                              │
        │  確認執行 [Y/n]          │                              │
        │─────────────────────────>│                              │
        │                          │                              │
        │                          │  4. Strategy.prepare()       │
        │                          │  (建立備份表)                │
        │                          │─────────────────────────────>│
        │                          │                              │
        │                          │  5. 建立 Checkpoint          │
        │                          │  ~/.zhtw/checkpoints/xxx.json│
        │                          │                              │
        │                          │  6. 批次轉換                 │
        │  [████████░░] 80%        │─────────────────────────────>│
        │<─────────────────────────│  (每批次更新 Checkpoint)     │
        │                          │                              │
        │                          │  7. Strategy.finalize()      │
        │                          │  (VACUUM / RENAME)           │
        │                          │─────────────────────────────>│
        │                          │                              │
        │  ✅ 轉換完成！           │  8. Checkpoint.complete()    │
        │  回滾指令: zhtw db       │                              │
        │  rollback --job-id xxx   │                              │
        │<─────────────────────────│                              │
```

---

## Checkpoint 狀態機

```
                    ┌─────────────────────────────────────────┐
                    │                                         │
                    ▼                                         │
              ┌──────────┐                                    │
   create()   │          │                                    │
  ─────────>  │ running  │ ──────────────────────────────────>│
              │          │        complete()                  │
              └────┬─────┘                                    │
                   │                                          │
         fail() or │                                          │
         中斷      │                                          │
                   ▼                                          │
              ┌──────────┐        resume()              ┌─────┴────┐
              │          │ ────────────────────────────>│          │
              │  failed  │                              │ completed│
              │  paused  │                              │          │
              │          │                              └──────────┘
              └──────────┘
```

---

## 模組依賴圖

```
                              ┌─────────┐
                              │   CLI   │
                              └────┬────┘
                                   │
                    ┌──────────────┼──────────────┐
                    │              │              │
                    ▼              ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │ Scanner  │  │Converter │  │Checkpoint│
              └────┬─────┘  └────┬─────┘  └──────────┘
                   │             │
                   │             ├──────────────┐
                   │             │              │
                   ▼             ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │  Driver  │  │ Strategy │  │   Type   │
              │ (SQLite) │  │ (Shadow) │  │ (JSON)   │
              └────┬─────┘  └────┬─────┘  └──────────┘
                   │             │
                   ▼             │
              ┌──────────┐       │
              │ Database │ <─────┘
              │ (實際DB) │
              └──────────┘


  外部依賴：
  ┌─────────────────────────────────────────────────────┐
  │  zhtw-db                                            │
  │  ├── zhtw (核心詞庫)                                │
  │  ├── sqlalchemy (資料庫抽象)                        │
  │  ├── click (CLI)                                   │
  │  └── [可選]                                        │
  │      ├── psycopg2 / psycopg3 (PostgreSQL)          │
  │      ├── mysqlclient / PyMySQL (MySQL)             │
  │      └── pymongo (MongoDB)                         │
  └─────────────────────────────────────────────────────┘
```

---

## MVP 實作順序

### Phase 1: 基礎架構 (v3.0.0-alpha)
1. [ ] 專案初始化（pyproject.toml、結構）
2. [ ] DatabaseDriver 抽象基類
3. [ ] SQLite Driver 實作
4. [ ] 基本 scan 指令
5. [ ] 基本 check 指令

### Phase 2: 轉換功能 (v3.0.0-beta)
6. [ ] OutputStrategy 抽象基類
7. [ ] InplaceStrategy (A) 實作
8. [ ] ShadowStrategy (C') 實作
9. [ ] fix 指令
10. [ ] CheckpointManager
11. [ ] 進度條/ETA

### Phase 3: 資料類型 (v3.0.0-rc)
12. [ ] TextTypeHandler
13. [ ] JsonTypeHandler
14. [ ] ArrayTypeHandler
15. [ ] EnumTypeHandler（警告模式）

### Phase 4: 回滾與測試 (v3.0.0)
16. [ ] rollback 指令
17. [ ] jobs/resume 指令
18. [ ] 單元測試完成
19. [ ] SQLite 整合測試完成
20. [ ] 文件完成

---

*架構設計 v1.0 - 2025-12-31*
