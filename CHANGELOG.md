# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.4.0] - 2025-12-26

### Added
- 進度條顯示：掃描檔案時顯示即時進度
  - TTY 模式：動態進度條 `掃描中 [████████░░░░] 50/100`
  - 非 TTY 模式（Jenkins/CI）：靜態輸出 `掃描中... 25% (25/100)`
- `--json` 模式自動停用進度顯示

## [2.3.0] - 2025-12-26

### Added
- `--show-diff` 選項：顯示修改預覽，確認後才執行
- `--backup` 選項：修改前備份原檔到 `.zhtw-backup/`
- 非 git 目錄警告：提醒使用者使用 --backup 或 --dry-run
- 142 個測試

## [2.2.0] - 2025-12-26

### Added
- `.zhtwignore` 檔案支援，可排除不需檢查的目錄和檔案
- 139 個測試（CLI、忽略指令、.zhtwignore）

### Fixed
- 測試檔案中未使用的 imports

## [2.1.0] - 2025-12-25

### Added
- 47 個 IT 術語（來自 OpenCC TWPhrasesIT.txt）
- `zhtw review` 預設啟用 LLM 驗證

### Changed
- 簡化 README，移除 LLM 功能文件（進階功能）

## [2.0.0] - 2025-12-24

### Added
- LLM 整合功能
  - `zhtw import` - 從外部來源匯入詞彙
  - `zhtw review` - 審核待匯入詞彙（支援 LLM 驗證）
  - `zhtw validate-llm` - 用 LLM 驗證詞庫正確性
  - `zhtw usage` - 顯示 LLM 用量統計
  - `zhtw config` - 管理設定
- 用量追蹤與成本控制

## [1.5.0] - 2025-12-24

### Added
- `zhtw stats` - 顯示詞庫統計資訊
- `zhtw validate` - 驗證詞庫品質（衝突、無效轉換）
- 忽略註解功能
  - `zhtw:disable-line` - 忽略當前行
  - `zhtw:disable-next` - 忽略下一行
  - `zhtw:disable` / `zhtw:enable` - 區塊忽略

### Changed
- 優化詞庫品質，移除無效轉換

## [1.0.0] - 2025-12-23

### Added
- 初始版本
- `zhtw check` - 檢查簡體中文
- `zhtw fix` - 自動修正
- 支援 cn（簡體）和 hk（港式）來源
- 330+ 精選詞彙（IT、商業、基礎）
- Aho-Corasick 高效匹配演算法
- `--json` 輸出（CI/CD 整合）
- `--dry-run` 模擬執行
- `--exclude` 排除目錄
- 自訂詞庫支援

[2.4.0]: https://github.com/rajatim/zhtw/compare/v2.3.0...v2.4.0
[2.3.0]: https://github.com/rajatim/zhtw/compare/v2.2.0...v2.3.0
[2.2.0]: https://github.com/rajatim/zhtw/compare/v2.1.0...v2.2.0
[2.1.0]: https://github.com/rajatim/zhtw/compare/v2.0.0...v2.1.0
[2.0.0]: https://github.com/rajatim/zhtw/compare/v1.5.0...v2.0.0
[1.5.0]: https://github.com/rajatim/zhtw/compare/v1.0.0...v1.5.0
[1.0.0]: https://github.com/rajatim/zhtw/releases/tag/v1.0.0
