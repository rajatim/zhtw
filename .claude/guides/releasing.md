# ZHTW 版本發佈 SOP

> 版本發佈標準作業流程，確保每次發佈品質一致。

---

## 📝 必改檔案清單

### 🔴 必改（每次發佈都要改）

| 檔案 | 修改內容 | 範例 |
|------|----------|------|
| `pyproject.toml` | `version = "X.Y.Z"` | `version = "2.8.0"` |
| `src/zhtw/__init__.py` | `__version__ = "X.Y.Z"` | `__version__ = "2.8.0"` |
| `CHANGELOG.md` | 新增版本區塊 | `## [2.8.0] - 2026-01-04` |

### 🟡 視情況改（有相關變更才改）

| 檔案 | 何時需要改 | 負責專家 |
|------|------------|----------|
| `README.md` | 新增功能、使用方式變更 | 📣 行銷專家 |
| `README.md` 徽章 | 新增 CI/品質徽章 | 📣 行銷專家 |
| `CLAUDE.md` | AI 開發指南變更 | 📝 技術文件 |
| `.claude/guides/*.md` | 開發流程變更 | 📝 技術文件 |
| `pyproject.toml` 依賴 | 新增/更新依賴 | 📦 發佈工程師 |

### 🟢 自動更新（不用手動改）

| 檔案 | 說明 |
|------|------|
| `git tag` | 發佈流程建立（Jenkins 或手動） |
| PyPI | Jenkins 或 GitHub Actions 自動發佈 |

---

## 🔀 發佈方式選擇

| 方式 | 適用情境 | 優點 |
|------|----------|------|
| **Jenkins（推薦）** | 正式發佈 | 人工審核、Slack 通知、完整驗證 |
| GitHub Actions | 緊急修復、Jenkins 不可用時 | 快速、無需額外設定 |

### Jenkins Pipeline 位置

```
jenkins-cicd-infrastructure/pipelines/zhtw-release.groovy
```

Jenkins URL: `https://cicd.rajatim.com`

---

## 🔍 發佈前檢查

### 1️⃣ 程式碼品質（QA 工程師）

| 檢查項目 | 指令 | 通過標準 |
|----------|------|----------|
| 單元測試 | `pytest` | 全部通過（目前 208+） |
| 測試覆蓋率 | `pytest --cov` | >80% |
| Lint 檢查 | `ruff check .` | 無錯誤 |
| 格式檢查 | `ruff format --check .` | 無問題 |

### 2️⃣ 詞庫品質（領域專家）

| 檢查項目 | 指令 | 通過標準 |
|----------|------|----------|
| 詞庫衝突 | `zhtw validate` | 無衝突 |
| 準確度測試 | 參考 `deep-testing.md` | >95% |
| 詞條統計 | `zhtw stats` | 記錄數量變化 |

### 3️⃣ 版本一致性（發佈工程師）

```bash
# 確認三處版本號一致
grep 'version' pyproject.toml | head -1
grep '__version__' src/zhtw/__init__.py
head -20 CHANGELOG.md | grep '## \['
```

### 4️⃣ 相容性（相容性專家）

| 檢查項目 | 方法 |
|----------|------|
| Python 3.9+ | CI 自動測試（3.9, 3.11, 3.12） |
| macOS/Linux | CI 在 ubuntu-latest 測試 |
| 依賴版本 | `pip list --outdated` |

### 5️⃣ 安全性（資安專家）

| 檢查項目 | 指令/方法 |
|----------|-----------|
| 依賴漏洞 | `pip-audit` 或 `safety check` |
| 敏感資訊 | 確認無 API key/密碼提交 |
| .gitignore | 確認敏感檔案已排除 |

### 6️⃣ 文件完整性（技術文件）

| 檔案 | 檢查項目 |
|------|----------|
| `CHANGELOG.md` | 本版變更已記錄 |
| `README.md` | 功能說明正確 |
| CLI help | `zhtw --help` 各指令說明正確 |

### 6️⃣+ README 行銷檢查（行銷專家）

有新功能時，確認 README 符合以下標準：

| 檢查項目 | 說明 |
|----------|------|
| **價值主張清晰** | 一句話說明產品解決什麼問題 |
| **功能亮點更新** | 新功能有列出並說明效益 |
| **使用範例具體** | 有實際指令和輸出範例 |
| **數據佐證** | 詞庫規模、準確率等具體數字 |
| **安裝簡單** | pip install 指令清楚 |
| **快速上手** | 30 秒內能跑出第一個結果 |
| **徽章更新** | 確認徽章正確且有效 |

#### 徽章檢查清單

```markdown
# 目前使用的徽章（9 個）
[![CI](https://github.com/rajatim/zhtw/actions/workflows/ci.yml/badge.svg)]
[![codecov](https://codecov.io/gh/rajatim/zhtw/branch/main/graph/badge.svg)]
[![PyPI](https://img.shields.io/pypi/v/zhtw.svg)]
[![Downloads](https://img.shields.io/pypi/dm/zhtw.svg)]
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)]
[![Ruff](https://img.shields.io/endpoint?url=...)]
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)]
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)]
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]
```

| 徽章 | 用途 | 何時更新 |
|------|------|----------|
| CI | 顯示測試狀態 | workflow 檔名變更時 |
| Codecov | 測試覆蓋率 | 自動更新 |
| PyPI | 顯示最新版本 | 自動更新 |
| Downloads | 月下載量 | 自動更新 |
| Python | 支援的 Python 版本 | pyproject.toml requires-python 變更時 |
| Ruff | 程式碼風格 | 不需更新 |
| pre-commit | 開發品質 | 不需更新 |
| Bandit | SAST 安全掃描 | 不需更新 |
| License | 授權類型 | 授權變更時 |

#### README 結構建議

```markdown
# 產品名稱 + 一句話價值主張

## 亮點功能（3-5 個 bullet points）

## 快速開始（安裝 + 第一個指令）

## 使用範例（常見情境）

## 功能說明（詳細）

## 安裝與設定
```

### 7️⃣ 功能驗證（使用者體驗）

| 測試項目 | 方法 |
|----------|------|
| 新功能 | 手動測試所有新增功能 |
| 回歸測試 | 確認現有功能正常 |
| 錯誤訊息 | 觸發錯誤情境，確認訊息友善 |
| CLI 操作 | 各指令實際執行一次 |

### 8️⃣ 效能驗證（效能專家）

| 測試項目 | 方法 | 基準 |
|----------|------|------|
| 掃描速度 | 對 1000+ 檔案目錄計時 | <10s |
| 記憶體使用 | 大檔案不 OOM | <500MB |
| 無效能退化 | 與前版比較 | ±10% |

---

## ✅ 發佈 Checklist 範本

每次發佈前複製使用：

```markdown
## vX.Y.Z 發佈檢查

### 版本號同步（全部要一致！）
- [ ] `pyproject.toml` → version = "X.Y.Z"
- [ ] `src/zhtw/__init__.py` → __version__ = "X.Y.Z"
- [ ] `CHANGELOG.md` → ## [X.Y.Z] - YYYY-MM-DD

### 程式碼品質
- [ ] `pytest` 全部通過
- [ ] `ruff check .` 無錯誤
- [ ] `zhtw validate` 無衝突

### 功能驗證
- [ ] 新功能手動測試通過
- [ ] 現有功能無 regression
- [ ] `zhtw --help` 說明正確

### 文件
- [ ] CHANGELOG.md 已更新
- [ ] README.md 已更新（如有新功能）
  - [ ] 功能亮點有列出
  - [ ] 使用範例正確
  - [ ] 數據（詞庫規模等）正確

### 最終確認
- [ ] `git status` 無未提交變更
- [ ] `python3 -m zhtw --version` 顯示正確版本
```

---

## 🚀 發佈流程

### Step 1: 更新版本號（共通）

```bash
# 編輯這三個檔案，確保版本號一致
# 1. pyproject.toml
# 2. src/zhtw/__init__.py
# 3. CHANGELOG.md
```

### Step 2: 提交版本變更（共通）

```bash
git add pyproject.toml src/zhtw/__init__.py CHANGELOG.md
git commit -m "chore: release vX.Y.Z"
git push
```

---

### 方式 A: Jenkins 發佈（推薦）

```
1. 前往 Jenkins: https://cicd.rajatim.com
2. 找到 Job: zhtw-release
3. 點擊 Build Now
4. Jenkins 自動執行所有發佈步驟
```

**Jenkins Credentials 需求：**

| Credential ID | 類型 | 用途 |
|---------------|------|------|
| `github-credentials` | Username/Password (PAT) | Git push tag、gh CLI |
| `pypi-token` | Secret text | PyPI API Token |
| `slack-webhook` | — | 由 notifyService 使用 |

**Pipeline 執行內容：**

| Stage | 說明 |
|-------|------|
| Checkout | 從 GitHub clone main |
| Version Check | 驗證 3 檔案版本一致、tag 不存在 |
| Setup | 建立 Python venv（`/tmp/zhtw-venv-$BUILD_NUMBER`） |
| Validate | pytest / ruff / zhtw validate（平行執行） |
| Build | `python -m build` 產生 dist/ |
| **Approval** | ⏸️ 人工確認（顯示 CHANGELOG，Slack 通知） |
| Publish to PyPI | `twine upload dist/*` |
| GitHub Release | `git tag` + `gh release create` |
| Verify | `pip index versions zhtw` 確認已上架 |
| Badge Health | 驗證 PyPI/CI 徽章內容正確 |

**Slack 通知：**

| 時機 | 頻道 | 內容 |
|------|------|------|
| Approval 等待 | #pipeline | 版本號、CHANGELOG、審核連結 |
| 發佈成功 | #pipeline | 版本號、PyPI/GitHub/Jenkins 連結 |
| 發佈失敗 | #pipeline | 版本號、Console 連結 |

---

### 方式 B: GitHub Actions 發佈（備用）

適用：Jenkins 不可用、緊急修復

```bash
# Step 3: 建立 Tag
git tag -a vX.Y.Z -m "vX.Y.Z: 簡短說明"
git push origin vX.Y.Z

# Step 4: 建立 GitHub Release
gh release create vX.Y.Z \
  --title "vX.Y.Z: 標題" \
  --notes "變更內容（可從 CHANGELOG 複製）"
```

這會自動觸發 `.github/workflows/publish.yml` 發佈到 PyPI。

---

## ✅ 發佈後驗證

### Jenkins 發佈（自動驗證）

Jenkins Pipeline 的 Verify 和 Badge Health stage 已自動驗證：
- ✅ PyPI 已上架（`pip index versions`）
- ✅ PyPI 徽章顯示正確版本
- ✅ CI 徽章狀態為 passing

**手動確認（可選）：**

| 項目 | 方法 |
|------|------|
| 安裝測試 | `pip install zhtw==X.Y.Z` |
| 版本確認 | `zhtw --version` |
| 基本功能 | `zhtw check .` |

### GitHub Actions 發佈（手動驗證）

| 項目 | 方法 |
|------|------|
| GitHub Actions | 確認 publish workflow 成功（綠勾） |
| PyPI 頁面 | https://pypi.org/project/zhtw/ 版本正確 |
| 安裝測試 | `pip install zhtw==X.Y.Z` |
| 版本確認 | `zhtw --version` 顯示正確 |
| 基本功能 | `zhtw check .` 正常執行 |

---

## 🔧 常見問題

### Q: 忘記更新 `__init__.py` 怎麼辦？

已發佈的版本無法修改。下個版本記得同步更新。

### Q: Tag 打錯怎麼辦？

```bash
# 刪除本機 tag
git tag -d vX.Y.Z

# 刪除遠端 tag
git push origin :refs/tags/vX.Y.Z

# 重新建立
git tag -a vX.Y.Z -m "訊息"
git push origin vX.Y.Z
```

### Q: PyPI 發佈失敗怎麼辦？

1. 檢查 GitHub Actions 錯誤訊息
2. 確認 `PYPI_API_TOKEN` secret 有效
3. 確認版本號未被佔用（PyPI 不允許覆蓋）

### Q: Jenkins 顯示「Tag vX.Y.Z 已存在」怎麼辦？

表示該版本已發佈過。需要更新版本號：

1. 修改 `pyproject.toml`、`__init__.py`、`CHANGELOG.md`
2. `git commit && git push`
3. 重新觸發 Jenkins job

### Q: Jenkins Badge Health 失敗怎麼辦？

Badge Health 驗證 SVG 內容，可能原因：

| 問題 | 原因 | 解法 |
|------|------|------|
| PyPI 徽章版本不對 | CDN 快取延遲 | 等 1-2 分鐘後 Retry |
| CI 徽章非 passing | main 有失敗的 commit | 修復 CI 後重新發佈 |

### Q: Jenkins Approval 沒收到 Slack 通知？

檢查：
1. `notifyService` 是否正確設定
2. Slack webhook 是否有效
3. Jenkins console 有無錯誤訊息

即使通知失敗，仍可在 Jenkins UI 手動審核。

---

## 📊 版本號規則（Semantic Versioning）

| 變更類型 | 版本位置 | 範例 |
|----------|----------|------|
| 重大變更（破壞性） | MAJOR | 2.0.0 → 3.0.0 |
| 新功能（向下相容） | MINOR | 2.7.0 → 2.8.0 |
| Bug 修正 | PATCH | 2.7.0 → 2.7.1 |

---

*最後更新：2026-01-04（Jenkins Pipeline 完整文件化）*
