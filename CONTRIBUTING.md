# Contributing to ZHTW

感謝你協助改善簡體中文轉台灣繁體中文的精準度、程式碼與文件。

## 開始之前

- 先搜尋現有 [Issues](https://github.com/rajatim/zhtw/issues)，避免重複工作。
- 大型功能、轉換策略或廣泛詞庫修改，請先開 Issue 說明案例與影響範圍。
- 安全漏洞不要開公開 Issue，請依 [Security Policy](SECURITY.md) 私下回報。
- 開發規則以專案根目錄的 [`AGENTS.md`](AGENTS.md) 為準。

## 精準度黃金規則

```text
1. 寧可少轉，不要錯轉
2. 不使用 OpenCC 作為執行期依賴
3. 不新增缺少台灣語境證據的廣泛詞彙
4. 詞庫修改後執行 validate 與 pytest
5. 必要時加入 identity mapping，保護正確子字串
6. benchmark expected 必須由 maintainer 確認，AI 只能提供建議
```

## 建立開發環境

推薦使用 `uv`：

```bash
uv sync --extra dev
uv run pytest
uv run ruff check .
uv run zhtw validate
```

也可以使用一般 Python 環境：

```bash
python3 -m pip install -e ".[dev]"
pytest
ruff check .
zhtw validate
```

## 修改詞庫

主要詞庫位於：

```text
src/zhtw/data/terms/
├── cn/       # 簡體與中國用語轉台灣繁體
├── hk/       # 香港用語轉台灣繁體
└── pending/  # 尚未正式納入的候選資料
```

新增或修改詞彙時：

1. 先確認來源詞於台灣語境中確實需要轉換。
2. 選擇最接近領域的 JSON 檔案，不要把所有規則都放進 `base.json`。
3. 裸詞具有多重語意時，改用完整語境或保護詞，不要強制單一答案。
4. 新增最小且能重現問題的測試，包含正向轉換與必要的過度轉換保護。
5. 執行 `uv run zhtw validate` 與完整 `uv run pytest`。

詞庫格式：

```json
{
  "terms": {
    "來源詞": "台灣用詞"
  }
}
```

不要在一般功能 PR 中修改版本號或產生 release artifacts。版本與所有 SDK 由 maintainer 透過 `make bump VERSION=X.Y.Z` 統一更新。

## 提供真實簡體中文用例

真實 input-only 語料會用於未來的新鮮 benchmark 與錯誤分析。請使用[專用投稿表單](https://github.com/rajatim/zhtw/issues/new?template=permissioned-user-report.yml)，每次提供 1 至 10 個由你原創或有權公開的完整句子。

請勿提供：

- 繁體 expected 或任何轉換器輸出
- 個資、客戶資料、憑證或未公開內容
- 無法確認授權的第三方文字

提交前請閱讀 [Permissioned User Report Consent v1](docs/benchmark/PERMISSIONED-USER-REPORT-CONSENT.md)。可分享的三語邀請文見[語料徵集說明](docs/benchmark/PERMISSIONED-USER-REPORT-INVITATION.md)。授權問題可先到 [Discussion #49](https://github.com/rajatim/zhtw/discussions/49) 詢問；Discussion 回覆不會自動視為投稿同意。

## 回報轉換問題

請開 [Issue](https://github.com/rajatim/zhtw/issues) 並提供：

- 使用的 zhtw 版本與 ambiguity mode
- 完整且最小的輸入文字
- 實際結果
- 你建議的台灣繁體結果與理由或參考來源
- 這項修改可能造成過度轉換的反例

不要只提供沒有語境的單一歧義詞。

## Pull Request 檢查清單

- 修改範圍集中，沒有無關的格式化或版本變動。
- 新行為有測試，既有測試全部通過。
- 詞庫修改已通過 `zhtw validate`。
- 新文件與註解使用自然的台灣繁體中文或清楚的英文。
- 沒有提交私有 benchmark expected、憑證、個資或授權不明內容。
- PR 說明列出測試指令與結果。

## AI 輔助開發

本專案允許使用 OpenAI Codex、Anthropic Claude 與其他 AI 工具協助開發。所有工具都應先讀取 [`AGENTS.md`](AGENTS.md)，不要依賴只有單一工具能讀取的私有規則。

使用 AI 協助時，貢獻者仍必須：

- 理解、檢查並測試提交的每一項變更。
- 對程式碼、授權、安全與精準度負責。
- 不把私有 expected、未公開語料、憑證或敏感資料傳給未經專案允許的外部服務。
- 不把 AI 產生的翻譯或 expected 直接當作 benchmark ground truth。
- 只使用真實且可驗證的 GitHub 身分作為 commit 作者或共同作者。

專案的 AI 開發協助記錄在[致謝文件](docs/reference/ACKNOWLEDGMENTS.md)。

## 行為準則

- 保持尊重並專注於可驗證的技術與語言問題。
- 對台灣用語有不同看法時，提供完整語境、來源與反例。
- 不因工具、模型或個人偏好取代測試與人工判斷。
