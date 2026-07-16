<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：social-daily-0001-social-daily-0050（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-social-daily-0001-0050-2026-07-07.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 50
- Exact matches with Codex draft: 39
- Differences from Codex draft: 11

## Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### social-daily-0001：match

Input:

```text
这个视频太好笑了。
```

Codex draft expected:

```text
這個影片太好笑了。
```

Gemini advisory expected:

```text
這個影片太好笑了。
```

Gemini notes:

```text

```

### social-daily-0002：match

Input:

```text
我把视频分享到群里了。
```

Codex draft expected:

```text
我把影片分享到群組裡了。
```

Gemini advisory expected:

```text
我把影片分享到群組裡了。
```

Gemini notes:

```text

```

### social-daily-0003：match

Input:

```text
评论区已经吵起来了。
```

Codex draft expected:

```text
留言區已經吵起來了。
```

Gemini advisory expected:

```text
留言區已經吵起來了。
```

Gemini notes:

```text

```

### social-daily-0004：match

Input:

```text
请在评论区留言。
```

Codex draft expected:

```text
請在留言區留言。
```

Gemini advisory expected:

```text
請在留言區留言。
```

Gemini notes:

```text

```

### social-daily-0005：different

Input:

```text
这个帖子被置顶了。
```

Codex draft expected:

```text
這篇貼文被置頂了。
```

Gemini advisory expected:

```text
這個貼文被置頂了。
```

Gemini notes:

```text

```

### social-daily-0006：match

Input:

```text
我刚刚点赞了你的动态。
```

Codex draft expected:

```text
我剛剛按讚了你的動態。
```

Gemini advisory expected:

```text
我剛剛按讚了你的動態。
```

Gemini notes:

```text

```

### social-daily-0007：match

Input:

```text
别忘了点赞和订阅频道。
```

Codex draft expected:

```text
別忘了按讚和訂閱頻道。
```

Gemini advisory expected:

```text
別忘了按讚和訂閱頻道。
```

Gemini notes:

```text

```

### social-daily-0008：different

Input:

```text
这个博主今天又更新了。
```

Codex draft expected:

```text
這個創作者今天又更新了。
```

Gemini advisory expected:

```text
這個部落客今天又更新了。
```

Gemini notes:

```text

```

### social-daily-0009：different

Input:

```text
主播正在直播开箱。
```

Codex draft expected:

```text
實況主正在直播開箱。
```

Gemini advisory expected:

```text
主播正在直播開箱。
```

Gemini notes:

```text

```

### social-daily-0010：match

Input:

```text
弹幕刷得太快了。
```

Codex draft expected:

```text
彈幕刷得太快了。
```

Gemini advisory expected:

```text
彈幕刷得太快了。
```

Gemini notes:

```text

```

### social-daily-0011：match

Input:

```text
私信我你的地址。
```

Codex draft expected:

```text
私訊我你的地址。
```

Gemini advisory expected:

```text
私訊我你的地址。
```

Gemini notes:

```text

```

### social-daily-0012：match

Input:

```text
群聊通知一直跳出来。
```

Codex draft expected:

```text
群組聊天通知一直跳出來。
```

Gemini advisory expected:

```text
群組聊天通知一直跳出來。
```

Gemini notes:

```text

```

### social-daily-0013：different

Input:

```text
这个表情包太传神了。
```

Codex draft expected:

```text
這個貼圖太傳神了。
```

Gemini advisory expected:

```text
這個表情貼圖太傳神了。
```

Gemini notes:

```text

```

### social-daily-0014：match

Input:

```text
贴纸包已经下载完成。
```

Codex draft expected:

```text
貼圖包已經下載完成。
```

Gemini advisory expected:

```text
貼圖包已經下載完成。
```

Gemini notes:

```text

```

### social-daily-0015：different

Input:

```text
朋友圈都是旅行照片。
```

Codex draft expected:

```text
朋友圈都是旅行照片。
```

Gemini advisory expected:

```text
社群動態都是旅行照片。
```

Gemini notes:

```text

```

### social-daily-0016：match

Input:

```text
我把他拉黑了。
```

Codex draft expected:

```text
我把他封鎖了。
```

Gemini advisory expected:

```text
我把他封鎖了。
```

Gemini notes:

```text

```

### social-daily-0017：match

Input:

```text
这个账号被举报了。
```

Codex draft expected:

```text
這個帳號被檢舉了。
```

Gemini advisory expected:

```text
這個帳號被檢舉了。
```

Gemini notes:

```text

```

### social-daily-0018：match

Input:

```text
别在留言里泄露个人信息。
```

Codex draft expected:

```text
別在留言裡洩漏個人資訊。
```

Gemini advisory expected:

```text
別在留言裡洩漏個人資訊。
```

Gemini notes:

```text

```

### social-daily-0019：match

Input:

```text
我已经关注这个频道。
```

Codex draft expected:

```text
我已經追蹤這個頻道。
```

Gemini advisory expected:

```text
我已經追蹤這個頻道。
```

Gemini notes:

```text

```

### social-daily-0020：match

Input:

```text
取消关注后就看不到更新。
```

Codex draft expected:

```text
取消追蹤後就看不到更新。
```

Gemini advisory expected:

```text
取消追蹤後就看不到更新。
```

Gemini notes:

```text

```

### social-daily-0021：match

Input:

```text
周末要不要一起骑自行车？
```

Codex draft expected:

```text
週末要不要一起騎腳踏車？
```

Gemini advisory expected:

```text
週末要不要一起騎腳踏車？
```

Gemini notes:

```text

```

### social-daily-0022：different

Input:

```text
我今天坐地铁去上班。
```

Codex draft expected:

```text
我今天搭捷運去上班。
```

Gemini advisory expected:

```text
我今天坐捷運去上班。
```

Gemini notes:

```text

```

### social-daily-0023：match

Input:

```text
下班后搭公交回家。
```

Codex draft expected:

```text
下班後搭公車回家。
```

Gemini advisory expected:

```text
下班後搭公車回家。
```

Gemini notes:

```text

```

### social-daily-0024：match

Input:

```text
公交车站离这里很近。
```

Codex draft expected:

```text
公車站離這裡很近。
```

Gemini advisory expected:

```text
公車站離這裡很近。
```

Gemini notes:

```text

```

### social-daily-0025：match

Input:

```text
我叫了出租车去机场。
```

Codex draft expected:

```text
我叫了計程車去機場。
```

Gemini advisory expected:

```text
我叫了計程車去機場。
```

Gemini notes:

```text

```

### social-daily-0026：different

Input:

```text
打车费用比预期高。
```

Codex draft expected:

```text
叫車費用比預期高。
```

Gemini advisory expected:

```text
搭計程車費用比預期高。
```

Gemini notes:

```text

```

### social-daily-0027：match

Input:

```text
手机快没电了。
```

Codex draft expected:

```text
手機快沒電了。
```

Gemini advisory expected:

```text
手機快沒電了。
```

Gemini notes:

```text

```

### social-daily-0028：match

Input:

```text
充电线放在抽屉里。
```

Codex draft expected:

```text
充電線放在抽屜裡。
```

Gemini advisory expected:

```text
充電線放在抽屜裡。
```

Gemini notes:

```text

```

### social-daily-0029：match

Input:

```text
我把钥匙忘在车里。
```

Codex draft expected:

```text
我把鑰匙忘在車裡。
```

Gemini advisory expected:

```text
我把鑰匙忘在車裡。
```

Gemini notes:

```text

```

### social-daily-0030：match

Input:

```text
晚点再回你消息。
```

Codex draft expected:

```text
晚點再回你訊息。
```

Gemini advisory expected:

```text
晚點再回你訊息。
```

Gemini notes:

```text

```

### social-daily-0031：different

Input:

```text
这个消息不要转发。
```

Codex draft expected:

```text
這則訊息不要轉傳。
```

Gemini advisory expected:

```text
這個訊息不要轉發。
```

Gemini notes:

```text

```

### social-daily-0032：different

Input:

```text
我刚收到快递。
```

Codex draft expected:

```text
我剛收到包裹。
```

Gemini advisory expected:

```text
我剛收到快遞。
```

Gemini notes:

```text

```

### social-daily-0033：different

Input:

```text
快递员把包裹放门口了。
```

Codex draft expected:

```text
宅配員把包裹放門口了。
```

Gemini advisory expected:

```text
快遞員把包裹放門口了。
```

Gemini notes:

```text

```

### social-daily-0034：match

Input:

```text
外卖已经送到了。
```

Codex draft expected:

```text
外送已經送到了。
```

Gemini advisory expected:

```text
外送已經送到了。
```

Gemini notes:

```text

```

### social-daily-0035：match

Input:

```text
今天中午订便当。
```

Codex draft expected:

```text
今天中午訂便當。
```

Gemini advisory expected:

```text
今天中午訂便當。
```

Gemini notes:

```text

```

### social-daily-0036：match

Input:

```text
冰箱里还有昨天的饭。
```

Codex draft expected:

```text
冰箱裡還有昨天的飯。
```

Gemini advisory expected:

```text
冰箱裡還有昨天的飯。
```

Gemini notes:

```text

```

### social-daily-0037：match

Input:

```text
这个小区晚上很安静。
```

Codex draft expected:

```text
這個社區晚上很安靜。
```

Gemini advisory expected:

```text
這個社區晚上很安靜。
```

Gemini notes:

```text

```

### social-daily-0038：match

Input:

```text
物业通知明天停水。
```

Codex draft expected:

```text
管委會通知明天停水。
```

Gemini advisory expected:

```text
管委會通知明天停水。
```

Gemini notes:

```text

```

### social-daily-0039：match

Input:

```text
电梯维修到下午。
```

Codex draft expected:

```text
電梯維修到下午。
```

Gemini advisory expected:

```text
電梯維修到下午。
```

Gemini notes:

```text

```

### social-daily-0040：match

Input:

```text
垃圾车已经过了。
```

Codex draft expected:

```text
垃圾車已經過了。
```

Gemini advisory expected:

```text
垃圾車已經過了。
```

Gemini notes:

```text

```

### social-daily-0041：match

Input:

```text
我在便利店买咖啡。
```

Codex draft expected:

```text
我在便利商店買咖啡。
```

Gemini advisory expected:

```text
我在便利商店買咖啡。
```

Gemini notes:

```text

```

### social-daily-0042：different

Input:

```text
这个优惠券明天过期。
```

Codex draft expected:

```text
這張優惠券明天過期。
```

Gemini advisory expected:

```text
這個優惠券明天過期。
```

Gemini notes:

```text

```

### social-daily-0043：match

Input:

```text
购物车里还有三件商品。
```

Codex draft expected:

```text
購物車裡還有三件商品。
```

Gemini advisory expected:

```text
購物車裡還有三件商品。
```

Gemini notes:

```text

```

### social-daily-0044：match

Input:

```text
卖家已经发货。
```

Codex draft expected:

```text
賣家已經出貨。
```

Gemini advisory expected:

```text
賣家已經出貨。
```

Gemini notes:

```text

```

### social-daily-0045：match

Input:

```text
订单状态显示已签收。
```

Codex draft expected:

```text
訂單狀態顯示已簽收。
```

Gemini advisory expected:

```text
訂單狀態顯示已簽收。
```

Gemini notes:

```text

```

### social-daily-0046：match

Input:

```text
退货申请还在审核。
```

Codex draft expected:

```text
退貨申請還在審核。
```

Gemini advisory expected:

```text
退貨申請還在審核。
```

Gemini notes:

```text

```

### social-daily-0047：match

Input:

```text
客服说可以换货。
```

Codex draft expected:

```text
客服說可以換貨。
```

Gemini advisory expected:

```text
客服說可以換貨。
```

Gemini notes:

```text

```

### social-daily-0048：match

Input:

```text
这个商品没有现货。
```

Codex draft expected:

```text
這個商品沒有現貨。
```

Gemini advisory expected:

```text
這個商品沒有現貨。
```

Gemini notes:

```text

```

### social-daily-0049：match

Input:

```text
发票要开公司抬头。
```

Codex draft expected:

```text
發票要開公司抬頭。
```

Gemini advisory expected:

```text
發票要開公司抬頭。
```

Gemini notes:

```text

```

### social-daily-0050：match

Input:

```text
我把地址填错了。
```

Codex draft expected:

```text
我把地址填錯了。
```

Gemini advisory expected:

```text
我把地址填錯了。
```

Gemini notes:

```text

```
