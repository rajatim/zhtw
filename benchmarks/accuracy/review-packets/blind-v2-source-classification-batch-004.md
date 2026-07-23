<!-- zhtw:disable -->
# Blind-v2 Source Classification 004

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-004.json`
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

### zhtw-project-llm-product-v1/llm-001

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-001`
- Split: `project_original`

Input:

```text
系统提示应明确说明模型可以使用哪些工具。
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

### zhtw-project-llm-product-v1/llm-002

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-002`
- Split: `project_original`

Input:

```text
工具调用失败后，代理最多自动重试一次。
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

### zhtw-project-llm-product-v1/llm-003

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-003`
- Split: `project_original`

Input:

```text
模型回答引用资料时，必须附上可验证的来源链接。
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

### zhtw-project-llm-product-v1/llm-004

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-004`
- Split: `project_original`

Input:

```text
检索不到相关内容时，不要编造引用或文档编号。
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

### zhtw-project-llm-product-v1/llm-005

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-005`
- Split: `project_original`

Input:

```text
对话历史超过上下文限制时，优先保留最近的用户问题。
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

### zhtw-project-llm-product-v1/llm-006

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-006`
- Split: `project_original`

Input:

```text
流式输出中断后，界面应保留已经生成的文字。
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

### zhtw-project-llm-product-v1/llm-007

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-007`
- Split: `project_original`

Input:

```text
用户停止生成后，不再发送新的模型请求。
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

### zhtw-project-llm-product-v1/llm-008

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-008`
- Split: `project_original`

Input:

```text
提示模板中的 {{user_locale}} 必须保持原样。
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

### zhtw-project-llm-product-v1/llm-009

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-009`
- Split: `project_original`

Input:

```text
JSON 模式下，模型输出必须通过指定的结构验证。
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

### zhtw-project-llm-product-v1/llm-010

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-010`
- Split: `project_original`

Input:

```text
工具参数缺少必填字段时，不应直接执行调用。
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

### zhtw-project-llm-product-v1/llm-011

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-011`
- Split: `project_original`

Input:

```text
代理执行高风险操作前，必须再次请求用户确认。
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

### zhtw-project-llm-product-v1/llm-012

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-012`
- Split: `project_original`

Input:

```text
模型无法确定答案时，应明确表达不确定性。
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

### zhtw-project-llm-product-v1/llm-013

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-013`
- Split: `project_original`

Input:

```text
系统消息与用户消息发生冲突时，遵循系统消息。
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

### zhtw-project-llm-product-v1/llm-014

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-014`
- Split: `project_original`

Input:

```text
检索片段应记录所属文件和原始段落位置。
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

### zhtw-project-llm-product-v1/llm-015

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-015`
- Split: `project_original`

Input:

```text
相同请求重试时，应复用已经完成的检索结果。
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

### zhtw-project-llm-product-v1/llm-016

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-016`
- Split: `project_original`

Input:

```text
嵌入向量的版本变化后，需要重新建立索引。
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

### zhtw-project-llm-product-v1/llm-017

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-017`
- Split: `project_original`

Input:

```text
知识库更新完成前，旧索引仍应保持可查询。
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

### zhtw-project-llm-product-v1/llm-018

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-018`
- Split: `project_original`

Input:

```text
分块策略改变后，评测结果不能与旧版本直接混合。
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

### zhtw-project-llm-product-v1/llm-019

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-019`
- Split: `project_original`

Input:

```text
模型切换后，界面需要显示当前使用的模型名称。
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

### zhtw-project-llm-product-v1/llm-020

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-020`
- Split: `project_original`

Input:

```text
达到令牌上限前，应为最终答案预留输出空间。
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

### zhtw-project-llm-product-v1/llm-021

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-021`
- Split: `project_original`

Input:

```text
计算用量时，分别记录输入令牌和输出令牌。
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

### zhtw-project-llm-product-v1/llm-022

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-022`
- Split: `project_original`

Input:

```text
敏感信息发送给模型前，先执行脱敏处理。
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

### zhtw-project-llm-product-v1/llm-023

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-023`
- Split: `project_original`

Input:

```text
日志中不得保存完整的 API 密钥或访问令牌。
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

### zhtw-project-llm-product-v1/llm-024

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-024`
- Split: `project_original`

Input:

```text
用户要求删除对话后，缓存副本也必须一起清除。
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

### zhtw-project-llm-product-v1/llm-025

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-025`
- Split: `project_original`

Input:

```text
内容过滤器拦截回答时，应向用户显示适当说明。
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

### zhtw-project-llm-product-v1/llm-026

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-026`
- Split: `project_original`

Input:

```text
审核结果只能作为建议，最终决定由授权人员确认。
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

### zhtw-project-llm-product-v1/llm-027

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-027`
- Split: `project_original`

Input:

```text
多代理协作时，每个代理只能访问完成任务所需的工具。
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

### zhtw-project-llm-product-v1/llm-028

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-028`
- Split: `project_original`

Input:

```text
代理转交任务时，应同时传递必要的上下文摘要。
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

### zhtw-project-llm-product-v1/llm-029

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-029`
- Split: `project_original`

Input:

```text
工具返回的数据不得被当作新的系统指令执行。
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

### zhtw-project-llm-product-v1/llm-030

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-030`
- Split: `project_original`

Input:

```text
网页内容中的提示注入文本必须视为不可信输入。
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

### zhtw-project-llm-product-v1/llm-031

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-031`
- Split: `project_original`

Input:

```text
模型生成代码后，应在隔离环境中运行测试。
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

### zhtw-project-llm-product-v1/llm-032

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-032`
- Split: `project_original`

Input:

```text
自动修改文件前，先显示将要变更的文件清单。
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

### zhtw-project-llm-product-v1/llm-033

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-033`
- Split: `project_original`

Input:

```text
代码审查通过前，不得自动合并到主分支。
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

### zhtw-project-llm-product-v1/llm-034

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-034`
- Split: `project_original`

Input:

```text
评测集的参考答案不能出现在训练提示中。
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

### zhtw-project-llm-product-v1/llm-035

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-035`
- Split: `project_original`

Input:

```text
同一评测只能在固定模型和固定参数下比较。
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

### zhtw-project-llm-product-v1/llm-036

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-036`
- Split: `project_original`

Input:

```text
评分脚本需要记录模型版本、温度和随机种子。
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

### zhtw-project-llm-product-v1/llm-037

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-037`
- Split: `project_original`

Input:

```text
人工审核前，不得把模型建议写成最终标准答案。
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

### zhtw-project-llm-product-v1/llm-038

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-038`
- Split: `project_original`

Input:

```text
两个审核模型意见一致，也不能替代人工确认。
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

### zhtw-project-llm-product-v1/llm-039

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-039`
- Split: `project_original`

Input:

```text
低信心案例应进入单独的人工审核队列。
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

### zhtw-project-llm-product-v1/llm-040

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-040`
- Split: `project_original`

Input:

```text
回答包含表格时，流式渲染不得破坏列结构。
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

### zhtw-project-llm-product-v1/llm-041

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-041`
- Split: `project_original`

Input:

```text
Markdown 代码块中的变量名称必须保持原样。
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

### zhtw-project-llm-product-v1/llm-042

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-042`
- Split: `project_original`

Input:

```text
模型输出繁体中文时，不要自动改写专有名词。
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

### zhtw-project-llm-product-v1/llm-043

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-043`
- Split: `project_original`

Input:

```text
用户要求简短回答时，仍需保留必要的安全说明。
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

### zhtw-project-llm-product-v1/llm-044

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-044`
- Split: `project_original`

Input:

```text
语音转写内容不清楚时，先请求用户确认关键词。
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

### zhtw-project-llm-product-v1/llm-045

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-045`
- Split: `project_original`

Input:

```text
图片识别结果应区分可见事实和模型推断。
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

### zhtw-project-llm-product-v1/llm-046

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-046`
- Split: `project_original`

Input:

```text
文件解析失败时，不要根据文件名称猜测内容。
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

### zhtw-project-llm-product-v1/llm-047

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-047`
- Split: `project_original`

Input:

```text
长文摘要必须保留原文中的日期和数字。
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

### zhtw-project-llm-product-v1/llm-048

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-048`
- Split: `project_original`

Input:

```text
翻译请求包含代码时，只翻译代码之外的说明文字。
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

### zhtw-project-llm-product-v1/llm-049

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-049`
- Split: `project_original`

Input:

```text
批量生成任务应允许单独重试失败的项目。
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

### zhtw-project-llm-product-v1/llm-050

- Source: `zhtw-project-llm-product-v1`
- Source case: `llm-050`
- Split: `project_original`

Input:

```text
服务降级时，明确告知哪些模型功能暂时不可用。
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

### zhtw-project-ui-i18n-v1/ui-001

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-001`
- Split: `project_original`

Input:

```text
用户点击保存按钮后，页面应显示成功提示。
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

### zhtw-project-ui-i18n-v1/ui-002

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-002`
- Split: `project_original`

Input:

```text
表单提交失败时，应将焦点移到第一个错误字段。
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

### zhtw-project-ui-i18n-v1/ui-003

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-003`
- Split: `project_original`

Input:

```text
下拉列表打开后，应高亮显示当前选项。
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

### zhtw-project-ui-i18n-v1/ui-004

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-004`
- Split: `project_original`

Input:

```text
上传失败后，保留用户已经选择的文件。
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

### zhtw-project-ui-i18n-v1/ui-005

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-005`
- Split: `project_original`

Input:

```text
文件大小超过限制时，提示允许的最大容量。
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

### zhtw-project-ui-i18n-v1/ui-006

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-006`
- Split: `project_original`

Input:

```text
日期选择器应支持键盘方向键操作。
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

### zhtw-project-ui-i18n-v1/ui-007

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-007`
- Split: `project_original`

Input:

```text
关闭弹窗前，询问是否放弃未保存的修改。
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

### zhtw-project-ui-i18n-v1/ui-008

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-008`
- Split: `project_original`

Input:

```text
搜索结果为空时，显示清晰的空白状态。
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

### zhtw-project-ui-i18n-v1/ui-009

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-009`
- Split: `project_original`

Input:

```text
网络恢复后，自动重新加载未完成的请求。
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

### zhtw-project-ui-i18n-v1/ui-010

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-010`
- Split: `project_original`

Input:

```text
删除操作完成后，提供短暂的撤销入口。
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

### zhtw-project-ui-i18n-v1/ui-011

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-011`
- Split: `project_original`

Input:

```text
切换语言后，导航菜单不应保留旧语言文本。
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

### zhtw-project-ui-i18n-v1/ui-012

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-012`
- Split: `project_original`

Input:

```text
阿拉伯语界面启用从右到左的布局方向。
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

### zhtw-project-ui-i18n-v1/ui-013

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-013`
- Split: `project_original`

Input:

```text
金额输入框应根据地区格式显示小数点和千位分隔符。
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

### zhtw-project-ui-i18n-v1/ui-014

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-014`
- Split: `project_original`

Input:

```text
系统时区变化后，日程时间需要重新计算。
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

### zhtw-project-ui-i18n-v1/ui-015

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-015`
- Split: `project_original`

Input:

```text
日期格式应遵循用户选择的语言区域。
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

### zhtw-project-ui-i18n-v1/ui-016

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-016`
- Split: `project_original`

Input:

```text
文本长度增加时，按钮标签不得被图标遮挡。
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

### zhtw-project-ui-i18n-v1/ui-017

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-017`
- Split: `project_original`

Input:

```text
翻译缺失时，记录键名并使用默认语言内容。
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

### zhtw-project-ui-i18n-v1/ui-018

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-018`
- Split: `project_original`

Input:

```text
占位符 {{user_name}} 在翻译过程中必须保持原样。
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

### zhtw-project-ui-i18n-v1/ui-019

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-019`
- Split: `project_original`

Input:

```text
复数消息应根据数量选择正确的语言形式。
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

### zhtw-project-ui-i18n-v1/ui-020

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-020`
- Split: `project_original`

Input:

```text
屏幕阅读器需要读出输入框的错误说明。
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

### zhtw-project-ui-i18n-v1/ui-021

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-021`
- Split: `project_original`

Input:

```text
图片未加载时，替代文字仍应说明图片内容。
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

### zhtw-project-ui-i18n-v1/ui-022

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-022`
- Split: `project_original`

Input:

```text
颜色选择不能作为区分状态的唯一方式。
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

### zhtw-project-ui-i18n-v1/ui-023

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-023`
- Split: `project_original`

Input:

```text
对话框打开后，键盘焦点应限制在对话框内。
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

### zhtw-project-ui-i18n-v1/ui-024

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-024`
- Split: `project_original`

Input:

```text
按下 Escape 键时，只关闭最上层的对话框。
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

### zhtw-project-ui-i18n-v1/ui-025

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-025`
- Split: `project_original`

Input:

```text
用户放大文字后，工具栏仍应完整显示所有操作。
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

### zhtw-project-ui-i18n-v1/ui-026

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-026`
- Split: `project_original`

Input:

```text
移动设备横屏时，表格允许水平滚动。
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

### zhtw-project-ui-i18n-v1/ui-027

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-027`
- Split: `project_original`

Input:

```text
分页切换后，列表应回到内容区域顶部。
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

### zhtw-project-ui-i18n-v1/ui-028

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-028`
- Split: `project_original`

Input:

```text
筛选条件清除后，结果数量需要立即更新。
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

### zhtw-project-ui-i18n-v1/ui-029

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-029`
- Split: `project_original`

Input:

```text
排序方向改变时，表头应同步更新辅助说明。
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

### zhtw-project-ui-i18n-v1/ui-030

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-030`
- Split: `project_original`

Input:

```text
加载时间较长时，骨架屏不能造成页面跳动。
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

### zhtw-project-ui-i18n-v1/ui-031

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-031`
- Split: `project_original`

Input:

```text
按钮正在处理请求时，应防止用户重复提交。
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

### zhtw-project-ui-i18n-v1/ui-032

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-032`
- Split: `project_original`

Input:

```text
会话过期后，登录页面需要保留原来的跳转目标。
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

### zhtw-project-ui-i18n-v1/ui-033

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-033`
- Split: `project_original`

Input:

```text
权限不足时，不要显示无法执行的批量操作。
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

### zhtw-project-ui-i18n-v1/ui-034

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-034`
- Split: `project_original`

Input:

```text
通知中心按照时间倒序显示未读消息。
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

### zhtw-project-ui-i18n-v1/ui-035

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-035`
- Split: `project_original`

Input:

```text
已读状态应在多个设备之间保持同步。
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

### zhtw-project-ui-i18n-v1/ui-036

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-036`
- Split: `project_original`

Input:

```text
设置恢复默认值前，先显示将被重置的项目。
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

### zhtw-project-ui-i18n-v1/ui-037

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-037`
- Split: `project_original`

Input:

```text
自动保存失败时，明确说明本地草稿是否仍然存在。
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

### zhtw-project-ui-i18n-v1/ui-038

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-038`
- Split: `project_original`

Input:

```text
地址表单应根据国家调整省份和邮政编码字段。
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

### zhtw-project-ui-i18n-v1/ui-039

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-039`
- Split: `project_original`

Input:

```text
电话号码输入框不要强制使用单一国家格式。
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

### zhtw-project-ui-i18n-v1/ui-040

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-040`
- Split: `project_original`

Input:

```text
姓名字段应允许单字姓名和较长的复姓。
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

### zhtw-project-ui-i18n-v1/ui-041

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-041`
- Split: `project_original`

Input:

```text
排版方向改变时，前进和后退图标需要交换位置。
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

### zhtw-project-ui-i18n-v1/ui-042

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-042`
- Split: `project_original`

Input:

```text
用户选择深色模式后，系统刷新页面仍应保留设置。
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

### zhtw-project-ui-i18n-v1/ui-043

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-043`
- Split: `project_original`

Input:

```text
高对比度模式下，禁用状态也必须清楚可辨。
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

### zhtw-project-ui-i18n-v1/ui-044

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-044`
- Split: `project_original`

Input:

```text
触摸目标之间应保留足够间距，避免误触。
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

### zhtw-project-ui-i18n-v1/ui-045

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-045`
- Split: `project_original`

Input:

```text
错误提示出现时，不应导致提交按钮突然移动。
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

### zhtw-project-ui-i18n-v1/ui-046

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-046`
- Split: `project_original`

Input:

```text
表格列名过长时，允许换行但不能截断关键信息。
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

### zhtw-project-ui-i18n-v1/ui-047

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-047`
- Split: `project_original`

Input:

```text
导出完成后，下载通知应包含文件名称。
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

### zhtw-project-ui-i18n-v1/ui-048

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-048`
- Split: `project_original`

Input:

```text
预览区域必须完整显示文件的第一页。
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

### zhtw-project-ui-i18n-v1/ui-049

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-049`
- Split: `project_original`

Input:

```text
图片裁剪工具应保留用户上一次选择的比例。
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

### zhtw-project-ui-i18n-v1/ui-050

- Source: `zhtw-project-ui-i18n-v1`
- Source case: `ui-050`
- Split: `project_original`

Input:

```text
应用更新后，首次启动只显示一次版本说明。
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
