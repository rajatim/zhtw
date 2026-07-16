<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：it-api-cli 0126-0175（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### it-api-cli-0126

Input:

```text
幂等键可以避免重复扣款。
```

AI draft expected:

```text
冪等鍵可以避免重複扣款。
```

Notes：付款 API 語境：幂等键→冪等鍵、重复→重複。

### it-api-cli-0127

Input:

```text
请在请求中加入幂等键。
```

AI draft expected:

```text
請在請求中加入冪等鍵。
```

Notes：付款/API 語境：请求→請求、幂等键→冪等鍵。

### it-api-cli-0128

Input:

```text
重试策略使用指数退避。
```

AI draft expected:

```text
重試策略使用指數退避。
```

Notes：可靠性語境：重试→重試、指数退避→指數退避。

### it-api-cli-0129

Input:

```text
速率限制器会使用令牌桶算法。
```

AI draft expected:

```text
速率限制器會使用權杖桶演算法。
```

Notes：限流語境：令牌桶→權杖桶、算法→演算法。

### it-api-cli-0130

Input:

```text
请把突发容量设置为二十。
```

AI draft expected:

```text
請將突發容量設定為二十。
```

Notes：限流設定語境：把→將、设置→設定。

### it-api-cli-0131

Input:

```text
这个接口会返回当前速率限制。
```

AI draft expected:

```text
這個介面會傳回目前速率限制。
```

Notes：API 語境：接口→介面、返回→傳回、当前→目前。

### it-api-cli-0132

Input:

```text
客户端收到 429 后应等待重试。
```

AI draft expected:

```text
用戶端收到 429 後應等待重試。
```

Notes：HTTP 語境：客户端→用戶端、后→後、重试→重試。

### it-api-cli-0133

Input:

```text
响应头会包含重试时间。
```

AI draft expected:

```text
回應標頭會包含重試時間。
```

Notes：HTTP 語境：响应头→回應標頭、重试→重試。

### it-api-cli-0134

Input:

```text
请不要缓存带有授权头的响应。
```

AI draft expected:

```text
請不要快取帶有授權標頭的回應。
```

Notes：HTTP 快取語境：缓存→快取、授权头→授權標頭、响应→回應。

### it-api-cli-0135

Input:

```text
缓存条目会根据租户隔离。
```

AI draft expected:

```text
快取項目會根據租用戶隔離。
```

Notes：多租戶語境：缓存条目→快取項目、租户→租用戶。

### it-api-cli-0136

Input:

```text
租户标识必须写入审计记录。
```

AI draft expected:

```text
租用戶識別碼必須寫入稽核記錄。
```

Notes：多租戶/稽核語境：租户标识→租用戶識別碼、审计记录→稽核記錄。

### it-api-cli-0137

Input:

```text
请确认服务账户具有最小权限。
```

AI draft expected:

```text
請確認服務帳戶具有最小權限。
```

Notes：IAM 語境：账户→帳戶、权限→權限。

### it-api-cli-0138

Input:

```text
角色绑定会授予读取机密的权限。
```

AI draft expected:

```text
角色繫結會授予讀取機密的權限。
```

Notes：Kubernetes/IAM 語境：绑定→繫結、读取→讀取、机密→機密。

### it-api-cli-0139

Input:

```text
机密值不应写入配置文件。
```

AI draft expected:

```text
機密值不應寫入設定檔。
```

Notes：資安設定語境：机密→機密、配置文件→設定檔。

### it-api-cli-0140

Input:

```text
环境变量会覆盖默认配置。
```

AI draft expected:

```text
環境變數會覆寫預設配置。
```

Notes：設定語境：环境变量→環境變數、覆盖→覆寫、默认配置→預設配置。

### it-api-cli-0141

Input:

```text
配置热重载会保留现有连接。
```

AI draft expected:

```text
設定熱重新載入會保留現有連線。
```

Notes：設定/服務語境：配置→設定、热重载→熱重新載入、连接→連線。

### it-api-cli-0142

Input:

```text
请在变更配置后发送重载信号。
```

AI draft expected:

```text
請在變更設定後傳送重新載入訊號。
```

Notes：系統服務語境：配置→設定、重载→重新載入、信号→訊號。

### it-api-cli-0143

Input:

```text
健康检查端点不会访问数据库。
```

AI draft expected:

```text
健康檢查端點不會存取資料庫。
```

Notes：健康檢查/API 語境：访问→存取、数据库→資料庫。

### it-api-cli-0144

Input:

```text
就绪检查会确认依赖服务可用。
```

AI draft expected:

```text
就緒檢查會確認相依服務可用。
```

Notes：Kubernetes readiness 語境：依赖服务→相依服務。

### it-api-cli-0145

Input:

```text
存活探针失败时会重启容器。
```

AI draft expected:

```text
存活探針失敗時會重新啟動容器。
```

Notes：Kubernetes liveness 語境：探针→探針、重启→重新啟動。

### it-api-cli-0146

Input:

```text
请将指标暴露在内部端口。
```

AI draft expected:

```text
請將指標公開在內部連接埠。
```

Notes：監控語境：暴露→公開、端口→連接埠。

### it-api-cli-0147

Input:

```text
指标标签会包含区域和版本。
```

AI draft expected:

```text
指標標籤會包含區域和版本。
```

Notes：監控語境：标签→標籤、区域→區域。

### it-api-cli-0148

Input:

```text
追踪上下文会通过请求头传播。
```

AI draft expected:

```text
追蹤上下文會透過請求標頭傳播。
```

Notes：Tracing 語境：追踪→追蹤、请求头→請求標頭、传播→傳播。

### it-api-cli-0149

Input:

```text
请把跨度编号写入日志。
```

AI draft expected:

```text
請將跨度編號寫入記錄檔。
```

Notes：Tracing 語境：span→跨度、编号→編號、日志→記錄檔。

### it-api-cli-0150

Input:

```text
采样率可以通过启动参数调整。
```

AI draft expected:

```text
取樣率可以透過啟動參數調整。
```

Notes：Tracing 語境：采样率→取樣率、通过→透過、启动参数→啟動參數。

### it-api-cli-0151

Input:

```text
这个告警规则会检查错误率。
```

AI draft expected:

```text
這個警示規則會檢查錯誤率。
```

Notes：監控告警語境：告警→警示、错误率→錯誤率。

### it-api-cli-0152

Input:

```text
请为高延迟请求建立告警。
```

AI draft expected:

```text
請為高延遲請求建立警示。
```

Notes：監控語境：延迟→延遲、请求→請求、告警→警示。

### it-api-cli-0153

Input:

```text
仪表盘会显示每分钟请求数。
```

AI draft expected:

```text
儀表板會顯示每分鐘請求數。
```

Notes：監控儀表板語境：仪表盘→儀表板、请求数→請求數。

### it-api-cli-0154

Input:

```text
请在发布流水线中加入回滚步骤。
```

AI draft expected:

```text
請在發布管線中加入復原步驟。
```

Notes：CI/CD 語境：发布流水线→發布管線、回滚→復原。

### it-api-cli-0155

Input:

```text
蓝绿部署会先切换少量流量。
```

AI draft expected:

```text
藍綠部署會先切換少量流量。
```

Notes：部署語境：蓝绿部署→藍綠部署、切换→切換。

### it-api-cli-0156

Input:

```text
灰度发布会根据用户分组启用功能。
```

AI draft expected:

```text
灰度發布會根據使用者分組啟用功能。
```

Notes：發布語境：用户→使用者、发布→發布。

### it-api-cli-0157

Input:

```text
功能开关默认保持关闭。
```

AI draft expected:

```text
功能開關預設保持關閉。
```

Notes：Feature flag 語境：默认→預設、关闭→關閉。

### it-api-cli-0158

Input:

```text
请在实验结束后删除开关。
```

AI draft expected:

```text
請在實驗結束後刪除開關。
```

Notes：Feature flag lifecycle 語境：删除→刪除、后→後。

### it-api-cli-0159

Input:

```text
迁移任务会分批更新旧记录。
```

AI draft expected:

```text
移轉任務會分批更新舊記錄。
```

Notes：資料移轉語境：迁移→移轉、任务→任務、记录→記錄。

### it-api-cli-0160

Input:

```text
请在迁移前创建快照。
```

AI draft expected:

```text
請在移轉前建立快照。
```

Notes：資料移轉語境：迁移→移轉、创建→建立。

### it-api-cli-0161

Input:

```text
快照恢复会覆盖当前数据。
```

AI draft expected:

```text
快照還原會覆寫目前資料。
```

Notes：備份語境：恢复→還原、覆盖→覆寫、当前数据→目前資料。

### it-api-cli-0162

Input:

```text
备份任务会上传压缩包。
```

AI draft expected:

```text
備份任務會上傳壓縮檔。
```

Notes：備份語境：任务→任務、上传→上傳、压缩包→壓縮檔。

### it-api-cli-0163

Input:

```text
归档文件会保留三十天。
```

AI draft expected:

```text
封存檔案會保留三十天。
```

Notes：儲存語境：归档文件→封存檔案。

### it-api-cli-0164

Input:

```text
对象存储桶需要开启版本控制。
```

AI draft expected:

```text
物件儲存桶需要開啟版本控制。
```

Notes：物件儲存語境：对象存储桶→物件儲存桶、开启→開啟。

### it-api-cli-0165

Input:

```text
预签名链接会在一分钟后失效。
```

AI draft expected:

```text
預先簽署連結會在一分鐘後失效。
```

Notes：物件儲存語境：预签名链接→預先簽署連結、后→後。

### it-api-cli-0166

Input:

```text
请检查上传分片是否全部完成。
```

AI draft expected:

```text
請檢查上傳分片是否全部完成。
```

Notes：分片上傳語境：上传→上傳、分片→分片。

### it-api-cli-0167

Input:

```text
这个 SDK 会自动续签凭证。
```

AI draft expected:

```text
這個 SDK 會自動續簽憑證。
```

Notes：SDK/auth 語境：续签→續簽、凭证→憑證。

### it-api-cli-0168

Input:

```text
请在初始化客户端时传入区域。
```

AI draft expected:

```text
請在初始化用戶端時傳入區域。
```

Notes：SDK 語境：客户端→用戶端、区域→區域。

### it-api-cli-0169

Input:

```text
调用失败时会返回可重试错误。
```

AI draft expected:

```text
呼叫失敗時會傳回可重試錯誤。
```

Notes：SDK/API 語境：调用→呼叫、返回→傳回、重试→重試。

### it-api-cli-0170

Input:

```text
异步客户端会返回未来对象。
```

AI draft expected:

```text
非同步用戶端會傳回未來物件。
```

Notes：SDK async 語境：异步→非同步、客户端→用戶端、返回→傳回、对象→物件。

### it-api-cli-0171

Input:

```text
请释放响应主体以复用连接。
```

AI draft expected:

```text
請釋放回應主體以重複使用連線。
```

Notes：HTTP client 語境：响应主体→回應主體、复用→重複使用、连接→連線。

### it-api-cli-0172

Input:

```text
连接池会限制每个主机的并发数。
```

AI draft expected:

```text
連線集區會限制每個主機的並行數。
```

Notes：HTTP client 語境：连接池→連線集區、并发→並行。

### it-api-cli-0173

Input:

```text
请设置读取超时和连接超时。
```

AI draft expected:

```text
請設定讀取逾時和連線逾時。
```

Notes：HTTP client 語境：设置→設定、读取→讀取、超时→逾時、连接→連線。

### it-api-cli-0174

Input:

```text
这个解析器会忽略未知字段。
```

AI draft expected:

```text
這個剖析器會忽略未知欄位。
```

Notes：解析器語境：解析器→剖析器、字段→欄位。

### it-api-cli-0175

Input:

```text
序列化器会保留空字符串。
```

AI draft expected:

```text
序列化器會保留空字串。
```

Notes：序列化語境：字符串→字串。
