<!-- zhtw:disable -->
# Annotation First-Pass AI Draft：mixed-ambiguity 0001-0025（2026-07-07）

Backlog：`benchmarks/accuracy/annotation-backlog-v1.json`

## Boundary

- This is Codex AI draft only.
- Do not promote these expected values directly.
- Workflow for this batch is Codex draft -> Gemini independent advisory -> maintainer final review.
- Maintainer must choose the final expected value before anything is copied into `review.expected`.
- Do not set `review.expected_source = "human_first_pass"` until maintainer final review accepts a value.

## Cases

### mixed-ambiguity-0001

Input:

```text
这个程序会自动退出。
```

AI draft expected:

```text
這個程式會自動結束。
```

Notes：軟體語境：程序→程式、自動退出→自動結束。

### mixed-ambiguity-0002

Input:

```text
会议程序已经排好。
```

AI draft expected:

```text
會議程序已經排好。
```

Notes：流程語境：程序保留為程序，不轉成程式。

### mixed-ambiguity-0003

Input:

```text
请打开这个文件。
```

AI draft expected:

```text
請開啟這個檔案。
```

Notes：電腦檔案語境：文件→檔案、打开→開啟。

### mixed-ambiguity-0004

Input:

```text
请提交证明文件。
```

AI draft expected:

```text
請提交證明文件。
```

Notes：正式文件語境：文件保留為文件，不轉成檔案。

### mixed-ambiguity-0005

Input:

```text
这个对象包含三个字段。
```

AI draft expected:

```text
這個物件包含三個欄位。
```

Notes：程式資料結構語境：对象→物件、字段→欄位。

### mixed-ambiguity-0006

Input:

```text
研究对象需要签署同意书。
```

AI draft expected:

```text
研究對象需要簽署同意書。
```

Notes：研究對象語境：对象→對象，不轉成物件。

### mixed-ambiguity-0007

Input:

```text
技术支持会协助排查。
```

AI draft expected:

```text
技術支援會協助排查。
```

Notes：客服/技術語境：支持→支援。

### mixed-ambiguity-0008

Input:

```text
这份证据支持他的说法。
```

AI draft expected:

```text
這份證據支持他的說法。
```

Notes：一般動詞語境：支持保留支持，不轉成支援。

### mixed-ambiguity-0009

Input:

```text
后台服务正在重启。
```

AI draft expected:

```text
背景服務正在重新啟動。
```

Notes：系統服務語境：后台→背景、重启→重新啟動。

### mixed-ambiguity-0010

Input:

```text
她在后台准备上场。
```

AI draft expected:

```text
她在後台準備上場。
```

Notes：舞台語境：后台→後台。

### mixed-ambiguity-0011

Input:

```text
接口返回空数组。
```

AI draft expected:

```text
介面回傳空陣列。
```

Notes：API 語境：接口→介面、返回→回傳、数组→陣列。

### mixed-ambiguity-0012

Input:

```text
海关窗口今天暂停服务。
```

AI draft expected:

```text
海關窗口今天暫停服務。
```

Notes：行政窗口語境：窗口保留窗口，不轉成視窗。

### mixed-ambiguity-0013

Input:

```text
服务端口被占用。
```

AI draft expected:

```text
服務連接埠被佔用。
```

Notes：網路服務語境：端口→連接埠、占用→佔用。

### mixed-ambiguity-0014

Input:

```text
港口今天暂停开放。
```

AI draft expected:

```text
港口今天暫停開放。
```

Notes：港口語境：港口保留港口，不轉成連接埠。

### mixed-ambiguity-0015

Input:

```text
线程阻塞会影响性能。
```

AI draft expected:

```text
執行緒阻塞會影響效能。
```

Notes：程式效能語境：线程→執行緒、性能→效能。

### mixed-ambiguity-0016

Input:

```text
道路阻塞会影响通行。
```

AI draft expected:

```text
道路阻塞會影響通行。
```

Notes：交通語境：阻塞保留阻塞，不改成程式術語。

### mixed-ambiguity-0017

Input:

```text
缓存命中率下降。
```

AI draft expected:

```text
快取命中率下降。
```

Notes：系統效能語境：缓存→快取。

### mixed-ambiguity-0018

Input:

```text
他缓存了那张照片。
```

AI draft expected:

```text
他快取了那張照片。
```

Notes：日常裝置語境：缓存→快取、那张→那張。

### mixed-ambiguity-0019

Input:

```text
项目经理更新了排程。
```

AI draft expected:

```text
專案經理更新了排程。
```

Notes：專案管理語境：项目→專案。

### mixed-ambiguity-0020

Input:

```text
补助项目明天截止。
```

AI draft expected:

```text
補助計畫明天截止。
```

Notes：政府補助語境：项目→計畫。

### mixed-ambiguity-0021

Input:

```text
服务器返回状态码。
```

AI draft expected:

```text
伺服器回傳狀態碼。
```

Notes：技術語境：服务器→伺服器、返回→回傳。

### mixed-ambiguity-0022

Input:

```text
他返回家乡工作。
```

AI draft expected:

```text
他返回家鄉工作。
```

Notes：一般動詞語境：返回保留返回，不轉成回傳。

### mixed-ambiguity-0023

Input:

```text
这个入口会跳转到登录页。
```

AI draft expected:

```text
這個入口會跳轉到登入頁。
```

Notes：網頁入口語境：登录页→登入頁。

### mixed-ambiguity-0024

Input:

```text
捷运入口在便利店旁边。
```

AI draft expected:

```text
捷運入口在便利商店旁邊。
```

Notes：交通日常語境：入口保留入口、便利店→便利商店。

### mixed-ambiguity-0025

Input:

```text
数据表字段不能重复。
```

AI draft expected:

```text
資料表欄位不能重複。
```

Notes：資料庫語境：数据表→資料表、字段→欄位。
