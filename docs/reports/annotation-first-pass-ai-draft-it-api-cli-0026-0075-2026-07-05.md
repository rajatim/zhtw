<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：it-api-cli 0026-0075（2026-07-05）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### it-api-cli-0026

Input:

```text
请在请求主体中加入分页参数。
```

AI draft expected:

```text
請在要求主體中加入分頁參數。
```

Notes：API 語境：请求主体→要求主體、分页→分頁、参数→參數。

### it-api-cli-0027

Input:

```text
这个 API 会返回资源列表和总数。
```

AI draft expected:

```text
這個 API 會傳回資源清單和總數。
```

Notes：API 語境：返回→傳回、列表→清單。

### it-api-cli-0028

Input:

```text
如果签名无效，服务端会拒绝请求。
```

AI draft expected:

```text
如果簽章無效，伺服器端會拒絕要求。
```

Notes：資安/API 語境：签名→簽章、服务端→伺服器端、请求→要求。

### it-api-cli-0029

Input:

```text
命令行参数支持短选项和长选项。
```

AI draft expected:

```text
命令列參數支援短選項和長選項。
```

Notes：CLI 語境：命令行→命令列、参数→參數、支持→支援。

### it-api-cli-0030

Input:

```text
请把配置项写入环境变量。
```

AI draft expected:

```text
請將設定項目寫入環境變數。
```

Notes：設定語境：配置项→設定項目、环境变量→環境變數。

### it-api-cli-0031

Input:

```text
证书链缺少中间证书。
```

AI draft expected:

```text
憑證鏈缺少中繼憑證。
```

Notes：TLS 語境：证书链→憑證鏈、中间证书→中繼憑證。

### it-api-cli-0032

Input:

```text
服务启动后会绑定本地端口。
```

AI draft expected:

```text
服務啟動後會繫結本機連接埠。
```

Notes：伺服器語境：绑定→繫結、本地→本機、端口→連接埠。

### it-api-cli-0033

Input:

```text
连接失败时会输出详细错误消息。
```

AI draft expected:

```text
連線失敗時會輸出詳細錯誤訊息。
```

Notes：錯誤處理語境：连接→連線、错误消息→錯誤訊息。

### it-api-cli-0034

Input:

```text
请检查防火墙规则是否允许入站流量。
```

AI draft expected:

```text
請檢查防火牆規則是否允許傳入流量。
```

Notes：網路語境：防火墙→防火牆、入站流量→傳入流量。

### it-api-cli-0035

Input:

```text
客户端缓存会在五分钟后失效。
```

AI draft expected:

```text
用戶端快取會在五分鐘後失效。
```

Notes：用戶端語境：客户端→用戶端、缓存→快取。

### it-api-cli-0036

Input:

```text
这个标志会跳过证书验证。
```

AI draft expected:

```text
這個旗標會略過憑證驗證。
```

Notes：CLI flag 語境：标志→旗標、跳过→略過、证书→憑證。

### it-api-cli-0037

Input:

```text
请使用子命令列出所有插件。
```

AI draft expected:

```text
請使用子命令列出所有外掛程式。
```

Notes：CLI 語境：子命令、插件→外掛程式。

### it-api-cli-0038

Input:

```text
默认配置会启用压缩响应。
```

AI draft expected:

```text
預設設定會啟用壓縮回應。
```

Notes：設定/API 語境：默认→預設、配置→設定、响应→回應。

### it-api-cli-0039

Input:

```text
响应状态码为 429 时请稍后重试。
```

AI draft expected:

```text
回應狀態碼為 429 時請稍後重試。
```

Notes：HTTP 語境：响应状态码→回應狀態碼。

### it-api-cli-0040

Input:

```text
后端会把任务推送到消息队列。
```

AI draft expected:

```text
後端會把工作推送到訊息佇列。
```

Notes：後端/佇列語境：任务→工作、消息队列→訊息佇列。

### it-api-cli-0041

Input:

```text
请不要在日志里记录访问令牌。
```

AI draft expected:

```text
請不要在日誌裡記錄存取權杖。
```

Notes：日誌語境：日志→日誌、访问令牌→存取權杖。

### it-api-cli-0042

Input:

```text
数据库迁移脚本会新增索引。
```

AI draft expected:

```text
資料庫遷移指令碼會新增索引。
```

Notes：資料庫語境：数据库→資料庫、迁移脚本→遷移指令碼。

### it-api-cli-0043

Input:

```text
请确认回滚脚本已经备份。
```

AI draft expected:

```text
請確認復原指令碼已經備份。
```

Notes：部署/復原語境：回滚脚本→復原指令碼。

### it-api-cli-0044

Input:

```text
这个端点需要管理员权限。
```

AI draft expected:

```text
這個端點需要管理員權限。
```

Notes：API 語境：端点→端點、权限→權限。

### it-api-cli-0045

Input:

```text
请求头必须包含内容类型。
```

AI draft expected:

```text
要求標頭必須包含內容類型。
```

Notes：HTTP 語境：请求头→要求標頭、内容类型→內容類型。

### it-api-cli-0046

Input:

```text
响应主体可能为空对象。
```

AI draft expected:

```text
回應主體可能為空物件。
```

Notes：API 語境：响应主体→回應主體、对象→物件。

### it-api-cli-0047

Input:

```text
请将输出格式设置为表格。
```

AI draft expected:

```text
請將輸出格式設定為表格。
```

Notes：CLI 輸出語境：设置→設定。

### it-api-cli-0048

Input:

```text
这个命令支持递归删除空目录。
```

AI draft expected:

```text
這個命令支援遞迴刪除空目錄。
```

Notes：CLI 語境：支持→支援、递归→遞迴。

### it-api-cli-0049

Input:

```text
服务端会校验上传文件的哈希值。
```

AI draft expected:

```text
伺服器端會驗證上傳檔案的雜湊值。
```

Notes：資安/API 語境：服务端→伺服器端、哈希值→雜湊值。

### it-api-cli-0050

Input:

```text
请先解码令牌再读取声明。
```

AI draft expected:

```text
請先解碼權杖再讀取宣告。
```

Notes：JWT 語境：令牌→權杖、声明→宣告。

### it-api-cli-0051

Input:

```text
客户端会根据状态码决定是否重试。
```

AI draft expected:

```text
用戶端會根據狀態碼決定是否重試。
```

Notes：用戶端/API 語境：客户端→用戶端、状态码→狀態碼。

### it-api-cli-0052

Input:

```text
这个接口会分页返回审计记录。
```

AI draft expected:

```text
這個介面會分頁傳回稽核記錄。
```

Notes：API 語境：接口→介面、返回→傳回、审计→稽核。

### it-api-cli-0053

Input:

```text
请在发布前更新版本号。
```

AI draft expected:

```text
請在發布前更新版本號。
```

Notes：發布流程語境：发布→發布、版本号→版本號。

### it-api-cli-0054

Input:

```text
构建缓存命中时会跳过编译。
```

AI draft expected:

```text
建置快取命中時會略過編譯。
```

Notes：建置語境：构建→建置、缓存→快取、跳过→略過。

### it-api-cli-0055

Input:

```text
请检查依赖项是否存在安全漏洞。
```

AI draft expected:

```text
請檢查相依套件是否存在安全漏洞。
```

Notes：套件管理語境：依赖项→相依套件。

### it-api-cli-0056

Input:

```text
这个选项会禁用自动更新。
```

AI draft expected:

```text
這個選項會停用自動更新。
```

Notes：CLI/UI 設定語境：禁用功能→停用。

### it-api-cli-0057

Input:

```text
服务器会限制每个用户的请求速率。
```

AI draft expected:

```text
伺服器會限制每個使用者的要求速率。
```

Notes：API rate limit 語境：请求速率→要求速率、用户→使用者。

### it-api-cli-0058

Input:

```text
请在本地启动模拟服务器。
```

AI draft expected:

```text
請在本機啟動模擬伺服器。
```

Notes：開發環境語境：本地→本機、服务器→伺服器。

### it-api-cli-0059

Input:

```text
测试夹具会建立临时数据库。
```

AI draft expected:

```text
測試夾具會建立暫存資料庫。
```

Notes：測試語境：测试夹具→測試夾具、临时数据库→暫存資料庫。

### it-api-cli-0060

Input:

```text
队列消费者会批量处理事件。
```

AI draft expected:

```text
佇列消費者會批次處理事件。
```

Notes：佇列語境：队列→佇列、批量处理→批次處理。

### it-api-cli-0061

Input:

```text
这个错误码表示权限不足。
```

AI draft expected:

```text
這個錯誤碼表示權限不足。
```

Notes：錯誤處理語境：错误码→錯誤碼、权限→權限。

### it-api-cli-0062

Input:

```text
请为服务账户生成新的密钥。
```

AI draft expected:

```text
請為服務帳戶產生新的金鑰。
```

Notes：雲端/IAM 語境：服务账户→服務帳戶、密钥→金鑰。

### it-api-cli-0063

Input:

```text
容器镜像会上传到私有仓库。
```

AI draft expected:

```text
容器映像檔會上傳到私有儲存庫。
```

Notes：容器語境：镜像→映像檔、仓库→儲存庫。

### it-api-cli-0064

Input:

```text
部署脚本会读取当前分支名称。
```

AI draft expected:

```text
部署指令碼會讀取目前分支名稱。
```

Notes：部署/Git 語境：脚本→指令碼、当前→目前。

### it-api-cli-0065

Input:

```text
负载均衡器会检查健康状态。
```

AI draft expected:

```text
負載平衡器會檢查健康狀態。
```

Notes：網路語境：负载均衡器→負載平衡器。

### it-api-cli-0066

Input:

```text
请把超时时间设置为三十秒。
```

AI draft expected:

```text
請將逾時時間設定為三十秒。
```

Notes：設定語境：超时→逾時、设置→設定。

### it-api-cli-0067

Input:

```text
这个参数会覆盖默认路径。
```

AI draft expected:

```text
這個參數會覆寫預設路徑。
```

Notes：CLI 語境：覆盖→覆寫、默认→預設。

### it-api-cli-0068

Input:

```text
错误堆栈会显示调用链。
```

AI draft expected:

```text
錯誤堆疊會顯示呼叫鏈。
```

Notes：錯誤診斷語境：堆栈→堆疊、调用链→呼叫鏈。

### it-api-cli-0069

Input:

```text
请在配置文件里声明输出编码。
```

AI draft expected:

```text
請在設定檔裡宣告輸出編碼。
```

Notes：設定檔語境：配置文件→設定檔、声明→宣告。

### it-api-cli-0070

Input:

```text
这个中间件会注入请求标识。
```

AI draft expected:

```text
這個中介軟體會注入要求識別碼。
```

Notes：Middleware/API 語境：中间件→中介軟體、请求标识→要求識別碼。

### it-api-cli-0071

Input:

```text
异步任务完成后会触发回调。
```

AI draft expected:

```text
非同步工作完成後會觸發回呼。
```

Notes：非同步語境：异步→非同步、任务→工作、回调→回呼。

### it-api-cli-0072

Input:

```text
请不要把密码写进命令历史。
```

AI draft expected:

```text
請不要把密碼寫進命令歷程。
```

Notes：CLI 語境：命令历史→命令歷程。

### it-api-cli-0073

Input:

```text
这个端点会返回下载链接。
```

AI draft expected:

```text
這個端點會傳回下載連結。
```

Notes：API 語境：端点→端點、返回→傳回、链接→連結。

### it-api-cli-0074

Input:

```text
请检查代理服务器的转发规则。
```

AI draft expected:

```text
請檢查代理伺服器的轉送規則。
```

Notes：網路語境：代理服务器→代理伺服器、转发规则→轉送規則。

### it-api-cli-0075

Input:

```text
服务会在内存不足时自动重启。
```

AI draft expected:

```text
服務會在記憶體不足時自動重新啟動。
```

Notes：系統語境：内存→記憶體、重启→重新啟動。
