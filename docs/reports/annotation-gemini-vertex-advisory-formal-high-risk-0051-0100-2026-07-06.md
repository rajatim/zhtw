<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：formal-high-risk-0051-formal-high-risk-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-formal-high-risk-0051-0100-2026-07-06.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 48
- Differences from Codex draft: 2

## Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### formal-high-risk-0051：different

Input:

```text
请勿泄露信用卡安全码。
```

Codex draft expected:

```text
請勿洩露信用卡安全碼。
```

Gemini advisory expected:

```text
請勿洩漏信用卡安全碼。
```

Gemini notes:

```text

```

### formal-high-risk-0052：match

Input:

```text
自动扣款授权可随时取消。
```

Codex draft expected:

```text
自動扣款授權可隨時取消。
```

Gemini advisory expected:

```text
自動扣款授權可隨時取消。
```

Gemini notes:

```text

```

### formal-high-risk-0053：match

Input:

```text
退款金额将退回原付款账户。
```

Codex draft expected:

```text
退款金額將退回原付款帳戶。
```

Gemini advisory expected:

```text
退款金額將退回原付款帳戶。
```

Gemini notes:

```text

```

### formal-high-risk-0054：match

Input:

```text
请核对收款人姓名。
```

Codex draft expected:

```text
請核對收款人姓名。
```

Gemini advisory expected:

```text
請核對收款人姓名。
```

Gemini notes:

```text

```

### formal-high-risk-0055：match

Input:

```text
外币存款适用不同汇率。
```

Codex draft expected:

```text
外幣存款適用不同匯率。
```

Gemini advisory expected:

```text
外幣存款適用不同匯率。
```

Gemini notes:

```text

```

### formal-high-risk-0056：match

Input:

```text
电子对账单默认发送。
```

Codex draft expected:

```text
電子對帳單預設寄送。
```

Gemini advisory expected:

```text
電子對帳單預設寄送。
```

Gemini notes:

```text
「默认」轉為「預設」，「发送」轉為「寄送」更符合台灣用語習慣。
```

### formal-high-risk-0057：match

Input:

```text
开户申请需完成身份验证。
```

Codex draft expected:

```text
開戶申請需完成身分驗證。
```

Gemini advisory expected:

```text
開戶申請需完成身分驗證。
```

Gemini notes:

```text
「身份」轉為「身分」為台灣常用寫法。
```

### formal-high-risk-0058：match

Input:

```text
本产品不保证收益。
```

Codex draft expected:

```text
本產品不保證收益。
```

Gemini advisory expected:

```text
本產品不保證收益。
```

Gemini notes:

```text

```

### formal-high-risk-0059：match

Input:

```text
逾期缴款将产生滞纳金。
```

Codex draft expected:

```text
逾期繳款將產生滯納金。
```

Gemini advisory expected:

```text
逾期繳款將產生滯納金。
```

Gemini notes:

```text

```

### formal-high-risk-0060：match

Input:

```text
网上银行服务暂时中断。
```

Codex draft expected:

```text
網路銀行服務暫時中斷。
```

Gemini advisory expected:

```text
網路銀行服務暫時中斷。
```

Gemini notes:

```text
「网上银行」轉為「網路銀行」為台灣常用稱呼。
```

### formal-high-risk-0061：match

Input:

```text
门诊预约已确认。
```

Codex draft expected:

```text
門診預約已確認。
```

Gemini advisory expected:

```text
門診預約已確認。
```

Gemini notes:

```text

```

### formal-high-risk-0062：match

Input:

```text
急诊检伤分类由现场人员判断。
```

Codex draft expected:

```text
急診檢傷分類由現場人員判斷。
```

Gemini advisory expected:

```text
急診檢傷分類由現場人員判斷。
```

Gemini notes:

```text

```

### formal-high-risk-0063：match

Input:

```text
请携带健保卡报到。
```

Codex draft expected:

```text
請攜帶健保卡報到。
```

Gemini advisory expected:

```text
請攜帶健保卡報到。
```

Gemini notes:

```text

```

### formal-high-risk-0064：match

Input:

```text
筛查结果仅供医师参考。
```

Codex draft expected:

```text
篩檢結果僅供醫師參考。
```

Gemini advisory expected:

```text
篩檢結果僅供醫師參考。
```

Gemini notes:

```text
「筛查」轉為「篩檢」為台灣常用醫學用語。
```

### formal-high-risk-0065：match

Input:

```text
复查时间请依医嘱安排。
```

Codex draft expected:

```text
複診時間請依醫囑安排。
```

Gemini advisory expected:

```text
複診時間請依醫囑安排。
```

Gemini notes:

```text
「复查」轉為「複診」更符合台灣醫學領域的語境。
```

### formal-high-risk-0066：match

Input:

```text
过敏史请主动告知护理师。
```

Codex draft expected:

```text
過敏史請主動告知護理師。
```

Gemini advisory expected:

```text
過敏史請主動告知護理師。
```

Gemini notes:

```text

```

### formal-high-risk-0067：match

Input:

```text
处方药应按剂量服用。
```

Codex draft expected:

```text
處方藥應按劑量服用。
```

Gemini advisory expected:

```text
處方藥應按劑量服用。
```

Gemini notes:

```text

```

### formal-high-risk-0068：match

Input:

```text
病历摘要可申请纸本副本。
```

Codex draft expected:

```text
病歷摘要可申請紙本副本。
```

Gemini advisory expected:

```text
病歷摘要可申請紙本副本。
```

Gemini notes:

```text

```

### formal-high-risk-0069：match

Input:

```text
检查报告预计三日后完成。
```

Codex draft expected:

```text
檢查報告預計三日後完成。
```

Gemini advisory expected:

```text
檢查報告預計三日後完成。
```

Gemini notes:

```text

```

### formal-high-risk-0070：match

Input:

```text
转诊单请交给柜台。
```

Codex draft expected:

```text
轉診單請交給櫃檯。
```

Gemini advisory expected:

```text
轉診單請交給櫃檯。
```

Gemini notes:

```text

```

### formal-high-risk-0071：match

Input:

```text
疫苗接种纪录将同步更新。
```

Codex draft expected:

```text
疫苗接種紀錄將同步更新。
```

Gemini advisory expected:

```text
疫苗接種紀錄將同步更新。
```

Gemini notes:

```text

```

### formal-high-risk-0072：match

Input:

```text
发烧症状请先至分流站。
```

Codex draft expected:

```text
發燒症狀請先至分流站。
```

Gemini advisory expected:

```text
發燒症狀請先至分流站。
```

Gemini notes:

```text

```

### formal-high-risk-0073：match

Input:

```text
住院同意书需由本人签名。
```

Codex draft expected:

```text
住院同意書需由本人簽名。
```

Gemini advisory expected:

```text
住院同意書需由本人簽名。
```

Gemini notes:

```text

```

### formal-high-risk-0074：match

Input:

```text
手术风险已于说明书载明。
```

Codex draft expected:

```text
手術風險已於說明書載明。
```

Gemini advisory expected:

```text
手術風險已於說明書載明。
```

Gemini notes:

```text

```

### formal-high-risk-0075：match

Input:

```text
药品保存条件请遵照标签。
```

Codex draft expected:

```text
藥品保存條件請遵照標籤。
```

Gemini advisory expected:

```text
藥品保存條件請遵照標籤。
```

Gemini notes:

```text

```

### formal-high-risk-0076：match

Input:

```text
核酸检测阴性证明仍须上传。
```

Codex draft expected:

```text
核酸檢測陰性證明仍須上傳。
```

Gemini advisory expected:

```text
核酸檢測陰性證明仍須上傳。
```

Gemini notes:

```text

```

### formal-high-risk-0077：match

Input:

```text
慢性病连续处方笺可提前领取。
```

Codex draft expected:

```text
慢性病連續處方箋可提前領取。
```

Gemini advisory expected:

```text
慢性病連續處方箋可提前領取。
```

Gemini notes:

```text

```

### formal-high-risk-0078：match

Input:

```text
孕妇产检补助额度已调整。
```

Codex draft expected:

```text
孕婦產檢補助額度已調整。
```

Gemini advisory expected:

```text
孕婦產檢補助額度已調整。
```

Gemini notes:

```text

```

### formal-high-risk-0079：match

Input:

```text
儿童预防接种请依时程办理。
```

Codex draft expected:

```text
兒童預防接種請依時程辦理。
```

Gemini advisory expected:

```text
兒童預防接種請依時程辦理。
```

Gemini notes:

```text

```

### formal-high-risk-0080：match

Input:

```text
疑似不良反应请回诊评估。
```

Codex draft expected:

```text
疑似不良反應請回診評估。
```

Gemini advisory expected:

```text
疑似不良反應請回診評估。
```

Gemini notes:

```text

```

### formal-high-risk-0081：match

Input:

```text
中央流行疫情指挥中心说明最新措施。
```

Codex draft expected:

```text
中央流行疫情指揮中心說明最新措施。
```

Gemini advisory expected:

```text
中央流行疫情指揮中心說明最新措施。
```

Gemini notes:

```text

```

### formal-high-risk-0082：match

Input:

```text
道路施工期间请改道通行。
```

Codex draft expected:

```text
道路施工期間請改道通行。
```

Gemini advisory expected:

```text
道路施工期間請改道通行。
```

Gemini notes:

```text

```

### formal-high-risk-0083：match

Input:

```text
公共工程进度每周公布。
```

Codex draft expected:

```text
公共工程進度每週公布。
```

Gemini advisory expected:

```text
公共工程進度每週公布。
```

Gemini notes:

```text

```

### formal-high-risk-0084：match

Input:

```text
捷运班距将视人潮调整。
```

Codex draft expected:

```text
捷運班距將視人潮調整。
```

Gemini advisory expected:

```text
捷運班距將視人潮調整。
```

Gemini notes:

```text

```

### formal-high-risk-0085：match

Input:

```text
公交线路临时改道。
```

Codex draft expected:

```text
公車路線臨時改道。
```

Gemini advisory expected:

```text
公車路線臨時改道。
```

Gemini notes:

```text
「公交」轉為「公車」，「线路」轉為「路線」為台灣常用稱呼。
```

### formal-high-risk-0086：match

Input:

```text
出租车乘车点移至东侧出口。
```

Codex draft expected:

```text
計程車乘車點移至東側出口。
```

Gemini advisory expected:

```text
計程車乘車點移至東側出口。
```

Gemini notes:

```text
「出租车」轉為「計程車」為台灣常用稱呼。
```

### formal-high-risk-0087：match

Input:

```text
停车场入口暂停开放。
```

Codex draft expected:

```text
停車場入口暫停開放。
```

Gemini advisory expected:

```text
停車場入口暫停開放。
```

Gemini notes:

```text

```

### formal-high-risk-0088：match

Input:

```text
环境影响评估报告公开展览。
```

Codex draft expected:

```text
環境影響評估報告公開展覽。
```

Gemini advisory expected:

```text
環境影響評估報告公開展覽。
```

Gemini notes:

```text

```

### formal-high-risk-0089：match

Input:

```text
空气质量不良时建议减少外出。
```

Codex draft expected:

```text
空氣品質不良時建議減少外出。
```

Gemini advisory expected:

```text
空氣品質不良時建議減少外出。
```

Gemini notes:

```text
「质量」轉為「品質」為台灣常用詞。
```

### formal-high-risk-0090：match

Input:

```text
用水限制措施将分区实施。
```

Codex draft expected:

```text
用水限制措施將分區實施。
```

Gemini advisory expected:

```text
用水限制措施將分區實施。
```

Gemini notes:

```text

```

### formal-high-risk-0091：match

Input:

```text
电力公司提醒用户节约用电。
```

Codex draft expected:

```text
電力公司提醒用戶節約用電。
```

Gemini advisory expected:

```text
電力公司提醒用戶節約用電。
```

Gemini notes:

```text

```

### formal-high-risk-0092：match

Input:

```text
疫区返国旅客应主动申报。
```

Codex draft expected:

```text
疫區返國旅客應主動申報。
```

Gemini advisory expected:

```text
疫區返國旅客應主動申報。
```

Gemini notes:

```text

```

### formal-high-risk-0093：match

Input:

```text
新闻稿标题不得误导公众。
```

Codex draft expected:

```text
新聞稿標題不得誤導公眾。
```

Gemini advisory expected:

```text
新聞稿標題不得誤導公眾。
```

Gemini notes:

```text

```

### formal-high-risk-0094：match

Input:

```text
统计数据将于月底发布。
```

Codex draft expected:

```text
統計數據將於月底發布。
```

Gemini advisory expected:

```text
統計數據將於月底發布。
```

Gemini notes:

```text

```

### formal-high-risk-0095：match

Input:

```text
年度预算案送交议会审议。
```

Codex draft expected:

```text
年度預算案送交議會審議。
```

Gemini advisory expected:

```text
年度預算案送交議會審議。
```

Gemini notes:

```text

```

### formal-high-risk-0096：match

Input:

```text
补助计划受理至名额额满为止。
```

Codex draft expected:

```text
補助計畫受理至名額額滿為止。
```

Gemini advisory expected:

```text
補助計畫受理至名額額滿為止。
```

Gemini notes:

```text

```

### formal-high-risk-0097：match

Input:

```text
采购案决标结果已公告。
```

Codex draft expected:

```text
採購案決標結果已公告。
```

Gemini advisory expected:

```text
採購案決標結果已公告。
```

Gemini notes:

```text

```

### formal-high-risk-0098：different

Input:

```text
项目经费不得挪用于私人用途。
```

Codex draft expected:

```text
計畫經費不得挪用於私人用途。
```

Gemini advisory expected:

```text
專案經費不得挪用於私人用途。
```

Gemini notes:

```text
「项目」轉為「專案」更符合台灣正式文件語境。
```

### formal-high-risk-0099：match

Input:

```text
数据开放平台新增下载格式。
```

Codex draft expected:

```text
資料開放平台新增下載格式。
```

Gemini advisory expected:

```text
資料開放平台新增下載格式。
```

Gemini notes:

```text
「数据」轉為「資料」更符合台灣常用詞。
```

### formal-high-risk-0100：match

Input:

```text
线上服务因维护暂停。
```

Codex draft expected:

```text
線上服務因維護暫停。
```

Gemini advisory expected:

```text
線上服務因維護暫停。
```

Gemini notes:

```text

```
