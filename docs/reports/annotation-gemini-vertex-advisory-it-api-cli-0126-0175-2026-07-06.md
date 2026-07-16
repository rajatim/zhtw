<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：it-api-cli-0126-it-api-cli-0175（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0126-0175-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 34
- Differences from Codex draft: 16

## Maintainer Decision

Maintainer `tim` accepted the Gemini advisory version for all 16 differing cases
on 2026-07-06. The backlog was updated as follows:

- 34 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 16 differing cases use the Gemini advisory expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- Gemini is recorded under `review.ai_advisory`, not as a human
  `blind_reviewer`.
- All 50 cases are now `approved` and promotion-ready under the
  `single_human_with_ai_advisory_or_independent_blind_review` policy.

## Historical Maintainer Action

This was the action required before the decision above was applied:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### it-api-cli-0126：match

Input:

```text
幂等键可以避免重复扣款。
```

Codex draft expected:

```text
冪等鍵可以避免重複扣款。
```

Gemini advisory expected:

```text
冪等鍵可以避免重複扣款。
```

Gemini notes:

```text

```

### it-api-cli-0127：match

Input:

```text
请在请求中加入幂等键。
```

Codex draft expected:

```text
請在請求中加入冪等鍵。
```

Gemini advisory expected:

```text
請在請求中加入冪等鍵。
```

Gemini notes:

```text

```

### it-api-cli-0128：match

Input:

```text
重试策略使用指数退避。
```

Codex draft expected:

```text
重試策略使用指數退避。
```

Gemini advisory expected:

```text
重試策略使用指數退避。
```

Gemini notes:

```text

```

### it-api-cli-0129：different

Input:

```text
速率限制器会使用令牌桶算法。
```

Codex draft expected:

```text
速率限制器會使用權杖桶演算法。
```

Gemini advisory expected:

```text
速率限制器會使用令牌桶演算法。
```

Gemini notes:

```text

```

### it-api-cli-0130：different

Input:

```text
请把突发容量设置为二十。
```

Codex draft expected:

```text
請將突發容量設定為二十。
```

Gemini advisory expected:

```text
請把突發容量設定為二十。
```

Gemini notes:

```text

```

### it-api-cli-0131：match

Input:

```text
这个接口会返回当前速率限制。
```

Codex draft expected:

```text
這個介面會傳回目前速率限制。
```

Gemini advisory expected:

```text
這個介面會傳回目前速率限制。
```

Gemini notes:

```text

```

### it-api-cli-0132：match

Input:

```text
客户端收到 429 后应等待重试。
```

Codex draft expected:

```text
用戶端收到 429 後應等待重試。
```

Gemini advisory expected:

```text
用戶端收到 429 後應等待重試。
```

Gemini notes:

```text

```

### it-api-cli-0133：match

Input:

```text
响应头会包含重试时间。
```

Codex draft expected:

```text
回應標頭會包含重試時間。
```

Gemini advisory expected:

```text
回應標頭會包含重試時間。
```

Gemini notes:

```text

```

### it-api-cli-0134：match

Input:

```text
请不要缓存带有授权头的响应。
```

Codex draft expected:

```text
請不要快取帶有授權標頭的回應。
```

Gemini advisory expected:

```text
請不要快取帶有授權標頭的回應。
```

Gemini notes:

```text

```

### it-api-cli-0135：match

Input:

```text
缓存条目会根据租户隔离。
```

Codex draft expected:

```text
快取項目會根據租用戶隔離。
```

Gemini advisory expected:

```text
快取項目會根據租用戶隔離。
```

Gemini notes:

```text

```

### it-api-cli-0136：match

Input:

```text
租户标识必须写入审计记录。
```

Codex draft expected:

```text
租用戶識別碼必須寫入稽核記錄。
```

Gemini advisory expected:

```text
租用戶識別碼必須寫入稽核記錄。
```

Gemini notes:

```text

```

### it-api-cli-0137：match

Input:

```text
请确认服务账户具有最小权限。
```

Codex draft expected:

```text
請確認服務帳戶具有最小權限。
```

Gemini advisory expected:

```text
請確認服務帳戶具有最小權限。
```

Gemini notes:

```text

```

### it-api-cli-0138：match

Input:

```text
角色绑定会授予读取机密的权限。
```

Codex draft expected:

```text
角色繫結會授予讀取機密的權限。
```

Gemini advisory expected:

```text
角色繫結會授予讀取機密的權限。
```

Gemini notes:

```text

```

### it-api-cli-0139：different

Input:

```text
机密值不应写入配置文件。
```

Codex draft expected:

```text
機密值不應寫入設定檔。
```

Gemini advisory expected:

```text
機密值不應寫入組態檔。
```

Gemini notes:

```text

```

### it-api-cli-0140：different

Input:

```text
环境变量会覆盖默认配置。
```

Codex draft expected:

```text
環境變數會覆寫預設配置。
```

Gemini advisory expected:

```text
環境變數會覆寫預設組態。
```

Gemini notes:

```text

```

### it-api-cli-0141：different

Input:

```text
配置热重载会保留现有连接。
```

Codex draft expected:

```text
設定熱重新載入會保留現有連線。
```

Gemini advisory expected:

```text
組態熱重新載入會保留現有連線。
```

Gemini notes:

```text

```

### it-api-cli-0142：different

Input:

```text
请在变更配置后发送重载信号。
```

Codex draft expected:

```text
請在變更設定後傳送重新載入訊號。
```

Gemini advisory expected:

```text
請在變更組態後傳送重新載入訊號。
```

Gemini notes:

```text

```

### it-api-cli-0143：match

Input:

```text
健康检查端点不会访问数据库。
```

Codex draft expected:

```text
健康檢查端點不會存取資料庫。
```

Gemini advisory expected:

```text
健康檢查端點不會存取資料庫。
```

Gemini notes:

```text

```

### it-api-cli-0144：match

Input:

```text
就绪检查会确认依赖服务可用。
```

Codex draft expected:

```text
就緒檢查會確認相依服務可用。
```

Gemini advisory expected:

```text
就緒檢查會確認相依服務可用。
```

Gemini notes:

```text

```

### it-api-cli-0145：different

Input:

```text
存活探针失败时会重启容器。
```

Codex draft expected:

```text
存活探針失敗時會重新啟動容器。
```

Gemini advisory expected:

```text
存活探測失敗時會重新啟動容器。
```

Gemini notes:

```text

```

### it-api-cli-0146：match

Input:

```text
请将指标暴露在内部端口。
```

Codex draft expected:

```text
請將指標公開在內部連接埠。
```

Gemini advisory expected:

```text
請將指標公開在內部連接埠。
```

Gemini notes:

```text

```

### it-api-cli-0147：match

Input:

```text
指标标签会包含区域和版本。
```

Codex draft expected:

```text
指標標籤會包含區域和版本。
```

Gemini advisory expected:

```text
指標標籤會包含區域和版本。
```

Gemini notes:

```text

```

### it-api-cli-0148：different

Input:

```text
追踪上下文会通过请求头传播。
```

Codex draft expected:

```text
追蹤上下文會透過請求標頭傳播。
```

Gemini advisory expected:

```text
追蹤內容會透過請求標頭傳播。
```

Gemini notes:

```text

```

### it-api-cli-0149：different

Input:

```text
请把跨度编号写入日志。
```

Codex draft expected:

```text
請將跨度編號寫入記錄檔。
```

Gemini advisory expected:

```text
請將跨度編號寫入日誌。
```

Gemini notes:

```text

```

### it-api-cli-0150：match

Input:

```text
采样率可以通过启动参数调整。
```

Codex draft expected:

```text
取樣率可以透過啟動參數調整。
```

Gemini advisory expected:

```text
取樣率可以透過啟動參數調整。
```

Gemini notes:

```text

```

### it-api-cli-0151：match

Input:

```text
这个告警规则会检查错误率。
```

Codex draft expected:

```text
這個警示規則會檢查錯誤率。
```

Gemini advisory expected:

```text
這個警示規則會檢查錯誤率。
```

Gemini notes:

```text

```

### it-api-cli-0152：match

Input:

```text
请为高延迟请求建立告警。
```

Codex draft expected:

```text
請為高延遲請求建立警示。
```

Gemini advisory expected:

```text
請為高延遲請求建立警示。
```

Gemini notes:

```text

```

### it-api-cli-0153：match

Input:

```text
仪表盘会显示每分钟请求数。
```

Codex draft expected:

```text
儀表板會顯示每分鐘請求數。
```

Gemini advisory expected:

```text
儀表板會顯示每分鐘請求數。
```

Gemini notes:

```text

```

### it-api-cli-0154：different

Input:

```text
请在发布流水线中加入回滚步骤。
```

Codex draft expected:

```text
請在發布管線中加入復原步驟。
```

Gemini advisory expected:

```text
請在發佈管線中加入回復步驟。
```

Gemini notes:

```text

```

### it-api-cli-0155：match

Input:

```text
蓝绿部署会先切换少量流量。
```

Codex draft expected:

```text
藍綠部署會先切換少量流量。
```

Gemini advisory expected:

```text
藍綠部署會先切換少量流量。
```

Gemini notes:

```text

```

### it-api-cli-0156：different

Input:

```text
灰度发布会根据用户分组启用功能。
```

Codex draft expected:

```text
灰度發布會根據使用者分組啟用功能。
```

Gemini advisory expected:

```text
灰度發佈會根據使用者分組啟用功能。
```

Gemini notes:

```text

```

### it-api-cli-0157：match

Input:

```text
功能开关默认保持关闭。
```

Codex draft expected:

```text
功能開關預設保持關閉。
```

Gemini advisory expected:

```text
功能開關預設保持關閉。
```

Gemini notes:

```text

```

### it-api-cli-0158：match

Input:

```text
请在实验结束后删除开关。
```

Codex draft expected:

```text
請在實驗結束後刪除開關。
```

Gemini advisory expected:

```text
請在實驗結束後刪除開關。
```

Gemini notes:

```text

```

### it-api-cli-0159：match

Input:

```text
迁移任务会分批更新旧记录。
```

Codex draft expected:

```text
移轉任務會分批更新舊記錄。
```

Gemini advisory expected:

```text
移轉任務會分批更新舊記錄。
```

Gemini notes:

```text

```

### it-api-cli-0160：match

Input:

```text
请在迁移前创建快照。
```

Codex draft expected:

```text
請在移轉前建立快照。
```

Gemini advisory expected:

```text
請在移轉前建立快照。
```

Gemini notes:

```text

```

### it-api-cli-0161：different

Input:

```text
快照恢复会覆盖当前数据。
```

Codex draft expected:

```text
快照還原會覆寫目前資料。
```

Gemini advisory expected:

```text
快照復原會覆寫目前資料。
```

Gemini notes:

```text

```

### it-api-cli-0162：match

Input:

```text
备份任务会上传压缩包。
```

Codex draft expected:

```text
備份任務會上傳壓縮檔。
```

Gemini advisory expected:

```text
備份任務會上傳壓縮檔。
```

Gemini notes:

```text

```

### it-api-cli-0163：match

Input:

```text
归档文件会保留三十天。
```

Codex draft expected:

```text
封存檔案會保留三十天。
```

Gemini advisory expected:

```text
封存檔案會保留三十天。
```

Gemini notes:

```text

```

### it-api-cli-0164：different

Input:

```text
对象存储桶需要开启版本控制。
```

Codex draft expected:

```text
物件儲存桶需要開啟版本控制。
```

Gemini advisory expected:

```text
物件儲存貯體需要啟用版本控制。
```

Gemini notes:

```text

```

### it-api-cli-0165：different

Input:

```text
预签名链接会在一分钟后失效。
```

Codex draft expected:

```text
預先簽署連結會在一分鐘後失效。
```

Gemini advisory expected:

```text
預先簽章連結會在一分鐘後失效。
```

Gemini notes:

```text

```

### it-api-cli-0166：different

Input:

```text
请检查上传分片是否全部完成。
```

Codex draft expected:

```text
請檢查上傳分片是否全部完成。
```

Gemini advisory expected:

```text
請檢查上傳分段是否全部完成。
```

Gemini notes:

```text

```

### it-api-cli-0167：different

Input:

```text
这个 SDK 会自动续签凭证。
```

Codex draft expected:

```text
這個 SDK 會自動續簽憑證。
```

Gemini advisory expected:

```text
這個 SDK 會自動續約憑證。
```

Gemini notes:

```text

```

### it-api-cli-0168：match

Input:

```text
请在初始化客户端时传入区域。
```

Codex draft expected:

```text
請在初始化用戶端時傳入區域。
```

Gemini advisory expected:

```text
請在初始化用戶端時傳入區域。
```

Gemini notes:

```text

```

### it-api-cli-0169：match

Input:

```text
调用失败时会返回可重试错误。
```

Codex draft expected:

```text
呼叫失敗時會傳回可重試錯誤。
```

Gemini advisory expected:

```text
呼叫失敗時會傳回可重試錯誤。
```

Gemini notes:

```text

```

### it-api-cli-0170：match

Input:

```text
异步客户端会返回未来对象。
```

Codex draft expected:

```text
非同步用戶端會傳回未來物件。
```

Gemini advisory expected:

```text
非同步用戶端會傳回未來物件。
```

Gemini notes:

```text

```

### it-api-cli-0171：match

Input:

```text
请释放响应主体以复用连接。
```

Codex draft expected:

```text
請釋放回應主體以重複使用連線。
```

Gemini advisory expected:

```text
請釋放回應主體以重複使用連線。
```

Gemini notes:

```text

```

### it-api-cli-0172：match

Input:

```text
连接池会限制每个主机的并发数。
```

Codex draft expected:

```text
連線集區會限制每個主機的並行數。
```

Gemini advisory expected:

```text
連線集區會限制每個主機的並行數。
```

Gemini notes:

```text

```

### it-api-cli-0173：match

Input:

```text
请设置读取超时和连接超时。
```

Codex draft expected:

```text
請設定讀取逾時和連線逾時。
```

Gemini advisory expected:

```text
請設定讀取逾時和連線逾時。
```

Gemini notes:

```text

```

### it-api-cli-0174：match

Input:

```text
这个解析器会忽略未知字段。
```

Codex draft expected:

```text
這個剖析器會忽略未知欄位。
```

Gemini advisory expected:

```text
這個剖析器會忽略未知欄位。
```

Gemini notes:

```text

```

### it-api-cli-0175：match

Input:

```text
序列化器会保留空字符串。
```

Codex draft expected:

```text
序列化器會保留空字串。
```

Gemini advisory expected:

```text
序列化器會保留空字串。
```

Gemini notes:

```text

```
