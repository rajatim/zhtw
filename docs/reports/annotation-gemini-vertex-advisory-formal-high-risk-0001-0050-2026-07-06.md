<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：formal-high-risk-0001-formal-high-risk-0050（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0001-0050-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 43
- Differences from Codex draft: 7

## Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### formal-high-risk-0001：match

Input:

```text
市政府发布防灾公告。
```

Codex draft expected:

```text
市政府發布防災公告。
```

Gemini advisory expected:

```text
市政府發布防災公告。
```

Gemini notes:

```text
「發布」為台灣常用詞。
```

### formal-high-risk-0002：different

Input:

```text
气象局发出海上台风警报。
```

Codex draft expected:

```text
氣象局發出海上颱風警報。
```

Gemini advisory expected:

```text
氣象局發布海上颱風警報。
```

Gemini notes:

```text
「氣象局」、「發出」改為「發布」、「颱風」為台灣常用詞。
```

### formal-high-risk-0003：match

Input:

```text
强降雨可能造成道路积水。
```

Codex draft expected:

```text
強降雨可能造成道路積水。
```

Gemini advisory expected:

```text
強降雨可能造成道路積水。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0004：match

Input:

```text
请民众避免前往山区。
```

Codex draft expected:

```text
請民眾避免前往山區。
```

Gemini advisory expected:

```text
請民眾避免前往山區。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0005：match

Input:

```text
灾害应变中心二级开设。
```

Codex draft expected:

```text
災害應變中心二級開設。
```

Gemini advisory expected:

```text
災害應變中心二級開設。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0006：match

Input:

```text
停班停课信息将于晚间公布。
```

Codex draft expected:

```text
停班停課資訊將於晚間公布。
```

Gemini advisory expected:

```text
停班停課資訊將於晚間公布。
```

Gemini notes:

```text
「信息」改為「資訊」，繁體字轉換。
```

### formal-high-risk-0007：match

Input:

```text
学校暂停户外课程。
```

Codex draft expected:

```text
學校暫停戶外課程。
```

Gemini advisory expected:

```text
學校暫停戶外課程。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0008：different

Input:

```text
会议纪要将上传至机关网站。
```

Codex draft expected:

```text
會議紀要將上傳至機關網站。
```

Gemini advisory expected:

```text
會議紀錄將上傳至機關網站。
```

Gemini notes:

```text
「会议纪要」改為「會議紀錄」，繁體字轉換。
```

### formal-high-risk-0009：match

Input:

```text
本公告自发布日起生效。
```

Codex draft expected:

```text
本公告自發布日起生效。
```

Gemini advisory expected:

```text
本公告自發布日起生效。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0010：match

Input:

```text
记者会改为线上举行。
```

Codex draft expected:

```text
記者會改為線上舉行。
```

Gemini advisory expected:

```text
記者會改為線上舉行。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0011：match

Input:

```text
主管机关将召开说明会。
```

Codex draft expected:

```text
主管機關將召開說明會。
```

Gemini advisory expected:

```text
主管機關將召開說明會。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0012：match

Input:

```text
请下载最新申请表。
```

Codex draft expected:

```text
請下載最新申請表。
```

Gemini advisory expected:

```text
請下載最新申請表。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0013：match

Input:

```text
资料不全者将退回补件。
```

Codex draft expected:

```text
資料不全者將退回補件。
```

Gemini advisory expected:

```text
資料不全者將退回補件。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0014：match

Input:

```text
窗口受理时间延长至下午五点。
```

Codex draft expected:

```text
窗口受理時間延長至下午五點。
```

Gemini advisory expected:

```text
窗口受理時間延長至下午五點。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0015：match

Input:

```text
申请人应携带身份证明文件。
```

Codex draft expected:

```text
申請人應攜帶身分證明文件。
```

Gemini advisory expected:

```text
申請人應攜帶身分證明文件。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0016：match

Input:

```text
户籍资料不得任意外泄。
```

Codex draft expected:

```text
戶籍資料不得任意外洩。
```

Gemini advisory expected:

```text
戶籍資料不得任意外洩。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0017：match

Input:

```text
公文附件请依序编号。
```

Codex draft expected:

```text
公文附件請依序編號。
```

Gemini advisory expected:

```text
公文附件請依序編號。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0018：match

Input:

```text
审查结果将以电子邮件通知。
```

Codex draft expected:

```text
審查結果將以電子郵件通知。
```

Gemini advisory expected:

```text
審查結果將以電子郵件通知。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0019：different

Input:

```text
隐私声明已更新。
```

Codex draft expected:

```text
隱私聲明已更新。
```

Gemini advisory expected:

```text
隱私權聲明已更新。
```

Gemini notes:

```text
「隐私声明」改為「隱私權聲明」，繁體字轉換。
```

### formal-high-risk-0020：match

Input:

```text
缴费期限不得逾期。
```

Codex draft expected:

```text
繳費期限不得逾期。
```

Gemini advisory expected:

```text
繳費期限不得逾期。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0021：match

Input:

```text
本合同经双方签署后生效。
```

Codex draft expected:

```text
本合約經雙方簽署後生效。
```

Gemini advisory expected:

```text
本合約經雙方簽署後生效。
```

Gemini notes:

```text
「合同」改為「合約」，繁體字轉換。
```

### formal-high-risk-0022：match

Input:

```text
合同条款应以书面为准。
```

Codex draft expected:

```text
合約條款應以書面為準。
```

Gemini advisory expected:

```text
合約條款應以書面為準。
```

Gemini notes:

```text
「合同」改為「合約」，繁體字轉換。
```

### formal-high-risk-0023：match

Input:

```text
违约金计算方式如下。
```

Codex draft expected:

```text
違約金計算方式如下。
```

Gemini advisory expected:

```text
違約金計算方式如下。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0024：match

Input:

```text
争议应提交管辖法院处理。
```

Codex draft expected:

```text
爭議應提交管轄法院處理。
```

Gemini advisory expected:

```text
爭議應提交管轄法院處理。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0025：match

Input:

```text
当事人应履行通知义务。
```

Codex draft expected:

```text
當事人應履行通知義務。
```

Gemini advisory expected:

```text
當事人應履行通知義務。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0026：match

Input:

```text
授权书需载明委托事项。
```

Codex draft expected:

```text
授權書需載明委託事項。
```

Gemini advisory expected:

```text
授權書需載明委託事項。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0027：match

Input:

```text
登记完成后不得擅自变更。
```

Codex draft expected:

```text
登記完成後不得擅自變更。
```

Gemini advisory expected:

```text
登記完成後不得擅自變更。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0028：match

Input:

```text
申请许可前请确认资格。
```

Codex draft expected:

```text
申請許可前請確認資格。
```

Gemini advisory expected:

```text
申請許可前請確認資格。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0029：match

Input:

```text
行政处分书已送达。
```

Codex draft expected:

```text
行政處分書已送達。
```

Gemini advisory expected:

```text
行政處分書已送達。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0030：match

Input:

```text
权利义务不得转让。
```

Codex draft expected:

```text
權利義務不得轉讓。
```

Gemini advisory expected:

```text
權利義務不得轉讓。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0031：match

Input:

```text
诉讼期间仍须缴纳费用。
```

Codex draft expected:

```text
訴訟期間仍須繳納費用。
```

Gemini advisory expected:

```text
訴訟期間仍須繳納費用。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0032：match

Input:

```text
法院裁定驳回申请。
```

Codex draft expected:

```text
法院裁定駁回申請。
```

Gemini advisory expected:

```text
法院裁定駁回申請。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0033：match

Input:

```text
证据目录请另行附上。
```

Codex draft expected:

```text
證據目錄請另行附上。
```

Gemini advisory expected:

```text
證據目錄請另行附上。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0034：match

Input:

```text
本案适用简易程序。
```

Codex draft expected:

```text
本案適用簡易程序。
```

Gemini advisory expected:

```text
本案適用簡易程序。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0035：different

Input:

```text
罚款应于期限内缴清。
```

Codex draft expected:

```text
罰鍰應於期限內繳清。
```

Gemini advisory expected:

```text
罰款應於期限內繳清。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0036：match

Input:

```text
公司章程修正案已备案。
```

Codex draft expected:

```text
公司章程修正案已備案。
```

Gemini advisory expected:

```text
公司章程修正案已備案。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0037：match

Input:

```text
股东会决议应保存备查。
```

Codex draft expected:

```text
股東會決議應保存備查。
```

Gemini advisory expected:

```text
股東會決議應保存備查。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0038：different

Input:

```text
营业执照副本需附印章。
```

Codex draft expected:

```text
營業執照副本需附印章。
```

Gemini advisory expected:

```text
營業執照影本需附印章。
```

Gemini notes:

```text
「副本」改為「影本」，繁體字轉換。
```

### formal-high-risk-0039：match

Input:

```text
债权人可依法请求清偿。
```

Codex draft expected:

```text
債權人可依法請求清償。
```

Gemini advisory expected:

```text
債權人可依法請求清償。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0040：different

Input:

```text
不得以格式条款排除责任。
```

Codex draft expected:

```text
不得以定型化契約條款排除責任。
```

Gemini advisory expected:

```text
不得以格式條款排除責任。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0041：match

Input:

```text
请确认银行账户号码。
```

Codex draft expected:

```text
請確認銀行帳戶號碼。
```

Gemini advisory expected:

```text
請確認銀行帳戶號碼。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0042：match

Input:

```text
转账失败时不会扣款。
```

Codex draft expected:

```text
轉帳失敗時不會扣款。
```

Gemini advisory expected:

```text
轉帳失敗時不會扣款。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0043：different

Input:

```text
跨行汇款手续费由用户承担。
```

Codex draft expected:

```text
跨行匯款手續費由使用者負擔。
```

Gemini advisory expected:

```text
跨行匯款手續費由使用者承擔。
```

Gemini notes:

```text
「用户」改為「使用者」，繁體字轉換。
```

### formal-high-risk-0044：match

Input:

```text
贷款利率按年利率计算。
```

Codex draft expected:

```text
貸款利率按年利率計算。
```

Gemini advisory expected:

```text
貸款利率按年利率計算。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0045：match

Input:

```text
账单明细可在线查询。
```

Codex draft expected:

```text
帳單明細可線上查詢。
```

Gemini advisory expected:

```text
帳單明細可線上查詢。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0046：match

Input:

```text
余额不足将导致付款失败。
```

Codex draft expected:

```text
餘額不足將導致付款失敗。
```

Gemini advisory expected:

```text
餘額不足將導致付款失敗。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0047：match

Input:

```text
电子发票已寄送至邮箱。
```

Codex draft expected:

```text
電子發票已寄送至信箱。
```

Gemini advisory expected:

```text
電子發票已寄送至信箱。
```

Gemini notes:

```text
「邮箱」改為「信箱」，繁體字轉換。
```

### formal-high-risk-0048：match

Input:

```text
税务资料请妥善保存。
```

Codex draft expected:

```text
稅務資料請妥善保存。
```

Gemini advisory expected:

```text
稅務資料請妥善保存。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0049：match

Input:

```text
证券交易风险请自行评估。
```

Codex draft expected:

```text
證券交易風險請自行評估。
```

Gemini advisory expected:

```text
證券交易風險請自行評估。
```

Gemini notes:

```text
繁體字轉換。
```

### formal-high-risk-0050：match

Input:

```text
基金净值每个交易日更新。
```

Codex draft expected:

```text
基金淨值每個交易日更新。
```

Gemini advisory expected:

```text
基金淨值每個交易日更新。
```

Gemini notes:

```text
繁體字轉換。
```
