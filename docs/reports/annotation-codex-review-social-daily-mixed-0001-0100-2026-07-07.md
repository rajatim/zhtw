<!-- zhtw:disable -->
# Codex Review：social-daily 0001-0075 + mixed-ambiguity 0001-0025（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Codex drafts：

- `docs/reports/annotation-first-pass-ai-draft-social-daily-0001-0075-2026-07-07.md`
- `docs/reports/annotation-first-pass-ai-draft-mixed-ambiguity-0001-0025-2026-07-07.md`

Gemini advisory：

- `docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.md`
- `docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.md`
- `docs/reports/annotation-gemini-vertex-advisory-mixed-ambiguity-0001-0025-2026-07-07.md`

## Boundary

- This is Codex advisory review only, not maintainer approval.
- Do not copy recommendations into `review.expected` without maintainer final review.
- Gemini remains an AI advisory, not a human `blind_reviewer`.

## Summary

- Cases reviewed: 100
- Codex/Gemini exact matches: 78
- Codex/Gemini differences: 22
- Recommendation on differences: Codex 19, Gemini 3
- Maintainer final decision on differences: Codex 19, Gemini 3
- Current backlog status: `approved`

## Maintainer Final Decision

Maintainer `tim` accepted the Codex recommendations on 2026-07-07:

- Gemini accepted: `social-daily-0008`, `social-daily-0026`,
  `mixed-ambiguity-0007`
- Codex accepted for the other 19 differing cases listed below.

The 78 exact-match cases use the shared Codex/Gemini expected output as
`human_first_pass`. The 22 differing cases are recorded as
`human_adjudication`.

## Difference Recommendations

| ID | Input | Codex draft | Gemini advisory | Recommendation | Reason |
|----|-------|-------------|-----------------|----------------|--------|
| social-daily-0005 | 这个帖子被置顶了。 | 這篇貼文被置頂了。 | 這個貼文被置頂了。 | Codex | 「帖子」在台灣社群語境用「貼文」；「這篇貼文」比「這個貼文」更自然。 |
| social-daily-0008 | 这个博主今天又更新了。 | 這個創作者今天又更新了。 | 這個部落客今天又更新了。 | Gemini | 未限定影片或直播時，「博主」較接近「部落客」；比泛稱「創作者」更貼近原意。 |
| social-daily-0009 | 主播正在直播开箱。 | 實況主正在直播開箱。 | 主播正在直播開箱。 | Codex | 直播開箱語境在台灣常稱「實況主」；「主播」較偏新聞或節目主持。 |
| social-daily-0013 | 这个表情包太传神了。 | 這個貼圖太傳神了。 | 這個表情貼圖太傳神了。 | Codex | 聊天語境中「表情包」常作「貼圖」；「表情貼圖」較冗。 |
| social-daily-0015 | 朋友圈都是旅行照片。 | 朋友圈都是旅行照片。 | 社群動態都是旅行照片。 | Codex | 「朋友圈」是特定社群功能名稱；改成「社群動態」會泛化原文。 |
| social-daily-0022 | 我今天坐地铁去上班。 | 我今天搭捷運去上班。 | 我今天坐捷運去上班。 | Codex | 台灣日常交通常說「搭捷運」；「坐捷運」較不在地。 |
| social-daily-0026 | 打车费用比预期高。 | 叫車費用比預期高。 | 搭計程車費用比預期高。 | Gemini | 費用語境中「搭計程車費用」比「叫車費用」更直接表示車資。 |
| social-daily-0031 | 这个消息不要转发。 | 這則訊息不要轉傳。 | 這個訊息不要轉發。 | Codex | 訊息語境中台灣常用「轉傳」；「這則訊息」也比「這個訊息」自然。 |
| social-daily-0032 | 我刚收到快递。 | 我剛收到包裹。 | 我剛收到快遞。 | Codex | 日常收件語境「收到包裹」比「收到快遞」更常見。 |
| social-daily-0033 | 快递员把包裹放门口了。 | 宅配員把包裹放門口了。 | 快遞員把包裹放門口了。 | Codex | 台灣收件語境「宅配員」比「快遞員」更常見。 |
| social-daily-0042 | 这个优惠券明天过期。 | 這張優惠券明天過期。 | 這個優惠券明天過期。 | Codex | 「優惠券」量詞用「張」更自然。 |
| social-daily-0052 | 这部剧更新到第八集。 | 這部影集更新到第八集。 | 這部劇更新到第八集。 | Codex | 串流更新到集數的語境，台灣常用「影集」。 |
| social-daily-0053 | 片尾彩蛋不要剧透。 | 片尾彩蛋不要爆雷。 | 片尾彩蛋不要劇透。 | Codex | 社群口語提醒中「不要爆雷」比「不要劇透」更台灣。 |
| social-daily-0065 | 系统提醒我更改密码。 | 系統提醒我變更密碼。 | 系統提醒我更改密碼。 | Codex | 帳號安全/系統提醒語境中「變更密碼」較符合台灣介面用語。 |
| social-daily-0068 | 别用公共电脑登录账号。 | 別用公用電腦登入帳號。 | 別用公共電腦登入帳號。 | Codex | 台灣常說「公用電腦」；「公共電腦」較不自然。 |
| mixed-ambiguity-0002 | 会议程序已经排好。 | 會議程序已經排好。 | 會議議程已經排好了。 | Codex | 此 case 主要保護「程序」不要誤轉成「程式」；Gemini 另改成「議程」且加語氣詞，超出保守轉換。 |
| mixed-ambiguity-0007 | 技术支持会协助排查。 | 技術支援會協助排查。 | 技術支援會協助排除問題。 | Gemini | 台灣疑難排解語境「協助排除問題」比保留「排查」自然。 |
| mixed-ambiguity-0009 | 后台服务正在重启。 | 背景服務正在重新啟動。 | 後端服務正在重新啟動。 | Codex | 「后台服务」可指背景服務；改成「後端服務」會縮窄成 backend 語意。 |
| mixed-ambiguity-0011 | 接口返回空数组。 | 介面回傳空陣列。 | 介面傳回空陣列。 | Codex | API 語境本專案慣用「回傳」；維持既有 IT regression 用語。 |
| mixed-ambiguity-0018 | 他缓存了那张照片。 | 他快取了那張照片。 | 他將那張照片快取起來了。 | Codex | 保守保留原句結構；「快取了那張照片」可接受，Gemini 加了「將…起來」屬改寫。 |
| mixed-ambiguity-0020 | 补助项目明天截止。 | 補助計畫明天截止。 | 補助項目明天截止。 | Codex | 補助語境常用「補助計畫」；「項目」較偏條目，不一定是申請案。 |
| mixed-ambiguity-0021 | 服务器返回状态码。 | 伺服器回傳狀態碼。 | 伺服器傳回狀態碼。 | Codex | API 語境本專案慣用「回傳狀態碼」，維持一致。 |

## Maintainer Apply Rules

- If accepting an exact-match case, copy the shared expected value to `review.expected`, set `review.expected_source = "human_first_pass"`, `review.first_reviewer = "tim"`, and record Gemini advisory as accepted.
- If accepting a differing Codex recommendation, set `review.expected_source = "human_adjudication"`, `review.adjudicator = "tim"`, `review.disagreement = true`, and record Gemini advisory as rejected.
- If accepting a differing Gemini recommendation, set `review.expected_source = "human_adjudication"`, `review.adjudicator = "tim"`, `review.disagreement = true`, and record Gemini advisory as accepted with `exact_match_with_first_pass = false`.
