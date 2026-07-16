<!-- zhtw:disable -->
# Batch 12 新 miss Codex 語意分類

- Total: 15
- Acceptable variant: 7
- Public regression candidate: 8
- Strict private signal: 0
- Expected/output values included: false
- Promotion allowed: false

## Cases

- `blind-formal-0154`: `add_zhtw_output_as_acceptable_variant`
  - 正體字形存在語義相同的傳統異體，不應以單一 house style 判錯。
- `blind-formal-0158`: `add_zhtw_output_as_acceptable_variant`
  - 查核用字存在語義相同的正體異體，不應用於詞庫 tuning。
- `blind-high-risk-0103`: `add_zhtw_output_as_acceptable_variant`
  - 保險領域存在臺灣法規常用的同義角色名稱，語義未改變。
- `blind-high-risk-0105`: `add_zhtw_output_as_acceptable_variant`
  - 勞動與身分用語雖不同於 primary，但在臺灣語境語義等價。
- `blind-high-risk-0117`: `move_to_public_regression_candidate`
  - 備註欄位用字未符合臺灣通行正體，屬可公開重現的區域詞缺口。
- `blind-social-0165`: `move_to_public_regression_candidate`
  - 乾濕語境的多義字未依上下文轉換，屬真正語意缺口。
- `blind-social-0172`: `add_zhtw_output_as_acceptable_variant`
  - 消費付款語境的臺灣同義表達語意一致，不應強制單一用詞。
- `blind-it-0268`: `add_zhtw_output_as_acceptable_variant`
  - 容器映像術語存在帶「檔」與不帶「檔」的臺灣常見變體。
- `blind-it-0269`: `move_to_public_regression_candidate`
  - 核心訊息系統術語仍保留非臺灣區域詞，屬明確能力缺口。
- `blind-it-0271`: `move_to_public_regression_candidate`
  - Git commit message 的領域詞被轉成不同概念，應作公開回歸案例。
- `blind-it-0274`: `move_to_public_regression_candidate`
  - 設定項目的臺灣術語未完成區域轉換。
- `blind-ui-0210`: `move_to_public_regression_candidate`
  - UI 方位詞出現語義錯置，且表格欄位術語不正確。
- `blind-llm-0156`: `add_zhtw_output_as_acceptable_variant`
  - script 在臺灣技術文件有多個可接受譯法，語義一致。
- `blind-llm-0158`: `move_to_public_regression_candidate`
  - localization 被轉成 local-machine 概念，屬明確語義錯置。
- `blind-llm-0162`: `move_to_public_regression_candidate`
  - 原句表示通過複核，現有轉換弱化為經由複核，結果語義不同。
