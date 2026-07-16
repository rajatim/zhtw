<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：social-daily 0001-0075（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### social-daily-0001

Input:

```text
这个视频太好笑了。
```

AI draft expected:

```text
這個影片太好笑了。
```

Notes：社群短句語境：视频→影片。

### social-daily-0002

Input:

```text
我把视频分享到群里了。
```

AI draft expected:

```text
我把影片分享到群組裡了。
```

Notes：聊天分享語境：视频→影片、群→群組、里→裡。

### social-daily-0003

Input:

```text
评论区已经吵起来了。
```

AI draft expected:

```text
留言區已經吵起來了。
```

Notes：社群留言語境：评论区→留言區。

### social-daily-0004

Input:

```text
请在评论区留言。
```

AI draft expected:

```text
請在留言區留言。
```

Notes：社群互動語境：评论区→留言區、请→請。

### social-daily-0005

Input:

```text
这个帖子被置顶了。
```

AI draft expected:

```text
這篇貼文被置頂了。
```

Notes：社群貼文語境：帖子→貼文、置顶→置頂。

### social-daily-0006

Input:

```text
我刚刚点赞了你的动态。
```

AI draft expected:

```text
我剛剛按讚了你的動態。
```

Notes：社群互動語境：点赞→按讚、动态→動態。

### social-daily-0007

Input:

```text
别忘了点赞和订阅频道。
```

AI draft expected:

```text
別忘了按讚和訂閱頻道。
```

Notes：影片平台語境：点赞→按讚、订阅频道→訂閱頻道。

### social-daily-0008

Input:

```text
这个博主今天又更新了。
```

AI draft expected:

```text
這個創作者今天又更新了。
```

Notes：社群創作者語境：博主→創作者。

### social-daily-0009

Input:

```text
主播正在直播开箱。
```

AI draft expected:

```text
實況主正在直播開箱。
```

Notes：直播語境：主播→實況主、开箱→開箱。

### social-daily-0010

Input:

```text
弹幕刷得太快了。
```

AI draft expected:

```text
彈幕刷得太快了。
```

Notes：影片平台語境：弹幕→彈幕。

### social-daily-0011

Input:

```text
私信我你的地址。
```

AI draft expected:

```text
私訊我你的地址。
```

Notes：社群訊息語境：私信→私訊。

### social-daily-0012

Input:

```text
群聊通知一直跳出来。
```

AI draft expected:

```text
群組聊天通知一直跳出來。
```

Notes：通訊軟體語境：群聊→群組聊天、出来→出來。

### social-daily-0013

Input:

```text
这个表情包太传神了。
```

AI draft expected:

```text
這個貼圖太傳神了。
```

Notes：台灣聊天語境：表情包→貼圖。

### social-daily-0014

Input:

```text
贴纸包已经下载完成。
```

AI draft expected:

```text
貼圖包已經下載完成。
```

Notes：聊天素材語境：贴纸包→貼圖包。

### social-daily-0015

Input:

```text
朋友圈都是旅行照片。
```

AI draft expected:

```text
朋友圈都是旅行照片。
```

Notes：專有社群功能名稱：朋友圈保留，照片不改。

### social-daily-0016

Input:

```text
我把他拉黑了。
```

AI draft expected:

```text
我把他封鎖了。
```

Notes：社群封鎖語境：拉黑→封鎖。

### social-daily-0017

Input:

```text
这个账号被举报了。
```

AI draft expected:

```text
這個帳號被檢舉了。
```

Notes：社群平台語境：账号→帳號、举报→檢舉。

### social-daily-0018

Input:

```text
别在留言里泄露个人信息。
```

AI draft expected:

```text
別在留言裡洩漏個人資訊。
```

Notes：社群安全語境：里→裡、泄露→洩漏、信息→資訊。

### social-daily-0019

Input:

```text
我已经关注这个频道。
```

AI draft expected:

```text
我已經追蹤這個頻道。
```

Notes：社群/影片平台語境：关注→追蹤。

### social-daily-0020

Input:

```text
取消关注后就看不到更新。
```

AI draft expected:

```text
取消追蹤後就看不到更新。
```

Notes：社群平台語境：取消关注→取消追蹤、后→後。

### social-daily-0021

Input:

```text
周末要不要一起骑自行车？
```

AI draft expected:

```text
週末要不要一起騎腳踏車？
```

Notes：日常交通語境：周末→週末、自行车→腳踏車。

### social-daily-0022

Input:

```text
我今天坐地铁去上班。
```

AI draft expected:

```text
我今天搭捷運去上班。
```

Notes：台灣日常交通語境：坐→搭、地铁→捷運。

### social-daily-0023

Input:

```text
下班后搭公交回家。
```

AI draft expected:

```text
下班後搭公車回家。
```

Notes：台灣日常交通語境：公交→公車、后→後。

### social-daily-0024

Input:

```text
公交车站离这里很近。
```

AI draft expected:

```text
公車站離這裡很近。
```

Notes：台灣交通語境：公交车站→公車站、这里→這裡。

### social-daily-0025

Input:

```text
我叫了出租车去机场。
```

AI draft expected:

```text
我叫了計程車去機場。
```

Notes：台灣交通語境：出租车→計程車、机场→機場。

### social-daily-0026

Input:

```text
打车费用比预期高。
```

AI draft expected:

```text
叫車費用比預期高。
```

Notes：日常叫車語境：打车→叫車。

### social-daily-0027

Input:

```text
手机快没电了。
```

AI draft expected:

```text
手機快沒電了。
```

Notes：日常語境：手机→手機、没→沒。

### social-daily-0028

Input:

```text
充电线放在抽屉里。
```

AI draft expected:

```text
充電線放在抽屜裡。
```

Notes：日常物品語境：充电线→充電線、里→裡。

### social-daily-0029

Input:

```text
我把钥匙忘在车里。
```

AI draft expected:

```text
我把鑰匙忘在車裡。
```

Notes：日常語境：钥匙→鑰匙、里→裡。

### social-daily-0030

Input:

```text
晚点再回你消息。
```

AI draft expected:

```text
晚點再回你訊息。
```

Notes：聊天語境：晚点→晚點、消息→訊息。

### social-daily-0031

Input:

```text
这个消息不要转发。
```

AI draft expected:

```text
這則訊息不要轉傳。
```

Notes：聊天語境：消息→訊息、转发→轉傳。

### social-daily-0032

Input:

```text
我刚收到快递。
```

AI draft expected:

```text
我剛收到包裹。
```

Notes：日常收件語境：快递→包裹。

### social-daily-0033

Input:

```text
快递员把包裹放门口了。
```

AI draft expected:

```text
宅配員把包裹放門口了。
```

Notes：台灣收件語境：快递员→宅配員。

### social-daily-0034

Input:

```text
外卖已经送到了。
```

AI draft expected:

```text
外送已經送到了。
```

Notes：台灣點餐語境：外卖→外送。

### social-daily-0035

Input:

```text
今天中午订便当。
```

AI draft expected:

```text
今天中午訂便當。
```

Notes：日常用餐語境：订→訂。

### social-daily-0036

Input:

```text
冰箱里还有昨天的饭。
```

AI draft expected:

```text
冰箱裡還有昨天的飯。
```

Notes：日常語境：里→裡、还有→還有。

### social-daily-0037

Input:

```text
这个小区晚上很安静。
```

AI draft expected:

```text
這個社區晚上很安靜。
```

Notes：台灣居住語境：小区→社區、安静→安靜。

### social-daily-0038

Input:

```text
物业通知明天停水。
```

AI draft expected:

```text
管委會通知明天停水。
```

Notes：台灣社區語境：物业→管委會。

### social-daily-0039

Input:

```text
电梯维修到下午。
```

AI draft expected:

```text
電梯維修到下午。
```

Notes：日常公告語境：电梯→電梯、维修→維修。

### social-daily-0040

Input:

```text
垃圾车已经过了。
```

AI draft expected:

```text
垃圾車已經過了。
```

Notes：台灣日常語境：垃圾车→垃圾車。

### social-daily-0041

Input:

```text
我在便利店买咖啡。
```

AI draft expected:

```text
我在便利商店買咖啡。
```

Notes：台灣日常購物語境：便利店→便利商店、买→買。

### social-daily-0042

Input:

```text
这个优惠券明天过期。
```

AI draft expected:

```text
這張優惠券明天過期。
```

Notes：購物語境：优惠券→優惠券、过期→過期。

### social-daily-0043

Input:

```text
购物车里还有三件商品。
```

AI draft expected:

```text
購物車裡還有三件商品。
```

Notes：購物語境：购物车→購物車、里→裡、还有→還有。

### social-daily-0044

Input:

```text
卖家已经发货。
```

AI draft expected:

```text
賣家已經出貨。
```

Notes：電商語境：发货→出貨。

### social-daily-0045

Input:

```text
订单状态显示已签收。
```

AI draft expected:

```text
訂單狀態顯示已簽收。
```

Notes：電商物流語境：订单→訂單、状态→狀態、签收→簽收。

### social-daily-0046

Input:

```text
退货申请还在审核。
```

AI draft expected:

```text
退貨申請還在審核。
```

Notes：電商售後語境：退货→退貨、审核→審核。

### social-daily-0047

Input:

```text
客服说可以换货。
```

AI draft expected:

```text
客服說可以換貨。
```

Notes：購物客服語境：说→說、换货→換貨。

### social-daily-0048

Input:

```text
这个商品没有现货。
```

AI draft expected:

```text
這個商品沒有現貨。
```

Notes：購物語境：没有→沒有、现货→現貨。

### social-daily-0049

Input:

```text
发票要开公司抬头。
```

AI draft expected:

```text
發票要開公司抬頭。
```

Notes：日常商務語境：发票→發票。

### social-daily-0050

Input:

```text
我把地址填错了。
```

AI draft expected:

```text
我把地址填錯了。
```

Notes：表單日常語境：错→錯。

### social-daily-0051

Input:

```text
晚上要不要看电影？
```

AI draft expected:

```text
晚上要不要看電影？
```

Notes：日常娛樂語境：电影→電影。

### social-daily-0052

Input:

```text
这部剧更新到第八集。
```

AI draft expected:

```text
這部影集更新到第八集。
```

Notes：台灣串流語境：剧→影集。

### social-daily-0053

Input:

```text
片尾彩蛋不要剧透。
```

AI draft expected:

```text
片尾彩蛋不要爆雷。
```

Notes：台灣影視語境：剧透→爆雷。

### social-daily-0054

Input:

```text
游戏服务器又炸了。
```

AI draft expected:

```text
遊戲伺服器又掛了。
```

Notes：日常遊戲語境：服务器→伺服器、炸了→掛了。

### social-daily-0055

Input:

```text
队友一直掉线。
```

AI draft expected:

```text
隊友一直斷線。
```

Notes：遊戲語境：掉线→斷線。

### social-daily-0056

Input:

```text
这个关卡有隐藏任务。
```

AI draft expected:

```text
這個關卡有隱藏任務。
```

Notes：遊戲語境：关卡→關卡、隐藏→隱藏、任务→任務。

### social-daily-0057

Input:

```text
语音聊天有杂音。
```

AI draft expected:

```text
語音聊天有雜音。
```

Notes：聊天/遊戲語境：语音→語音、杂音→雜音。

### social-daily-0058

Input:

```text
我把照片上传到相册。
```

AI draft expected:

```text
我把照片上傳到相簿。
```

Notes：日常照片語境：上传→上傳、相册→相簿。

### social-daily-0059

Input:

```text
相机自动对焦失败。
```

AI draft expected:

```text
相機自動對焦失敗。
```

Notes：日常拍照語境：相机→相機、自动→自動、失败→失敗。

### social-daily-0060

Input:

```text
这个滤镜颜色太重。
```

AI draft expected:

```text
這個濾鏡顏色太重。
```

Notes：修圖語境：滤镜→濾鏡、颜色→顏色。

### social-daily-0061

Input:

```text
别把原图压缩太多。
```

AI draft expected:

```text
別把原圖壓縮太多。
```

Notes：圖片分享語境：原图→原圖、压缩→壓縮。

### social-daily-0062

Input:

```text
我换了新的头像。
```

AI draft expected:

```text
我換了新的大頭貼。
```

Notes：社群個人資料語境：头像→大頭貼。

### social-daily-0063

Input:

```text
昵称不要用真实姓名。
```

AI draft expected:

```text
暱稱不要用真實姓名。
```

Notes：社群帳號語境：昵称→暱稱、真实→真實。

### social-daily-0064

Input:

```text
这个账号看起来像机器人。
```

AI draft expected:

```text
這個帳號看起來像機器人。
```

Notes：社群風控語境：账号→帳號、机器人→機器人。

### social-daily-0065

Input:

```text
系统提醒我更改密码。
```

AI draft expected:

```text
系統提醒我變更密碼。
```

Notes：帳號安全語境：更改密码→變更密碼。

### social-daily-0066

Input:

```text
验证码一直收不到。
```

AI draft expected:

```text
驗證碼一直收不到。
```

Notes：帳號驗證語境：验证码→驗證碼。

### social-daily-0067

Input:

```text
我忘记登录密码了。
```

AI draft expected:

```text
我忘記登入密碼了。
```

Notes：帳號登入語境：登录→登入。

### social-daily-0068

Input:

```text
别用公共电脑登录账号。
```

AI draft expected:

```text
別用公用電腦登入帳號。
```

Notes：帳號安全語境：公共电脑→公用電腦、登录账号→登入帳號。

### social-daily-0069

Input:

```text
浏览记录不要同步。
```

AI draft expected:

```text
瀏覽紀錄不要同步。
```

Notes：隱私語境：浏览记录→瀏覽紀錄。

### social-daily-0070

Input:

```text
这个软件更新后变慢了。
```

AI draft expected:

```text
這個軟體更新後變慢了。
```

Notes：日常軟體語境：软件→軟體、后→後。

### social-daily-0071

Input:

```text
应用商店打不开。
```

AI draft expected:

```text
應用程式商店打不開。
```

Notes：手機日常語境：应用商店→應用程式商店、打不开→打不開。

### social-daily-0072

Input:

```text
手机桌面图标乱了。
```

AI draft expected:

```text
手機桌面圖示亂了。
```

Notes：手機介面語境：图标→圖示。

### social-daily-0073

Input:

```text
闹钟没有响。
```

AI draft expected:

```text
鬧鐘沒有響。
```

Notes：日常語境：闹钟→鬧鐘、没有→沒有。

### social-daily-0074

Input:

```text
明早七点提醒我出门。
```

AI draft expected:

```text
明早七點提醒我出門。
```

Notes：日常提醒語境：点→點、出门→出門。

### social-daily-0075

Input:

```text
今天空气质量不错。
```

AI draft expected:

```text
今天空氣品質不錯。
```

Notes：日常天氣語境：空气质量→空氣品質、不错→不錯。
