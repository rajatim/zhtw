<!-- zhtw:disable -->
# Blind-v2 Permissioned User Report Intake Readiness

日期：2026-07-23

## 結論

第一批 permissioned-user-report 的收集與 fail-closed 驗證管線已可使用，目前為
`collecting` 0/100。這不是已取得 100 筆資料，也不增加現有 611 筆 candidate pool。

## 已完成

- GitHub issue form：`.github/ISSUE_TEMPLATE/permissioned-user-report.yml`
- 同意與資料治理條款：`docs/benchmark/PERMISSIONED-USER-REPORT-CONSENT.md`
- 100 筆收集模板：
  `benchmarks/accuracy/sources/permissioned-user-report-batch-001.json`
- JSON Schema：
  `benchmarks/accuracy/blind-v2.permissioned-user-report-source.schema.json`
- 收集驗證器：`scripts/validate_permissioned_user_reports.py`
- GitHub issue 預覽／確認匯入器：
  `scripts/import_permissioned_user_report_issue.py`。預設 dry-run；只有明確提供
  `--write`、maintainer 與含時區 review timestamp 才會原子寫入。
- Blind-v2 importer 已支援 `permissioned-user-report-batch-NNN`，但只有
  `ready_for_import` 且恰好 100 筆時才接受。
- 測試涵蓋 collecting/ready 狀態、100 筆門檻、input-only、同意欄位、來源 ID、
  normalized duplicate、敏感資料模式、GitHub form parsing、dry-run 與 atomic write。

## 收集規則

1. 每個 input 必須來自公開 `rajatim/zhtw` GitHub issue，並保存 issue URL、提交時間
   與 `permissioned-user-report-v1` consent。
2. 只保存簡體中文 input；不得保存 expected、可接受答案、annotation 或任何轉換器
   output。
3. Issue 內的 context 只協助理解來源，不匯入，也不直接當作 domain/risk 真值。
4. 自動敏感資料偵測只是最低門檻；maintainer 仍須閱讀原句。命中時拒絕並請提交者
   另送已自行去識別的新句，不由工具靜默遮罩或改寫。
5. 收滿 100 筆並人工完成來源／敏感資料檢查後，才可把狀態改為
   `ready_for_import`。
6. 每筆保存 maintainer、review timestamp、`accepted` decision 與 reviewed issue
   body SHA-256。Issue 後續若被編輯，仍可辨認當時核准的公開內容。

## 驗證指令

收集中：

```bash
make benchmark-blind-v2-permissioned-intake-check
```

收到 issue 後先預覽，不修改 collection：

```bash
make benchmark-blind-v2-permissioned-issue-preview ISSUE=123
```

Maintainer 讀過原始 issue 並接受全部 proposed inputs 後才寫入：

```bash
make benchmark-blind-v2-permissioned-issue-import \
  ISSUE=123 \
  MAINTAINER=tim \
  REVIEWED_AT=2026-07-23T17:00:00+08:00
```

收滿 100 筆後：

```bash
make benchmark-blind-v2-permissioned-ready-check
```

## 匯入後流程

通過 ready gate 只代表資料格式、同意與基本安全條件合格。後續仍依固定順序執行：

1. Codex 先做 input-only eligibility/domain/risk 建議。
2. Gemini 不看 Codex 結論，獨立 review。
3. Codex 彙整一致、差異與低信心案例。
4. Maintainer 確認必要案例；AI 輸出不直接成為 ground truth。
5. 通過 exact/reference 與 character 5-gram Jaccard 0.85 near-dedupe 後，才可重建
   collecting candidate pool。

## 尚未完成

- 尚無 permissioned inputs，進度為 0/100。
- 尚未建立 batch 001 manifest 與 normalized external dataset；這兩項只在 100 筆
  ready gate 通過後建立，避免把未完成批次誤當可用來源。
- 尚未進行 Codex/Gemini/maintainer source classification。
