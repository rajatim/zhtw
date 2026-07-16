# Accuracy Ground-truth Corrections（2026-07-16）

## 決策

Maintainer 指示依 expert review 全部修正。本次重新裁決 3 筆已公開案例；歷史 AI
原始報告保持不變，目前 annotation backlog、public regression 與產品詞庫同步修正。

Approval policy：`single_human_with_ai_advisory_and_authoritative_sources`。

## 修正

| Case | 修正理由 | 依據 |
|---|---|---|
| `it-api-cli-0043` | rollback 是復原／回復，不是 trace-back「回溯」 | [Microsoft Learn](https://learn.microsoft.com/zh-tw/windows-server/administration/windows-commands/scwcmd-rollback) |
| `it-api-cli-0170` | `future` 是程式型別名稱，不直譯成時間意義的「未來物件」 | [Microsoft Learn](https://learn.microsoft.com/zh-tw/cpp/standard-library/future-class?view=msvc-170) |
| `social-daily-0038` | 物業管理單位與管委會是不同組織，不可互換 | [內政部研究資料](https://ws.moi.gov.tw/Download.ashx?n=Y29tcGxldGUucGRm&u=LzAwMS9VcGxvYWQvT2xkRmlsZV9BYnJpX0dvdi9yZXNlYXJjaC83MjEvMTQ0NzkyOTgzNzEucGRm) |

## 稽核政策

- 不回寫歷史 AI advisory 或 promotion gate，避免抹除當時決策。
- Regression case 的 source report 改指向本修正報告。
- 修正後仍須通過 exact match、target idempotency 與完整 release gates。
