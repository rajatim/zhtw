<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：mixed-ambiguity-0001-mixed-ambiguity-0025（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 25
- Exact matches with Codex draft: 18
- Differences from Codex draft: 7

## Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### mixed-ambiguity-0001：match

Input:

```text
这个程序会自动退出。
```

Codex draft expected:

```text
這個程式會自動結束。
```

Gemini advisory expected:

```text
這個程式會自動結束。
```

Gemini notes:

```text
「程序」(program) 轉為「程式」；「退出」(exit) 轉為「結束」。
```

### mixed-ambiguity-0002：different

Input:

```text
会议程序已经排好。
```

Codex draft expected:

```text
會議程序已經排好。
```

Gemini advisory expected:

```text
會議議程已經排好了。
```

Gemini notes:

```text
「程序」(agenda) 轉為「議程」。
```

### mixed-ambiguity-0003：match

Input:

```text
请打开这个文件。
```

Codex draft expected:

```text
請開啟這個檔案。
```

Gemini advisory expected:

```text
請開啟這個檔案。
```

Gemini notes:

```text
「打开」(open) 轉為「開啟」；「文件」(computer file) 轉為「檔案」。
```

### mixed-ambiguity-0004：match

Input:

```text
请提交证明文件。
```

Codex draft expected:

```text
請提交證明文件。
```

Gemini advisory expected:

```text
請提交證明文件。
```

Gemini notes:

```text
「文件」(document) 維持「文件」。
```

### mixed-ambiguity-0005：match

Input:

```text
这个对象包含三个字段。
```

Codex draft expected:

```text
這個物件包含三個欄位。
```

Gemini advisory expected:

```text
這個物件包含三個欄位。
```

Gemini notes:

```text
「对象」(programming object) 轉為「物件」；「字段」(field) 轉為「欄位」。
```

### mixed-ambiguity-0006：match

Input:

```text
研究对象需要签署同意书。
```

Codex draft expected:

```text
研究對象需要簽署同意書。
```

Gemini advisory expected:

```text
研究對象需要簽署同意書。
```

Gemini notes:

```text
「对象」(subject) 維持「對象」。
```

### mixed-ambiguity-0007：different

Input:

```text
技术支持会协助排查。
```

Codex draft expected:

```text
技術支援會協助排查。
```

Gemini advisory expected:

```text
技術支援會協助排除問題。
```

Gemini notes:

```text
「技术支持」(technical support) 轉為「技術支援」；「排查」(troubleshoot) 轉為「排除問題」。
```

### mixed-ambiguity-0008：match

Input:

```text
这份证据支持他的说法。
```

Codex draft expected:

```text
這份證據支持他的說法。
```

Gemini advisory expected:

```text
這份證據支持他的說法。
```

Gemini notes:

```text
「支持」(support a claim) 維持「支持」。
```

### mixed-ambiguity-0009：different

Input:

```text
后台服务正在重启。
```

Codex draft expected:

```text
背景服務正在重新啟動。
```

Gemini advisory expected:

```text
後端服務正在重新啟動。
```

Gemini notes:

```text
「后台」(backend) 轉為「後端」；「重启」(restart) 轉為「重新啟動」。
```

### mixed-ambiguity-0010：match

Input:

```text
她在后台准备上场。
```

Codex draft expected:

```text
她在後台準備上場。
```

Gemini advisory expected:

```text
她在後台準備上場。
```

Gemini notes:

```text
「后台」(backstage) 維持「後台」。
```

### mixed-ambiguity-0011：different

Input:

```text
接口返回空数组。
```

Codex draft expected:

```text
介面回傳空陣列。
```

Gemini advisory expected:

```text
介面傳回空陣列。
```

Gemini notes:

```text
「接口」(interface/API) 轉為「介面」；「返回」(return data) 轉為「傳回」；「数组」(array) 轉為「陣列」。
```

### mixed-ambiguity-0012：match

Input:

```text
海关窗口今天暂停服务。
```

Codex draft expected:

```text
海關窗口今天暫停服務。
```

Gemini advisory expected:

```text
海關窗口今天暫停服務。
```

Gemini notes:

```text
「窗口」(service window) 維持「窗口」。
```

### mixed-ambiguity-0013：match

Input:

```text
服务端口被占用。
```

Codex draft expected:

```text
服務連接埠被佔用。
```

Gemini advisory expected:

```text
服務連接埠被佔用。
```

Gemini notes:

```text
「端口」(port) 轉為「連接埠」。
```

### mixed-ambiguity-0014：match

Input:

```text
港口今天暂停开放。
```

Codex draft expected:

```text
港口今天暫停開放。
```

Gemini advisory expected:

```text
港口今天暫停開放。
```

Gemini notes:

```text
「港口」(harbor/port) 維持「港口」。
```

### mixed-ambiguity-0015：match

Input:

```text
线程阻塞会影响性能。
```

Codex draft expected:

```text
執行緒阻塞會影響效能。
```

Gemini advisory expected:

```text
執行緒阻塞會影響效能。
```

Gemini notes:

```text
「线程」(thread) 轉為「執行緒」；「性能」(performance) 轉為「效能」。
```

### mixed-ambiguity-0016：match

Input:

```text
道路阻塞会影响通行。
```

Codex draft expected:

```text
道路阻塞會影響通行。
```

Gemini advisory expected:

```text
道路阻塞會影響通行。
```

Gemini notes:

```text
「阻塞」(blockage) 維持「阻塞」。
```

### mixed-ambiguity-0017：match

Input:

```text
缓存命中率下降。
```

Codex draft expected:

```text
快取命中率下降。
```

Gemini advisory expected:

```text
快取命中率下降。
```

Gemini notes:

```text
「缓存」(cache) 轉為「快取」。
```

### mixed-ambiguity-0018：different

Input:

```text
他缓存了那张照片。
```

Codex draft expected:

```text
他快取了那張照片。
```

Gemini advisory expected:

```text
他將那張照片快取起來了。
```

Gemini notes:

```text
「缓存」(to cache) 轉為「快取起來」。
```

### mixed-ambiguity-0019：match

Input:

```text
项目经理更新了排程。
```

Codex draft expected:

```text
專案經理更新了排程。
```

Gemini advisory expected:

```text
專案經理更新了排程。
```

Gemini notes:

```text
「项目」(project) 轉為「專案」。
```

### mixed-ambiguity-0020：different

Input:

```text
补助项目明天截止。
```

Codex draft expected:

```text
補助計畫明天截止。
```

Gemini advisory expected:

```text
補助項目明天截止。
```

Gemini notes:

```text
「项目」(item/program) 維持「項目」。
```

### mixed-ambiguity-0021：different

Input:

```text
服务器返回状态码。
```

Codex draft expected:

```text
伺服器回傳狀態碼。
```

Gemini advisory expected:

```text
伺服器傳回狀態碼。
```

Gemini notes:

```text
「服务器」(server) 轉為「伺服器」；「返回」(return data) 轉為「傳回」。
```

### mixed-ambiguity-0022：match

Input:

```text
他返回家乡工作。
```

Codex draft expected:

```text
他返回家鄉工作。
```

Gemini advisory expected:

```text
他返回家鄉工作。
```

Gemini notes:

```text
「返回」(return to a place) 維持「返回」。
```

### mixed-ambiguity-0023：match

Input:

```text
这个入口会跳转到登录页。
```

Codex draft expected:

```text
這個入口會跳轉到登入頁。
```

Gemini advisory expected:

```text
這個入口會跳轉到登入頁。
```

Gemini notes:

```text
「登录页」(login page) 轉為「登入頁」。
```

### mixed-ambiguity-0024：match

Input:

```text
捷运入口在便利店旁边。
```

Codex draft expected:

```text
捷運入口在便利商店旁邊。
```

Gemini advisory expected:

```text
捷運入口在便利商店旁邊。
```

Gemini notes:

```text
「便利店」(convenience store) 轉為「便利商店」。
```

### mixed-ambiguity-0025：match

Input:

```text
数据表字段不能重复。
```

Codex draft expected:

```text
資料表欄位不能重複。
```

Gemini advisory expected:

```text
資料表欄位不能重複。
```

Gemini notes:

```text
「数据表」(data table) 轉為「資料表」；「字段」(field) 轉為「欄位」。
```
