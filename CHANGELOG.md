# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.8.5] - 2026-01-05

### Changed
- **validate 命令大幅改善**：808 警告 → 0
  - 預設跳過 identity mapping（設計如此）
  - 區分同來源衝突（bug）與跨來源衝突（設計）
  - 新增 `--strict` 選項顯示完整資訊
- 測試覆蓋率提升：82% → 90%
- 新增 Codecov 整合與徽章

### Fixed
- 移除 28 個跨檔案重複詞彙
- 修正「控制台」衝突（控制台→控制台 vs 控制台→主控台）
- 修正「奶油」連鎖轉換問題

## [2.8.4] - 2026-01-04

### Changed
- 完整測試 Jenkins Pipeline（含 GitHub Release）

## [2.8.3] - 2026-01-04

### Changed
- 測試 Jenkins Pipeline 發佈流程

## [2.8.2] - 2026-01-04

### Changed
- 新增 Jenkins 發佈流程

## [2.8.1] - 2026-01-04

### Changed
- 精簡發佈 SOP 文件

## [2.8.0] - 2026-01-04

### Added
- **單檔案掃描模式**：現在可以直接對單一檔案執行 check 或 fix
  - `zhtw check ./file.py`
  - `zhtw fix ./file.py`
- CLI 訊息區分檔案（📄）和目錄（📁）圖示
- 版本發佈 SOP 文件（`.claude/guides/releasing.md`）

### Fixed
- 補齊 77 條基礎簡繁字元對應（P0）
- 統一術語 key 格式為簡體（P1）
- 補上 隨身碟→隨身碟 轉換（P2）

## [2.7.0] - 2026-01-03

### Added
- **詞庫重大擴充**：433 → 3,490 詞彙（8 倍成長）
- 10+ 專業領域詞庫：
  - 醫療健康（230+）、法律合規（170+）、金融財務（140+）
  - 遊戲娛樂（150+）、電商零售（110+）、學術教育（110+）
  - 每日生活（230+）、地理國名（160+）、商業基礎（80+）
- 22 個一對多危險字完整覆蓋（發/髮、面/麵、裡/裡 等）

### Fixed
- 語義衝突智慧處理（禁用/撤銷/登出 在 UI 語境的正確轉換）

### Changed
- 使用 Trusted Publishing 發佈到 PyPI

## [2.6.0] - 2026-01-03

### Added
- 900+ 高頻簡體單字轉換（詞庫從 ~1100 → 2071 個詞彙）
  - 涵蓋人稱代詞：們→們、他→他
  - 常用動詞：說→說、會→會、進→進、動→動
  - 常用名詞：國→國、時→時、機→機、電→電
  - 形容詞副詞：難→難、專→專、遠→遠

### Fixed
- 修正 identity mapping 阻擋長詞轉換問題
  - 例如「件→件」不再阻擋「軟體→軟體」
  - 保留正確的保護機制（如「檔案」保護免受「文件」影響）

## [2.5.0] - 2025-12-31

### Added
- 一對多危險字完整覆蓋（22 個字）
  - 發→發/髮、面→面/麵、裡→裡/裡、後→後/後
  - 複→複/復、幹→幹/乾、隻→隻/隻 等
- 完整測試覆蓋（208 個測試案例）

### Changed
- 最佳化 Token 使用：AI 檔案分層架構

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
- 簡化 README，移除 LLM 功能檔案（進階功能）

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
