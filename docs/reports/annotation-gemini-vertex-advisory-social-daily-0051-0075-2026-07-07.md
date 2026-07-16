<!-- zhtw:disable -->
# Gemini Vertex Advisory Review：social-daily-0051-social-daily-0075（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`
Raw JSON：`docs/reports/annotation-gemini-vertex-advisory-social-daily-0051-0075-2026-07-07.json`

## Boundary

- This is Gemini Vertex AI advisory output, not a human review.
- It must not be recorded as `human_first_pass`, `human_adjudication`, or `blind_reviewer`.
- Maintainer review is required before any `review.expected` value becomes promotion-ready.

## Summary

- Model: `gemini-2.5-flash`
- Project: `tw-el-gemini`
- Location: `us-central1`
- Cases: 25
- Exact matches with Codex draft: 21
- Differences from Codex draft: 4

## Maintainer Action

For each case, choose the final Taiwan Traditional expected output. After maintainer approval:

- write the final value to `review.expected`
- set `review.expected_source = "human_first_pass"` when accepting one advisory version unchanged
- set `review.expected_source = "human_adjudication"` and `review.adjudicator = "tim"` when resolving a difference
- keep Gemini under `review.ai_advisory`; do not set it as `blind_reviewer`

## Comparison

### social-daily-0051：match

Input:

```text
晚上要不要看电影？
```

Codex draft expected:

```text
晚上要不要看電影？
```

Gemini advisory expected:

```text
晚上要不要看電影？
```

Gemini notes:

```text

```

### social-daily-0052：different

Input:

```text
这部剧更新到第八集。
```

Codex draft expected:

```text
這部影集更新到第八集。
```

Gemini advisory expected:

```text
這部劇更新到第八集。
```

Gemini notes:

```text

```

### social-daily-0053：different

Input:

```text
片尾彩蛋不要剧透。
```

Codex draft expected:

```text
片尾彩蛋不要爆雷。
```

Gemini advisory expected:

```text
片尾彩蛋不要劇透。
```

Gemini notes:

```text

```

### social-daily-0054：match

Input:

```text
游戏服务器又炸了。
```

Codex draft expected:

```text
遊戲伺服器又掛了。
```

Gemini advisory expected:

```text
遊戲伺服器又掛了。
```

Gemini notes:

```text
「炸了」在遊戲伺服器情境下，台灣常用「掛了」表示當機或故障。
```

### social-daily-0055：match

Input:

```text
队友一直掉线。
```

Codex draft expected:

```text
隊友一直斷線。
```

Gemini advisory expected:

```text
隊友一直斷線。
```

Gemini notes:

```text
「掉線」在台灣常用「斷線」。
```

### social-daily-0056：match

Input:

```text
这个关卡有隐藏任务。
```

Codex draft expected:

```text
這個關卡有隱藏任務。
```

Gemini advisory expected:

```text
這個關卡有隱藏任務。
```

Gemini notes:

```text

```

### social-daily-0057：match

Input:

```text
语音聊天有杂音。
```

Codex draft expected:

```text
語音聊天有雜音。
```

Gemini advisory expected:

```text
語音聊天有雜音。
```

Gemini notes:

```text

```

### social-daily-0058：match

Input:

```text
我把照片上传到相册。
```

Codex draft expected:

```text
我把照片上傳到相簿。
```

Gemini advisory expected:

```text
我把照片上傳到相簿。
```

Gemini notes:

```text
「相册」在台灣常用「相簿」。
```

### social-daily-0059：match

Input:

```text
相机自动对焦失败。
```

Codex draft expected:

```text
相機自動對焦失敗。
```

Gemini advisory expected:

```text
相機自動對焦失敗。
```

Gemini notes:

```text

```

### social-daily-0060：match

Input:

```text
这个滤镜颜色太重。
```

Codex draft expected:

```text
這個濾鏡顏色太重。
```

Gemini advisory expected:

```text
這個濾鏡顏色太重。
```

Gemini notes:

```text

```

### social-daily-0061：match

Input:

```text
别把原图压缩太多。
```

Codex draft expected:

```text
別把原圖壓縮太多。
```

Gemini advisory expected:

```text
別把原圖壓縮太多。
```

Gemini notes:

```text

```

### social-daily-0062：match

Input:

```text
我换了新的头像。
```

Codex draft expected:

```text
我換了新的大頭貼。
```

Gemini advisory expected:

```text
我換了新的大頭貼。
```

Gemini notes:

```text
「头像」在台灣社群媒體中常用「大頭貼」。
```

### social-daily-0063：match

Input:

```text
昵称不要用真实姓名。
```

Codex draft expected:

```text
暱稱不要用真實姓名。
```

Gemini advisory expected:

```text
暱稱不要用真實姓名。
```

Gemini notes:

```text

```

### social-daily-0064：match

Input:

```text
这个账号看起来像机器人。
```

Codex draft expected:

```text
這個帳號看起來像機器人。
```

Gemini advisory expected:

```text
這個帳號看起來像機器人。
```

Gemini notes:

```text

```

### social-daily-0065：different

Input:

```text
系统提醒我更改密码。
```

Codex draft expected:

```text
系統提醒我變更密碼。
```

Gemini advisory expected:

```text
系統提醒我更改密碼。
```

Gemini notes:

```text

```

### social-daily-0066：match

Input:

```text
验证码一直收不到。
```

Codex draft expected:

```text
驗證碼一直收不到。
```

Gemini advisory expected:

```text
驗證碼一直收不到。
```

Gemini notes:

```text

```

### social-daily-0067：match

Input:

```text
我忘记登录密码了。
```

Codex draft expected:

```text
我忘記登入密碼了。
```

Gemini advisory expected:

```text
我忘記登入密碼了。
```

Gemini notes:

```text
「登录」在台灣常用「登入」。
```

### social-daily-0068：different

Input:

```text
别用公共电脑登录账号。
```

Codex draft expected:

```text
別用公用電腦登入帳號。
```

Gemini advisory expected:

```text
別用公共電腦登入帳號。
```

Gemini notes:

```text
「电脑」在台灣常用「電腦」，「登录」常用「登入」，「账号」常用「帳號」。
```

### social-daily-0069：match

Input:

```text
浏览记录不要同步。
```

Codex draft expected:

```text
瀏覽紀錄不要同步。
```

Gemini advisory expected:

```text
瀏覽紀錄不要同步。
```

Gemini notes:

```text

```

### social-daily-0070：match

Input:

```text
这个软件更新后变慢了。
```

Codex draft expected:

```text
這個軟體更新後變慢了。
```

Gemini advisory expected:

```text
這個軟體更新後變慢了。
```

Gemini notes:

```text
「软件」在台灣常用「軟體」。
```

### social-daily-0071：match

Input:

```text
应用商店打不开。
```

Codex draft expected:

```text
應用程式商店打不開。
```

Gemini advisory expected:

```text
應用程式商店打不開。
```

Gemini notes:

```text
「应用商店」在台灣常用「應用程式商店」。
```

### social-daily-0072：match

Input:

```text
手机桌面图标乱了。
```

Codex draft expected:

```text
手機桌面圖示亂了。
```

Gemini advisory expected:

```text
手機桌面圖示亂了。
```

Gemini notes:

```text
「手机」在台灣常用「手機」，「图标」常用「圖示」。
```

### social-daily-0073：match

Input:

```text
闹钟没有响。
```

Codex draft expected:

```text
鬧鐘沒有響。
```

Gemini advisory expected:

```text
鬧鐘沒有響。
```

Gemini notes:

```text

```

### social-daily-0074：match

Input:

```text
明早七点提醒我出门。
```

Codex draft expected:

```text
明早七點提醒我出門。
```

Gemini advisory expected:

```text
明早七點提醒我出門。
```

Gemini notes:

```text

```

### social-daily-0075：match

Input:

```text
今天空气质量不错。
```

Codex draft expected:

```text
今天空氣品質不錯。
```

Gemini advisory expected:

```text
今天空氣品質不錯。
```

Gemini notes:

```text
「质量」在台灣常用「品質」。
```
