<!-- zhtw:disable -->
# Holdout Maintainer Confirmation Packet - blind-v1 Expansion Policy Review

Dataset: `blind-v1`
Source diff review: `docs/reports/holdout-codex-gemini-diff-review-blind-v1-expansion-127-cases-2026-07-09.json`
Raw JSON: `docs/reports/holdout-maintainer-confirmation-blind-v1-expansion-policy-review-2026-07-09.json`
Scope: `expansion_policy_review_only`

## Boundary

- This packet is for maintainer confirmation only.
- It includes only Codex/Gemini exact-match cases that still need policy review.
- Codex/Gemini values are advisory; maintainer confirmation is the first human decision.
- Do not write these values into `blind-v1.expected.json` until maintainer decisions are recorded.
- `promotion_allowed = false` until expected values are confirmed and source metadata is updated.

## Summary

- Cases needing maintainer confirmation: 33
- Policy-review cases: 33
- Difference cases: 0
- No immediate-question cases: 46

Domain:

- `formal`: 4
- `high_risk`: 8
- `it`: 3
- `llm`: 4
- `social`: 5
- `ui`: 9

Risk:

- `baseline_guard`: 3
- `candidate_gap`: 14
- `over_conversion_guard`: 16

## How To Review

For each case, choose one:

- `OK` means accept `Recommended expected` unchanged.
- `EDIT` means write a replacement Taiwan Traditional expected value.
- `DROP` means remove the case from sealed holdout before benchmark.

## Policy Review Cases

### blind-it-0040：Codex/Gemini exact match

- Domain: `it`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
我们需要记录每个请求的追踪编号。
```

Recommended expected:

```text
我們需要記錄每個請求的追蹤編號。
```

Codex rationale:

```text
trace id 可譯「追蹤編號」或保留 ID，需看產品風格。
```

Gemini notes:

```text
「我们」轉「我們」，「记录」轉「記錄」，「追踪编号」轉「追蹤編號」。
```

Maintainer decision:

```text

```

### blind-it-0053：Codex/Gemini exact match

- Domain: `it`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
这个程序会保留用户自定义的模板名称。
```

Recommended expected:

```text
這個程式會保留使用者自訂的範本名稱。
```

Codex rationale:

```text
over-conversion guard；「模板」在台灣軟體語境作「範本」，但重點是保留自訂名稱。
```

Gemini notes:

```text
「这个」轉「這個」，「程序」轉「程式」，「用户」轉「使用者」，「自定义」轉「自訂」，「模板」轉「範本」。
```

Maintainer decision:

```text

```

### blind-it-0062：Codex/Gemini exact match

- Domain: `it`
- Risk: `baseline_guard`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
系统会在七天后删除未使用的令牌。
```

Recommended expected:

```text
系統會在七天後刪除未使用的權杖。
```

Codex rationale:

```text
token 在安全語境多採「權杖」，但部分產品保留「令牌」。
```

Gemini notes:

```text
「删除」轉「刪除」，「令牌」轉「權杖」。
```

Maintainer decision:

```text

```

### blind-ui-0021：Codex/Gemini exact match

- Domain: `ui`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
点击刷新按钮后，列表会重新加载。
```

Recommended expected:

```text
點擊重新整理按鈕後，清單會重新載入。
```

Codex rationale:

```text
UI 語境「刷新」採「重新整理」；list 可作清單或列表。
```

Gemini notes:

```text
「刷新」在台灣UI中常用「重新整理」；「列表」在台灣UI中常用「清單」；「加载」在台灣UI中常用「載入」。
```

Maintainer decision:

```text

```

### blind-ui-0025：Codex/Gemini exact match

- Domain: `ui`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
用户可以在设置页管理订阅方案。
```

Recommended expected:

```text
使用者可以在設定頁管理訂閱方案。
```

Codex rationale:

```text
subscription plan 可作「訂閱方案」或「訂閱計畫」。
```

Gemini notes:

```text
「用户」在台灣UI中常用「使用者」；「设置页」在台灣UI中常用「設定頁」；「订阅」轉為「訂閱」。
```

Maintainer decision:

```text

```

### blind-ui-0028：Codex/Gemini exact match

- Domain: `ui`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
弹窗关闭后不会保存草稿内容。
```

Recommended expected:

```text
彈出視窗關閉後不會儲存草稿內容。
```

Codex rationale:

```text
「弹窗」正式 UI 可作「彈出視窗」，產品短文案也可能用「彈窗」。
```

Gemini notes:

```text
「弹窗」在台灣UI中常用「彈出視窗」；「保存」在台灣UI中常用「儲存」；「内容」轉為「內容」。
```

Maintainer decision:

```text

```

### blind-ui-0035：Codex/Gemini exact match

- Domain: `ui`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
如果没有网络，应用会显示离线提示。
```

Recommended expected:

```text
如果沒有網路，應用程式會顯示離線提示。
```

Codex rationale:

```text
「应用」可作「應用程式」或 App，需依產品語氣確認。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-ui-0038：Codex/Gemini exact match

- Domain: `ui`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
登录逾时后，请重新验证身份。
```

Recommended expected:

```text
登入逾時後，請重新驗證身分。
```

Codex rationale:

```text
台灣正式用字偏「身分」，但「身份」也常見；需確認產品用字。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-ui-0041：Codex/Gemini exact match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
页面标题里的品牌名称必须保持原样。
```

Recommended expected:

```text
頁面標題裡的品牌名稱必須保持原樣。
```

Codex rationale:

```text
over-conversion guard；品牌名稱應保留。
```

Gemini notes:

```text
「页面」轉為「頁面」，「标题」轉為「標題」，「里」轉為「裡」，「名称」轉為「名稱」，「必须」轉為「必須」，「原样」轉為「原樣」。
```

Maintainer decision:

```text

```

### blind-ui-0042：Codex/Gemini exact match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
用户自订标签不会套用地区词转换。
```

Recommended expected:

```text
使用者自訂標籤不會套用地區詞轉換。
```

Codex rationale:

```text
over-conversion guard；自訂標籤不應被地區詞規則改寫。
```

Gemini notes:

```text
「用户」在台灣UI語境中常轉為「使用者」；「自订」轉為「自訂」，「标签」轉為「標籤」，「不会」轉為「不會」，「地区词」轉為「地區詞」，「转换」轉為「轉換」。
```

Maintainer decision:

```text

```

### blind-ui-0043：Codex/Gemini exact match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
请保留繁体说明中的专有名词。
```

Recommended expected:

```text
請保留繁體說明中的專有名詞。
```

Codex rationale:

```text
over-conversion guard；繁體說明中的專有名詞需保留。
```

Gemini notes:

```text
「请」轉為「請」，「繁体」轉為「繁體」，「说明」轉為「說明」，「专有名词」轉為「專有名詞」。
```

Maintainer decision:

```text

```

### blind-ui-0044：Codex/Gemini exact match

- Domain: `ui`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
导览列中的 OpenAPI 字样不需要转换。
```

Recommended expected:

```text
導覽列中的 OpenAPI 字樣不需要轉換。
```

Codex rationale:

```text
over-conversion guard；英文技術名稱保留。
```

Gemini notes:

```text
「导览列」轉為「導覽列」，「字样」轉為「字樣」，「不需要」轉為「不需要」，「转换」轉為「轉換」。OpenAPI 為專有名詞，保持不變。
```

Maintainer decision:

```text

```

### blind-llm-0019：Codex/Gemini exact match

- Domain: `llm`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
如果用户没有提供日志，请说明需要哪些信息。
```

Recommended expected:

```text
如果使用者沒有提供日誌，請說明需要哪些資訊。
```

Codex rationale:

```text
「日志」可作日誌或記錄檔，需看產品用語。
```

Gemini notes:

```text
「用户」轉為「使用者」為UI/IT常見用語；「日志」轉為「日誌」為IT術語；「信息」轉為「資訊」更符合台灣用語習慣。
```

Maintainer decision:

```text

```

### blind-llm-0023：Codex/Gemini exact match

- Domain: `llm`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
生成的说明需要包含安装步骤和常见错误。
```

Recommended expected:

```text
產生的說明需要包含安裝步驟和常見錯誤。
```

Codex rationale:

```text
LLM output 可作「產生」或「生成」，需看文件風格。
```

Gemini notes:

```text
「生成」轉為「產生」更符合台灣口語習慣；「说明」轉為「說明」；「安装」轉為「安裝」；「常见」轉為「常見」。
```

Maintainer decision:

```text

```

### blind-llm-0027：Codex/Gemini exact match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
系统提示词要求保留产品名称和变量名。
```

Recommended expected:

```text
系統提示詞要求保留產品名稱和變數名稱。
```

Codex rationale:

```text
over-conversion guard；產品名稱與變數名稱不可改。
```

Gemini notes:

```text
「系统」轉為「系統」；「提示词」轉為「提示詞」為LLM相關術語；「产品」轉為「產品」；「变量名」轉為「變數名稱」為IT術語。
```

Maintainer decision:

```text

```

### blind-llm-0030：Codex/Gemini exact match

- Domain: `llm`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
这段内容混合了英文 API 名称和中文说明。
```

Recommended expected:

```text
這段內容混合了英文 API 名稱和中文說明。
```

Codex rationale:

```text
over-conversion guard；英文 API 名稱保留。
```

Gemini notes:

```text
「这段」轉為「這段」；「内容」轉為「內容」；「名称」轉為「名稱」為IT術語；「说明」轉為「說明」。
```

Maintainer decision:

```text

```

### blind-formal-0023：Codex/Gemini exact match

- Domain: `formal`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
承办单位应保存完整申请记录。
```

Recommended expected:

```text
承辦單位應保存完整申請紀錄。
```

Codex rationale:

```text
正式文件可用「紀錄」或「記錄」，需確認用字慣例。
```

Gemini notes:

```text
承辦 (承办), 單位 (单位), 申請 (申请), 紀錄 (记录) 為台灣繁體中文常用詞彙。
```

Maintainer decision:

```text

```

### blind-formal-0026：Codex/Gemini exact match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
契约条款不得排除消费者依法享有的权利。
```

Recommended expected:

```text
契約條款不得排除消費者依法享有的權利。
```

Codex rationale:

```text
法律/消保語境使用「契約條款」；over-conversion guard。
```

Gemini notes:

```text
契約 (契约), 條款 (条款), 消費者 (消费者), 權利 (权利) 為台灣繁體中文常用詞彙。
```

Maintainer decision:

```text

```

### blind-formal-0028：Codex/Gemini exact match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
文件中的机关名称应依原核定名称记载。
```

Recommended expected:

```text
文件中的機關名稱應依原核定名稱記載。
```

Codex rationale:

```text
正式文件中的機關名稱不得任意改寫。
```

Gemini notes:

```text
機關 (机关), 名稱 (名称), 記載 (记载) 為台灣繁體中文常用詞彙。
```

Maintainer decision:

```text

```

### blind-formal-0030：Codex/Gemini exact match

- Domain: `formal`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
公文附件内的专有名词不得任意改写。
```

Recommended expected:

```text
公文附件內的專有名詞不得任意改寫。
```

Codex rationale:

```text
over-conversion guard；公文專有名詞需保留。
```

Gemini notes:

```text
專有 (专有), 名詞 (名词), 改寫 (改写) 為台灣繁體中文常用詞彙。
```

Maintainer decision:

```text

```

### blind-social-0019：Codex/Gemini exact match

- Domain: `social`
- Risk: `candidate_gap`
- Policy reason: `Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
我晚点再把照片上传到共享相册。
```

Recommended expected:

```text
我晚點再把照片上傳到共享相簿。
```

Codex rationale:

```text
shared album 可作「共享相簿」或「共用相簿」。
```

Gemini notes:

```text
「晚点」轉為「晚點」、「上传」轉為「上傳」為標準簡繁轉換。「相册」在台灣慣用「相簿」。
```

Maintainer decision:

```text

```

### blind-social-0027：Codex/Gemini exact match

- Domain: `social`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
昵称和频道名称应该保持原样。
```

Recommended expected:

```text
暱稱和頻道名稱應該保持原樣。
```

Codex rationale:

```text
over-conversion guard；暱稱與頻道名稱需保留。
```

Gemini notes:

```text
「昵称」轉為「暱稱」、「频道」轉為「頻道」、「应该」轉為「應該」、「原样」轉為「原樣」為標準簡繁轉換。
```

Maintainer decision:

```text

```

### blind-social-0028：Codex/Gemini exact match

- Domain: `social`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
请不要把社群里的品牌标签自动转换。
```

Recommended expected:

```text
請不要把社群裡的品牌標籤自動轉換。
```

Codex rationale:

```text
over-conversion guard；品牌標籤不可改。
```

Gemini notes:

```text
「请」轉為「請」、「里」轉為「裡」、「标签」轉為「標籤」、「自动」轉為「自動」、「转换」轉為「轉換」為標準簡繁轉換。
```

Maintainer decision:

```text

```

### blind-social-0030：Codex/Gemini exact match

- Domain: `social`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
用户自订表情名称需要原样保留。
```

Recommended expected:

```text
使用者自訂表情名稱需要原樣保留。
```

Codex rationale:

```text
over-conversion guard；自訂表情名稱需保留。
```

Gemini notes:

```text
「用户」在台灣UI/IT語境中常用「使用者」，「用戶」亦可接受。「自订」轉為「自訂」、「名称」轉為「名稱」、「原样」轉為「原樣」為標準簡繁轉換。
```

Maintainer decision:

```text

```

### blind-social-0031：Codex/Gemini exact match

- Domain: `social`
- Risk: `over_conversion_guard`
- Policy reason: `over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
这则评论混合了繁体和简体，先只作为输入保留。
```

Recommended expected:

```text
這則評論混合了繁體和簡體，先只作為輸入保留。
```

Codex rationale:

```text
over-conversion guard；混合文本先作輸入，不應用來調詞庫。
```

Gemini notes:

```text
「这则」轉為「這則」、「评论」轉為「評論」、「繁体」轉為「繁體」、「简体」轉為「簡體」、「作为」轉為「作為」、「输入」轉為「輸入」為標準簡繁轉換。
```

Maintainer decision:

```text

```

### blind-high-risk-0011：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Policy reason: `high-risk domain, Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
医师建议患者按时回诊并记录症状变化。
```

Recommended expected:

```text
醫師建議病患按時回診並記錄症狀變化。
```

Codex rationale:

```text
醫療高風險；「患者/病患」需由 maintainer 確認，但台灣醫療語境常用「病患」。
```

Gemini notes:

```text
「患者」在台灣醫療語境中也通用，但「病患」更為常見且正式。
```

Maintainer decision:

```text

```

### blind-high-risk-0013：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Policy reason: `high-risk domain`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
申请贷款前，请确认利率和还款期限。
```

Recommended expected:

```text
申請貸款前，請確認利率和還款期限。
```

Codex rationale:

```text
金融高風險；貸款/利率/還款期限用語穩定但仍需人工確認。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0014：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Policy reason: `high-risk domain`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
药品说明应清楚标示使用剂量和禁忌。
```

Recommended expected:

```text
藥品說明應清楚標示使用劑量和禁忌。
```

Codex rationale:

```text
醫療高風險；藥品劑量與禁忌用語需人工確認。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0015：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `candidate_gap`
- Policy reason: `high-risk domain`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
保险契约变更需要经双方书面同意。
```

Recommended expected:

```text
保險契約變更需要經雙方書面同意。
```

Codex rationale:

```text
保險/契約高風險；採台灣法律語境「契約」。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0017：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Policy reason: `high-risk domain, over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
病历中的专有缩写不得任意改写。
```

Recommended expected:

```text
病歷中的專有縮寫不得任意改寫。
```

Codex rationale:

```text
醫療高風險 + over-conversion guard；病歷縮寫不得改。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0018：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `over_conversion_guard`
- Policy reason: `high-risk domain, over-conversion guard`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
金融机构应保留客户原始签署文件。
```

Recommended expected:

```text
金融機構應保留客戶原始簽署文件。
```

Codex rationale:

```text
金融高風險 + over-conversion guard；簽署文件需保守。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0019：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `baseline_guard`
- Policy reason: `high-risk domain, Codex confidence medium`
- Codex confidence: `medium`
- Gemini confidence: `high`

Input:

```text
请妥善保管个人身份证件。
```

Recommended expected:

```text
請妥善保管個人身分證件。
```

Codex rationale:

```text
身分/身份用字需確認；正式台灣用字偏「身分」。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```

### blind-high-risk-0020：Codex/Gemini exact match

- Domain: `high_risk`
- Risk: `baseline_guard`
- Policy reason: `high-risk domain`
- Codex confidence: `high`
- Gemini confidence: `high`

Input:

```text
未成年人开户需由法定代理人陪同。
```

Recommended expected:

```text
未成年人開戶需由法定代理人陪同。
```

Codex rationale:

```text
金融/法律高風險；需人工確認。
```

Gemini notes:

```text

```

Maintainer decision:

```text

```
