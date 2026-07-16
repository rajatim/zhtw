<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：it-api-cli 0076-0125（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### it-api-cli-0076

Input:

```text
请在响应头中加入缓存控制字段。
```

AI draft expected:

```text
請在回應標頭中加入快取控制欄位。
```

Notes：HTTP 語境：响应头→回應標頭、缓存→快取、字段→欄位。

### it-api-cli-0077

Input:

```text
这个端点会返回剩余配额。
```

AI draft expected:

```text
這個端點會傳回剩餘配額。
```

Notes：API 語境：端点→端點、返回→傳回、配额→配額。

### it-api-cli-0078

Input:

```text
回调地址必须使用 HTTPS。
```

AI draft expected:

```text
回呼位址必須使用 HTTPS。
```

Notes：Webhook 語境：回调→回呼、地址→位址。

### it-api-cli-0079

Input:

```text
请验证请求签名和时间戳。
```

AI draft expected:

```text
請驗證要求簽章和時間戳記。
```

Notes：資安/API 語境：请求签名→要求簽章、时间戳→時間戳記。

### it-api-cli-0080

Input:

```text
客户端会自动刷新访问令牌。
```

AI draft expected:

```text
用戶端會自動重新整理存取權杖。
```

Notes：OAuth 語境：客户端→用戶端、刷新访问令牌→重新整理存取權杖。

### it-api-cli-0081

Input:

```text
如果刷新失败，请重新登录。
```

AI draft expected:

```text
如果重新整理失敗，請重新登入。
```

Notes：登入/session 語境：刷新→重新整理、登录→登入。

### it-api-cli-0082

Input:

```text
配置文件支持 YAML 和 JSON。
```

AI draft expected:

```text
設定檔支援 YAML 和 JSON。
```

Notes：設定語境：配置文件→設定檔、支持→支援。

### it-api-cli-0083

Input:

```text
命令会输出机器可读的 JSON。
```

AI draft expected:

```text
指令會輸出機器可讀的 JSON。
```

Notes：CLI 語境：命令→指令、输出→輸出。

### it-api-cli-0084

Input:

```text
请在安装脚本里检查操作系统版本。
```

AI draft expected:

```text
請在安裝指令碼裡檢查作業系統版本。
```

Notes：安裝語境：脚本→指令碼、操作系统→作業系統。

### it-api-cli-0085

Input:

```text
这个标志会强制覆盖目标文件。
```

AI draft expected:

```text
這個旗標會強制覆寫目標檔案。
```

Notes：CLI flag 語境：标志→旗標、覆盖→覆寫、文件→檔案。

### it-api-cli-0086

Input:

```text
插件加载失败时会显示堆栈跟踪。
```

AI draft expected:

```text
外掛程式載入失敗時會顯示堆疊追蹤。
```

Notes：外掛/錯誤語境：插件→外掛程式、加载→載入、堆栈跟踪→堆疊追蹤。

### it-api-cli-0087

Input:

```text
请把日志级别调成详细模式。
```

AI draft expected:

```text
請將記錄等級調成詳細模式。
```

Notes：日誌設定語境：日志级别→記錄等級、把→將。

### it-api-cli-0088

Input:

```text
服务器会把请求写入审计日志。
```

AI draft expected:

```text
伺服器會將請求寫入稽核記錄檔。
```

Notes：稽核語境：服务器→伺服器、审计日志→稽核記錄檔。

### it-api-cli-0089

Input:

```text
后台任务会定期清理过期会话。
```

AI draft expected:

```text
背景任務會定期清理過期工作階段。
```

Notes：背景工作語境：后台→背景、任务→任務、会话→工作階段。

### it-api-cli-0090

Input:

```text
队列消费者会批量确认消息。
```

AI draft expected:

```text
佇列消費者會批次確認訊息。
```

Notes：訊息佇列語境：队列→佇列、批量→批次、消息→訊息。

### it-api-cli-0091

Input:

```text
生产者需要设置消息键。
```

AI draft expected:

```text
生產者需要設定訊息索引鍵。
```

Notes：訊息佇列語境：生产者→生產者、设置→設定、消息键→訊息索引鍵。

### it-api-cli-0092

Input:

```text
数据库事务提交后才会发布事件。
```

AI draft expected:

```text
資料庫交易提交後才會發布事件。
```

Notes：資料庫語境：数据库→資料庫、事务→交易、发布→發布。

### it-api-cli-0093

Input:

```text
索引重建期间查询可能变慢。
```

AI draft expected:

```text
索引重建期間查詢可能變慢。
```

Notes：資料庫語境：查询→查詢、期间→期間。

### it-api-cli-0094

Input:

```text
请避免在主线程执行阻塞操作。
```

AI draft expected:

```text
請避免在主執行緒執行阻塞操作。
```

Notes：效能語境：线程→執行緒、执行→執行。

### it-api-cli-0095

Input:

```text
这个线程池会复用工作线程。
```

AI draft expected:

```text
這個執行緒集區會重複使用工作執行緒。
```

Notes：並行語境：线程池→執行緒集區、复用→重複使用。

### it-api-cli-0096

Input:

```text
容器启动前会拉取最新镜像。
```

AI draft expected:

```text
容器啟動前會拉取最新映像檔。
```

Notes：容器語境：启动→啟動、镜像→映像檔。

### it-api-cli-0097

Input:

```text
镜像标签必须包含版本号。
```

AI draft expected:

```text
映像檔標籤必須包含版本號。
```

Notes：容器語境：镜像标签→映像檔標籤、版本号→版本號。

### it-api-cli-0098

Input:

```text
部署清单会声明资源限制。
```

AI draft expected:

```text
部署資訊清單會宣告資源限制。
```

Notes：Kubernetes 語境：清单→資訊清單、声明→宣告、资源→資源。

### it-api-cli-0099

Input:

```text
请检查命名空间是否存在。
```

AI draft expected:

```text
請檢查命名空間是否存在。
```

Notes：Kubernetes 語境：命名空间→命名空間。

### it-api-cli-0100

Input:

```text
探针失败后容器会重新启动。
```

AI draft expected:

```text
探針失敗後容器會重新啟動。
```

Notes：容器健康檢查語境：探针→探針、重新启动→重新啟動。

### it-api-cli-0101

Input:

```text
服务发现会返回可用节点列表。
```

AI draft expected:

```text
服務探索會傳回可用節點清單。
```

Notes：服務探索語境：返回→傳回、节点→節點、列表→清單。

### it-api-cli-0102

Input:

```text
负载均衡器会跳过不健康实例。
```

AI draft expected:

```text
負載平衡器會略過不健康實例。
```

Notes：網路語境：负载均衡器→負載平衡器、跳过→略過。

### it-api-cli-0103

Input:

```text
网关会把路径前缀转发到后端。
```

AI draft expected:

```text
閘道會將路徑前置詞轉送到後端。
```

Notes：閘道語境：网关→閘道、路径前缀→路徑前置詞、转发→轉送。

### it-api-cli-0104

Input:

```text
代理会保留原始客户端地址。
```

AI draft expected:

```text
代理會保留原始用戶端位址。
```

Notes：代理語境：客户端→用戶端、地址→位址。

### it-api-cli-0105

Input:

```text
证书吊销列表会定期更新。
```

AI draft expected:

```text
憑證撤銷清單會定期更新。
```

Notes：TLS 語境：证书吊销列表→憑證撤銷清單。

### it-api-cli-0106

Input:

```text
私钥必须存放在密钥库中。
```

AI draft expected:

```text
私鑰必須存放在金鑰庫中。
```

Notes：資安語境：私钥→私鑰、密钥库→金鑰庫。

### it-api-cli-0107

Input:

```text
请轮换长期有效的访问密钥。
```

AI draft expected:

```text
請輪替長期有效的存取金鑰。
```

Notes：資安語境：轮换→輪替、访问密钥→存取金鑰。

### it-api-cli-0108

Input:

```text
这个错误码表示资源不存在。
```

AI draft expected:

```text
這個錯誤碼表示資源不存在。
```

Notes：API 錯誤語境：错误码→錯誤碼、资源→資源。

### it-api-cli-0109

Input:

```text
错误响应会包含追踪编号。
```

AI draft expected:

```text
錯誤回應會包含追蹤編號。
```

Notes：API 錯誤語境：响应→回應、追踪编号→追蹤編號。

### it-api-cli-0110

Input:

```text
请在工单中附上请求编号。
```

AI draft expected:

```text
請在工單中附上請求編號。
```

Notes：客服/API 語境：请求编号→請求編號。

### it-api-cli-0111

Input:

```text
分页游标会在下一次请求中使用。
```

AI draft expected:

```text
分頁游標會在下一次請求中使用。
```

Notes：分頁 API 語境：分页→分頁、游标→游標、请求→請求。

### it-api-cli-0112

Input:

```text
批量接口最多接受一千个项目。
```

AI draft expected:

```text
批次介面最多接受一千個項目。
```

Notes：API 語境：批量→批次、接口→介面、项目→項目。

### it-api-cli-0113

Input:

```text
上传接口会检查文件大小限制。
```

AI draft expected:

```text
上傳介面會檢查檔案大小限制。
```

Notes：上傳 API 語境：接口→介面、文件→檔案。

### it-api-cli-0114

Input:

```text
下载链接会在十分钟后过期。
```

AI draft expected:

```text
下載連結會在十分鐘後過期。
```

Notes：下載語境：下载→下載、链接→連結。

### it-api-cli-0115

Input:

```text
这个参数接受逗号分隔的字符串。
```

AI draft expected:

```text
這個參數接受逗號分隔的字串。
```

Notes：CLI/API 參數語境：参数→參數、字符串→字串。

### it-api-cli-0116

Input:

```text
布尔选项可以省略等号。
```

AI draft expected:

```text
布林選項可以省略等號。
```

Notes：CLI 語境：布尔→布林、选项→選項。

### it-api-cli-0117

Input:

```text
请把输出重定向到文件。
```

AI draft expected:

```text
請將輸出重新導向到檔案。
```

Notes：CLI 語境：把→將、输出→輸出、重定向→重新導向、文件→檔案。

### it-api-cli-0118

Input:

```text
标准错误会显示警告消息。
```

AI draft expected:

```text
標準錯誤會顯示警告訊息。
```

Notes：CLI stderr 語境：标准错误→標準錯誤、消息→訊息。

### it-api-cli-0119

Input:

```text
命令退出码为零表示成功。
```

AI draft expected:

```text
指令結束碼為零表示成功。
```

Notes：CLI 語境：命令→指令、退出码→結束碼。

### it-api-cli-0120

Input:

```text
子进程继承当前环境变量。
```

AI draft expected:

```text
子處理程序繼承目前環境變數。
```

Notes：程序語境：子进程→子處理程序、当前→目前、环境变量→環境變數。

### it-api-cli-0121

Input:

```text
守护进程会在后台监听套接字。
```

AI draft expected:

```text
常駐處理程序會在背景監聽 Socket。
```

Notes：系統程式語境：守护进程→常駐處理程序、后台→背景、套接字→Socket。

### it-api-cli-0122

Input:

```text
请不要在配置中写入明文密码。
```

AI draft expected:

```text
請不要在設定中寫入明文密碼。
```

Notes：設定/資安語境：配置→設定、写入→寫入、密码→密碼。

### it-api-cli-0123

Input:

```text
敏感字段会在日志中被遮蔽。
```

AI draft expected:

```text
敏感欄位會在記錄檔中被遮蔽。
```

Notes：日誌/隱私語境：字段→欄位、日志→記錄檔。

### it-api-cli-0124

Input:

```text
这个钩子会在提交前运行格式化程序。
```

AI draft expected:

```text
這個掛鉤會在提交前執行格式化程式。
```

Notes：Git hook 語境：钩子→掛鉤、运行→執行、程序→程式。

### it-api-cli-0125

Input:

```text
预检检查会验证依赖库版本。
```

AI draft expected:

```text
預檢檢查會驗證相依性程式庫版本。
```

Notes：發布/CI 語境：预检→預檢、依赖库→相依性程式庫。
