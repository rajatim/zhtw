# Holdout Remaining Signal Summary: After Batch10 Miss Review

- Generated date: `2026-07-13`
- Dataset: `blind-v1`
- Current sealed cases: `751`
- Current accepted: `719`
- Remaining misses/signals: `32`
- Public regression candidates: `0`
- Expected recheck cases: `0`
- Converter/dictionary updates from these signals: `false`

Sealed content policy: this report contains case ids and metadata only. It omits sealed inputs, expected values, acceptable variants, converter outputs, and benchmark rows.

## Summary

- By domain: `{'formal': 6, 'high_risk': 8, 'it': 3, 'llm': 4, 'social': 6, 'ui': 5}`
- By risk: `{'baseline_guard': 1, 'candidate_gap': 2, 'over_conversion_guard': 29}`
- By signal category: `{'high_risk_holdout_signal': 8, 'over_conversion_guard_holdout_signal': 24}`
- Non-idempotent signal case ids: `['blind-ui-0147']`

## Case Signals

- `blind-llm-0026`: domain=`llm`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-llm-0028`: domain=`llm`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-formal-0029`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-social-0025`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-social-0026`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-it-0083`: domain=`it`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-ui-0060`: domain=`ui`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-ui-0061`: domain=`ui`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-llm-0043`: domain=`llm`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-llm-0044`: domain=`llm`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-formal-0043`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-formal-0044`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-formal-0045`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-formal-0046`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-social-0042`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-social-0043`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-social-0044`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-high-risk-0026`: domain=`high_risk`, risk=`over_conversion_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-high-risk-0027`: domain=`high_risk`, risk=`over_conversion_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-it-0108`: domain=`it`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-ui-0081`: domain=`ui`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-high-risk-0039`: domain=`high_risk`, risk=`over_conversion_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-it-0131`: domain=`it`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-ui-0102`: domain=`ui`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-high-risk-0053`: domain=`high_risk`, risk=`candidate_gap`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-high-risk-0058`: domain=`high_risk`, risk=`over_conversion_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-ui-0147`: domain=`ui`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`False`
- `blind-formal-0105`: domain=`formal`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-high-risk-0064`: domain=`high_risk`, risk=`candidate_gap`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-high-risk-0068`: domain=`high_risk`, risk=`baseline_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
- `blind-social-0110`: domain=`social`, risk=`over_conversion_guard`, signal=`over_conversion_guard_holdout_signal`, idempotent=`True`
- `blind-high-risk-0084`: domain=`high_risk`, risk=`over_conversion_guard`, signal=`high_risk_holdout_signal`, idempotent=`True`
