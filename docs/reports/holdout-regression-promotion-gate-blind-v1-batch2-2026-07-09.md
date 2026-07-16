<!-- zhtw:disable -->
# Holdout Regression Promotion Gate - blind-v1 batch2

Generated: `2026-07-09`

These cases were removed from sealed holdout before tuning. Inputs, expected values, and actual outputs are public in this report.

## Summary

- checked: 5
- promotion_ready: 5
- needs_zhtw_fix: 0
- convert_matches: 5
- convert_mismatches: 0
- expected_idempotent: 5
- expected_not_idempotent: 0
- output_idempotent: 5
- output_not_idempotent: 0

## Promotion Ready

### blind-it-0014

- Promoted id: `holdout/blind-it-0014`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
合并请求通过检查后，机器人会自动发布预览版本。
```

Expected:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

Actual:

```text
合併請求通過檢查後，機器人會自動發布預覽版本。
```

### blind-ui-0002

- Promoted id: `holdout/blind-ui-0002`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
请输入验证码，系统会发送简讯到你的手机。
```

Expected:

```text
請輸入驗證碼，系統會傳送簡訊到你的手機。
```

Actual:

```text
請輸入驗證碼，系統會傳送簡訊到你的手機。
```

### blind-formal-0006

- Promoted id: `holdout/blind-formal-0006`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
会议记录应列明出席人员和决议事项。
```

Expected:

```text
會議紀錄應列明出席人員和決議事項。
```

Actual:

```text
會議紀錄應列明出席人員和決議事項。
```

### blind-formal-0010

- Promoted id: `holdout/blind-formal-0010`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
新闻稿指出，合作项目不会影响现有用户权益。
```

Expected:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

Actual:

```text
新聞稿指出，合作專案不會影響現有使用者權益。
```

### blind-social-0015

- Promoted id: `holdout/blind-social-0015`
- Status: `promotion_ready`
- Convert matches: `True`
- Expected idempotent: `True`

Input:

```text
今天的直播回放什么时候会上架？
```

Expected:

```text
今天的直播重播什麼時候會上架？
```

Actual:

```text
今天的直播重播什麼時候會上架？
```
