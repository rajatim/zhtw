<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：it-api-cli-0076-it-api-cli-0125（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0076-0125-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 24
- Differences from Codex draft: 26

## Maintainer Decision

Maintainer `tim` accepted the Codex draft version for all 26 differing cases on
2026-07-06. The backlog was updated as follows:

- 24 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 26 differing cases use the Codex draft expected output with
  `expected_source = "human_adjudication"` and `adjudicator = "tim"`.
- Gemini is recorded under `review.ai_advisory` with `decision = "rejected"` for
  the 26 differing cases; it is not recorded as a human `blind_reviewer`.
- All 50 cases are now `approved` and promotion-ready under the
  `single_human_with_ai_advisory_or_independent_blind_review` policy.

## Historical Maintainer Action

This was the action required before the decision above was applied:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### it-api-cli-0076：match

Input:

```text
请在响应头中加入缓存控制字段。
```

Codex draft expected:

```text
請在回應標頭中加入快取控制欄位。
```

Gemini advisory expected:

```text
請在回應標頭中加入快取控制欄位。
```

Gemini notes:

```text
「响应头」轉為「回應標頭」，「缓存」轉為「快取」，「字段」轉為「欄位」。
```

### it-api-cli-0077：match

Input:

```text
这个端点会返回剩余配额。
```

Codex draft expected:

```text
這個端點會傳回剩餘配額。
```

Gemini advisory expected:

```text
這個端點會傳回剩餘配額。
```

Gemini notes:

```text
「这个」轉為「這個」，「返回」轉為「傳回」，「剩余」轉為「剩餘」。
```

### it-api-cli-0078：different

Input:

```text
回调地址必须使用 HTTPS。
```

Codex draft expected:

```text
回呼位址必須使用 HTTPS。
```

Gemini advisory expected:

```text
回呼網址必須使用 HTTPS。
```

Gemini notes:

```text
「回调地址」轉為「回呼網址」，「必须」轉為「必須」。
```

### it-api-cli-0079：different

Input:

```text
请验证请求签名和时间戳。
```

Codex draft expected:

```text
請驗證要求簽章和時間戳記。
```

Gemini advisory expected:

```text
請驗證請求簽章和時間戳記。
```

Gemini notes:

```text
「请」轉為「請」，「验证」轉為「驗證」，「签名」轉為「簽章」，「时间戳」轉為「時間戳記」。
```

### it-api-cli-0080：match

Input:

```text
客户端会自动刷新访问令牌。
```

Codex draft expected:

```text
用戶端會自動重新整理存取權杖。
```

Gemini advisory expected:

```text
用戶端會自動重新整理存取權杖。
```

Gemini notes:

```text
「客户端」轉為「用戶端」，「刷新」轉為「重新整理」，「访问令牌」轉為「存取權杖」。
```

### it-api-cli-0081：match

Input:

```text
如果刷新失败，请重新登录。
```

Codex draft expected:

```text
如果重新整理失敗，請重新登入。
```

Gemini advisory expected:

```text
如果重新整理失敗，請重新登入。
```

Gemini notes:

```text
「刷新」轉為「重新整理」，「请」轉為「請」，「登录」轉為「登入」。
```

### it-api-cli-0082：match

Input:

```text
配置文件支持 YAML 和 JSON。
```

Codex draft expected:

```text
設定檔支援 YAML 和 JSON。
```

Gemini advisory expected:

```text
設定檔支援 YAML 和 JSON。
```

Gemini notes:

```text
「配置文件」轉為「設定檔」，「支持」轉為「支援」。
```

### it-api-cli-0083：match

Input:

```text
命令会输出机器可读的 JSON。
```

Codex draft expected:

```text
指令會輸出機器可讀的 JSON。
```

Gemini advisory expected:

```text
指令會輸出機器可讀的 JSON。
```

Gemini notes:

```text
「命令」轉為「指令」，「机器可读」轉為「機器可讀」。
```

### it-api-cli-0084：match

Input:

```text
请在安装脚本里检查操作系统版本。
```

Codex draft expected:

```text
請在安裝指令碼裡檢查作業系統版本。
```

Gemini advisory expected:

```text
請在安裝指令碼裡檢查作業系統版本。
```

Gemini notes:

```text
「请」轉為「請」，「脚本」轉為「指令碼」，「操作系统」轉為「作業系統」。
```

### it-api-cli-0085：match

Input:

```text
这个标志会强制覆盖目标文件。
```

Codex draft expected:

```text
這個旗標會強制覆寫目標檔案。
```

Gemini advisory expected:

```text
這個旗標會強制覆寫目標檔案。
```

Gemini notes:

```text
「这个」轉為「這個」，「标志」轉為「旗標」，「覆盖」轉為「覆寫」，「文件」轉為「檔案」。
```

### it-api-cli-0086：match

Input:

```text
插件加载失败时会显示堆栈跟踪。
```

Codex draft expected:

```text
外掛程式載入失敗時會顯示堆疊追蹤。
```

Gemini advisory expected:

```text
外掛程式載入失敗時會顯示堆疊追蹤。
```

Gemini notes:

```text
「插件」轉為「外掛程式」，「加载」轉為「載入」，「堆栈跟踪」轉為「堆疊追蹤」。
```

### it-api-cli-0087：different

Input:

```text
请把日志级别调成详细模式。
```

Codex draft expected:

```text
請將記錄等級調成詳細模式。
```

Gemini advisory expected:

```text
請將記錄層級調整為詳細模式。
```

Gemini notes:

```text
「请」轉為「請」，「把」轉為「將」，「日志级别」轉為「記錄層級」，「调成」轉為「調整為」。
```

### it-api-cli-0088：different

Input:

```text
服务器会把请求写入审计日志。
```

Codex draft expected:

```text
伺服器會將請求寫入稽核記錄檔。
```

Gemini advisory expected:

```text
伺服器會將請求寫入稽核記錄。
```

Gemini notes:

```text
「服务器」轉為「伺服器」，「把」轉為「將」，「审计日志」轉為「稽核記錄」。
```

### it-api-cli-0089：different

Input:

```text
后台任务会定期清理过期会话。
```

Codex draft expected:

```text
背景任務會定期清理過期工作階段。
```

Gemini advisory expected:

```text
背景工作會定期清除過期工作階段。
```

Gemini notes:

```text
「后台任务」轉為「背景工作」，「清理」轉為「清除」，「会话」轉為「工作階段」。
```

### it-api-cli-0090：different

Input:

```text
队列消费者会批量确认消息。
```

Codex draft expected:

```text
佇列消費者會批次確認訊息。
```

Gemini advisory expected:

```text
佇列取用者會批次確認訊息。
```

Gemini notes:

```text
「队列」轉為「佇列」，「消费者」轉為「取用者」，「批量」轉為「批次」，「消息」轉為「訊息」。
```

### it-api-cli-0091：different

Input:

```text
生产者需要设置消息键。
```

Codex draft expected:

```text
生產者需要設定訊息索引鍵。
```

Gemini advisory expected:

```text
生產者需要設定訊息金鑰。
```

Gemini notes:

```text
「生产者」轉為「生產者」，「设置」轉為「設定」，「消息键」轉為「訊息金鑰」。
```

### it-api-cli-0092：different

Input:

```text
数据库事务提交后才会发布事件。
```

Codex draft expected:

```text
資料庫交易提交後才會發布事件。
```

Gemini advisory expected:

```text
資料庫交易提交後才會發佈事件。
```

Gemini notes:

```text
「数据库」轉為「資料庫」，「事务」轉為「交易」，「发布」轉為「發佈」。
```

### it-api-cli-0093：different

Input:

```text
索引重建期间查询可能变慢。
```

Codex draft expected:

```text
索引重建期間查詢可能變慢。
```

Gemini advisory expected:

```text
索引重建期間查詢可能會變慢。
```

Gemini notes:

```text
「查询」轉為「查詢」，「变慢」轉為「變慢」。
```

### it-api-cli-0094：different

Input:

```text
请避免在主线程执行阻塞操作。
```

Codex draft expected:

```text
請避免在主執行緒執行阻塞操作。
```

Gemini advisory expected:

```text
請避免在主執行緒執行阻斷作業。
```

Gemini notes:

```text
「请」轉為「請」，「线程」轉為「執行緒」，「阻塞操作」轉為「阻斷作業」。
```

### it-api-cli-0095：match

Input:

```text
这个线程池会复用工作线程。
```

Codex draft expected:

```text
這個執行緒集區會重複使用工作執行緒。
```

Gemini advisory expected:

```text
這個執行緒集區會重複使用工作執行緒。
```

Gemini notes:

```text
「这个」轉為「這個」，「线程池」轉為「執行緒集區」，「复用」轉為「重複使用」，「工作线程」轉為「工作執行緒」。
```

### it-api-cli-0096：different

Input:

```text
容器启动前会拉取最新镜像。
```

Codex draft expected:

```text
容器啟動前會拉取最新映像檔。
```

Gemini advisory expected:

```text
容器啟動前會提取最新映像。
```

Gemini notes:

```text
「启动」轉為「啟動」，「拉取」轉為「提取」，「镜像」轉為「映像」。
```

### it-api-cli-0097：different

Input:

```text
镜像标签必须包含版本号。
```

Codex draft expected:

```text
映像檔標籤必須包含版本號。
```

Gemini advisory expected:

```text
映像標籤必須包含版本號。
```

Gemini notes:

```text
「镜像标签」轉為「映像標籤」，「必须」轉為「必須」，「版本号」轉為「版本號」。
```

### it-api-cli-0098：match

Input:

```text
部署清单会声明资源限制。
```

Codex draft expected:

```text
部署資訊清單會宣告資源限制。
```

Gemini advisory expected:

```text
部署資訊清單會宣告資源限制。
```

Gemini notes:

```text
「清单」轉為「資訊清單」，「声明」轉為「宣告」。
```

### it-api-cli-0099：match

Input:

```text
请检查命名空间是否存在。
```

Codex draft expected:

```text
請檢查命名空間是否存在。
```

Gemini advisory expected:

```text
請檢查命名空間是否存在。
```

Gemini notes:

```text
「请」轉為「請」，「命名空间」轉為「命名空間」。
```

### it-api-cli-0100：different

Input:

```text
探针失败后容器会重新启动。
```

Codex draft expected:

```text
探針失敗後容器會重新啟動。
```

Gemini advisory expected:

```text
探測失敗後容器會重新啟動。
```

Gemini notes:

```text
「探针」轉為「探測」，「启动」轉為「啟動」。
```

### it-api-cli-0101：match

Input:

```text
服务发现会返回可用节点列表。
```

Codex draft expected:

```text
服務探索會傳回可用節點清單。
```

Gemini advisory expected:

```text
服務探索會傳回可用節點清單。
```

Gemini notes:

```text
「服务发现」轉為「服務探索」，「返回」轉為「傳回」，「节点列表」轉為「節點清單」。
```

### it-api-cli-0102：different

Input:

```text
负载均衡器会跳过不健康实例。
```

Codex draft expected:

```text
負載平衡器會略過不健康實例。
```

Gemini advisory expected:

```text
負載平衡器會跳過不健全的執行個體。
```

Gemini notes:

```text
「负载均衡器」轉為「負載平衡器」，「实例」轉為「執行個體」。
```

### it-api-cli-0103：match

Input:

```text
网关会把路径前缀转发到后端。
```

Codex draft expected:

```text
閘道會將路徑前置詞轉送到後端。
```

Gemini advisory expected:

```text
閘道會將路徑前置詞轉送到後端。
```

Gemini notes:

```text
「网关」轉為「閘道」，「把」轉為「將」，「路径前缀」轉為「路徑前置詞」，「转发」轉為「轉送」。
```

### it-api-cli-0104：different

Input:

```text
代理会保留原始客户端地址。
```

Codex draft expected:

```text
代理會保留原始用戶端位址。
```

Gemini advisory expected:

```text
Proxy 會保留原始用戶端位址。
```

Gemini notes:

```text
「代理」轉為「Proxy」（常見於 IT 領域），「客户端地址」轉為「用戶端位址」。
```

### it-api-cli-0105：match

Input:

```text
证书吊销列表会定期更新。
```

Codex draft expected:

```text
憑證撤銷清單會定期更新。
```

Gemini advisory expected:

```text
憑證撤銷清單會定期更新。
```

Gemini notes:

```text
「证书」轉為「憑證」，「吊销列表」轉為「撤銷清單」。
```

### it-api-cli-0106：different

Input:

```text
私钥必须存放在密钥库中。
```

Codex draft expected:

```text
私鑰必須存放在金鑰庫中。
```

Gemini advisory expected:

```text
私密金鑰必須存放在金鑰儲存庫中。
```

Gemini notes:

```text
「私钥」轉為「私密金鑰」，「必须」轉為「必須」，「密钥库」轉為「金鑰儲存庫」。
```

### it-api-cli-0107：match

Input:

```text
请轮换长期有效的访问密钥。
```

Codex draft expected:

```text
請輪替長期有效的存取金鑰。
```

Gemini advisory expected:

```text
請輪替長期有效的存取金鑰。
```

Gemini notes:

```text
「请」轉為「請」，「轮换」轉為「輪替」，「访问密钥」轉為「存取金鑰」。
```

### it-api-cli-0108：match

Input:

```text
这个错误码表示资源不存在。
```

Codex draft expected:

```text
這個錯誤碼表示資源不存在。
```

Gemini advisory expected:

```text
這個錯誤碼表示資源不存在。
```

Gemini notes:

```text
「这个」轉為「這個」，「错误码」轉為「錯誤碼」。
```

### it-api-cli-0109：match

Input:

```text
错误响应会包含追踪编号。
```

Codex draft expected:

```text
錯誤回應會包含追蹤編號。
```

Gemini advisory expected:

```text
錯誤回應會包含追蹤編號。
```

Gemini notes:

```text
「错误响应」轉為「錯誤回應」，「追踪编号」轉為「追蹤編號」。
```

### it-api-cli-0110：match

Input:

```text
请在工单中附上请求编号。
```

Codex draft expected:

```text
請在工單中附上請求編號。
```

Gemini advisory expected:

```text
請在工單中附上請求編號。
```

Gemini notes:

```text
「请」轉為「請」，「工单」轉為「工單」。
```

### it-api-cli-0111：different

Input:

```text
分页游标会在下一次请求中使用。
```

Codex draft expected:

```text
分頁游標會在下一次請求中使用。
```

Gemini advisory expected:

```text
分頁游標會於下一個請求中使用。
```

Gemini notes:

```text
「分页游标」轉為「分頁游標」，「会在」轉為「會於」，「下一次」轉為「下一個」。
```

### it-api-cli-0112：different

Input:

```text
批量接口最多接受一千个项目。
```

Codex draft expected:

```text
批次介面最多接受一千個項目。
```

Gemini advisory expected:

```text
批次 API 最多接受一千個項目。
```

Gemini notes:

```text
「批量接口」轉為「批次 API」。
```

### it-api-cli-0113：different

Input:

```text
上传接口会检查文件大小限制。
```

Codex draft expected:

```text
上傳介面會檢查檔案大小限制。
```

Gemini advisory expected:

```text
上傳 API 會檢查檔案大小限制。
```

Gemini notes:

```text
「上传接口」轉為「上傳 API」，「文件」轉為「檔案」。
```

### it-api-cli-0114：different

Input:

```text
下载链接会在十分钟后过期。
```

Codex draft expected:

```text
下載連結會在十分鐘後過期。
```

Gemini advisory expected:

```text
下載連結會於十分鐘後過期。
```

Gemini notes:

```text
「下载链接」轉為「下載連結」，「会在」轉為「會於」。
```

### it-api-cli-0115：match

Input:

```text
这个参数接受逗号分隔的字符串。
```

Codex draft expected:

```text
這個參數接受逗號分隔的字串。
```

Gemini advisory expected:

```text
這個參數接受逗號分隔的字串。
```

Gemini notes:

```text
「这个」轉為「這個」，「参数」轉為「參數」，「字符串」轉為「字串」。
```

### it-api-cli-0116：match

Input:

```text
布尔选项可以省略等号。
```

Codex draft expected:

```text
布林選項可以省略等號。
```

Gemini advisory expected:

```text
布林選項可以省略等號。
```

Gemini notes:

```text
「布尔选项」轉為「布林選項」，「等号」轉為「等號」。
```

### it-api-cli-0117：different

Input:

```text
请把输出重定向到文件。
```

Codex draft expected:

```text
請將輸出重新導向到檔案。
```

Gemini advisory expected:

```text
請將輸出重新導向至檔案。
```

Gemini notes:

```text
「请」轉為「請」，「把」轉為「將」，「重定向到」轉為「重新導向至」，「文件」轉為「檔案」。
```

### it-api-cli-0118：match

Input:

```text
标准错误会显示警告消息。
```

Codex draft expected:

```text
標準錯誤會顯示警告訊息。
```

Gemini advisory expected:

```text
標準錯誤會顯示警告訊息。
```

Gemini notes:

```text
「标准错误」轉為「標準錯誤」，「消息」轉為「訊息」。
```

### it-api-cli-0119：match

Input:

```text
命令退出码为零表示成功。
```

Codex draft expected:

```text
指令結束碼為零表示成功。
```

Gemini advisory expected:

```text
指令結束碼為零表示成功。
```

Gemini notes:

```text
「命令」轉為「指令」，「退出码」轉為「結束碼」。
```

### it-api-cli-0120：different

Input:

```text
子进程继承当前环境变量。
```

Codex draft expected:

```text
子處理程序繼承目前環境變數。
```

Gemini advisory expected:

```text
子程序繼承目前的環境變數。
```

Gemini notes:

```text
「子进程」轉為「子程序」，「当前」轉為「目前的」，「环境变量」轉為「環境變數」。
```

### it-api-cli-0121：different

Input:

```text
守护进程会在后台监听套接字。
```

Codex draft expected:

```text
常駐處理程序會在背景監聽 Socket。
```

Gemini advisory expected:

```text
常駐程式會於背景監聽通訊端。
```

Gemini notes:

```text
「守护进程」轉為「常駐程式」，「会在」轉為「會於」，「后台」轉為「背景」，「套接字」轉為「通訊端」。
```

### it-api-cli-0122：different

Input:

```text
请不要在配置中写入明文密码。
```

Codex draft expected:

```text
請不要在設定中寫入明文密碼。
```

Gemini advisory expected:

```text
請不要在組態中寫入純文字密碼。
```

Gemini notes:

```text
「请」轉為「請」，「配置」轉為「組態」，「明文密码」轉為「純文字密碼」。
```

### it-api-cli-0123：different

Input:

```text
敏感字段会在日志中被遮蔽。
```

Codex draft expected:

```text
敏感欄位會在記錄檔中被遮蔽。
```

Gemini advisory expected:

```text
敏感欄位會於記錄中被遮蔽。
```

Gemini notes:

```text
「敏感字段」轉為「敏感欄位」，「会在」轉為「會於」，「日志」轉為「記錄」。
```

### it-api-cli-0124：different

Input:

```text
这个钩子会在提交前运行格式化程序。
```

Codex draft expected:

```text
這個掛鉤會在提交前執行格式化程式。
```

Gemini advisory expected:

```text
這個掛鉤會於提交前執行格式化工具。
```

Gemini notes:

```text
「这个」轉為「這個」，「钩子」轉為「掛鉤」，「会在」轉為「會於」，「运行」轉為「執行」，「格式化程序」轉為「格式化工具」。
```

### it-api-cli-0125：match

Input:

```text
预检检查会验证依赖库版本。
```

Codex draft expected:

```text
預檢檢查會驗證相依性程式庫版本。
```

Gemini advisory expected:

```text
預檢檢查會驗證相依性程式庫版本。
```

Gemini notes:

```text
「预检检查」轉為「預檢檢查」，「验证」轉為「驗證」，「依赖库」轉為「相依性程式庫」。
```
