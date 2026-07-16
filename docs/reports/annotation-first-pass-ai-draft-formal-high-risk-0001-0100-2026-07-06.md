<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：formal-high-risk 0001-0100（2026-07-06）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### formal-high-risk-0001

Input:

```text
市政府发布防灾公告。
```

AI draft expected:

```text
市政府發布防災公告。
```

Notes：公告語境：发布→發布、防灾→防災。

### formal-high-risk-0002

Input:

```text
气象局发出海上台风警报。
```

AI draft expected:

```text
氣象局發出海上颱風警報。
```

Notes：氣象警報語境：气象局→氣象局、台风→颱風。

### formal-high-risk-0003

Input:

```text
强降雨可能造成道路积水。
```

AI draft expected:

```text
強降雨可能造成道路積水。
```

Notes：災防語境：强→強、积水→積水。

### formal-high-risk-0004

Input:

```text
请民众避免前往山区。
```

AI draft expected:

```text
請民眾避免前往山區。
```

Notes：公共安全語境：请→請、民众→民眾、山区→山區。

### formal-high-risk-0005

Input:

```text
灾害应变中心二级开设。
```

AI draft expected:

```text
災害應變中心二級開設。
```

Notes：災害應變語境：灾害→災害、应变→應變、开设→開設。

### formal-high-risk-0006

Input:

```text
停班停课信息将于晚间公布。
```

AI draft expected:

```text
停班停課資訊將於晚間公布。
```

Notes：政府公告語境：停课→停課、信息→資訊、于→於。

### formal-high-risk-0007

Input:

```text
学校暂停户外课程。
```

AI draft expected:

```text
學校暫停戶外課程。
```

Notes：校園公告語境：学校→學校、暂停→暫停、课程→課程。

### formal-high-risk-0008

Input:

```text
会议纪要将上传至机关网站。
```

AI draft expected:

```text
會議紀要將上傳至機關網站。
```

Notes：公文語境：会议→會議、上传→上傳、机关网站→機關網站。

### formal-high-risk-0009

Input:

```text
本公告自发布日起生效。
```

AI draft expected:

```text
本公告自發布日起生效。
```

Notes：公告效力語境：发布日→發布日。

### formal-high-risk-0010

Input:

```text
记者会改为线上举行。
```

AI draft expected:

```text
記者會改為線上舉行。
```

Notes：新聞發布語境：记者会→記者會、线上→線上、举行→舉行。

### formal-high-risk-0011

Input:

```text
主管机关将召开说明会。
```

AI draft expected:

```text
主管機關將召開說明會。
```

Notes：政府程序語境：机关→機關、召开→召開、说明会→說明會。

### formal-high-risk-0012

Input:

```text
请下载最新申请表。
```

AI draft expected:

```text
請下載最新申請表。
```

Notes：申請文件語境：请→請、下载→下載、申请表→申請表。

### formal-high-risk-0013

Input:

```text
资料不全者将退回补件。
```

AI draft expected:

```text
資料不全者將退回補件。
```

Notes：行政審查語境：资料→資料、补件→補件。

### formal-high-risk-0014

Input:

```text
窗口受理时间延长至下午五点。
```

AI draft expected:

```text
窗口受理時間延長至下午五點。
```

Notes：行政服務語境：时间→時間、延长→延長、点→點。

### formal-high-risk-0015

Input:

```text
申请人应携带身份证明文件。
```

AI draft expected:

```text
申請人應攜帶身分證明文件。
```

Notes：行政申請語境：申请→申請、身份证明→身分證明。

### formal-high-risk-0016

Input:

```text
户籍资料不得任意外泄。
```

AI draft expected:

```text
戶籍資料不得任意外洩。
```

Notes：個資語境：户籍→戶籍、资料→資料、外泄→外洩。

### formal-high-risk-0017

Input:

```text
公文附件请依序编号。
```

AI draft expected:

```text
公文附件請依序編號。
```

Notes：公文格式語境：请→請、编号→編號。

### formal-high-risk-0018

Input:

```text
审查结果将以电子邮件通知。
```

AI draft expected:

```text
審查結果將以電子郵件通知。
```

Notes：行政審查語境：审查→審查、电子邮件→電子郵件。

### formal-high-risk-0019

Input:

```text
隐私声明已更新。
```

AI draft expected:

```text
隱私聲明已更新。
```

Notes：隱私文件語境：隐私→隱私、声明→聲明。

### formal-high-risk-0020

Input:

```text
缴费期限不得逾期。
```

AI draft expected:

```text
繳費期限不得逾期。
```

Notes：行政繳費語境：缴费→繳費。

### formal-high-risk-0021

Input:

```text
本合同经双方签署后生效。
```

AI draft expected:

```text
本合約經雙方簽署後生效。
```

Notes：契約語境：合同→合約、双方→雙方、签署后→簽署後。

### formal-high-risk-0022

Input:

```text
合同条款应以书面为准。
```

AI draft expected:

```text
合約條款應以書面為準。
```

Notes：契約條款語境：合同→合約、条款→條款、为准→為準。

### formal-high-risk-0023

Input:

```text
违约金计算方式如下。
```

AI draft expected:

```text
違約金計算方式如下。
```

Notes：法律/契約語境：违约→違約、计算→計算。

### formal-high-risk-0024

Input:

```text
争议应提交管辖法院处理。
```

AI draft expected:

```text
爭議應提交管轄法院處理。
```

Notes：爭議處理語境：争议→爭議、管辖→管轄、处理→處理。

### formal-high-risk-0025

Input:

```text
当事人应履行通知义务。
```

AI draft expected:

```text
當事人應履行通知義務。
```

Notes：法律義務語境：当事人→當事人、义务→義務。

### formal-high-risk-0026

Input:

```text
授权书需载明委托事项。
```

AI draft expected:

```text
授權書需載明委託事項。
```

Notes：授權文件語境：授权→授權、载明→載明、委托→委託。

### formal-high-risk-0027

Input:

```text
登记完成后不得擅自变更。
```

AI draft expected:

```text
登記完成後不得擅自變更。
```

Notes：登記程序語境：登记→登記、后→後、变更→變更。

### formal-high-risk-0028

Input:

```text
申请许可前请确认资格。
```

AI draft expected:

```text
申請許可前請確認資格。
```

Notes：許可程序語境：申请→申請、许可→許可、请→請。

### formal-high-risk-0029

Input:

```text
行政处分书已送达。
```

AI draft expected:

```text
行政處分書已送達。
```

Notes：行政法語境：处分书→處分書、送达→送達。

### formal-high-risk-0030

Input:

```text
权利义务不得转让。
```

AI draft expected:

```text
權利義務不得轉讓。
```

Notes：法律權利義務語境：权利义务→權利義務、转让→轉讓。

### formal-high-risk-0031

Input:

```text
诉讼期间仍须缴纳费用。
```

AI draft expected:

```text
訴訟期間仍須繳納費用。
```

Notes：訴訟語境：诉讼→訴訟、须→須、缴纳→繳納。

### formal-high-risk-0032

Input:

```text
法院裁定驳回申请。
```

AI draft expected:

```text
法院裁定駁回申請。
```

Notes：法院裁定語境：驳回→駁回、申请→申請。

### formal-high-risk-0033

Input:

```text
证据目录请另行附上。
```

AI draft expected:

```text
證據目錄請另行附上。
```

Notes：訴訟文件語境：证据→證據、目录→目錄、请→請。

### formal-high-risk-0034

Input:

```text
本案适用简易程序。
```

AI draft expected:

```text
本案適用簡易程序。
```

Notes：程序法語境：适用→適用、程序→程序。

### formal-high-risk-0035

Input:

```text
罚款应于期限内缴清。
```

AI draft expected:

```text
罰鍰應於期限內繳清。
```

Notes：台灣行政罰語境：罚款→罰鍰、于→於、缴清→繳清。

### formal-high-risk-0036

Input:

```text
公司章程修正案已备案。
```

AI draft expected:

```text
公司章程修正案已備案。
```

Notes：公司文件語境：备案→備案。

### formal-high-risk-0037

Input:

```text
股东会决议应保存备查。
```

AI draft expected:

```text
股東會決議應保存備查。
```

Notes：公司治理語境：股东会→股東會、决议→決議、备查→備查。

### formal-high-risk-0038

Input:

```text
营业执照副本需附印章。
```

AI draft expected:

```text
營業執照副本需附印章。
```

Notes：商業登記語境：营业→營業、执照→執照。

### formal-high-risk-0039

Input:

```text
债权人可依法请求清偿。
```

AI draft expected:

```text
債權人可依法請求清償。
```

Notes：債權語境：债权人→債權人、请求→請求、清偿→清償。

### formal-high-risk-0040

Input:

```text
不得以格式条款排除责任。
```

AI draft expected:

```text
不得以定型化契約條款排除責任。
```

Notes：台灣消保語境：格式条款→定型化契約條款、责任→責任。

### formal-high-risk-0041

Input:

```text
请确认银行账户号码。
```

AI draft expected:

```text
請確認銀行帳戶號碼。
```

Notes：金融帳戶語境：账户→帳戶、号码→號碼。

### formal-high-risk-0042

Input:

```text
转账失败时不会扣款。
```

AI draft expected:

```text
轉帳失敗時不會扣款。
```

Notes：金融交易語境：转账→轉帳、失败→失敗。

### formal-high-risk-0043

Input:

```text
跨行汇款手续费由用户承担。
```

AI draft expected:

```text
跨行匯款手續費由使用者負擔。
```

Notes：金融付款語境：汇款→匯款、手续费→手續費、用户→使用者、承担→負擔。

### formal-high-risk-0044

Input:

```text
贷款利率按年利率计算。
```

AI draft expected:

```text
貸款利率按年利率計算。
```

Notes：貸款語境：贷款→貸款、计算→計算。

### formal-high-risk-0045

Input:

```text
账单明细可在线查询。
```

AI draft expected:

```text
帳單明細可線上查詢。
```

Notes：帳務語境：账单→帳單、在线→線上、查询→查詢。

### formal-high-risk-0046

Input:

```text
余额不足将导致付款失败。
```

AI draft expected:

```text
餘額不足將導致付款失敗。
```

Notes：付款語境：余额→餘額、导致→導致、失败→失敗。

### formal-high-risk-0047

Input:

```text
电子发票已寄送至邮箱。
```

AI draft expected:

```text
電子發票已寄送至信箱。
```

Notes：發票通知語境：电子发票→電子發票、邮箱→信箱。

### formal-high-risk-0048

Input:

```text
税务资料请妥善保存。
```

AI draft expected:

```text
稅務資料請妥善保存。
```

Notes：稅務資料語境：税务→稅務、资料→資料、请→請。

### formal-high-risk-0049

Input:

```text
证券交易风险请自行评估。
```

AI draft expected:

```text
證券交易風險請自行評估。
```

Notes：證券揭露語境：证券→證券、风险→風險、评估→評估。

### formal-high-risk-0050

Input:

```text
基金净值每个交易日更新。
```

AI draft expected:

```text
基金淨值每個交易日更新。
```

Notes：基金資訊語境：净值→淨值、每个→每個。

### formal-high-risk-0051

Input:

```text
请勿泄露信用卡安全码。
```

AI draft expected:

```text
請勿洩露信用卡安全碼。
```

Notes：金融安全語境：泄露→洩露、码→碼。

### formal-high-risk-0052

Input:

```text
自动扣款授权可随时取消。
```

AI draft expected:

```text
自動扣款授權可隨時取消。
```

Notes：扣款授權語境：自动→自動、授权→授權、随时→隨時。

### formal-high-risk-0053

Input:

```text
退款金额将退回原付款账户。
```

AI draft expected:

```text
退款金額將退回原付款帳戶。
```

Notes：退款語境：金额→金額、账户→帳戶。

### formal-high-risk-0054

Input:

```text
请核对收款人姓名。
```

AI draft expected:

```text
請核對收款人姓名。
```

Notes：匯款確認語境：请→請、核对→核對。

### formal-high-risk-0055

Input:

```text
外币存款适用不同汇率。
```

AI draft expected:

```text
外幣存款適用不同匯率。
```

Notes：外幣交易語境：外币→外幣、适用→適用、汇率→匯率。

### formal-high-risk-0056

Input:

```text
电子对账单默认发送。
```

AI draft expected:

```text
電子對帳單預設寄送。
```

Notes：帳務通知語境：对账单→對帳單、默认→預設、发送→寄送。

### formal-high-risk-0057

Input:

```text
开户申请需完成身份验证。
```

AI draft expected:

```text
開戶申請需完成身分驗證。
```

Notes：金融 KYC 語境：开户→開戶、身份验证→身分驗證。

### formal-high-risk-0058

Input:

```text
本产品不保证收益。
```

AI draft expected:

```text
本產品不保證收益。
```

Notes：金融揭露語境：产品→產品、保证→保證、收益→收益。

### formal-high-risk-0059

Input:

```text
逾期缴款将产生滞纳金。
```

AI draft expected:

```text
逾期繳款將產生滯納金。
```

Notes：費用繳納語境：缴款→繳款、产生→產生、滞纳金→滯納金。

### formal-high-risk-0060

Input:

```text
网上银行服务暂时中断。
```

AI draft expected:

```text
網路銀行服務暫時中斷。
```

Notes：金融服務語境：网上银行→網路銀行、暂时→暫時。

### formal-high-risk-0061

Input:

```text
门诊预约已确认。
```

AI draft expected:

```text
門診預約已確認。
```

Notes：醫療掛號語境：门诊→門診、预约→預約、确认→確認。

### formal-high-risk-0062

Input:

```text
急诊检伤分类由现场人员判断。
```

AI draft expected:

```text
急診檢傷分類由現場人員判斷。
```

Notes：急診語境：急诊→急診、检伤→檢傷、现场→現場。

### formal-high-risk-0063

Input:

```text
请携带健保卡报到。
```

AI draft expected:

```text
請攜帶健保卡報到。
```

Notes：台灣醫療語境：请→請、携带→攜帶、健保卡保留台灣用語。

### formal-high-risk-0064

Input:

```text
筛查结果仅供医师参考。
```

AI draft expected:

```text
篩檢結果僅供醫師參考。
```

Notes：醫療檢查語境：筛查→篩檢、医师→醫師、参考→參考。

### formal-high-risk-0065

Input:

```text
复查时间请依医嘱安排。
```

AI draft expected:

```text
複診時間請依醫囑安排。
```

Notes：醫療回診語境：复查→複診、医嘱→醫囑。

### formal-high-risk-0066

Input:

```text
过敏史请主动告知护理师。
```

AI draft expected:

```text
過敏史請主動告知護理師。
```

Notes：病史告知語境：过敏→過敏、护理师→護理師。

### formal-high-risk-0067

Input:

```text
处方药应按剂量服用。
```

AI draft expected:

```text
處方藥應按劑量服用。
```

Notes：處方語境：处方药→處方藥、剂量→劑量。

### formal-high-risk-0068

Input:

```text
病历摘要可申请纸本副本。
```

AI draft expected:

```text
病歷摘要可申請紙本副本。
```

Notes：病歷申請語境：病历→病歷、申请→申請。

### formal-high-risk-0069

Input:

```text
检查报告预计三日后完成。
```

AI draft expected:

```text
檢查報告預計三日後完成。
```

Notes：檢查報告語境：检查→檢查、预计→預計、后→後。

### formal-high-risk-0070

Input:

```text
转诊单请交给柜台。
```

AI draft expected:

```text
轉診單請交給櫃檯。
```

Notes：轉診語境：转诊→轉診、柜台→櫃檯。

### formal-high-risk-0071

Input:

```text
疫苗接种纪录将同步更新。
```

AI draft expected:

```text
疫苗接種紀錄將同步更新。
```

Notes：疫苗語境：接种→接種、纪录→紀錄。

### formal-high-risk-0072

Input:

```text
发烧症状请先至分流站。
```

AI draft expected:

```text
發燒症狀請先至分流站。
```

Notes：公共衛生語境：发烧→發燒、症状→症狀。

### formal-high-risk-0073

Input:

```text
住院同意书需由本人签名。
```

AI draft expected:

```text
住院同意書需由本人簽名。
```

Notes：醫療同意書語境：签名→簽名。

### formal-high-risk-0074

Input:

```text
手术风险已于说明书载明。
```

AI draft expected:

```text
手術風險已於說明書載明。
```

Notes：醫療同意語境：手术→手術、风险→風險、于→於、载明→載明。

### formal-high-risk-0075

Input:

```text
药品保存条件请遵照标签。
```

AI draft expected:

```text
藥品保存條件請遵照標籤。
```

Notes：藥品標示語境：药品→藥品、条件→條件、标签→標籤。

### formal-high-risk-0076

Input:

```text
核酸检测阴性证明仍须上传。
```

AI draft expected:

```text
核酸檢測陰性證明仍須上傳。
```

Notes：檢測證明語境：检测→檢測、阴性→陰性、须→須、上传→上傳。

### formal-high-risk-0077

Input:

```text
慢性病连续处方笺可提前领取。
```

AI draft expected:

```text
慢性病連續處方箋可提前領取。
```

Notes：台灣醫療語境：连续处方笺→連續處方箋、领取→領取。

### formal-high-risk-0078

Input:

```text
孕妇产检补助额度已调整。
```

AI draft expected:

```text
孕婦產檢補助額度已調整。
```

Notes：產檢補助語境：孕妇→孕婦、产检→產檢、额度→額度、调整→調整。

### formal-high-risk-0079

Input:

```text
儿童预防接种请依时程办理。
```

AI draft expected:

```text
兒童預防接種請依時程辦理。
```

Notes：疫苗時程語境：儿童→兒童、接种→接種、时程→時程。

### formal-high-risk-0080

Input:

```text
疑似不良反应请回诊评估。
```

AI draft expected:

```text
疑似不良反應請回診評估。
```

Notes：醫療追蹤語境：反应→反應、回诊→回診、评估→評估。

### formal-high-risk-0081

Input:

```text
中央流行疫情指挥中心说明最新措施。
```

AI draft expected:

```text
中央流行疫情指揮中心說明最新措施。
```

Notes：公共衛生發布語境：指挥→指揮、说明→說明。

### formal-high-risk-0082

Input:

```text
道路施工期间请改道通行。
```

AI draft expected:

```text
道路施工期間請改道通行。
```

Notes：交通公告語境：期间→期間、请→請。

### formal-high-risk-0083

Input:

```text
公共工程进度每周公布。
```

AI draft expected:

```text
公共工程進度每週公布。
```

Notes：工程公告語境：进度→進度、每周→每週。

### formal-high-risk-0084

Input:

```text
捷运班距将视人潮调整。
```

AI draft expected:

```text
捷運班距將視人潮調整。
```

Notes：大眾運輸語境：捷运→捷運、调整→調整。

### formal-high-risk-0085

Input:

```text
公交线路临时改道。
```

AI draft expected:

```text
公車路線臨時改道。
```

Notes：台灣交通語境：公交线路→公車路線、临时→臨時。

### formal-high-risk-0086

Input:

```text
出租车乘车点移至东侧出口。
```

AI draft expected:

```text
計程車乘車點移至東側出口。
```

Notes：台灣交通語境：出租车→計程車、点→點、东侧→東側。

### formal-high-risk-0087

Input:

```text
停车场入口暂停开放。
```

AI draft expected:

```text
停車場入口暫停開放。
```

Notes：場站公告語境：停车场→停車場、暂停→暫停、开放→開放。

### formal-high-risk-0088

Input:

```text
环境影响评估报告公开展览。
```

AI draft expected:

```text
環境影響評估報告公開展覽。
```

Notes：環評語境：环境→環境、评估→評估。

### formal-high-risk-0089

Input:

```text
空气质量不良时建议减少外出。
```

AI draft expected:

```text
空氣品質不良時建議減少外出。
```

Notes：環境公告語境：空气质量→空氣品質、建议→建議。

### formal-high-risk-0090

Input:

```text
用水限制措施将分区实施。
```

AI draft expected:

```text
用水限制措施將分區實施。
```

Notes：民生公告語境：分区→分區、实施→實施。

### formal-high-risk-0091

Input:

```text
电力公司提醒用户节约用电。
```

AI draft expected:

```text
電力公司提醒用戶節約用電。
```

Notes：公共事業語境：电力→電力、用户→用戶、节约→節約。

### formal-high-risk-0092

Input:

```text
疫区返国旅客应主动申报。
```

AI draft expected:

```text
疫區返國旅客應主動申報。
```

Notes：邊境檢疫語境：疫区→疫區、返国→返國、申报→申報。

### formal-high-risk-0093

Input:

```text
新闻稿标题不得误导公众。
```

AI draft expected:

```text
新聞稿標題不得誤導公眾。
```

Notes：新聞稿語境：新闻稿→新聞稿、标题→標題、误导→誤導、公众→公眾。

### formal-high-risk-0094

Input:

```text
统计数据将于月底发布。
```

AI draft expected:

```text
統計數據將於月底發布。
```

Notes：統計發布語境：统计数据→統計數據、于→於、发布→發布。

### formal-high-risk-0095

Input:

```text
年度预算案送交议会审议。
```

AI draft expected:

```text
年度預算案送交議會審議。
```

Notes：議會審議語境：预算→預算、议会→議會、审议→審議。

### formal-high-risk-0096

Input:

```text
补助计划受理至名额额满为止。
```

AI draft expected:

```text
補助計畫受理至名額額滿為止。
```

Notes：補助公告語境：补助计划→補助計畫、额满→額滿、为止→為止。

### formal-high-risk-0097

Input:

```text
采购案决标结果已公告。
```

AI draft expected:

```text
採購案決標結果已公告。
```

Notes：政府採購語境：采购→採購、决标→決標。

### formal-high-risk-0098

Input:

```text
项目经费不得挪用于私人用途。
```

AI draft expected:

```text
計畫經費不得挪用於私人用途。
```

Notes：公共經費語境：项目→計畫、经费→經費、于→於。

### formal-high-risk-0099

Input:

```text
数据开放平台新增下载格式。
```

AI draft expected:

```text
資料開放平台新增下載格式。
```

Notes：開放資料語境：数据开放→資料開放、下载→下載。

### formal-high-risk-0100

Input:

```text
线上服务因维护暂停。
```

AI draft expected:

```text
線上服務因維護暫停。
```

Notes：公共服務語境：线上→線上、维护→維護、暂停→暫停。
