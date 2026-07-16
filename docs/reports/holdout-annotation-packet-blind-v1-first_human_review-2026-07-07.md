<!-- zhtw:disable -->
# Holdout Annotation Packet (2026-07-07)

Inputs: `benchmarks/accuracy/blind-v1.inputs.json`
Dataset: `blind-v1`
Reviewer stage: `first_human_review`
Batch filter: `all`
ID range: `first..last`
Cases: 100

## Reviewer Rules

- Write Taiwan Traditional Chinese expected output from the Simplified input only.
- Do not run zhtw, OpenCC, zhconv, Gemini, or any converter while filling this packet.
- Do not open any generated converter output or benchmark report.
- Keep the input text unchanged.
- Preserve punctuation and spacing unless a Taiwan Traditional output requires a direct change.
- Put optional variants in `Acceptable`, one per line.
- Mark issue tags only from the provided list.
- If unsure, write a short note instead of guessing.

Allowed issue tags:

- `over_conversion`
- `under_conversion`
- `regional_term`
- `it_term`
- `ui_term`
- `formal_term`
- `high_risk_term`
- `punctuation`
- `ambiguous_context`
- `other`

## Cases

### blind-it-0001

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `api, function, exception`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个函数会抛出异常，请在调用前检查返回值。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0002

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `auth, server, token`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
用户登录后，服务器会返回访问令牌和刷新令牌。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0003

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `client, cache, config`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
如果缓存过期，客户端应该重新请求配置文件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0004

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `deployment, environment, credential`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
部署脚本需要读取环境变量里的数据库凭证。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0005

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `api, pagination, order`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个接口会分页返回订单列表，每页最多五十条。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0006

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `over_conversion_guard`
- Tags: `timeout, form, submit`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
当连接超时发生时，请不要重复提交表单。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0007

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `background-job, retry, logging`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我们在后台任务里记录每一次重试的原因。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0008

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `sdk, upload, request`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
新版 SDK 支持批量上传文件和取消请求。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0009

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `cli, settings, backup`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个命令会覆盖本地设置，请先备份原始文件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0010

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `console, admin, api-key`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
管理员可以在控制台停用异常的 API 密钥。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0011

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `log, permission, resource`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
日志里显示用户权限不足，无法删除这个资源。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0012

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `queue, consumer, notification`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
如果消息队列阻塞，消费者会延迟处理通知。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0013

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `baseline_guard`
- Tags: `field, validation`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个字段只接受小写字母和数字。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0014

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `pull-request, bot, preview`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
合并请求通过检查后，机器人会自动发布预览版本。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0015

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `config, locale, timezone`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
你可以用配置文件指定默认语言和时区。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0016

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `migration, index, database`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
数据迁移完成后，请验证索引是否已经重建。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0017

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `endpoint, signature, gateway`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个端点需要签名，否则网关会拒绝请求。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0018

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `payment, callback, worker`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我们把支付回调放进独立的工作线程处理。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0019

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `over_conversion_guard`
- Tags: `client, conflict, sync`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
发生冲突时，客户端应该重新下载最新记录。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0020

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `logging, environment, production`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请在测试环境启用详细日志，线上环境保持关闭。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0021

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `archive, binary, path`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
压缩包解开后，把二进制文件移动到系统路径。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0022

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `plugin, format, code`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个插件会在保存文件时格式化代码。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0023

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `scheduler, retry, task`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
任务失败后，调度器会在五分钟后再次尝试。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0024

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `candidate_gap`
- Tags: `firewall, proxy, service`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请确认防火墙允许代理服务器访问内部服务。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-it-0025

- Batch: `blind-it-api-cli`
- Domain: `it`
- Risk: `baseline_guard`
- Tags: `installer, version, update`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
如果版本号不匹配，安装程序会停止更新。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0001

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Tags: `button, save, timestamp`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
点击保存后，页面会显示上次更新时间。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0002

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `verification, sms, input`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请输入验证码，系统会发送简讯到你的手机。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0003

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `settings, notification, desktop`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
你可以在设置页面关闭桌面通知。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0004

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `slider, volume, apply`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
拖动滑块调整音量，然后点击应用。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0005

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `search, filter, empty-state`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
搜索结果为空时，显示重置筛选按钮。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0006

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `dialog, unsaved, navigation`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个对话框会在离开页面前提醒尚未保存的更改。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0007

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `download, notification, button`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
下载完成后，通知中心会显示打开文件的按钮。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0008

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `profile, avatar, member`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
会员可以在个人资料里修改头像。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0009

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `table, sort, filter`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
表格支持按创建时间排序和按状态筛选。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0010

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `password, error, input`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
如果密码太短，输入框下方会显示错误消息。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0011

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Tags: `navigation, directory, back`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
点击返回箭头会回到上一层目录。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0012

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `favorite, page, bookmark`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
你可以把常用页面加入收藏夹。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0013

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `dark-mode, chart, color`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
开启深色模式后，图表颜色会自动调整。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0014

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `language, draft, i18n`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
语言切换后，当前草稿不会被清除。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0015

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Tags: `order, button, state`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
订单取消成功后，按钮会变成灰色。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0016

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `network, offline, banner`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
当网络中断时，页面顶部显示离线提示。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0017

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `over_conversion_guard`
- Tags: `account, delete, email`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请在删除账号前再次输入你的电子邮件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0018

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `baseline_guard`
- Tags: `admin, menu, collapse`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
管理页面左侧菜单可以折叠。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0019

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `image, upload, retry`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
图片上传失败时，缩略图旁边会显示重试图标。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-ui-0020

- Batch: `blind-ui-i18n`
- Domain: `ui`
- Risk: `candidate_gap`
- Tags: `session, expiration, prompt`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
系统会在会话即将过期时弹出提示。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0001

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `readme, quickstart, documentation`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这段说明可以放在 README 的快速开始章节。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0002

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `support, rewrite, taiwan-usage`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请把客服回复改写成更自然的台湾用语。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0003

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `summary, model-output, limits`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
模型生成的摘要保留了原文的关键限制。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0004

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `product-copy, team, permission`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这份产品文案强调团队协作和权限管理。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0005

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Tags: `medical, safety, support`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
如果回答涉及医疗建议，请提醒用户咨询专业人员。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0006

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Tags: `privacy, test-data, pii`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
生成测试资料时，不要使用真实的个人信息。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0007

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `prompt, assumption, conclusion`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这段提示词要求模型先列出假设再给结论。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0008

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `baseline_guard`
- Tags: `assistant, limitation, answer`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
机器人应该在不知道答案时明确说明限制。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0009

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `formatting, bullet, reader`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请把长段落拆成三点，方便使用者快速阅读。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0010

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `tutorial, developer, deployment`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这份教程适合第一次部署服务的开发者。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0011

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `over_conversion_guard`
- Tags: `support, promise, processing-time`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
自动回复需要避免承诺无法保证的处理时间。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0012

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `code, import, model-output`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
模型输出的代码片段应该包含必要的导入语句。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0013

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `system-message, assistant, policy`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这条系统消息限制助理不能泄露内部规则。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0014

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `candidate_gap`
- Tags: `comparison, criteria, assistant`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
使用者要求比较方案时，请先说明评估标准。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-llm-0015

- Batch: `blind-llm-content`
- Domain: `llm`
- Risk: `baseline_guard`
- Tags: `announcement, web, email`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这段公告要同时适合网页和电子邮件使用。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0001

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `policy, procedure, application`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
本计划将分阶段公布实施细则和申请流程。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0002

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `company, board, budget`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
公司董事会已经核准年度预算调整案。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0003

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `research, data, bias`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
研究团队发现数据来源存在明显偏差。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0004

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Tags: `regulator, consumer, business`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
主管机关提醒业者不得误导消费者。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0005

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Tags: `policy, pilot, schedule`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
新制度预计明年第一季度开始试办。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0006

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `meeting, minutes, resolution`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
会议记录应列明出席人员和决议事项。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0007

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Tags: `application, document, deadline`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
申请人须在期限内补交相关证明文件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0008

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `report, security, review`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
该报告建议提高资讯安全审查频率。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0009

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Tags: `government, policy, tracking`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
政府将持续追踪政策执行效果。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0010

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `press-release, partnership, rights`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
新闻稿指出，合作项目不会影响现有用户权益。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0011

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `committee, risk, agency`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
委员会要求承办单位重新评估风险。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0012

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Tags: `contract, payment, terms`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
合同签署前，双方应确认付款条件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0013

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `baseline_guard`
- Tags: `statistics, service, usage`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
统计资料显示，服务使用量持续增加。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0014

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `candidate_gap`
- Tags: `procurement, procedure, public`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
采购案将依公开程序办理。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-formal-0015

- Batch: `blind-formal-news`
- Domain: `formal`
- Risk: `over_conversion_guard`
- Tags: `finance, disclaimer, investment`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
本声明不构成任何投资建议。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0001

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `daily, drink, message`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我今天下班后想去买一杯珍珠奶茶。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0002

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `video, subtitle, comment`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这个视频的字幕有点太快，我来不及看完。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0003

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `weekend, bike, weather`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
周末如果没下雨，我们就去骑脚踏车。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0004

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `group-chat, restaurant, list`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
群组里有人分享了新的餐厅名单。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0005

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `photo, album, message`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
你把照片传给我，我晚点再整理相册。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0006

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `shopping, clothing, size`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这件外套颜色很好看，不过尺寸好像偏小。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0007

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `store, charging-cable, daily`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我刚刚在便利店看到同款充电线。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0008

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Tags: `weather, daily, reminder`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
明天早上记得带雨伞，天气预报说会下雨。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0009

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `over_conversion_guard`
- Tags: `music, comment, slang`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这首歌的副歌很洗脑，大家都在哼。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0010

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `meeting, link, comment`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
他把会议链接贴在留言区了。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0011

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `over_conversion_guard`
- Tags: `transport, meetup, taiwan`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我们先在捷运站出口集合。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0012

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Tags: `food, chat, daily`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
晚餐想吃面还是便当？
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0013

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Tags: `restaurant, queue, daily`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
这家店排队人很多，可能要等半小时。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0014

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `baseline_guard`
- Tags: `ticket, wallet, reminder`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
我把票放在钱包里，别让我忘记拿。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-social-0015

- Batch: `blind-social-daily`
- Domain: `social`
- Risk: `candidate_gap`
- Tags: `stream, replay, question`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
今天的直播回放什么时候会上架？
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0001

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `legal, contract, liability`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
不得以定型化契约条款排除责任。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0002

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `finance, bank, fee`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
跨行汇款手续费由使用者负担。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0003

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `medical, medicine, allergy`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
请依医师指示服用本药，并留意过敏反应。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0004

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `insurance, policy, exclusion`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
投保前应详阅保单条款和除外责任。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0005

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `candidate_gap`
- Tags: `identity, subsidy, document`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
申请补助时，必须提供有效的身分证明文件。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0006

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `medical, emergency, symptom`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
病人出现胸痛或呼吸困难时，应立即就医。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0007

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `candidate_gap`
- Tags: `finance, loan, interest-rate`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
贷款利率可能随市场条件调整。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0008

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `privacy, personal-data, purpose`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
个人资料不得用于原申请目的以外的用途。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0009

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `legal, contract, jurisdiction`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
本合约争议适用中华民国法律。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

### blind-high-risk-0010

- Batch: `blind-high-risk`
- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Tags: `medical, record, legal`
- Source: project_original_seed; license: MIT-compatible project original text; citation: Original M2 seed sentence written for zhtw on 2026-07-07.

Input:

```text
医疗纪录应依法保存，不得任意删除。
```

Reviewer:

```text

```

Expected:

```text

```

Acceptable:

```text

```

Issue tags:

```text

```

Reviewer notes:

```text

```

## Coordinator Rules

- This packet is an annotation aid, not ground truth by itself.
- Import completed values into `benchmarks/accuracy/blind-v1.expected.json` only after review.
- The expected file must stay private until benchmark publication.
- The expected file must keep `source_inputs_sha256` matching the input file hash.
- First and second reviewers must be different people.
- Disagreements require `human_adjudication` and a non-empty adjudicator.
