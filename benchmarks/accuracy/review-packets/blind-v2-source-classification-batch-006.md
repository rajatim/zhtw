<!-- zhtw:disable -->
# Blind-v2 Source Classification 006

Packet: `benchmarks/accuracy/review-packets/blind-v2-source-classification-batch-006.json`
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

### zhtw-project-it-api-cli-v1/it-001

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-001`
- Split: `project_original`

Input:

```text
调用接口前，先确认访问令牌没有过期。
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

### zhtw-project-it-api-cli-v1/it-002

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-002`
- Split: `project_original`

Input:

```text
请求体必须包含用户编号和当前时区。
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

### zhtw-project-it-api-cli-v1/it-003

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-003`
- Split: `project_original`

Input:

```text
服务器返回 429 时，客户端应按照响应头延迟重试。
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

### zhtw-project-it-api-cli-v1/it-004

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-004`
- Split: `project_original`

Input:

```text
分页接口使用游标，不要依赖不断变化的页码。
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

### zhtw-project-it-api-cli-v1/it-005

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-005`
- Split: `project_original`

Input:

```text
删除资源后，再次请求应返回明确的状态码。
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

### zhtw-project-it-api-cli-v1/it-006

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-006`
- Split: `project_original`

Input:

```text
批量接口需要报告每个项目的成功或失败结果。
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

### zhtw-project-it-api-cli-v1/it-007

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-007`
- Split: `project_original`

Input:

```text
Webhook 签名校验失败时，不要处理消息内容。
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

### zhtw-project-it-api-cli-v1/it-008

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-008`
- Split: `project_original`

Input:

```text
上传大文件时，客户端可以分块发送并支持断点续传。
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

### zhtw-project-it-api-cli-v1/it-009

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-009`
- Split: `project_original`

Input:

```text
GraphQL 查询深度超过限制时，应拒绝执行。
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

### zhtw-project-it-api-cli-v1/it-010

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-010`
- Split: `project_original`

Input:

```text
API 版本升级后，旧字段至少保留一个迁移周期。
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

### zhtw-project-it-api-cli-v1/it-011

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-011`
- Split: `project_original`

Input:

```text
在终端运行命令前，检查当前工作目录。
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

### zhtw-project-it-api-cli-v1/it-012

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-012`
- Split: `project_original`

Input:

```text
使用 --dry-run 参数预览即将发生的修改。
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

### zhtw-project-it-api-cli-v1/it-013

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-013`
- Split: `project_original`

Input:

```text
命令执行失败后，将退出码传给调用脚本。
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

### zhtw-project-it-api-cli-v1/it-014

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-014`
- Split: `project_original`

Input:

```text
管道中的前一个命令失败时，整个任务也应停止。
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

### zhtw-project-it-api-cli-v1/it-015

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-015`
- Split: `project_original`

Input:

```text
不要把密码直接写在命令行参数中。
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

### zhtw-project-it-api-cli-v1/it-016

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-016`
- Split: `project_original`

Input:

```text
配置文件路径可以通过环境变量覆盖。
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

### zhtw-project-it-api-cli-v1/it-017

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-017`
- Split: `project_original`

Input:

```text
日志输出到标准错误，正常结果输出到标准输出。
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

### zhtw-project-it-api-cli-v1/it-018

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-018`
- Split: `project_original`

Input:

```text
交互模式关闭后，命令不得等待用户输入。
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

### zhtw-project-it-api-cli-v1/it-019

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-019`
- Split: `project_original`

Input:

```text
使用引号包住包含空格的文件名。
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

### zhtw-project-it-api-cli-v1/it-020

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-020`
- Split: `project_original`

Input:

```text
帮助信息应列出参数默认值和可用示例。
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

### zhtw-project-it-api-cli-v1/it-021

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-021`
- Split: `project_original`

Input:

```text
提交代码前，先同步远程分支的最新修改。
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

### zhtw-project-it-api-cli-v1/it-022

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-022`
- Split: `project_original`

Input:

```text
合并冲突解决后，重新运行完整测试。
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

### zhtw-project-it-api-cli-v1/it-023

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-023`
- Split: `project_original`

Input:

```text
不要重写已经推送到共享分支的提交历史。
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

### zhtw-project-it-api-cli-v1/it-024

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-024`
- Split: `project_original`

Input:

```text
拉取请求需要关联问题编号和测试证据。
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

### zhtw-project-it-api-cli-v1/it-025

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-025`
- Split: `project_original`

Input:

```text
发布标签必须指向通过构建的提交。
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

### zhtw-project-it-api-cli-v1/it-026

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-026`
- Split: `project_original`

Input:

```text
子模块更新后，主仓库也要提交新的引用。
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

### zhtw-project-it-api-cli-v1/it-027

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-027`
- Split: `project_original`

Input:

```text
忽略规则不能隐藏需要纳入版本控制的配置模板。
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

### zhtw-project-it-api-cli-v1/it-028

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-028`
- Split: `project_original`

Input:

```text
执行变基前，先备份尚未推送的工作。
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

### zhtw-project-it-api-cli-v1/it-029

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-029`
- Split: `project_original`

Input:

```text
代码审查通过不代表可以跳过持续集成检查。
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

### zhtw-project-it-api-cli-v1/it-030

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-030`
- Split: `project_original`

Input:

```text
紧急修复分支合并后，也要同步回开发主线。
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

### zhtw-project-it-api-cli-v1/it-031

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-031`
- Split: `project_original`

Input:

```text
数据库迁移必须能在事务失败时安全回滚。
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

### zhtw-project-it-api-cli-v1/it-032

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-032`
- Split: `project_original`

Input:

```text
新增索引前，先检查写入延迟和磁盘空间。
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

### zhtw-project-it-api-cli-v1/it-033

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-033`
- Split: `project_original`

Input:

```text
查询条件缺少租户编号可能造成数据泄漏。
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

### zhtw-project-it-api-cli-v1/it-034

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-034`
- Split: `project_original`

Input:

```text
连接池耗尽时，应用应快速失败并记录原因。
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

### zhtw-project-it-api-cli-v1/it-035

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-035`
- Split: `project_original`

Input:

```text
只读副本落后时，不要用于读取刚写入的数据。
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

### zhtw-project-it-api-cli-v1/it-036

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-036`
- Split: `project_original`

Input:

```text
删除大量记录时，分批提交可以降低锁表风险。
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

### zhtw-project-it-api-cli-v1/it-037

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-037`
- Split: `project_original`

Input:

```text
备份完成不代表恢复流程已经验证。
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

### zhtw-project-it-api-cli-v1/it-038

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-038`
- Split: `project_original`

Input:

```text
时间戳统一保存为 UTC，显示时再转换时区。
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

### zhtw-project-it-api-cli-v1/it-039

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-039`
- Split: `project_original`

Input:

```text
唯一约束冲突应返回可识别的业务错误。
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

### zhtw-project-it-api-cli-v1/it-040

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-040`
- Split: `project_original`

Input:

```text
慢查询日志不得记录完整的敏感参数。
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

### zhtw-project-it-api-cli-v1/it-041

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-041`
- Split: `project_original`

Input:

```text
容器镜像只安装运行时真正需要的软件包。
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

### zhtw-project-it-api-cli-v1/it-042

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-042`
- Split: `project_original`

Input:

```text
构建镜像时固定基础镜像的摘要值。
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

### zhtw-project-it-api-cli-v1/it-043

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-043`
- Split: `project_original`

Input:

```text
容器启动后应以非 root 用户运行服务。
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

### zhtw-project-it-api-cli-v1/it-044

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-044`
- Split: `project_original`

Input:

```text
健康检查失败不一定代表进程已经退出。
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

### zhtw-project-it-api-cli-v1/it-045

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-045`
- Split: `project_original`

Input:

```text
部署前确认命名空间和集群上下文。
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

### zhtw-project-it-api-cli-v1/it-046

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-046`
- Split: `project_original`

Input:

```text
资源限制过低会让容器频繁被系统终止。
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

### zhtw-project-it-api-cli-v1/it-047

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-047`
- Split: `project_original`

Input:

```text
滚动更新期间必须维持最少可用实例数。
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

### zhtw-project-it-api-cli-v1/it-048

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-048`
- Split: `project_original`

Input:

```text
临时文件不要写入容器的只读文件系统。
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

### zhtw-project-it-api-cli-v1/it-049

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-049`
- Split: `project_original`

Input:

```text
密钥应从秘密管理服务注入，而不是放进镜像。
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

### zhtw-project-it-api-cli-v1/it-050

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-050`
- Split: `project_original`

Input:

```text
服务网格升级前，先验证代理版本兼容性。
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

### zhtw-project-it-api-cli-v1/it-051

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-051`
- Split: `project_original`

Input:

```text
持续集成任务应使用锁定版本的依赖项。
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

### zhtw-project-it-api-cli-v1/it-052

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-052`
- Split: `project_original`

Input:

```text
测试报告上传失败不能掩盖测试本身的失败。
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

### zhtw-project-it-api-cli-v1/it-053

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-053`
- Split: `project_original`

Input:

```text
缓存键必须包含操作系统和运行时版本。
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

### zhtw-project-it-api-cli-v1/it-054

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-054`
- Split: `project_original`

Input:

```text
并行任务不要写入同一个临时目录。
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

### zhtw-project-it-api-cli-v1/it-055

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-055`
- Split: `project_original`

Input:

```text
部署生产环境前，需要人工批准发布任务。
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

### zhtw-project-it-api-cli-v1/it-056

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-056`
- Split: `project_original`

Input:

```text
回滚脚本应使用已经验证过的制品。
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

### zhtw-project-it-api-cli-v1/it-057

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-057`
- Split: `project_original`

Input:

```text
构建日志中的访问令牌必须自动遮盖。
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

### zhtw-project-it-api-cli-v1/it-058

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-058`
- Split: `project_original`

Input:

```text
定时任务重复触发时，只允许一个实例继续执行。
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

### zhtw-project-it-api-cli-v1/it-059

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-059`
- Split: `project_original`

Input:

```text
失败任务重跑时，不要重复发布已经上传的制品。
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

### zhtw-project-it-api-cli-v1/it-060

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-060`
- Split: `project_original`

Input:

```text
预发布环境的配置结构应与生产环境一致。
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

### zhtw-project-it-api-cli-v1/it-061

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-061`
- Split: `project_original`

Input:

```text
依赖性锁定文件必须与软件包清单一起提交。
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

### zhtw-project-it-api-cli-v1/it-062

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-062`
- Split: `project_original`

Input:

```text
升级主版本前，先阅读不兼容变更说明。
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

### zhtw-project-it-api-cli-v1/it-063

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-063`
- Split: `project_original`

Input:

```text
私有软件包源不可接受来源不明的同名软件包。
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

### zhtw-project-it-api-cli-v1/it-064

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-064`
- Split: `project_original`

Input:

```text
安装脚本必须校验下载文件的摘要。
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

### zhtw-project-it-api-cli-v1/it-065

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-065`
- Split: `project_original`

Input:

```text
可选依赖缺失时，只停用相关功能。
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

### zhtw-project-it-api-cli-v1/it-066

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-066`
- Split: `project_original`

Input:

```text
依赖解析结果在不同平台上可能不完全相同。
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

### zhtw-project-it-api-cli-v1/it-067

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-067`
- Split: `project_original`

Input:

```text
许可证扫描失败时，不得继续发布。
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

### zhtw-project-it-api-cli-v1/it-068

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-068`
- Split: `project_original`

Input:

```text
移除软件包前，检查是否仍被其他模块引用。
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

### zhtw-project-it-api-cli-v1/it-069

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-069`
- Split: `project_original`

Input:

```text
开发依赖不要打包进生产制品。
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

### zhtw-project-it-api-cli-v1/it-070

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-070`
- Split: `project_original`

Input:

```text
软件物料清单应记录所有间接依赖。
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

### zhtw-project-it-api-cli-v1/it-071

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-071`
- Split: `project_original`

Input:

```text
认证成功后，仍需检查用户是否有操作权限。
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

### zhtw-project-it-api-cli-v1/it-072

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-072`
- Split: `project_original`

Input:

```text
刷新令牌只能使用一次，重复使用时立即撤销会话。
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

### zhtw-project-it-api-cli-v1/it-073

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-073`
- Split: `project_original`

Input:

```text
跨域请求只允许明确列出的来源地址。
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

### zhtw-project-it-api-cli-v1/it-074

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-074`
- Split: `project_original`

Input:

```text
用户输入进入查询语句前必须使用参数绑定。
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

### zhtw-project-it-api-cli-v1/it-075

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-075`
- Split: `project_original`

Input:

```text
文件上传服务不能信任客户端提供的扩展名。
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

### zhtw-project-it-api-cli-v1/it-076

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-076`
- Split: `project_original`

Input:

```text
审计日志需要记录操作者和目标资源。
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

### zhtw-project-it-api-cli-v1/it-077

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-077`
- Split: `project_original`

Input:

```text
签名密钥轮换期间，新旧密钥需要短暂并存。
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

### zhtw-project-it-api-cli-v1/it-078

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-078`
- Split: `project_original`

Input:

```text
内部服务之间也必须验证 TLS 证书。
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

### zhtw-project-it-api-cli-v1/it-079

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-079`
- Split: `project_original`

Input:

```text
错误页面不要暴露堆栈跟踪和服务器路径。
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

### zhtw-project-it-api-cli-v1/it-080

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-080`
- Split: `project_original`

Input:

```text
管理员下载资料前，需要再次确认身份。
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

### zhtw-project-it-api-cli-v1/it-081

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-081`
- Split: `project_original`

Input:

```text
指标标签不要使用用户编号等高基数数据。
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

### zhtw-project-it-api-cli-v1/it-082

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-082`
- Split: `project_original`

Input:

```text
分布式跟踪必须跨服务传递追踪编号。
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

### zhtw-project-it-api-cli-v1/it-083

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-083`
- Split: `project_original`

Input:

```text
告警条件应同时考虑错误率和请求量。
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

### zhtw-project-it-api-cli-v1/it-084

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-084`
- Split: `project_original`

Input:

```text
日志级别调整后，不需要重新启动服务。
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

### zhtw-project-it-api-cli-v1/it-085

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-085`
- Split: `project_original`

Input:

```text
仪表板上的延迟应显示分位数而不是平均值。
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

### zhtw-project-it-api-cli-v1/it-086

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-086`
- Split: `project_original`

Input:

```text
采样率变化必须记录在监控配置历史中。
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

### zhtw-project-it-api-cli-v1/it-087

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-087`
- Split: `project_original`

Input:

```text
健康检查请求不应污染业务访问日志。
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

### zhtw-project-it-api-cli-v1/it-088

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-088`
- Split: `project_original`

Input:

```text
错误预算耗尽后，暂停非必要的功能发布。
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

### zhtw-project-it-api-cli-v1/it-089

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-089`
- Split: `project_original`

Input:

```text
系统时间漂移会影响跨节点事件排序。
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

### zhtw-project-it-api-cli-v1/it-090

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-090`
- Split: `project_original`

Input:

```text
值班人员收到告警后，需要留下处理记录。
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

### zhtw-project-it-api-cli-v1/it-091

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-091`
- Split: `project_original`

Input:

```text
消息消费者必须能够安全处理重复事件。
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

### zhtw-project-it-api-cli-v1/it-092

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-092`
- Split: `project_original`

Input:

```text
事件格式新增字段时，旧消费者应继续正常工作。
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

### zhtw-project-it-api-cli-v1/it-093

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-093`
- Split: `project_original`

Input:

```text
队列积压超过阈值时，扩容消费者实例。
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

### zhtw-project-it-api-cli-v1/it-094

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-094`
- Split: `project_original`

Input:

```text
无法处理的消息应移到死信队列。
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

### zhtw-project-it-api-cli-v1/it-095

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-095`
- Split: `project_original`

Input:

```text
对象存储的公开读取权限必须明确关闭。
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

### zhtw-project-it-api-cli-v1/it-096

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-096`
- Split: `project_original`

Input:

```text
缓存失效后，避免大量请求同时查询数据库。
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

### zhtw-project-it-api-cli-v1/it-097

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-097`
- Split: `project_original`

Input:

```text
域名切换前，先降低 DNS 记录的生存时间。
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

### zhtw-project-it-api-cli-v1/it-098

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-098`
- Split: `project_original`

Input:

```text
区域故障演练不得依赖同一区域的控制服务。
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

### zhtw-project-it-api-cli-v1/it-099

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-099`
- Split: `project_original`

Input:

```text
配置中心不可用时，服务使用最后一次有效配置。
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

### zhtw-project-it-api-cli-v1/it-100

- Source: `zhtw-project-it-api-cli-v1`
- Source case: `it-100`
- Split: `project_original`

Input:

```text
远程端点恢复后，断路器应逐步允许测试请求。
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
