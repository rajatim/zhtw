<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：it-api-cli-0026-it-api-cli-0075（2026-07-05）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-it-api-cli-0026-0075-2026-07-05.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 25
- Differences from Codex draft: 25

## Maintainer Decision

Maintainer `tim` accepted the Gemini advisory version for all 25 differing cases
on 2026-07-05. The backlog was updated as follows:

- 25 exact-match cases use the shared Codex/Gemini expected output with
  `expected_source = "human_first_pass"`.
- 25 differing cases use the Gemini advisory expected output with
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

### it-api-cli-0026：different

Input:

```text
请在请求主体中加入分页参数。
```

Codex draft expected:

```text
請在要求主體中加入分頁參數。
```

Gemini advisory expected:

```text
請在請求主體中加入分頁參數。
```

Gemini notes:

```text

```

### it-api-cli-0027：different

Input:

```text
这个 API 会返回资源列表和总数。
```

Codex draft expected:

```text
這個 API 會傳回資源清單和總數。
```

Gemini advisory expected:

```text
這個 API 會回傳資源列表和總數。
```

Gemini notes:

```text

```

### it-api-cli-0028：different

Input:

```text
如果签名无效，服务端会拒绝请求。
```

Codex draft expected:

```text
如果簽章無效，伺服器端會拒絕要求。
```

Gemini advisory expected:

```text
如果簽章無效，伺服端會拒絕請求。
```

Gemini notes:

```text

```

### it-api-cli-0029：match

Input:

```text
命令行参数支持短选项和长选项。
```

Codex draft expected:

```text
命令列參數支援短選項和長選項。
```

Gemini advisory expected:

```text
命令列參數支援短選項和長選項。
```

Gemini notes:

```text

```

### it-api-cli-0030：different

Input:

```text
请把配置项写入环境变量。
```

Codex draft expected:

```text
請將設定項目寫入環境變數。
```

Gemini advisory expected:

```text
請將配置項寫入環境變數。
```

Gemini notes:

```text

```

### it-api-cli-0031：match

Input:

```text
证书链缺少中间证书。
```

Codex draft expected:

```text
憑證鏈缺少中繼憑證。
```

Gemini advisory expected:

```text
憑證鏈缺少中繼憑證。
```

Gemini notes:

```text

```

### it-api-cli-0032：match

Input:

```text
服务启动后会绑定本地端口。
```

Codex draft expected:

```text
服務啟動後會繫結本機連接埠。
```

Gemini advisory expected:

```text
服務啟動後會繫結本機連接埠。
```

Gemini notes:

```text

```

### it-api-cli-0033：match

Input:

```text
连接失败时会输出详细错误消息。
```

Codex draft expected:

```text
連線失敗時會輸出詳細錯誤訊息。
```

Gemini advisory expected:

```text
連線失敗時會輸出詳細錯誤訊息。
```

Gemini notes:

```text

```

### it-api-cli-0034：match

Input:

```text
请检查防火墙规则是否允许入站流量。
```

Codex draft expected:

```text
請檢查防火牆規則是否允許傳入流量。
```

Gemini advisory expected:

```text
請檢查防火牆規則是否允許傳入流量。
```

Gemini notes:

```text

```

### it-api-cli-0035：match

Input:

```text
客户端缓存会在五分钟后失效。
```

Codex draft expected:

```text
用戶端快取會在五分鐘後失效。
```

Gemini advisory expected:

```text
用戶端快取會在五分鐘後失效。
```

Gemini notes:

```text

```

### it-api-cli-0036：different

Input:

```text
这个标志会跳过证书验证。
```

Codex draft expected:

```text
這個旗標會略過憑證驗證。
```

Gemini advisory expected:

```text
這個旗標會跳過憑證驗證。
```

Gemini notes:

```text

```

### it-api-cli-0037：different

Input:

```text
请使用子命令列出所有插件。
```

Codex draft expected:

```text
請使用子命令列出所有外掛程式。
```

Gemini advisory expected:

```text
請使用子指令列出所有外掛程式。
```

Gemini notes:

```text

```

### it-api-cli-0038：different

Input:

```text
默认配置会启用压缩响应。
```

Codex draft expected:

```text
預設設定會啟用壓縮回應。
```

Gemini advisory expected:

```text
預設配置會啟用壓縮回應。
```

Gemini notes:

```text

```

### it-api-cli-0039：match

Input:

```text
响应状态码为 429 时请稍后重试。
```

Codex draft expected:

```text
回應狀態碼為 429 時請稍後重試。
```

Gemini advisory expected:

```text
回應狀態碼為 429 時請稍後重試。
```

Gemini notes:

```text

```

### it-api-cli-0040：different

Input:

```text
后端会把任务推送到消息队列。
```

Codex draft expected:

```text
後端會把工作推送到訊息佇列。
```

Gemini advisory expected:

```text
後端會將任務推送到訊息佇列。
```

Gemini notes:

```text

```

### it-api-cli-0041：different

Input:

```text
请不要在日志里记录访问令牌。
```

Codex draft expected:

```text
請不要在日誌裡記錄存取權杖。
```

Gemini advisory expected:

```text
請不要在記錄檔裡記錄存取權杖。
```

Gemini notes:

```text

```

### it-api-cli-0042：different

Input:

```text
数据库迁移脚本会新增索引。
```

Codex draft expected:

```text
資料庫遷移指令碼會新增索引。
```

Gemini advisory expected:

```text
資料庫移轉指令碼會新增索引。
```

Gemini notes:

```text

```

### it-api-cli-0043：different

Input:

```text
请确认回滚脚本已经备份。
```

Codex draft expected:

```text
請確認復原指令碼已經備份。
```

Gemini advisory expected:

```text
請確認回溯指令碼已經備份。
```

Gemini notes:

```text

```

### it-api-cli-0044：match

Input:

```text
这个端点需要管理员权限。
```

Codex draft expected:

```text
這個端點需要管理員權限。
```

Gemini advisory expected:

```text
這個端點需要管理員權限。
```

Gemini notes:

```text

```

### it-api-cli-0045：different

Input:

```text
请求头必须包含内容类型。
```

Codex draft expected:

```text
要求標頭必須包含內容類型。
```

Gemini advisory expected:

```text
請求標頭必須包含內容類型。
```

Gemini notes:

```text

```

### it-api-cli-0046：match

Input:

```text
响应主体可能为空对象。
```

Codex draft expected:

```text
回應主體可能為空物件。
```

Gemini advisory expected:

```text
回應主體可能為空物件。
```

Gemini notes:

```text

```

### it-api-cli-0047：match

Input:

```text
请将输出格式设置为表格。
```

Codex draft expected:

```text
請將輸出格式設定為表格。
```

Gemini advisory expected:

```text
請將輸出格式設定為表格。
```

Gemini notes:

```text

```

### it-api-cli-0048：different

Input:

```text
这个命令支持递归删除空目录。
```

Codex draft expected:

```text
這個命令支援遞迴刪除空目錄。
```

Gemini advisory expected:

```text
這個指令支援遞迴刪除空目錄。
```

Gemini notes:

```text

```

### it-api-cli-0049：different

Input:

```text
服务端会校验上传文件的哈希值。
```

Codex draft expected:

```text
伺服器端會驗證上傳檔案的雜湊值。
```

Gemini advisory expected:

```text
伺服端會驗證上傳檔案的雜湊值。
```

Gemini notes:

```text

```

### it-api-cli-0050：match

Input:

```text
请先解码令牌再读取声明。
```

Codex draft expected:

```text
請先解碼權杖再讀取宣告。
```

Gemini advisory expected:

```text
請先解碼權杖再讀取宣告。
```

Gemini notes:

```text

```

### it-api-cli-0051：match

Input:

```text
客户端会根据状态码决定是否重试。
```

Codex draft expected:

```text
用戶端會根據狀態碼決定是否重試。
```

Gemini advisory expected:

```text
用戶端會根據狀態碼決定是否重試。
```

Gemini notes:

```text

```

### it-api-cli-0052：different

Input:

```text
这个接口会分页返回审计记录。
```

Codex draft expected:

```text
這個介面會分頁傳回稽核記錄。
```

Gemini advisory expected:

```text
這個介面會分頁回傳稽核記錄。
```

Gemini notes:

```text

```

### it-api-cli-0053：match

Input:

```text
请在发布前更新版本号。
```

Codex draft expected:

```text
請在發布前更新版本號。
```

Gemini advisory expected:

```text
請在發布前更新版本號。
```

Gemini notes:

```text

```

### it-api-cli-0054：different

Input:

```text
构建缓存命中时会跳过编译。
```

Codex draft expected:

```text
建置快取命中時會略過編譯。
```

Gemini advisory expected:

```text
建置快取命中時會跳過編譯。
```

Gemini notes:

```text

```

### it-api-cli-0055：different

Input:

```text
请检查依赖项是否存在安全漏洞。
```

Codex draft expected:

```text
請檢查相依套件是否存在安全漏洞。
```

Gemini advisory expected:

```text
請檢查相依性是否存在安全漏洞。
```

Gemini notes:

```text

```

### it-api-cli-0056：match

Input:

```text
这个选项会禁用自动更新。
```

Codex draft expected:

```text
這個選項會停用自動更新。
```

Gemini advisory expected:

```text
這個選項會停用自動更新。
```

Gemini notes:

```text

```

### it-api-cli-0057：different

Input:

```text
服务器会限制每个用户的请求速率。
```

Codex draft expected:

```text
伺服器會限制每個使用者的要求速率。
```

Gemini advisory expected:

```text
伺服器會限制每個使用者的請求速率。
```

Gemini notes:

```text

```

### it-api-cli-0058：match

Input:

```text
请在本地启动模拟服务器。
```

Codex draft expected:

```text
請在本機啟動模擬伺服器。
```

Gemini advisory expected:

```text
請在本機啟動模擬伺服器。
```

Gemini notes:

```text

```

### it-api-cli-0059：different

Input:

```text
测试夹具会建立临时数据库。
```

Codex draft expected:

```text
測試夾具會建立暫存資料庫。
```

Gemini advisory expected:

```text
測試治具會建立暫存資料庫。
```

Gemini notes:

```text

```

### it-api-cli-0060：match

Input:

```text
队列消费者会批量处理事件。
```

Codex draft expected:

```text
佇列消費者會批次處理事件。
```

Gemini advisory expected:

```text
佇列消費者會批次處理事件。
```

Gemini notes:

```text

```

### it-api-cli-0061：match

Input:

```text
这个错误码表示权限不足。
```

Codex draft expected:

```text
這個錯誤碼表示權限不足。
```

Gemini advisory expected:

```text
這個錯誤碼表示權限不足。
```

Gemini notes:

```text

```

### it-api-cli-0062：different

Input:

```text
请为服务账户生成新的密钥。
```

Codex draft expected:

```text
請為服務帳戶產生新的金鑰。
```

Gemini advisory expected:

```text
請為服務帳戶產生新的密鑰。
```

Gemini notes:

```text

```

### it-api-cli-0063：match

Input:

```text
容器镜像会上传到私有仓库。
```

Codex draft expected:

```text
容器映像檔會上傳到私有儲存庫。
```

Gemini advisory expected:

```text
容器映像檔會上傳到私有儲存庫。
```

Gemini notes:

```text

```

### it-api-cli-0064：match

Input:

```text
部署脚本会读取当前分支名称。
```

Codex draft expected:

```text
部署指令碼會讀取目前分支名稱。
```

Gemini advisory expected:

```text
部署指令碼會讀取目前分支名稱。
```

Gemini notes:

```text

```

### it-api-cli-0065：match

Input:

```text
负载均衡器会检查健康状态。
```

Codex draft expected:

```text
負載平衡器會檢查健康狀態。
```

Gemini advisory expected:

```text
負載平衡器會檢查健康狀態。
```

Gemini notes:

```text

```

### it-api-cli-0066：match

Input:

```text
请把超时时间设置为三十秒。
```

Codex draft expected:

```text
請將逾時時間設定為三十秒。
```

Gemini advisory expected:

```text
請將逾時時間設定為三十秒。
```

Gemini notes:

```text

```

### it-api-cli-0067：match

Input:

```text
这个参数会覆盖默认路径。
```

Codex draft expected:

```text
這個參數會覆寫預設路徑。
```

Gemini advisory expected:

```text
這個參數會覆寫預設路徑。
```

Gemini notes:

```text

```

### it-api-cli-0068：match

Input:

```text
错误堆栈会显示调用链。
```

Codex draft expected:

```text
錯誤堆疊會顯示呼叫鏈。
```

Gemini advisory expected:

```text
錯誤堆疊會顯示呼叫鏈。
```

Gemini notes:

```text

```

### it-api-cli-0069：different

Input:

```text
请在配置文件里声明输出编码。
```

Codex draft expected:

```text
請在設定檔裡宣告輸出編碼。
```

Gemini advisory expected:

```text
請在配置檔裡宣告輸出編碼。
```

Gemini notes:

```text

```

### it-api-cli-0070：different

Input:

```text
这个中间件会注入请求标识。
```

Codex draft expected:

```text
這個中介軟體會注入要求識別碼。
```

Gemini advisory expected:

```text
這個中介軟體會注入請求識別碼。
```

Gemini notes:

```text

```

### it-api-cli-0071：different

Input:

```text
异步任务完成后会触发回调。
```

Codex draft expected:

```text
非同步工作完成後會觸發回呼。
```

Gemini advisory expected:

```text
非同步任務完成後會觸發回呼。
```

Gemini notes:

```text

```

### it-api-cli-0072：different

Input:

```text
请不要把密码写进命令历史。
```

Codex draft expected:

```text
請不要把密碼寫進命令歷程。
```

Gemini advisory expected:

```text
請不要將密碼寫入指令歷史。
```

Gemini notes:

```text

```

### it-api-cli-0073：different

Input:

```text
这个端点会返回下载链接。
```

Codex draft expected:

```text
這個端點會傳回下載連結。
```

Gemini advisory expected:

```text
這個端點會回傳下載連結。
```

Gemini notes:

```text

```

### it-api-cli-0074：match

Input:

```text
请检查代理服务器的转发规则。
```

Codex draft expected:

```text
請檢查代理伺服器的轉送規則。
```

Gemini advisory expected:

```text
請檢查代理伺服器的轉送規則。
```

Gemini notes:

```text

```

### it-api-cli-0075：match

Input:

```text
服务会在内存不足时自动重启。
```

Codex draft expected:

```text
服務會在記憶體不足時自動重新啟動。
```

Gemini advisory expected:

```text
服務會在記憶體不足時自動重新啟動。
```

Gemini notes:

```text

```
