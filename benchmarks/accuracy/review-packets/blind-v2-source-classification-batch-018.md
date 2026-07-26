<!-- zhtw:disable -->
# Blind-v2 Source Classification 018

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-018.json`
Cases: 100
Seed: `20260719`
Selection: `all-source-cases-sorted-v1`

## Rules

- Read only the input and provenance shown in this packet.
- Do not run zhtw, OpenCC, zhconv, Gemini, or another converter.
- Mark `eligible = no` for malformed, unclear, non-Mandarin, or unsuitable text.
- Script: `simplified`, `mixed`, `traditional`, or `uncertain`.
- Domain: `it_api_cli`, `ui_i18n`, `llm_generated`, `formal_news`, `social_daily`, or `high_stakes`.
- Risk: `candidate_gap`, `over_conversion_guard`, or `baseline_guard`.
- Confidence: `high`, `medium`, or `low`; do not guess when context is insufficient.
- This packet is advisory input classification, not expected-output annotation.

## Cases

### zhtw-project-it-llm-ui-guard-v1/it-001

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-001`
- Split: `project_original`

Input:

```text
执行 git rebase --onto release main feature 后检查提交历史。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-002

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-002`
- Split: `project_original`

Input:

```text
使用 kubectl get pods -n staging 查看服务状态。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-003

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-003`
- Split: `project_original`

Input:

```text
服务器返回 HTTP 429，并在 Retry-After 标头中提供秒数。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-004

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-004`
- Split: `project_original`

Input:

```text
客户端发送 If-None-Match 时必须保留原始 ETag。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-005

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-005`
- Split: `project_original`

Input:

```text
负载均衡器每十秒请求 /healthz 检查实例。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-006

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-006`
- Split: `project_original`

Input:

```text
请在日志中记录 X-Request-ID，但不要写入访问令牌。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-007

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-007`
- Split: `project_original`

Input:

```text
上传 JSON 时将 Content-Type 设置为 application/json。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-008

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-008`
- Split: `project_original`

Input:

```text
登录流程采用 OAuth 2.0 Authorization Code 与 PKCE。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-009

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-009`
- Split: `project_original`

Input:

```text
后端验证 JWT 的 iss、aud 与 exp 声明。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-010

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-010`
- Split: `project_original`

Input:

```text
生产环境只接受 TLS 1.3 加密连接。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-011

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-011`
- Split: `project_original`

Input:

```text
套件版本从 2.4.1 升级到 2.5.0-beta.1。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-012

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-012`
- Split: `project_original`

Input:

```text
安装 @acme/design-system 后重新启动开发服务器。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-013

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-013`
- Split: `project_original`

Input:

```text
配置文件位于 /etc/acme/service.yaml。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-014

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-014`
- Split: `project_original`

Input:

```text
将环境变量 DATABASE_URL 注入 worker 进程。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-015

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-015`
- Split: `project_original`

Input:

```text
SQL 查询引用 user_sessions.last_seen_at 字段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-016

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-016`
- Split: `project_original`

Input:

```text
正则表达式 ^[a-z0-9_-]{3,32}$ 用于验证账号名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-017

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-017`
- Split: `project_original`

Input:

```text
下载完成后以 SHA-256 核对文件摘要。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-018

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-018`
- Split: `project_original`

Input:

```text
请求中的 trace_id 为 550e8400-e29b-41d4-a716-446655440000。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-019

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-019`
- Split: `project_original`

Input:

```text
事件时间戳使用 2026-07-26T14:30:00+08:00。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-020

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-020`
- Split: `project_original`

Input:

```text
本机代理监听 127.0.0.1:8080。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-021

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-021`
- Split: `project_original`

Input:

```text
防火墙规则允许来自 2001:db8::/32 的测试流量。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-022

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-022`
- Split: `project_original`

Input:

```text
浏览器可以预览 image/avif 类型的响应。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-023

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-023`
- Split: `project_original`

Input:

```text
API 建立资源后应返回 201 Created。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-024

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-024`
- Split: `project_original`

Input:

```text
JSON 对象中的 userId 与 displayName 采用 camelCase。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-025

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-025`
- Split: `project_original`

Input:

```text
YAML 文件使用 &defaults 定义锚点，再以 *defaults 引用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-026

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-026`
- Split: `project_original`

Input:

```text
运行 npm ci 时必须使用 package-lock.json 的锁定版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-027

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-027`
- Split: `project_original`

Input:

```text
Rust 项目通过 cargo test --workspace 执行全部测试。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-028

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-028`
- Split: `project_original`

Input:

```text
Python 程序以 uv run pytest -q 执行快速测试。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-029

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-029`
- Split: `project_original`

Input:

```text
Java 服务的入口类是 com.acme.billing.Main。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-030

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-030`
- Split: `project_original`

Input:

```text
C# 项目将 Nullable 设为 enable。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-031

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-031`
- Split: `project_original`

Input:

```text
Docker 镜像标签为 ghcr.io/acme/api:2026.07。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-032

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-032`
- Split: `project_original`

Input:

```text
Kubernetes 部署引用 Secret 名称 billing-db。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-033

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-033`
- Split: `project_original`

Input:

```text
Terraform 状态储存在 s3://acme-tfstate/prod.tfstate。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-034

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-034`
- Split: `project_original`

Input:

```text
CI 工作流程只在 refs/heads/main 上发布。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-035

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-035`
- Split: `project_original`

Input:

```text
GraphQL 查询请求 node(id: $id) 的 title 字段。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-036

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-036`
- Split: `project_original`

Input:

```text
gRPC 服务实现 acme.billing.v1.InvoiceService。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-037

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-037`
- Split: `project_original`

Input:

```text
WebSocket 连接使用子协议 graphql-transport-ws。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-038

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-038`
- Split: `project_original`

Input:

```text
消息消费者从 orders.created.v2 主题读取事件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-039

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-039`
- Split: `project_original`

Input:

```text
Redis 键 session:{user_id} 的有效期为三十分钟。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-040

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-040`
- Split: `project_original`

Input:

```text
Prometheus 指标 http_request_duration_seconds 使用秒为单位。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-041

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-041`
- Split: `project_original`

Input:

```text
告警规则在 p95 延迟超过 500 ms 时触发。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-042

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-042`
- Split: `project_original`

Input:

```text
错误追踪系统将 release 标记为 web@4.8.2。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-043

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-043`
- Split: `project_original`

Input:

```text
OpenTelemetry span 的属性键为 http.request.method。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-044

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-044`
- Split: `project_original`

Input:

```text
浏览器策略将 default-src 设置为 'self'。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-045

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-045`
- Split: `project_original`

Input:

```text
Cookie 使用 Secure、HttpOnly 与 SameSite=Lax 属性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-046

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-046`
- Split: `project_original`

Input:

```text
跨域预检请求采用 OPTIONS 方法。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-047

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-047`
- Split: `project_original`

Input:

```text
缓存控制标头设为 max-age=3600, immutable。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-048

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-048`
- Split: `project_original`

Input:

```text
数据库迁移编号 202607260915_add_index 不可重复。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-049

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-049`
- Split: `project_original`

Input:

```text
备份文件命名为 customers_2026-07-26.sql.gz。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/it-050

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `it-050`
- Split: `project_original`

Input:

```text
终端显示 exit code 137，表示进程被系统终止。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-001

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-001`
- Split: `project_original`

Input:

```text
将 temperature 设为 0.2，以降低回答的随机性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-002

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
采样参数 top_p 与 temperature 不应同时大幅调整。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-003

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
请求中的 max_tokens 限制模型可生成的长度。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-004

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
消息依序使用 system、user 与 assistant 角色。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-005

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-005`
- Split: `project_original`

Input:

```text
工具调用名称为 get_weather，参数包含 location。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-006

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-006`
- Split: `project_original`

Input:

```text
函数参数必须符合 response_format 指定的 JSON Schema。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-007

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
启用 JSON mode 后，提示中仍应明确要求输出 JSON。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-008

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
嵌入向量的维度由 embedding_dimensions 字段记录。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-009

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
检索系统以 cosine similarity 排序候选段落。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-010

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
RAG 流程先检索文档，再将上下文交给模型。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-011

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
过滤器应识别提示注入，但不能删除正常引用。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-012

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-012`
- Split: `project_original`

Input:

```text
安全分类标签 safety_label 必须原样写入审计日志。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-013

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
提示中引用“Do not translate this string”作为测试文本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-014

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-014`
- Split: `project_original`

Input:

````text
模型回答中的 ```json 代码围栏必须成对出现。
````

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-015

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-015`
- Split: `project_original`

Input:

```text
数学表达式 $P(y\mid x)$ 使用 LaTeX 格式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-016

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
引用标记 [doc-3:12] 必须对应检索来源。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-017

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
提示模板使用 {{question}} 插入用户问题。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-018

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
批处理请求以 custom_id 关联每一笔结果。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-019

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-019`
- Split: `project_original`

Input:

```text
串流事件中的 delta 只包含本次新增内容。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-020

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
当 finish_reason 为 tool_calls 时继续执行工具。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-021

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-021`
- Split: `project_original`

Input:

```text
响应的 usage 字段列出 input_tokens 与 output_tokens。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-022

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
缓存键包含 model、prompt_hash 与 schema_version。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-023

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
评测记录使用 exact_match 与 pass@1 两项指标。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-024

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
人工审查员看不到 A/B 版本的模型名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-025

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
基准测试将 malformed_response 标记为不可评分。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-026

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
代理只允许调用 allowlist 中列出的工具。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-027

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-027`
- Split: `project_original`

Input:

```text
多轮对话以 conversation_id 串接上下文。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-028

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
摘要任务必须保留 CVE-2026-12345 与版本编号。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-029

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
语音模型输出的时间码格式为 00:01:23.450。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/llm-030

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
模型卡将 zh-TW 列为支持的语言标签。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-001

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-001`
- Split: `project_original`

Input:

```text
按钮显示“删除 {count} 个项目”，并保留变量名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-002

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-002`
- Split: `project_original`

Input:

```text
欢迎消息中的 %1$s 会替换为用户名称。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-003

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-003`
- Split: `project_original`

Input:

```text
复数规则使用 {count, plural, one {# item} other {# items}}。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-004

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-004`
- Split: `project_original`

Input:

```text
按 Ctrl+Shift+P 打开命令面板。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-005

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-005`
- Split: `project_original`

Input:

```text
应用名称 Acme Drive 不随界面语言改变。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-006

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-006`
- Split: `project_original`

Input:

```text
隐私政策链接为 https://example.com/privacy?lang=zh-CN。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-007

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-007`
- Split: `project_original`

Input:

```text
支持信箱显示为 help@example.com。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-008

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-008`
- Split: `project_original`

Input:

```text
载入期间显示“正在同步…”，完成后自动关闭。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-009

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-009`
- Split: `project_original`

Input:

```text
无障碍标签写入 aria-label 属性。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-010

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-010`
- Split: `project_original`

Input:

```text
日期字段接受 YYYY-MM-DD 格式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-011

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-011`
- Split: `project_original`

Input:

```text
订单总额显示为 NT$1,280。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-012

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-012`
- Split: `project_original`

Input:

```text
切换到 RTL 布局时，返回图标也会反向。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-013

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-013`
- Split: `project_original`

Input:

```text
多行说明以 \n 表示换行符。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-014

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-014`
- Split: `project_original`

Input:

```text
设置页面分为 General、Privacy 与 Advanced 三个分页。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-015

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-015`
- Split: `project_original`

Input:

```text
打开“自动更新”开关后立即检查新版本。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-016

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-016`
- Split: `project_original`

Input:

```text
通知标题保留 build #1842 的编号格式。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-017

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-017`
- Split: `project_original`

Input:

```text
文件选择器只显示 .csv 与 .tsv 文件。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-018

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-018`
- Split: `project_original`

Input:

```text
搜索框的占位文本为“输入关键字”。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-019

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-019`
- Split: `project_original`

Input:

```text
空白状态显示“尚无活动记录”。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```

### zhtw-project-it-llm-ui-guard-v1/ui-020

- Source: `zhtw-project-it-llm-ui-guard-v1`
- Source case: `ui-020`
- Split: `project_original`

Input:

```text
进度条旁显示 75%，不要插入额外空格。
```

Classification:

```text
eligible:
script:
domain:
risk:
quality_flags:
confidence:
notes:
```
