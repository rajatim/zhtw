<!-- zhtw:disable -->
# Gemini Policy Review - batch7 miss classification

Generated: `2026-07-10`

Gemini reviewed sanitized metadata only. Sealed inputs, expected values, acceptable variants, converter outputs, and benchmark rows were not provided.

## Summary

- Policy passed: True
- Classification changes recommended: 0
- Summary: 本審查報告完全符合密封內容政策（Sealed Content Policy），未洩露任何敏感的輸入、預期值、實際輸出或可接受變體。過度轉換防護案例皆已正確保留為私有保留訊號；所有高風險案例亦無列入公開迴歸候選。所有移動至公開迴歸候選與預期值重新檢查之案例，均已確實標記需要維護者確認並自密封保留集中移除後才可進行調校，非冪等輸出標記亦與後續追蹤清單一致，政策審查通過。

## Findings

### over_conversion_guard_cases

- Severity: `info`
- Finding: 所有 25 個過度轉換防護（over_conversion_guard）案例均正確設置為 keep_as_holdout_signal，符合保留為私有壓力訊號之規範。

### high_risk_cases

- Severity: `info`
- Finding: 所有 5 個高風險（high_risk）案例皆已正確排除在 move_to_public_regression_candidate 之外，維持為私有保留訊號。

### public_regression_candidate_cases

- Severity: `info`
- Finding: 所有 17 個 move_to_public_regression_candidate 案例均正確設定 needs_maintainer_review 為 true，並要求先從 sealed holdout 移除才進行 tuning，符合流程安全標準。

### expected_recheck_cases

- Severity: `info`
- Finding: 所有 7 個 requires_expected_recheck 案例均已標記 needs_maintainer_review 且限制需經維護者審查後方能更新私有預期值或可接受變體。

### non_idempotent_miss_ids

- Severity: `info`
- Finding: 5 個 non_idempotent_output 案例已正確標記並登載於 idempotency_notes 追蹤清單，將於後續 promotion 前進行處理。
