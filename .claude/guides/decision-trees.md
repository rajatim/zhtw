# 決策樹

## 使用者要求新增詞彙

```
使用者要求新增 "X" → "Y"
         │
         ▼
    "X" 是台灣不使用的用語嗎？
         │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  繼續      拒絕，說明原因
    │       （例：「權限」在台灣是正確用語）
    │
    ▼
  "Y" 在台灣常用嗎？
    │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  繼續      建議更好的翻譯
    │
    ▼
  "X" 是否為其他詞的子字串？
    │
    ┌────┴────┐
    是        否
    │         │
    ▼         ▼
  需要加入    直接新增到詞庫
  identity    執行 pytest
  mapping     確認通過
    │
    ▼
  找出包含 "X" 的台灣正確詞
  加入 identity mapping
  執行 pytest 確認通過
```

---

## 使用者報告誤判

```
使用者報告 "A" 被誤轉為 "B"
         │
         ▼
    檢查詞庫是否有 "A" → "B"
         │
    ┌────┴────┐
    有        沒有
    │         │
    ▼         ▼
  評估：      檢查：
  是否應該    是否為子字串問題
  移除此規則
    │         │
    ▼         ▼
  ┌────┴────┐    加入 identity
  是        否    mapping 保護
  │         │
  ▼         ▼
移除規則   加入例外
          或 identity
```

---

## 修改核心模組

```
要修改 converter.py / matcher.py / encoding.py
         │
         ▼
    1. 先 Read 完整檔案內容
         │
         ▼
    2. 理解現有邏輯
       （找出相關函式、追蹤資料流）
         │
         ▼
    3. 寫出修改計畫
       （告訴使用者你要改什麼）
         │
         ▼
    4. 執行修改
         │
         ▼
    5. 執行 pytest
         │
    ┌────┴────┐
  通過       失敗
    │         │
    ▼         ▼
  完成      分析錯誤
           修復後重測
```

---

## 新增 CLI 參數

```
要新增 CLI 參數
         │
         ▼
    1. 確認參數名稱和用途
         │
         ▼
    2. Read cli.py 找到對應的 command
         │
         ▼
    3. 加入 @click.option
       @click.option("--new-param", default=None, help="說明")
         │
         ▼
    4. 在函式簽名加入參數
       def check(path, new_param, ...):
         │
         ▼
    5. 實作邏輯
         │
         ▼
    6. 測試
       python -m zhtw check --help
       python -m zhtw check ./test --new-param value
         │
         ▼
    7. 如果需要，加入環境變數支援
       envvar="ZHTW_NEW_PARAM"
```

---

## 發布新版本

```
要發布新版本
         │
         ▼
    1. 確認所有測試通過
       pytest
         │
         ▼
    2. 更新版本號
       - src/zhtw/__init__.py
       - CLAUDE.md
         │
         ▼
    3. 更新 CHANGELOG.md
         │
         ▼
    4. 建立 commit
       git add -A
       git commit -m "chore: bump version to X.Y.Z"
         │
         ▼
    5. 建立 tag
       git tag -a vX.Y.Z -m "版本說明"
         │
         ▼
    6. 推送
       git push && git push --tags
         │
         ▼
    7. GitHub Release（如果需要）
       gh release create vX.Y.Z --notes "說明"
```

---

## 處理 Issue

```
GitHub Issue 進來
         │
         ▼
    Issue 類型？
         │
    ┌────┼────┬────┐
   Bug  功能  問題  其他
    │    │    │    │
    ▼    ▼    ▼    ▼
  排查  評估  回答  轉介
  修復  優先  問題  或關閉
        級
```

### Bug 處理流程

```
1. 重現問題
2. 找出根本原因
3. 寫測試案例（先失敗）
4. 修復
5. 確認測試通過
6. Commit（引用 Issue：Fixes #XX）
```

### 功能評估

```
1. 符合專案理念嗎？
2. 技術可行嗎？
3. 維護成本高嗎？
4. 使用者受益大嗎？

→ 記錄到 CLAUDE.md 的 GitHub Issues 表格
```
