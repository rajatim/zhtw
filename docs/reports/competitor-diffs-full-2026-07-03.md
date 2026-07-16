<!-- zhtw:disable -->
# 競品差異探索報告（2026-07-03）

## 摘要

- Corpus：`tests/data/corpus`
- Categories：news, regressions, social, tech, wiki
- 掃描 case：500 / 500
- 含 expected：500
- 輸出差異 rows：308
- Seed：42

## Engines

| Engine | Version | Status |
|--------|---------|--------|
| `zhtw` | 4.4.1 | available |
| `opencc-s2twp` | 0.1.7 | available |
| `zhconv-zh-tw` | 1.4.3 | available |

## Scanned Summary

| Classification | Count |
|----------------|-------|
| `all_match` | 192 |
| `zhtw_advantage` | 308 |

## Diff Row Summary

| Classification | Count |
|----------------|-------|
| `zhtw_advantage` | 308 |

## Rows

### regressions/regression_045 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：寫程式前先看法律程序
- Review：pending
- Notes：程式/程序雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 寫程式前先看法律程序 |
| `opencc-s2twp` | 寫程式前先看法律程式 |
| `zhconv-zh-tw` | 寫程序前先看法律程序 |

### tech/tech_004 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：透過非同步回呼來處理網路請求。
- Review：pending
- Notes：异步→非同步, 回调→回呼, 网络→網路

| Engine | Output |
|--------|--------|
| `zhtw` | 透過非同步回呼來處理網路請求。 |
| `opencc-s2twp` | 透過非同步回撥來處理網路請求。 |
| `zhconv-zh-tw` | 通過異步回調來處理網絡請求。 |

### regressions/regression_037 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：重新整理頁面看看
- Review：pending
- Notes：UI 刷新頁面→重新整理頁面

| Engine | Output |
|--------|--------|
| `zhtw` | 重新整理頁面看看 |
| `opencc-s2twp` | 重新整理頁面看看 |
| `zhconv-zh-tw` | 刷新頁面看看 |

### news/news_053 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：官方說明資料統計方式。
- Review：pending
- Notes：数据→數據，统计→統計

| Engine | Output |
|--------|--------|
| `zhtw` | 官方說明資料統計方式。 |
| `opencc-s2twp` | 官方說明資料統計方式。 |
| `zhconv-zh-tw` | 官方說明數據統計方式。 |

### tech/tech_076 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：伺服器憑證即將過期。
- Review：pending
- Notes：服务器→伺服器，证书→憑證

| Engine | Output |
|--------|--------|
| `zhtw` | 伺服器憑證即將過期。 |
| `opencc-s2twp` | 伺服器證書即將過期。 |
| `zhconv-zh-tw` | 伺服器證書即將過期。 |

### social/social_070 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：重新整理頁面後就能登入。
- Review：pending
- Notes：刷新页面→重新整理頁面

| Engine | Output |
|--------|--------|
| `zhtw` | 重新整理頁面後就能登入。 |
| `opencc-s2twp` | 重新整理頁面後就能登入。 |
| `zhconv-zh-tw` | 刷新頁面後就能登錄。 |

### news/news_055 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：選務機關公布投票注意事項。
- Review：pending
- Notes：公布保持公布，事项→事項

| Engine | Output |
|--------|--------|
| `zhtw` | 選務機關公布投票注意事項。 |
| `opencc-s2twp` | 選務機關公佈投票注意事項。 |
| `zhconv-zh-tw` | 選務機關公布投票注意事項。 |

### tech/tech_094 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：這個函式庫提供加密函式。
- Review：pending
- Notes：库→函式庫，函数→函式

| Engine | Output |
|--------|--------|
| `zhtw` | 這個函式庫提供加密函式。 |
| `opencc-s2twp` | 這個庫提供加密函式。 |
| `zhconv-zh-tw` | 這個庫提供加密函數。 |

### wiki/wiki_064 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：人工智慧系統依賴大量資料。
- Review：pending
- Notes：人工智能→人工智慧

| Engine | Output |
|--------|--------|
| `zhtw` | 人工智慧系統依賴大量資料。 |
| `opencc-s2twp` | 人工智慧系統依賴大量資料。 |
| `zhconv-zh-tw` | 人工智慧系統依賴大量數據。 |

### social/social_076 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：註銷公司需要準備文件。
- Review：pending
- Notes：注销公司→註銷公司

| Engine | Output |
|--------|--------|
| `zhtw` | 註銷公司需要準備文件。 |
| `opencc-s2twp` | 登出公司需要準備檔案。 |
| `zhconv-zh-tw` | 註銷公司需要準備文件。 |

### wiki/wiki_060 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：博物館保存歷史文物。
- Review：pending
- Notes：博物馆→博物館，历史→歷史

| Engine | Output |
|--------|--------|
| `zhtw` | 博物館保存歷史文物。 |
| `opencc-s2twp` | 博物館儲存歷史文物。 |
| `zhconv-zh-tw` | 博物館保存歷史文物。 |

### news/news_040 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：勞動部提醒雇主依法給付工資。
- Review：pending
- Notes：劳动→勞動，工资→工資

| Engine | Output |
|--------|--------|
| `zhtw` | 勞動部提醒雇主依法給付工資。 |
| `opencc-s2twp` | 勞動部提醒僱主依法給付工資。 |
| `zhconv-zh-tw` | 勞動部提醒僱主依法給付工資。 |

### tech/tech_049 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：日誌等級可以透過參數調整。
- Review：pending
- Notes：通过参数→透過參數，调整→調整

| Engine | Output |
|--------|--------|
| `zhtw` | 日誌等級可以透過參數調整。 |
| `opencc-s2twp` | 日誌等級可以透過引數調整。 |
| `zhconv-zh-tw` | 日誌等級可以通過參數調整。 |

### regressions/regression_044 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：政府發布官方文件
- Review：pending
- Notes：正式文件保持文件

| Engine | Output |
|--------|--------|
| `zhtw` | 政府發布官方文件 |
| `opencc-s2twp` | 政府釋出官方檔案 |
| `zhconv-zh-tw` | 政府發布官方文件 |

### social/social_071 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：留言區有人分享連結。
- Review：pending
- Notes：评论区→留言區

| Engine | Output |
|--------|--------|
| `zhtw` | 留言區有人分享連結。 |
| `opencc-s2twp` | 評論區有人分享連結。 |
| `zhconv-zh-tw` | 評論區有人分享連結。 |

### wiki/wiki_024 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：網路協議定義設備之間的通訊規則。
- Review：pending
- Notes：网络协议→網路協定，通信→通訊

| Engine | Output |
|--------|--------|
| `zhtw` | 網路協議定義設備之間的通訊規則。 |
| `opencc-s2twp` | 網路協議定義裝置之間的通訊規則。 |
| `zhconv-zh-tw` | 網絡協議定義設備之間的通信規則。 |

### tech/tech_081 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：訊息佇列處理失敗事件。
- Review：pending
- Notes：消息队列→訊息佇列

| Engine | Output |
|--------|--------|
| `zhtw` | 訊息佇列處理失敗事件。 |
| `opencc-s2twp` | 訊息佇列處理失敗事件。 |
| `zhconv-zh-tw` | 消息隊列處理失敗事件。 |

### social/social_010 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：預設頭像太醜了。
- Review：pending
- Notes：默认头像→預設頭像, 丑→醜

| Engine | Output |
|--------|--------|
| `zhtw` | 預設頭像太醜了。 |
| `opencc-s2twp` | 預設頭像太醜了。 |
| `zhconv-zh-tw` | 默認頭像太醜了。 |

### tech/tech_010 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：日誌文件記錄錯誤資訊。
- Review：pending
- Notes：日志→日誌, 记录→記錄, 错误→錯誤, 信息→資訊

| Engine | Output |
|--------|--------|
| `zhtw` | 日誌文件記錄錯誤資訊。 |
| `opencc-s2twp` | 日誌檔案記錄錯誤資訊。 |
| `zhconv-zh-tw` | 日誌文件記錄錯誤信息。 |

### news/news_068 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：央行宣布維持利率政策不變。
- Review：pending
- Notes：宣布保持宣布

| Engine | Output |
|--------|--------|
| `zhtw` | 央行宣布維持利率政策不變。 |
| `opencc-s2twp` | 央行宣佈維持利率政策不變。 |
| `zhconv-zh-tw` | 央行宣布維持利率政策不變。 |

### wiki/wiki_043 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：雲端運算提供彈性的計算資源。
- Review：pending
- Notes：云计算→雲端運算，资源→資源

| Engine | Output |
|--------|--------|
| `zhtw` | 雲端運算提供彈性的計算資源。 |
| `opencc-s2twp` | 雲端計算提供彈性的計算資源。 |
| `zhconv-zh-tw` | 雲計算提供彈性的計算資源。 |

### social/social_030 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這個連結可以直接打開。
- Review：pending
- Notes：链接→連結，打开→打開

| Engine | Output |
|--------|--------|
| `zhtw` | 這個連結可以直接打開。 |
| `opencc-s2twp` | 這個連結可以直接開啟。 |
| `zhconv-zh-tw` | 這個連結可以直接打開。 |

### social/social_026 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這個帳號終於恢復了。
- Review：pending
- Notes：账号→帳號，恢复保持恢復

| Engine | Output |
|--------|--------|
| `zhtw` | 這個帳號終於恢復了。 |
| `opencc-s2twp` | 這個賬號終於恢復了。 |
| `zhconv-zh-tw` | 這個帳號終於恢復了。 |

### regressions/regression_090 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：用戶端和伺服器端通訊
- Review：pending
- Notes：端點與通訊術語

| Engine | Output |
|--------|--------|
| `zhtw` | 用戶端和伺服器端通訊 |
| `opencc-s2twp` | 使用者端和伺服器端通訊 |
| `zhconv-zh-tw` | 用戶端和伺服器端通信 |

### regressions/regression_043 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：檔案系統損壞
- Review：pending
- Notes：文件系统→檔案系統

| Engine | Output |
|--------|--------|
| `zhtw` | 檔案系統損壞 |
| `opencc-s2twp` | 檔案系統損壞 |
| `zhconv-zh-tw` | 文件系統損壞 |

### social/social_084 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：這個頻道每週更新一次。
- Review：pending
- Notes：每周→每週

| Engine | Output |
|--------|--------|
| `zhtw` | 這個頻道每週更新一次。 |
| `opencc-s2twp` | 這個頻道每週更新一次。 |
| `zhconv-zh-tw` | 這個頻道每周更新一次。 |

### news/news_022 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：台積電宣布擴大先進製程投資。
- Review：pending
- Notes：宣布保持宣布，制程→製程

| Engine | Output |
|--------|--------|
| `zhtw` | 台積電宣布擴大先進製程投資。 |
| `opencc-s2twp` | 臺積電宣佈擴大先進製程投資。 |
| `zhconv-zh-tw` | 臺積電宣布擴大先進位程投資。 |

### social/social_059 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：剛才網路突然斷線。
- Review：pending
- Notes：网络→網路，断线→斷線

| Engine | Output |
|--------|--------|
| `zhtw` | 剛才網路突然斷線。 |
| `opencc-s2twp` | 剛才網路突然斷線。 |
| `zhconv-zh-tw` | 剛才網絡突然斷線。 |

### social/social_088 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：預設頭像和暱稱都要改。
- Review：pending
- Notes：默认头像→預設頭像

| Engine | Output |
|--------|--------|
| `zhtw` | 預設頭像和暱稱都要改。 |
| `opencc-s2twp` | 預設頭像和暱稱都要改。 |
| `zhconv-zh-tw` | 默認頭像和暱稱都要改。 |

### regressions/regression_032 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：我支持這個決定
- Review：pending
- Notes：一般語境支持保持支持

| Engine | Output |
|--------|--------|
| `zhtw` | 我支持這個決定 |
| `opencc-s2twp` | 我支援這個決定 |
| `zhconv-zh-tw` | 我支持這個決定 |

### tech/tech_050 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個模組負責資料同步。
- Review：pending
- Notes：模块→模組，数据→資料

| Engine | Output |
|--------|--------|
| `zhtw` | 這個模組負責資料同步。 |
| `opencc-s2twp` | 這個模組負責資料同步。 |
| `zhconv-zh-tw` | 這個模塊負責數據同步。 |

### social/social_078 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：手機網路突然變慢。
- Review：pending
- Notes：网络→網路

| Engine | Output |
|--------|--------|
| `zhtw` | 手機網路突然變慢。 |
| `opencc-s2twp` | 手機網路突然變慢。 |
| `zhconv-zh-tw` | 手機網絡突然變慢。 |

### regressions/regression_035 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：儲存檔案成功
- Review：pending
- Notes：UI 檔案語境保存→儲存

| Engine | Output |
|--------|--------|
| `zhtw` | 儲存檔案成功 |
| `opencc-s2twp` | 儲存檔案成功 |
| `zhconv-zh-tw` | 保存文件成功 |

### tech/tech_087 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：網路請求透過代理伺服器轉發。
- Review：pending
- Notes：通过代理→透過代理

| Engine | Output |
|--------|--------|
| `zhtw` | 網路請求透過代理伺服器轉發。 |
| `opencc-s2twp` | 網路請求透過代理伺服器轉發。 |
| `zhconv-zh-tw` | 網絡請求通過代理伺服器轉發。 |

### regressions/regression_051 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：好消息傳來
- Review：pending
- Notes：好消息保持消息

| Engine | Output |
|--------|--------|
| `zhtw` | 好消息傳來 |
| `opencc-s2twp` | 好訊息傳來 |
| `zhconv-zh-tw` | 好消息傳來 |

### news/news_009 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：該公司裁員計畫已經啟動。
- Review：pending
- Notes：该→該, 计划→計畫, 已经→已經, 启动→啟動

| Engine | Output |
|--------|--------|
| `zhtw` | 該公司裁員計畫已經啟動。 |
| `opencc-s2twp` | 該公司裁員計劃已經啟動。 |
| `zhconv-zh-tw` | 該公司裁員計劃已經啟動。 |

### wiki/wiki_100 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：統計學用於分析大量資料。
- Review：pending
- Notes：数据→資料

| Engine | Output |
|--------|--------|
| `zhtw` | 統計學用於分析大量資料。 |
| `opencc-s2twp` | 統計學用於分析大量資料。 |
| `zhconv-zh-tw` | 統計學用於分析大量數據。 |

### tech/tech_064 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：快取鍵包含使用者編號。
- Review：pending
- Notes：缓存→快取，用户→使用者

| Engine | Output |
|--------|--------|
| `zhtw` | 快取鍵包含使用者編號。 |
| `opencc-s2twp` | 快取鍵包含使用者編號。 |
| `zhconv-zh-tw` | 緩存鍵包含用戶編號。 |

### regressions/regression_020 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：背景程式裡的日誌文件
- Review：pending
- Notes：后台程序→背景程式, 里的→裡的, 日志→日誌

| Engine | Output |
|--------|--------|
| `zhtw` | 背景程式裡的日誌文件 |
| `opencc-s2twp` | 後臺程式裡的日誌檔案 |
| `zhconv-zh-tw` | 後臺程序裡的日誌文件 |

### regressions/regression_092 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：這週到店不是這周到的安排
- Review：pending
- Notes：週到店/周到安排雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 這週到店不是這周到的安排 |
| `opencc-s2twp` | 這周到店不是這周到的安排 |
| `zhconv-zh-tw` | 這周到店不是這周到的安排 |

### regressions/regression_081 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：登出帳戶不是註銷公司
- Review：pending
- Notes：登出/註銷雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 登出帳戶不是註銷公司 |
| `opencc-s2twp` | 登出賬戶不是登出公司 |
| `zhconv-zh-tw` | 註銷帳戶不是註銷公司 |

### tech/tech_039 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個介面回傳狀態碼和回應標頭。
- Review：pending
- Notes：返回状态码→回傳狀態碼，响应头→回應標頭

| Engine | Output |
|--------|--------|
| `zhtw` | 這個介面回傳狀態碼和回應標頭。 |
| `opencc-s2twp` | 這個介面返回狀態碼和響應頭。 |
| `zhconv-zh-tw` | 這個接口返回狀態碼和響應頭。 |

### tech/tech_051 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請確認網路介面是否啟用。
- Review：pending
- Notes：网络接口→網路介面，启用→啟用

| Engine | Output |
|--------|--------|
| `zhtw` | 請確認網路介面是否啟用。 |
| `opencc-s2twp` | 請確認網路介面是否啟用。 |
| `zhconv-zh-tw` | 請確認網絡接口是否啟用。 |

### regressions/regression_041 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：登出帳戶流程
- Review：pending
- Notes：帳戶語境→登出

| Engine | Output |
|--------|--------|
| `zhtw` | 登出帳戶流程 |
| `opencc-s2twp` | 登出賬戶流程 |
| `zhconv-zh-tw` | 註銷帳戶流程 |

### news/news_065 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：調查顯示年輕族群支持遠端辦公。
- Review：pending
- Notes：一般支持保持支持

| Engine | Output |
|--------|--------|
| `zhtw` | 調查顯示年輕族群支持遠端辦公。 |
| `opencc-s2twp` | 調查顯示年輕族群支援遠端辦公。 |
| `zhconv-zh-tw` | 調查顯示年輕族群支持遠程辦公。 |

### tech/tech_065 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：前端元件監聽點擊事件。
- Review：pending
- Notes：组件→元件

| Engine | Output |
|--------|--------|
| `zhtw` | 前端元件監聽點擊事件。 |
| `opencc-s2twp` | 前端元件監聽點選事件。 |
| `zhconv-zh-tw` | 前端組件監聽點擊事件。 |

### regressions/regression_009 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：重新整理頁面後再登入
- Review：pending
- Notes：刷新页面→重新整理頁面, 后→後, 登录→登入

| Engine | Output |
|--------|--------|
| `zhtw` | 重新整理頁面後再登入 |
| `opencc-s2twp` | 重新整理頁面後再登入 |
| `zhconv-zh-tw` | 刷新頁面後再登錄 |

### tech/tech_021 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：持續整合管線已經通過。
- Review：pending
- Notes：持续集成流水线→持續整合管線

| Engine | Output |
|--------|--------|
| `zhtw` | 持續整合管線已經通過。 |
| `opencc-s2twp` | 持續整合流水線已經透過。 |
| `zhconv-zh-tw` | 持續集成流水線已經通過。 |

### wiki/wiki_069 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：生態環境影響物種分布。
- Review：pending
- Notes：生态→生態

| Engine | Output |
|--------|--------|
| `zhtw` | 生態環境影響物種分布。 |
| `opencc-s2twp` | 生態環境影響物種分佈。 |
| `zhconv-zh-tw` | 生態環境影響物種分布。 |

### regressions/regression_088 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：資料中心和資料結構都不同
- Review：pending
- Notes：IT 資料語境

| Engine | Output |
|--------|--------|
| `zhtw` | 資料中心和資料結構都不同 |
| `opencc-s2twp` | 資料中心和資料結構都不同 |
| `zhconv-zh-tw` | 數據中心和數據結構都不同 |

### news/news_067 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：環保署公布空氣汙染監測結果。
- Review：pending
- Notes：公布保持公布

| Engine | Output |
|--------|--------|
| `zhtw` | 環保署公布空氣汙染監測結果。 |
| `opencc-s2twp` | 環保署公佈空氣汙染監測結果。 |
| `zhconv-zh-tw` | 環保署公布空氣汙染監測結果。 |

### wiki/wiki_023 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：編譯器會把原始碼轉換為機器程式碼。
- Review：pending
- Notes：编译器→編譯器，源代码→原始碼

| Engine | Output |
|--------|--------|
| `zhtw` | 編譯器會把原始碼轉換為機器程式碼。 |
| `opencc-s2twp` | 編譯器會把原始碼轉換為機器程式碼。 |
| `zhconv-zh-tw` | 編譯器會把原始碼轉換為機器代碼。 |

### social/social_027 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：我把文件上傳到群組了。
- Review：pending
- Notes：上传→上傳，群组→群組

| Engine | Output |
|--------|--------|
| `zhtw` | 我把文件上傳到群組了。 |
| `opencc-s2twp` | 我把檔案上傳到群組了。 |
| `zhconv-zh-tw` | 我把文件上傳到群組了。 |

### tech/tech_017 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：資料庫遷移指令碼失敗了。
- Review：pending
- Notes：数据库→資料庫, 脚本→指令碼, 失败→失敗

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫遷移指令碼失敗了。 |
| `opencc-s2twp` | 資料庫遷移指令碼失敗了。 |
| `zhconv-zh-tw` | 資料庫遷移腳本失敗了。 |

### tech/tech_026 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個函式會拋出例外。
- Review：pending
- Notes：函数→函式，异常→例外

| Engine | Output |
|--------|--------|
| `zhtw` | 這個函式會拋出例外。 |
| `opencc-s2twp` | 這個函式會丟擲異常。 |
| `zhconv-zh-tw` | 這個函數會拋出異常。 |

### wiki/wiki_087 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：雪梨港是澳大利亞重要港口。
- Review：pending
- Notes：悉尼→雪梨

| Engine | Output |
|--------|--------|
| `zhtw` | 雪梨港是澳大利亞重要港口。 |
| `opencc-s2twp` | 悉尼港是澳大利亞重要港口。 |
| `zhconv-zh-tw` | 雪梨港是澳大利亞重要港口。 |

### regressions/regression_005 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：隨身碟和隨身碟
- Review：pending
- Notes：优盘和U盘都應轉為隨身碟

| Engine | Output |
|--------|--------|
| `zhtw` | 隨身碟和隨身碟 |
| `opencc-s2twp` | 優盤和隨身碟 |
| `zhconv-zh-tw` | 優盤和U盤 |

### social/social_043 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這個選單選項藏太深。
- Review：pending
- Notes：菜单→選單，选项→選項

| Engine | Output |
|--------|--------|
| `zhtw` | 這個選單選項藏太深。 |
| `opencc-s2twp` | 這個選單選項藏太深。 |
| `zhconv-zh-tw` | 這個菜單選項藏太深。 |

### social/social_068 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：儲存檔案前先檢查格式。
- Review：pending
- Notes：保存文件→儲存檔案

| Engine | Output |
|--------|--------|
| `zhtw` | 儲存檔案前先檢查格式。 |
| `opencc-s2twp` | 儲存檔案前先檢查格式。 |
| `zhconv-zh-tw` | 保存文件前先檢查格式。 |

### regressions/regression_061 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：升級設備之後再次檢查設備
- Review：pending
- Notes：設備 target 冪等

| Engine | Output |
|--------|--------|
| `zhtw` | 升級設備之後再次檢查設備 |
| `opencc-s2twp` | 升級裝置之後再次檢查裝置 |
| `zhconv-zh-tw` | 升級設備之後再次檢查設備 |

### tech/tech_015 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：這個演算法的時間複雜度很高。
- Review：pending
- Notes：算法→演算法, 复杂度→複雜度

| Engine | Output |
|--------|--------|
| `zhtw` | 這個演算法的時間複雜度很高。 |
| `opencc-s2twp` | 這個演算法的時間複雜度很高。 |
| `zhconv-zh-tw` | 這個算法的時間複雜度很高。 |

### regressions/regression_036 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：保存文化遺產
- Review：pending
- Notes：一般保存不應轉儲存

| Engine | Output |
|--------|--------|
| `zhtw` | 保存文化遺產 |
| `opencc-s2twp` | 儲存文化遺產 |
| `zhconv-zh-tw` | 保存文化遺產 |

### social/social_091 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：他傳訊息提醒我下週到場。
- Review：pending
- Notes：下周到→下週到

| Engine | Output |
|--------|--------|
| `zhtw` | 他傳訊息提醒我下週到場。 |
| `opencc-s2twp` | 他發訊息提醒我下週到場。 |
| `zhconv-zh-tw` | 他發消息提醒我下周到場。 |

### tech/tech_043 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：伺服器憑證將在明天過期。
- Review：pending
- Notes：服务器→伺服器，证书→憑證

| Engine | Output |
|--------|--------|
| `zhtw` | 伺服器憑證將在明天過期。 |
| `opencc-s2twp` | 伺服器證書將在明天過期。 |
| `zhconv-zh-tw` | 伺服器證書將在明天過期。 |

### social/social_098 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：剛才網路突然斷線。
- Review：pending
- Notes：网络→網路

| Engine | Output |
|--------|--------|
| `zhtw` | 剛才網路突然斷線。 |
| `opencc-s2twp` | 剛才網路突然斷線。 |
| `zhconv-zh-tw` | 剛才網絡突然斷線。 |

### tech/tech_034 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：用戶端會保存會話權杖。
- Review：pending
- Notes：用户端→用戶端，会话→工作階段

| Engine | Output |
|--------|--------|
| `zhtw` | 用戶端會保存會話權杖。 |
| `opencc-s2twp` | 使用者端會儲存會話令牌。 |
| `zhconv-zh-tw` | 用戶端會保存會話令牌。 |

### tech/tech_084 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：模組載入順序會影響效能。
- Review：pending
- Notes：性能→效能

| Engine | Output |
|--------|--------|
| `zhtw` | 模組載入順序會影響效能。 |
| `opencc-s2twp` | 模組載入順序會影響效能。 |
| `zhconv-zh-tw` | 模塊加載順序會影響性能。 |

### tech/tech_014 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：後端服務回傳狀態碼。
- Review：pending
- Notes：后端→後端, 服务→服務, 返回状态码→回傳狀態碼

| Engine | Output |
|--------|--------|
| `zhtw` | 後端服務回傳狀態碼。 |
| `opencc-s2twp` | 後端服務返回狀態碼。 |
| `zhconv-zh-tw` | 後端服務返回狀態碼。 |

### regressions/regression_034 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：他的結婚對象很溫柔
- Review：pending
- Notes：一般對象不應轉物件

| Engine | Output |
|--------|--------|
| `zhtw` | 他的結婚對象很溫柔 |
| `opencc-s2twp` | 他的結婚物件很溫柔 |
| `zhconv-zh-tw` | 他的結婚對象很溫柔 |

### tech/tech_074 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：回應時間超過閾值。
- Review：pending
- Notes：响应时间→回應時間

| Engine | Output |
|--------|--------|
| `zhtw` | 回應時間超過閾值。 |
| `opencc-s2twp` | 響應時間超過閾值。 |
| `zhconv-zh-tw` | 響應時間超過閾值。 |

### news/news_099 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：消費糾紛調解會議下週召開。
- Review：pending
- Notes：下周→下週

| Engine | Output |
|--------|--------|
| `zhtw` | 消費糾紛調解會議下週召開。 |
| `opencc-s2twp` | 消費糾紛調解會議下週召開。 |
| `zhconv-zh-tw` | 消費糾紛調解會議下周召開。 |

### tech/tech_013 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：前端元件需要支援深色模式。
- Review：pending
- Notes：组件→元件, 支持深色模式→支援深色模式

| Engine | Output |
|--------|--------|
| `zhtw` | 前端元件需要支援深色模式。 |
| `opencc-s2twp` | 前端元件需要支援深色模式。 |
| `zhconv-zh-tw` | 前端組件需要支持深色模式。 |

### regressions/regression_067 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：請先登入系統再登出帳戶
- Review：pending
- Notes：登录系统→登入系統

| Engine | Output |
|--------|--------|
| `zhtw` | 請先登入系統再登出帳戶 |
| `opencc-s2twp` | 請先登入系統再登出賬戶 |
| `zhconv-zh-tw` | 請先登錄系統再註銷帳戶 |

### tech/tech_029 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：資料庫連線池已經耗盡。
- Review：pending
- Notes：数据库→資料庫，连接池→連線池

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫連線池已經耗盡。 |
| `opencc-s2twp` | 資料庫連線池已經耗盡。 |
| `zhconv-zh-tw` | 資料庫連接池已經耗盡。 |

### wiki/wiki_010 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：網際網路協定定義了資料傳輸規則。
- Review：pending
- Notes：互联网协议→網際網路協定, 数据→資料, 传输→傳輸, 规则→規則

| Engine | Output |
|--------|--------|
| `zhtw` | 網際網路協定定義了資料傳輸規則。 |
| `opencc-s2twp` | 網際網路協議定義了資料傳輸規則。 |
| `zhconv-zh-tw` | 網際網路協議定義了數據傳輸規則。 |

### regressions/regression_039 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：復原操作成功
- Review：pending
- Notes：UI 撤销操作→復原操作

| Engine | Output |
|--------|--------|
| `zhtw` | 復原操作成功 |
| `opencc-s2twp` | 撤銷操作成功 |
| `zhconv-zh-tw` | 撤銷操作成功 |

### social/social_025 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：剛剛看到一個超好笑的影片。
- Review：pending
- Notes：视频→影片

| Engine | Output |
|--------|--------|
| `zhtw` | 剛剛看到一個超好笑的影片。 |
| `opencc-s2twp` | 剛剛看到一個超好笑的影片。 |
| `zhconv-zh-tw` | 剛剛看到一個超好笑的視頻。 |

### social/social_048 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：週末要不要去看電影？
- Review：pending
- Notes：周末→週末，电影→電影

| Engine | Output |
|--------|--------|
| `zhtw` | 週末要不要去看電影？ |
| `opencc-s2twp` | 週末要不要去看電影？ |
| `zhconv-zh-tw` | 周末要不要去看電影？ |

### wiki/wiki_062 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：作業系統提供檔案系統介面。
- Review：pending
- Notes：文件系统→檔案系統

| Engine | Output |
|--------|--------|
| `zhtw` | 作業系統提供檔案系統介面。 |
| `opencc-s2twp` | 作業系統提供檔案系統介面。 |
| `zhconv-zh-tw` | 作業系統提供文件系統接口。 |

### social/social_012 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：週末想去騎腳踏車。
- Review：pending
- Notes：周末→週末, 骑→騎, 自行车→腳踏車

| Engine | Output |
|--------|--------|
| `zhtw` | 週末想去騎腳踏車。 |
| `opencc-s2twp` | 週末想去騎腳踏車。 |
| `zhconv-zh-tw` | 周末想去騎自行車。 |

### regressions/regression_019 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：檔案系統裡的檔名
- Review：pending
- Notes：文件系统→檔案系統, 里的→裡的, 文件名→檔名

| Engine | Output |
|--------|--------|
| `zhtw` | 檔案系統裡的檔名 |
| `opencc-s2twp` | 檔案系統裡的檔名 |
| `zhconv-zh-tw` | 文件系統裡的文件名 |

### regressions/regression_093 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：每週到店但服務很周到
- Review：pending
- Notes：每週到與周到雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 每週到店但服務很周到 |
| `opencc-s2twp` | 每週到店但服務很周到 |
| `zhconv-zh-tw` | 每周到店但服務很周到 |

### tech/tech_085 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：這個套件管理員會鎖定相依性版本。
- Review：pending
- Notes：包管理器→套件管理員

| Engine | Output |
|--------|--------|
| `zhtw` | 這個套件管理員會鎖定相依性版本。 |
| `opencc-s2twp` | 這個包管理器會鎖定依賴版本。 |
| `zhconv-zh-tw` | 這個包管理器會鎖定依賴版本。 |

### tech/tech_083 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：伺服器端回傳錯誤資訊。
- Review：pending
- Notes：服务端→伺服器端，返回→回傳

| Engine | Output |
|--------|--------|
| `zhtw` | 伺服器端回傳錯誤資訊。 |
| `opencc-s2twp` | 服務端返回錯誤資訊。 |
| `zhconv-zh-tw` | 服務端返回錯誤信息。 |

### wiki/wiki_009 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：雪梨位於澳大利亞東南部。
- Review：pending
- Notes：悉尼→雪梨, 位于→位於, 澳大利亚→澳大利亞

| Engine | Output |
|--------|--------|
| `zhtw` | 雪梨位於澳大利亞東南部。 |
| `opencc-s2twp` | 悉尼位於澳大利亞東南部。 |
| `zhconv-zh-tw` | 雪梨位於澳大利亞東南部。 |

### social/social_044 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：請幫我保存這張照片。
- Review：pending
- Notes：保存照片保持保存

| Engine | Output |
|--------|--------|
| `zhtw` | 請幫我保存這張照片。 |
| `opencc-s2twp` | 請幫我儲存這張照片。 |
| `zhconv-zh-tw` | 請幫我保存這張照片。 |

### news/news_057 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：警方加強週末酒駕取締。
- Review：pending
- Notes：周末→週末，酒驾→酒駕

| Engine | Output |
|--------|--------|
| `zhtw` | 警方加強週末酒駕取締。 |
| `opencc-s2twp` | 警方加強週末酒駕取締。 |
| `zhconv-zh-tw` | 警方加強周末酒駕取締。 |

### social/social_034 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：默認鈴聲聽起來很普通。
- Review：pending
- Notes：默认铃声→預設鈴聲

| Engine | Output |
|--------|--------|
| `zhtw` | 默認鈴聲聽起來很普通。 |
| `opencc-s2twp` | 預設鈴聲聽起來很普通。 |
| `zhconv-zh-tw` | 默認鈴聲聽起來很普通。 |

### tech/tech_075 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：記憶體使用量持續上升。
- Review：pending
- Notes：内存→記憶體

| Engine | Output |
|--------|--------|
| `zhtw` | 記憶體使用量持續上升。 |
| `opencc-s2twp` | 記憶體使用量持續上升。 |
| `zhconv-zh-tw` | 內存使用量持續上升。 |

### tech/tech_032 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：部署管線失敗後請查看日誌。
- Review：pending
- Notes：流水线→管線，日志→日誌

| Engine | Output |
|--------|--------|
| `zhtw` | 部署管線失敗後請查看日誌。 |
| `opencc-s2twp` | 部署流水線失敗後請檢視日誌。 |
| `zhconv-zh-tw` | 部署流水線失敗後請查看日誌。 |

### regressions/regression_024 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：台積電宣布擴大先進製程投資
- Review：pending
- Notes：宣布不應轉宣佈

| Engine | Output |
|--------|--------|
| `zhtw` | 台積電宣布擴大先進製程投資 |
| `opencc-s2twp` | 臺積電宣佈擴大先進製程投資 |
| `zhconv-zh-tw` | 臺積電宣布擴大先進位程投資 |

### regressions/regression_060 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：這個貼圖包太好笑了
- Review：pending
- Notes：表情包→貼圖包

| Engine | Output |
|--------|--------|
| `zhtw` | 這個貼圖包太好笑了 |
| `opencc-s2twp` | 這個表情包太好笑了 |
| `zhconv-zh-tw` | 這個表情包太好笑了 |

### regressions/regression_094 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：下週到校不要誤傷下周遭
- Review：pending
- Notes：下週到與下周遭雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 下週到校不要誤傷下周遭 |
| `opencc-s2twp` | 下週到校不要誤傷下週遭 |
| `zhconv-zh-tw` | 下周到校不要誤傷下周遭 |

### regressions/regression_025 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：持續整合管線已經通過
- Review：pending
- Notes：CI 通過語境

| Engine | Output |
|--------|--------|
| `zhtw` | 持續整合管線已經通過 |
| `opencc-s2twp` | 持續整合流水線已經透過 |
| `zhconv-zh-tw` | 持續集成流水線已經通過 |

### wiki/wiki_067 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：資訊安全強調身分驗證。
- Review：pending
- Notes：信息安全→資訊安全

| Engine | Output |
|--------|--------|
| `zhtw` | 資訊安全強調身分驗證。 |
| `opencc-s2twp` | 資訊保安強調身份驗證。 |
| `zhconv-zh-tw` | 信息安全強調身份驗證。 |

### social/social_050 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：我忘記註銷舊帳號。
- Review：pending
- Notes：注销账号→登出帳號

| Engine | Output |
|--------|--------|
| `zhtw` | 我忘記註銷舊帳號。 |
| `opencc-s2twp` | 我忘記登出舊賬號。 |
| `zhconv-zh-tw` | 我忘記註銷舊帳號。 |

### social/social_069 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：保存體力明天再出門。
- Review：pending
- Notes：一般保存保持保存

| Engine | Output |
|--------|--------|
| `zhtw` | 保存體力明天再出門。 |
| `opencc-s2twp` | 儲存體力明天再出門。 |
| `zhconv-zh-tw` | 保存體力明天再出門。 |

### regressions/regression_026 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：已經透過 API 上傳檔案
- Review：pending
- Notes：通过 API 應為透過 API

| Engine | Output |
|--------|--------|
| `zhtw` | 已經透過 API 上傳檔案 |
| `opencc-s2twp` | 已經透過 API 上傳檔案 |
| `zhconv-zh-tw` | 已經通過 API 上傳文件 |

### wiki/wiki_093 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：法國歷史包含多個王朝。
- Review：pending
- Notes：法国→法國

| Engine | Output |
|--------|--------|
| `zhtw` | 法國歷史包含多個王朝。 |
| `opencc-s2twp` | 法國曆史包含多個王朝。 |
| `zhconv-zh-tw` | 法國歷史包含多個王朝。 |

### tech/tech_022 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請更新相依套件並重新建置專案。
- Review：pending
- Notes：更新依赖→更新相依套件，项目→專案

| Engine | Output |
|--------|--------|
| `zhtw` | 請更新相依套件並重新建置專案。 |
| `opencc-s2twp` | 請更新依賴並重新構建專案。 |
| `zhconv-zh-tw` | 請更新依賴並重新構建項目。 |

### tech/tech_078 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：檔案路徑包含空格。
- Review：pending
- Notes：文件路径→檔案路徑

| Engine | Output |
|--------|--------|
| `zhtw` | 檔案路徑包含空格。 |
| `opencc-s2twp` | 檔案路徑包含空格。 |
| `zhconv-zh-tw` | 文件路徑包含空格。 |

### regressions/regression_091 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：禁用藥物和停用帳號
- Review：pending
- Notes：藥物/帳號雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 禁用藥物和停用帳號 |
| `opencc-s2twp` | 禁用藥物和禁用賬號 |
| `zhconv-zh-tw` | 禁用藥物和禁用帳號 |

### tech/tech_097 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：透過 API 下載檔案。
- Review：pending
- Notes：通过 API→透過 API

| Engine | Output |
|--------|--------|
| `zhtw` | 透過 API 下載檔案。 |
| `opencc-s2twp` | 透過 API 下載檔案。 |
| `zhconv-zh-tw` | 通過 API 下載文件。 |

### tech/tech_061 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：命令列工具支援自動補全。
- Review：pending
- Notes：技術語境支持→支援

| Engine | Output |
|--------|--------|
| `zhtw` | 命令列工具支援自動補全。 |
| `opencc-s2twp` | 命令列工具支援自動補全。 |
| `zhconv-zh-tw` | 命令行工具支持自動補全。 |

### regressions/regression_030 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：後端服務回傳狀態碼
- Review：pending
- Notes：返回状态码→回傳狀態碼

| Engine | Output |
|--------|--------|
| `zhtw` | 後端服務回傳狀態碼 |
| `opencc-s2twp` | 後端服務返回狀態碼 |
| `zhconv-zh-tw` | 後端服務返回狀態碼 |

### social/social_064 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：本週到貨的商品很好看。
- Review：pending
- Notes：本周到→本週到

| Engine | Output |
|--------|--------|
| `zhtw` | 本週到貨的商品很好看。 |
| `opencc-s2twp` | 本週到貨的商品很好看。 |
| `zhconv-zh-tw` | 本周到貨的商品很好看。 |

### tech/tech_008 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：伺服器需要安裝安全修補程式。
- Review：pending
- Notes：服务器→伺服器, 安装→安裝, 补丁→修補程式

| Engine | Output |
|--------|--------|
| `zhtw` | 伺服器需要安裝安全修補程式。 |
| `opencc-s2twp` | 伺服器需要安裝安全補丁。 |
| `zhconv-zh-tw` | 伺服器需要安裝安全補丁。 |

### regressions/regression_011 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：收藏這篇文章到我的最愛
- Review：pending
- Notes：收藏動詞保持，收藏夹→我的最愛

| Engine | Output |
|--------|--------|
| `zhtw` | 收藏這篇文章到我的最愛 |
| `opencc-s2twp` | 收藏這篇文章到收藏夾 |
| `zhconv-zh-tw` | 收藏這篇文章到收藏夾 |

### news/news_075 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：市議會通過年度預算。
- Review：pending
- Notes：通过作通過

| Engine | Output |
|--------|--------|
| `zhtw` | 市議會通過年度預算。 |
| `opencc-s2twp` | 市議會透過年度預算。 |
| `zhconv-zh-tw` | 市議會通過年度預算。 |

### news/news_100 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：公司董事會通過現金增資案。
- Review：pending
- Notes：通过作通過

| Engine | Output |
|--------|--------|
| `zhtw` | 公司董事會通過現金增資案。 |
| `opencc-s2twp` | 公司董事會透過現金增資案。 |
| `zhconv-zh-tw` | 公司董事會通過現金增資案。 |

### social/social_038 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：我已經透過連結報名了。
- Review：pending
- Notes：通过链接→透過連結

| Engine | Output |
|--------|--------|
| `zhtw` | 我已經透過連結報名了。 |
| `opencc-s2twp` | 我已經透過連結報名了。 |
| `zhconv-zh-tw` | 我已經通過連結報名了。 |

### regressions/regression_059 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：請更新相依套件並重新建置專案
- Review：pending
- Notes：相依套件與專案建置

| Engine | Output |
|--------|--------|
| `zhtw` | 請更新相依套件並重新建置專案 |
| `opencc-s2twp` | 請更新依賴並重新構建專案 |
| `zhconv-zh-tw` | 請更新依賴並重新構建項目 |

### social/social_073 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：復原操作後畫面恢復正常。
- Review：pending
- Notes：撤销操作→復原操作

| Engine | Output |
|--------|--------|
| `zhtw` | 復原操作後畫面恢復正常。 |
| `opencc-s2twp` | 撤銷操作後畫面恢復正常。 |
| `zhconv-zh-tw` | 撤銷操作後畫面恢復正常。 |

### wiki/wiki_053 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：遺傳演算法模擬自然選擇過程。
- Review：pending
- Notes：遗传算法→遺傳演算法，自然选择→自然選擇

| Engine | Output |
|--------|--------|
| `zhtw` | 遺傳演算法模擬自然選擇過程。 |
| `opencc-s2twp` | 遺傳演算法模擬自然選擇過程。 |
| `zhconv-zh-tw` | 遺傳算法模擬自然選擇過程。 |

### news/news_048 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：公司董事會通過現金增資案。
- Review：pending
- Notes：董事会→董事會，通过→通過

| Engine | Output |
|--------|--------|
| `zhtw` | 公司董事會通過現金增資案。 |
| `opencc-s2twp` | 公司董事會透過現金增資案。 |
| `zhconv-zh-tw` | 公司董事會通過現金增資案。 |

### news/news_018 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：環保署提醒民眾減少一次性塑膠使用。
- Review：pending
- Notes：环保署→環保署, 民众→民眾, 塑料→塑膠

| Engine | Output |
|--------|--------|
| `zhtw` | 環保署提醒民眾減少一次性塑膠使用。 |
| `opencc-s2twp` | 環保署提醒民眾減少一次性塑膠使用。 |
| `zhconv-zh-tw` | 環保署提醒民眾減少一次性塑料使用。 |

### regressions/regression_017 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：里長在鄰里服務中心
- Review：pending
- Notes：里长保持里, 邻里→鄰里

| Engine | Output |
|--------|--------|
| `zhtw` | 里長在鄰里服務中心 |
| `opencc-s2twp` | 里長在鄰里服務中心 |
| `zhconv-zh-tw` | 裡長在鄰裡服務中心 |

### tech/tech_100 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：程式退出前會釋放資源。
- Review：pending
- Notes：程序→程式，资源→資源

| Engine | Output |
|--------|--------|
| `zhtw` | 程式退出前會釋放資源。 |
| `opencc-s2twp` | 程式退出前會釋放資源。 |
| `zhconv-zh-tw` | 程序退出前會釋放資源。 |

### tech/tech_079 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：命令輸出顯示權限不足。
- Review：pending
- Notes：权限→權限

| Engine | Output |
|--------|--------|
| `zhtw` | 命令輸出顯示權限不足。 |
| `opencc-s2twp` | 命令輸出顯示許可權不足。 |
| `zhconv-zh-tw` | 命令輸出顯示權限不足。 |

### regressions/regression_085 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：通過測試不是透過 API
- Review：pending
- Notes：通過/透過雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 通過測試不是透過 API |
| `opencc-s2twp` | 透過測試不是透過 API |
| `zhconv-zh-tw` | 通過測試不是通過 API |

### social/social_023 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：每週到健身房三次。
- Review：pending
- Notes：每周到→每週到

| Engine | Output |
|--------|--------|
| `zhtw` | 每週到健身房三次。 |
| `opencc-s2twp` | 每週到健身房三次。 |
| `zhconv-zh-tw` | 每周到健身房三次。 |

### news/news_023 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：教育部公布考試日期。
- Review：pending
- Notes：公布保持公布，考试→考試

| Engine | Output |
|--------|--------|
| `zhtw` | 教育部公布考試日期。 |
| `opencc-s2twp` | 教育部公佈考試日期。 |
| `zhconv-zh-tw` | 教育部公布考試日期。 |

### news/news_041 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：檢方搜尋多處辦公室並帶回資料。
- Review：pending
- Notes：检方→檢方，资料→資料

| Engine | Output |
|--------|--------|
| `zhtw` | 檢方搜尋多處辦公室並帶回資料。 |
| `opencc-s2twp` | 檢方搜尋多處辦公室並帶回資料。 |
| `zhconv-zh-tw` | 檢方搜索多處辦公室並帶回資料。 |

### regressions/regression_013 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：復原操作不是撤銷合約
- Review：pending
- Notes：撤销操作→復原操作, 撤销合同→撤銷合約

| Engine | Output |
|--------|--------|
| `zhtw` | 復原操作不是撤銷合約 |
| `opencc-s2twp` | 撤銷操作不是撤銷合同 |
| `zhconv-zh-tw` | 撤銷操作不是撤銷合同 |

### social/social_035 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：請先重新整理頁面再試一次。
- Review：pending
- Notes：刷新页面→重新整理頁面

| Engine | Output |
|--------|--------|
| `zhtw` | 請先重新整理頁面再試一次。 |
| `opencc-s2twp` | 請先重新整理頁面再試一次。 |
| `zhconv-zh-tw` | 請先刷新頁面再試一次。 |

### tech/tech_005 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：資料庫的查詢效能需要最佳化。
- Review：pending
- Notes：数据库→資料庫, 性能→效能, 优化→最佳化

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫的查詢效能需要最佳化。 |
| `opencc-s2twp` | 資料庫的查詢效能需要最佳化。 |
| `zhconv-zh-tw` | 資料庫的查詢性能需要優化。 |

### wiki/wiki_016 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：演算法分析是電腦科學的重要主題。
- Review：pending
- Notes：算法→演算法, 计算机科学→電腦科學, 主题→主題

| Engine | Output |
|--------|--------|
| `zhtw` | 演算法分析是電腦科學的重要主題。 |
| `opencc-s2twp` | 演算法分析是電腦科學的重要主題。 |
| `zhconv-zh-tw` | 算法分析是計算機科學的重要主題。 |

### regressions/regression_074 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：留言區不是時事評論
- Review：pending
- Notes：评论雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 留言區不是時事評論 |
| `opencc-s2twp` | 評論區不是時事評論 |
| `zhconv-zh-tw` | 評論區不是時事評論 |

### social/social_079 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：騎腳踏車去上班很環保。
- Review：pending
- Notes：自行车→腳踏車

| Engine | Output |
|--------|--------|
| `zhtw` | 騎腳踏車去上班很環保。 |
| `opencc-s2twp` | 騎腳踏車去上班很環保。 |
| `zhconv-zh-tw` | 騎自行車去上班很環保。 |

### regressions/regression_079 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：重新整理頁面不是刷新紀錄
- Review：pending
- Notes：刷新雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 重新整理頁面不是刷新紀錄 |
| `opencc-s2twp` | 重新整理頁面不是重新整理紀錄 |
| `zhconv-zh-tw` | 刷新頁面不是刷新紀錄 |

### tech/tech_045 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：瀏覽器主控台顯示警告。
- Review：pending
- Notes：浏览器→瀏覽器，控制台→主控台

| Engine | Output |
|--------|--------|
| `zhtw` | 瀏覽器主控台顯示警告。 |
| `opencc-s2twp` | 瀏覽器控制檯顯示警告。 |
| `zhconv-zh-tw` | 瀏覽器控制臺顯示警告。 |

### tech/tech_006 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：請在設定檔中設定預設值。
- Review：pending
- Notes：配置文件→設定檔, 设置→設定, 默认值→預設值

| Engine | Output |
|--------|--------|
| `zhtw` | 請在設定檔中設定預設值。 |
| `opencc-s2twp` | 請在配置檔案中設定預設值。 |
| `zhconv-zh-tw` | 請在配置文件中設置默認值。 |

### tech/tech_059 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請把修補程式合併到主分支。
- Review：pending
- Notes：补丁→修補程式，主分支→主分支

| Engine | Output |
|--------|--------|
| `zhtw` | 請把修補程式合併到主分支。 |
| `opencc-s2twp` | 請把補丁合併到主分支。 |
| `zhconv-zh-tw` | 請把補丁合併到主分支。 |

### social/social_081 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：這個應用程式一直顯示錯誤資訊。
- Review：pending
- Notes：应用→應用程式

| Engine | Output |
|--------|--------|
| `zhtw` | 這個應用程式一直顯示錯誤資訊。 |
| `opencc-s2twp` | 這個應用一直顯示錯誤資訊。 |
| `zhconv-zh-tw` | 這個應用一直顯示錯誤信息。 |

### wiki/wiki_050 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：統計學用於分析大量資料。
- Review：pending
- Notes：统计学→統計學，数据→資料

| Engine | Output |
|--------|--------|
| `zhtw` | 統計學用於分析大量資料。 |
| `opencc-s2twp` | 統計學用於分析大量資料。 |
| `zhconv-zh-tw` | 統計學用於分析大量數據。 |

### news/news_007 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：新的資料中心將在下半年啟用。
- Review：pending
- Notes：数据中心→資料中心, 启用→啟用

| Engine | Output |
|--------|--------|
| `zhtw` | 新的資料中心將在下半年啟用。 |
| `opencc-s2twp` | 新的資料中心將在下半年啟用。 |
| `zhconv-zh-tw` | 新的數據中心將在下半年啟用。 |

### tech/tech_042 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請檢查環境變數是否設定正確。
- Review：pending
- Notes：环境变量→環境變數，设置→設定

| Engine | Output |
|--------|--------|
| `zhtw` | 請檢查環境變數是否設定正確。 |
| `opencc-s2twp` | 請檢查環境變數是否設定正確。 |
| `zhconv-zh-tw` | 請檢查環境變量是否設置正確。 |

### regressions/regression_064 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：部署管線已經通過
- Review：pending
- Notes：部署管線通過語境

| Engine | Output |
|--------|--------|
| `zhtw` | 部署管線已經通過 |
| `opencc-s2twp` | 部署流水線已經透過 |
| `zhconv-zh-tw` | 部署流水線已經通過 |

### wiki/wiki_002 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：人工智慧是電腦科學的一個分支。
- Review：pending
- Notes：人工智能→人工智慧, 计算机→電腦

| Engine | Output |
|--------|--------|
| `zhtw` | 人工智慧是電腦科學的一個分支。 |
| `opencc-s2twp` | 人工智慧是電腦科學的一個分支。 |
| `zhconv-zh-tw` | 人工智慧是計算機科學的一個分支。 |

### tech/tech_068 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：單元測試會模擬例外情況。
- Review：pending
- Notes：异常→例外

| Engine | Output |
|--------|--------|
| `zhtw` | 單元測試會模擬例外情況。 |
| `opencc-s2twp` | 單元測試會模擬異常情況。 |
| `zhconv-zh-tw` | 單元測試會模擬異常情況。 |

### regressions/regression_048 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：開源專案管理
- Review：pending
- Notes：開源專案

| Engine | Output |
|--------|--------|
| `zhtw` | 開源專案管理 |
| `opencc-s2twp` | 開源專案管理 |
| `zhconv-zh-tw` | 開源項目管理 |

### wiki/wiki_077 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：虛擬實境提供沉浸式體驗。
- Review：pending
- Notes：虚拟现实→虛擬實境

| Engine | Output |
|--------|--------|
| `zhtw` | 虛擬實境提供沉浸式體驗。 |
| `opencc-s2twp` | 虛擬現實提供沉浸式體驗。 |
| `zhconv-zh-tw` | 虛擬實境提供沉浸式體驗。 |

### regressions/regression_066 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：公布於眾後宣布結果
- Review：pending
- Notes：公布/宣布不轉公佈/宣佈

| Engine | Output |
|--------|--------|
| `zhtw` | 公布於眾後宣布結果 |
| `opencc-s2twp` | 公佈於眾後宣佈結果 |
| `zhconv-zh-tw` | 公布於眾後宣布結果 |

### tech/tech_052 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：快取失效會導致回應變慢。
- Review：pending
- Notes：缓存→快取，响应→回應

| Engine | Output |
|--------|--------|
| `zhtw` | 快取失效會導致回應變慢。 |
| `opencc-s2twp` | 快取失效會導致響應變慢。 |
| `zhconv-zh-tw` | 緩存失效會導致響應變慢。 |

### regressions/regression_049 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：檢查項目清單
- Review：pending
- Notes：檢查項目

| Engine | Output |
|--------|--------|
| `zhtw` | 檢查項目清單 |
| `opencc-s2twp` | 檢查專案清單 |
| `zhconv-zh-tw` | 檢查項目清單 |

### social/social_021 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這週到店領取贈品。
- Review：pending
- Notes：这周到店→這週到店

| Engine | Output |
|--------|--------|
| `zhtw` | 這週到店領取贈品。 |
| `opencc-s2twp` | 這周到店領取贈品。 |
| `zhconv-zh-tw` | 這周到店領取贈品。 |

### wiki/wiki_063 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：資料庫交易保證資料一致性。
- Review：pending
- Notes：事务→交易

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫交易保證資料一致性。 |
| `opencc-s2twp` | 資料庫事務保證資料一致性。 |
| `zhconv-zh-tw` | 資料庫事務保證數據一致性。 |

### regressions/regression_065 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：已經透過連結報名
- Review：pending
- Notes：通过链接→透過連結

| Engine | Output |
|--------|--------|
| `zhtw` | 已經透過連結報名 |
| `opencc-s2twp` | 已經透過連結報名 |
| `zhconv-zh-tw` | 已經通過連結報名 |

### social/social_067 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：預設密碼太簡單了。
- Review：pending
- Notes：默认→預設

| Engine | Output |
|--------|--------|
| `zhtw` | 預設密碼太簡單了。 |
| `opencc-s2twp` | 預設密碼太簡單了。 |
| `zhconv-zh-tw` | 默認密碼太簡單了。 |

### social/social_028 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：老闆今天遠端開會。
- Review：pending
- Notes：老板→老闆，远程→遠端

| Engine | Output |
|--------|--------|
| `zhtw` | 老闆今天遠端開會。 |
| `opencc-s2twp` | 老闆今天遠端開會。 |
| `zhconv-zh-tw` | 老闆今天遠程開會。 |

### social/social_061 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：這週到店消費有折扣。
- Review：pending
- Notes：这周到店→這週到店

| Engine | Output |
|--------|--------|
| `zhtw` | 這週到店消費有折扣。 |
| `opencc-s2twp` | 這周到店消費有折扣。 |
| `zhconv-zh-tw` | 這周到店消費有折扣。 |

### regressions/regression_028 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：停用帳號後請通知使用者
- Review：pending
- Notes：禁用账号→停用帳號

| Engine | Output |
|--------|--------|
| `zhtw` | 停用帳號後請通知使用者 |
| `opencc-s2twp` | 禁用賬號後請通知使用者 |
| `zhconv-zh-tw` | 禁用帳號後請通知用戶 |

### social/social_086 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：我的最愛裡的舊網頁打不開。
- Review：pending
- Notes：收藏夹→我的最愛

| Engine | Output |
|--------|--------|
| `zhtw` | 我的最愛裡的舊網頁打不開。 |
| `opencc-s2twp` | 收藏夾裡的舊網頁打不開。 |
| `zhconv-zh-tw` | 收藏夾裡的舊網頁打不開。 |

### wiki/wiki_005 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：資料庫系統用於儲存和管理資料。
- Review：pending
- Notes：数据库→資料庫, 存储→儲存, 数据→資料

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫系統用於儲存和管理資料。 |
| `opencc-s2twp` | 資料庫系統用於儲存和管理資料。 |
| `zhconv-zh-tw` | 資料庫系統用於存儲和管理數據。 |

### regressions/regression_070 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：還原備份需要管理員權限
- Review：pending
- Notes：備份語境還原

| Engine | Output |
|--------|--------|
| `zhtw` | 還原備份需要管理員權限 |
| `opencc-s2twp` | 恢復備份需要管理員許可權 |
| `zhconv-zh-tw` | 恢復備份需要管理員權限 |

### social/social_015 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：我把帳號密碼忘記了。
- Review：pending
- Notes：账号→帳號, 密码→密碼, 忘记→忘記

| Engine | Output |
|--------|--------|
| `zhtw` | 我把帳號密碼忘記了。 |
| `opencc-s2twp` | 我把賬號密碼忘記了。 |
| `zhconv-zh-tw` | 我把帳號密碼忘記了。 |

### regressions/regression_082 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：預設頭像不是他默認指控
- Review：pending
- Notes：預設/默認雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 預設頭像不是他默認指控 |
| `opencc-s2twp` | 預設頭像不是他預設指控 |
| `zhconv-zh-tw` | 默認頭像不是他默認指控 |

### regressions/regression_050 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：一則訊息
- Review：pending
- Notes：消息量詞語境→訊息

| Engine | Output |
|--------|--------|
| `zhtw` | 一則訊息 |
| `opencc-s2twp` | 一條訊息 |
| `zhconv-zh-tw` | 一條消息 |

### tech/tech_002 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：該軟體的原始碼託管在雲端伺服器上。
- Review：pending
- Notes：软件→軟體, 源代码→原始碼, 云→雲端, 服务器→伺服器

| Engine | Output |
|--------|--------|
| `zhtw` | 該軟體的原始碼託管在雲端伺服器上。 |
| `opencc-s2twp` | 該軟體的原始碼託管在雲伺服器上。 |
| `zhconv-zh-tw` | 該軟體的原始碼託管在雲伺服器上。 |

### news/news_095 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：動物園公布新生動物名單。
- Review：pending
- Notes：公布保持公布

| Engine | Output |
|--------|--------|
| `zhtw` | 動物園公布新生動物名單。 |
| `opencc-s2twp` | 動物園公佈新生動物名單。 |
| `zhconv-zh-tw` | 動物園公布新生動物名單。 |

### news/news_091 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：社區大學開放春季課程報名。
- Review：pending
- Notes：社区→社區

| Engine | Output |
|--------|--------|
| `zhtw` | 社區大學開放春季課程報名。 |
| `opencc-s2twp` | 社群大學開放春季課程報名。 |
| `zhconv-zh-tw` | 社區大學開放春季課程報名。 |

### wiki/wiki_061 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：電腦網路連線狀態穩定。
- Review：pending
- Notes：网络连接→網路連線

| Engine | Output |
|--------|--------|
| `zhtw` | 電腦網路連線狀態穩定。 |
| `opencc-s2twp` | 計算機網路連線狀態穩定。 |
| `zhconv-zh-tw` | 計算機網絡連接狀態穩定。 |

### wiki/wiki_042 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：密碼學研究資訊安全與加密技術。
- Review：pending
- Notes：密码学→密碼學，信息安全→資訊安全

| Engine | Output |
|--------|--------|
| `zhtw` | 密碼學研究資訊安全與加密技術。 |
| `opencc-s2twp` | 密碼學研究資訊保安與加密技術。 |
| `zhconv-zh-tw` | 密碼學研究信息安全與加密技術。 |

### tech/tech_035 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：訊息佇列處理非同步任務。
- Review：pending
- Notes：队列→佇列，异步→非同步

| Engine | Output |
|--------|--------|
| `zhtw` | 訊息佇列處理非同步任務。 |
| `opencc-s2twp` | 訊息佇列處理非同步任務。 |
| `zhconv-zh-tw` | 消息隊列處理異步任務。 |

### tech/tech_003 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：程式設計師需要除錯這個記憶體洩漏的問題。
- Review：pending
- Notes：程序员→程式設計師, 调试→除錯, 内存→記憶體

| Engine | Output |
|--------|--------|
| `zhtw` | 程式設計師需要除錯這個記憶體洩漏的問題。 |
| `opencc-s2twp` | 程式設計師需要除錯這個記憶體洩漏的問題。 |
| `zhconv-zh-tw` | 程式設計師需要調試這個內存洩漏的問題。 |

### regressions/regression_054 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：500公克巧克力蛋糕
- Review：pending
- Notes：數量克→公克，巧克力保持

| Engine | Output |
|--------|--------|
| `zhtw` | 500公克巧克力蛋糕 |
| `opencc-s2twp` | 500克巧克力蛋糕 |
| `zhconv-zh-tw` | 500克巧克力蛋糕 |

### tech/tech_023 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：已經透過 API 上傳檔案。
- Review：pending
- Notes：通过 API→透過 API

| Engine | Output |
|--------|--------|
| `zhtw` | 已經透過 API 上傳檔案。 |
| `opencc-s2twp` | 已經透過 API 上傳檔案。 |
| `zhconv-zh-tw` | 已經通過 API 上傳文件。 |

### regressions/regression_076 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：銷售通路不是灌溉渠道
- Review：pending
- Notes：通路/渠道雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 銷售通路不是灌溉渠道 |
| `opencc-s2twp` | 銷售渠道不是灌溉渠道 |
| `zhconv-zh-tw` | 銷售渠道不是灌溉渠道 |

### tech/tech_044 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個元件會監聽滾動事件。
- Review：pending
- Notes：组件→元件，事件→事件

| Engine | Output |
|--------|--------|
| `zhtw` | 這個元件會監聽滾動事件。 |
| `opencc-s2twp` | 這個元件會監聽滾動事件。 |
| `zhconv-zh-tw` | 這個組件會監聽滾動事件。 |

### social/social_092 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：遠端辦公讓我省下通勤時間。
- Review：pending
- Notes：远程办公→遠端辦公

| Engine | Output |
|--------|--------|
| `zhtw` | 遠端辦公讓我省下通勤時間。 |
| `opencc-s2twp` | 遠端辦公讓我省下通勤時間。 |
| `zhconv-zh-tw` | 遠程辦公讓我省下通勤時間。 |

### social/social_045 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：儲存檔案之後記得備份。
- Review：pending
- Notes：保存文件→儲存檔案

| Engine | Output |
|--------|--------|
| `zhtw` | 儲存檔案之後記得備份。 |
| `opencc-s2twp` | 儲存檔案之後記得備份。 |
| `zhconv-zh-tw` | 保存文件之後記得備份。 |

### social/social_085 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：我透過連結加入群組。
- Review：pending
- Notes：通过链接→透過連結

| Engine | Output |
|--------|--------|
| `zhtw` | 我透過連結加入群組。 |
| `opencc-s2twp` | 我透過連結加入群組。 |
| `zhconv-zh-tw` | 我通過連結加入群組。 |

### tech/tech_073 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：請求標頭缺少內容類型。
- Review：pending
- Notes：请求头→請求標頭

| Engine | Output |
|--------|--------|
| `zhtw` | 請求標頭缺少內容類型。 |
| `opencc-s2twp` | 請求頭缺少內容型別。 |
| `zhconv-zh-tw` | 請求頭缺少內容類型。 |

### tech/tech_037 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：命令列參數支持短選項。
- Review：pending
- Notes：命令行→命令列，选项→選項

| Engine | Output |
|--------|--------|
| `zhtw` | 命令列參數支持短選項。 |
| `opencc-s2twp` | 命令列引數支援短選項。 |
| `zhconv-zh-tw` | 命令行參數支持短選項。 |

### regressions/regression_040 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：撤銷合約條款
- Review：pending
- Notes：法律撤销→撤銷

| Engine | Output |
|--------|--------|
| `zhtw` | 撤銷合約條款 |
| `opencc-s2twp` | 撤銷合同條款 |
| `zhconv-zh-tw` | 撤銷合同條款 |

### regressions/regression_063 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：建置管線已經通過
- Review：pending
- Notes：建置管線通過語境

| Engine | Output |
|--------|--------|
| `zhtw` | 建置管線已經通過 |
| `opencc-s2twp` | 構建流水線已經透過 |
| `zhconv-zh-tw` | 構建流水線已經通過 |

### tech/tech_071 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：建置管線失敗時傳送通知。
- Review：pending
- Notes：构建流水线→建置管線

| Engine | Output |
|--------|--------|
| `zhtw` | 建置管線失敗時傳送通知。 |
| `opencc-s2twp` | 構建流水線失敗時傳送通知。 |
| `zhconv-zh-tw` | 構建流水線失敗時發送通知。 |

### tech/tech_053 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個演算法使用遞迴遍歷樹結構。
- Review：pending
- Notes：算法→演算法，递归→遞迴

| Engine | Output |
|--------|--------|
| `zhtw` | 這個演算法使用遞迴遍歷樹結構。 |
| `opencc-s2twp` | 這個演算法使用遞迴遍歷樹結構。 |
| `zhconv-zh-tw` | 這個算法使用遞歸遍歷樹結構。 |

### tech/tech_025 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請在終端機執行安裝命令。
- Review：pending
- Notes：终端→終端，安装→安裝

| Engine | Output |
|--------|--------|
| `zhtw` | 請在終端機執行安裝命令。 |
| `opencc-s2twp` | 請在終端執行安裝命令。 |
| `zhconv-zh-tw` | 請在終端執行安裝命令。 |

### tech/tech_098 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：瀏覽器主控台顯示警告。
- Review：pending
- Notes：控制台→主控台

| Engine | Output |
|--------|--------|
| `zhtw` | 瀏覽器主控台顯示警告。 |
| `opencc-s2twp` | 瀏覽器控制檯顯示警告。 |
| `zhconv-zh-tw` | 瀏覽器控制臺顯示警告。 |

### social/social_002 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：剛買的隨身碟壞了，氣死我了。
- Review：pending
- Notes：U盘→隨身碟

| Engine | Output |
|--------|--------|
| `zhtw` | 剛買的隨身碟壞了，氣死我了。 |
| `opencc-s2twp` | 剛買的隨身碟壞了，氣死我了。 |
| `zhconv-zh-tw` | 剛買的U盤壞了，氣死我了。 |

### social/social_024 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：下週到臺中找朋友。
- Review：pending
- Notes：下周到→下週到

| Engine | Output |
|--------|--------|
| `zhtw` | 下週到臺中找朋友。 |
| `opencc-s2twp` | 下週到臺中找朋友。 |
| `zhconv-zh-tw` | 下周到臺中找朋友。 |

### social/social_053 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：今天空氣質量不太好。
- Review：pending
- Notes：空气→空氣，质量保持質量

| Engine | Output |
|--------|--------|
| `zhtw` | 今天空氣質量不太好。 |
| `opencc-s2twp` | 今天空氣質量不太好。 |
| `zhconv-zh-tw` | 今天空氣品質不太好。 |

### wiki/wiki_084 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：聯合國大會通過決議。
- Review：pending
- Notes：通过作通過

| Engine | Output |
|--------|--------|
| `zhtw` | 聯合國大會通過決議。 |
| `opencc-s2twp` | 聯合國大會透過決議。 |
| `zhconv-zh-tw` | 聯合國大會通過決議。 |

### social/social_029 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：手機螢幕突然變暗。
- Review：pending
- Notes：手机→手機，屏幕→螢幕

| Engine | Output |
|--------|--------|
| `zhtw` | 手機螢幕突然變暗。 |
| `opencc-s2twp` | 手機螢幕突然變暗。 |
| `zhconv-zh-tw` | 手機屏幕突然變暗。 |

### news/news_024 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：行政院透過新的補助方案。
- Review：pending
- Notes：通过作通過，补助→補助

| Engine | Output |
|--------|--------|
| `zhtw` | 行政院透過新的補助方案。 |
| `opencc-s2twp` | 行政院透過新的補助方案。 |
| `zhconv-zh-tw` | 行政院通過新的補助方案。 |

### tech/tech_056 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：檔名包含非法字元。
- Review：pending
- Notes：文件名→檔名，字符→字元

| Engine | Output |
|--------|--------|
| `zhtw` | 檔名包含非法字元。 |
| `opencc-s2twp` | 檔名包含非法字元。 |
| `zhconv-zh-tw` | 文件名包含非法字符。 |

### regressions/regression_084 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：物件導向不是結婚對象
- Review：pending
- Notes：物件/對象雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 物件導向不是結婚對象 |
| `opencc-s2twp` | 物件導向不是結婚物件 |
| `zhconv-zh-tw` | 面向對象不是結婚對象 |

### regressions/regression_083 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：程式設計師寫程式不是行政程序
- Review：pending
- Notes：程式/程序雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 程式設計師寫程式不是行政程序 |
| `opencc-s2twp` | 程式設計師寫程式不是行政程式 |
| `zhconv-zh-tw` | 程式設計師寫程序不是行政程序 |

### regressions/regression_038 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：刷新世界紀錄
- Review：pending
- Notes：一般刷新保持刷新

| Engine | Output |
|--------|--------|
| `zhtw` | 刷新世界紀錄 |
| `opencc-s2twp` | 重新整理世界紀錄 |
| `zhconv-zh-tw` | 刷新世界紀錄 |

### tech/tech_036 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：請用設定檔覆蓋預設參數。
- Review：pending
- Notes：配置文件→設定檔，默认参数→預設參數

| Engine | Output |
|--------|--------|
| `zhtw` | 請用設定檔覆蓋預設參數。 |
| `opencc-s2twp` | 請用配置檔案覆蓋預設引數。 |
| `zhconv-zh-tw` | 請用配置文件覆蓋默認參數。 |

### tech/tech_091 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：終端機視窗顯示下載進度。
- Review：pending
- Notes：窗口→視窗

| Engine | Output |
|--------|--------|
| `zhtw` | 終端機視窗顯示下載進度。 |
| `opencc-s2twp` | 終端視窗顯示下載進度。 |
| `zhconv-zh-tw` | 終端窗口顯示下載進度。 |

### regressions/regression_046 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：預設頭像太醜了
- Review：pending
- Notes：UI 默认→預設

| Engine | Output |
|--------|--------|
| `zhtw` | 預設頭像太醜了 |
| `opencc-s2twp` | 預設頭像太醜了 |
| `zhconv-zh-tw` | 默認頭像太醜了 |

### tech/tech_067 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：非同步任務佇列已經排空。
- Review：pending
- Notes：异步→非同步，队列→佇列

| Engine | Output |
|--------|--------|
| `zhtw` | 非同步任務佇列已經排空。 |
| `opencc-s2twp` | 非同步任務佇列已經排空。 |
| `zhconv-zh-tw` | 異步任務隊列已經排空。 |

### news/news_061 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：市政府宣布新的交通管制措施。
- Review：pending
- Notes：宣布保持宣布

| Engine | Output |
|--------|--------|
| `zhtw` | 市政府宣布新的交通管制措施。 |
| `opencc-s2twp` | 市政府宣佈新的交通管制措施。 |
| `zhconv-zh-tw` | 市政府宣布新的交通管制措施。 |

### social/social_052 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：我的最愛裡面好多舊連結。
- Review：pending
- Notes：收藏夹→我的最愛，链接→連結

| Engine | Output |
|--------|--------|
| `zhtw` | 我的最愛裡面好多舊連結。 |
| `opencc-s2twp` | 收藏夾裡面好多舊連結。 |
| `zhconv-zh-tw` | 收藏夾裡面好多舊連結。 |

### social/social_057 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：預設頭像看起來有點怪。
- Review：pending
- Notes：默认头像→預設頭像

| Engine | Output |
|--------|--------|
| `zhtw` | 預設頭像看起來有點怪。 |
| `opencc-s2twp` | 預設頭像看起來有點怪。 |
| `zhconv-zh-tw` | 默認頭像看起來有點怪。 |

### news/news_003 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：該專案將於明年完成後投入使用。
- Review：pending
- Notes：项目→專案, 完成后→完成後

| Engine | Output |
|--------|--------|
| `zhtw` | 該專案將於明年完成後投入使用。 |
| `opencc-s2twp` | 該專案將於明年完成後投入使用。 |
| `zhconv-zh-tw` | 該項目將於明年完成後投入使用。 |

### tech/tech_028 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：前端路由需要處理登入狀態。
- Review：pending
- Notes：登录状态→登入狀態

| Engine | Output |
|--------|--------|
| `zhtw` | 前端路由需要處理登入狀態。 |
| `opencc-s2twp` | 前端路由需要處理登入狀態。 |
| `zhconv-zh-tw` | 前端路由需要處理登錄狀態。 |

### wiki/wiki_054 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：虛擬實境技術可以模擬沉浸體驗。
- Review：pending
- Notes：虚拟现实→虛擬實境，体验→體驗

| Engine | Output |
|--------|--------|
| `zhtw` | 虛擬實境技術可以模擬沉浸體驗。 |
| `opencc-s2twp` | 虛擬現實技術可以模擬沉浸體驗。 |
| `zhconv-zh-tw` | 虛擬實境技術可以模擬沉浸體驗。 |

### tech/tech_020 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：請檢查請求標頭和回應標頭。
- Review：pending
- Notes：请求头→請求標頭, 响应头→回應標頭

| Engine | Output |
|--------|--------|
| `zhtw` | 請檢查請求標頭和回應標頭。 |
| `opencc-s2twp` | 請檢查請求頭和響應頭。 |
| `zhconv-zh-tw` | 請檢查請求頭和響應頭。 |

### tech/tech_080 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：資料庫交易提交失敗。
- Review：pending
- Notes：事务→交易

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫交易提交失敗。 |
| `opencc-s2twp` | 資料庫事務提交失敗。 |
| `zhconv-zh-tw` | 資料庫事務提交失敗。 |

### regressions/regression_033 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：物件導向程式設計
- Review：pending
- Notes：技術語境对象→物件

| Engine | Output |
|--------|--------|
| `zhtw` | 物件導向程式設計 |
| `opencc-s2twp` | 物件導向程式設計 |
| `zhconv-zh-tw` | 面向對象編程 |

### social/social_040 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：今天騎腳踏車去河邊。
- Review：pending
- Notes：自行车→腳踏車

| Engine | Output |
|--------|--------|
| `zhtw` | 今天騎腳踏車去河邊。 |
| `opencc-s2twp` | 今天騎腳踏車去河邊。 |
| `zhconv-zh-tw` | 今天騎自行車去河邊。 |

### social/social_037 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：服務品質真的有改善。
- Review：pending
- Notes：服务质量→服務品質

| Engine | Output |
|--------|--------|
| `zhtw` | 服務品質真的有改善。 |
| `opencc-s2twp` | 服務質量真的有改善。 |
| `zhconv-zh-tw` | 服務質量真的有改善。 |

### news/news_062 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：交通局公布春節期間公車調整路線。
- Review：pending
- Notes：公布保持公布，公交→公車

| Engine | Output |
|--------|--------|
| `zhtw` | 交通局公布春節期間公車調整路線。 |
| `opencc-s2twp` | 交通局公佈春節期間公交調整路線。 |
| `zhconv-zh-tw` | 交通局公布春節期間公交調整路線。 |

### news/news_001 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：據新華社報導，該軟體已經發布。
- Review：pending
- Notes：软件→軟體, 发布→發布

| Engine | Output |
|--------|--------|
| `zhtw` | 據新華社報導，該軟體已經發布。 |
| `opencc-s2twp` | 據新華社報道，該軟體已經發布。 |
| `zhconv-zh-tw` | 據新華社報導，該軟體已經發布。 |

### social/social_083 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：帳號密碼不要放在截圖裡。
- Review：pending
- Notes：账号→帳號，截图→截圖

| Engine | Output |
|--------|--------|
| `zhtw` | 帳號密碼不要放在截圖裡。 |
| `opencc-s2twp` | 賬號密碼不要放在截圖裡。 |
| `zhconv-zh-tw` | 帳號密碼不要放在截圖裡。 |

### wiki/wiki_065 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：機器學習模型需要訓練資料。
- Review：pending
- Notes：机器学习→機器學習

| Engine | Output |
|--------|--------|
| `zhtw` | 機器學習模型需要訓練資料。 |
| `opencc-s2twp` | 機器學習模型需要訓練資料。 |
| `zhconv-zh-tw` | 機器學習模型需要訓練數據。 |

### regressions/regression_089 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：即時資料同步不是經濟數據
- Review：pending
- Notes：資料/數據雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 即時資料同步不是經濟數據 |
| `opencc-s2twp` | 實時資料同步不是經濟資料 |
| `zhconv-zh-tw` | 實時數據同步不是經濟數據 |

### wiki/wiki_066 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：雲端運算平臺提供彈性資源。
- Review：pending
- Notes：云计算→雲端運算

| Engine | Output |
|--------|--------|
| `zhtw` | 雲端運算平臺提供彈性資源。 |
| `opencc-s2twp` | 雲端計算平臺提供彈性資源。 |
| `zhconv-zh-tw` | 雲計算平臺提供彈性資源。 |

### regressions/regression_016 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：長髮程式設計師在理髮店寫程式
- Review：pending
- Notes：长发→長髮, 程序员→程式設計師, 写程序→寫程式

| Engine | Output |
|--------|--------|
| `zhtw` | 長髮程式設計師在理髮店寫程式 |
| `opencc-s2twp` | 長髮程式設計師在理髮店寫程式 |
| `zhconv-zh-tw` | 長發程式設計師在理髮店寫程序 |

### regressions/regression_018 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：停用帳號和禁用藥物不同
- Review：pending
- Notes：禁用账号→停用帳號, 禁用药物不應轉停用藥物

| Engine | Output |
|--------|--------|
| `zhtw` | 停用帳號和禁用藥物不同 |
| `opencc-s2twp` | 禁用賬號和禁用藥物不同 |
| `zhconv-zh-tw` | 禁用帳號和禁用藥物不同 |

### news/news_093 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：地方創生計畫吸引青年返鄉。
- Review：pending
- Notes：计划→計畫

| Engine | Output |
|--------|--------|
| `zhtw` | 地方創生計畫吸引青年返鄉。 |
| `opencc-s2twp` | 地方創生計劃吸引青年返鄉。 |
| `zhconv-zh-tw` | 地方創生計劃吸引青年返鄉。 |

### tech/tech_066 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：後端服務寫入日誌文件。
- Review：pending
- Notes：日志→日誌

| Engine | Output |
|--------|--------|
| `zhtw` | 後端服務寫入日誌文件。 |
| `opencc-s2twp` | 後端服務寫入日誌檔案。 |
| `zhconv-zh-tw` | 後端服務寫入日誌文件。 |

### social/social_033 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這家店支持電子付款。
- Review：pending
- Notes：支持保持支持，电子→電子

| Engine | Output |
|--------|--------|
| `zhtw` | 這家店支持電子付款。 |
| `opencc-s2twp` | 這家店支援電子支付。 |
| `zhconv-zh-tw` | 這家店支持電子支付。 |

### social/social_041 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：朋友傳訊息說他晚點到。
- Review：pending
- Notes：发消息→傳訊息

| Engine | Output |
|--------|--------|
| `zhtw` | 朋友傳訊息說他晚點到。 |
| `opencc-s2twp` | 朋友發訊息說他晚點到。 |
| `zhconv-zh-tw` | 朋友發消息說他晚點到。 |

### tech/tech_007 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：這個介面回傳一個布林類型的欄位。
- Review：pending
- Notes：接口返回→介面回傳, 布尔→布林, 字段→欄位

| Engine | Output |
|--------|--------|
| `zhtw` | 這個介面回傳一個布林類型的欄位。 |
| `opencc-s2twp` | 這個介面返回一個布林型別的欄位。 |
| `zhconv-zh-tw` | 這個接口返回一個布爾類型的欄位。 |

### social/social_065 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：剛剛更新應用程式之後變順了。
- Review：pending
- Notes：应用→應用程式

| Engine | Output |
|--------|--------|
| `zhtw` | 剛剛更新應用程式之後變順了。 |
| `opencc-s2twp` | 剛剛更新應用之後變順了。 |
| `zhconv-zh-tw` | 剛剛更新應用之後變順了。 |

### social/social_019 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：老闆說今天可以遠端辦公。
- Review：pending
- Notes：老板→老闆, 说→說, 远程办公→遠端辦公

| Engine | Output |
|--------|--------|
| `zhtw` | 老闆說今天可以遠端辦公。 |
| `opencc-s2twp` | 老闆說今天可以遠端辦公。 |
| `zhconv-zh-tw` | 老闆說今天可以遠程辦公。 |

### social/social_080 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：老闆傳訊息說會議延後。
- Review：pending
- Notes：发消息→傳訊息

| Engine | Output |
|--------|--------|
| `zhtw` | 老闆傳訊息說會議延後。 |
| `opencc-s2twp` | 老闆發訊息說會議延後。 |
| `zhconv-zh-tw` | 老闆發消息說會議延後。 |

### social/social_020 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：這個貼圖包太好笑了。
- Review：pending
- Notes：表情包→貼圖包

| Engine | Output |
|--------|--------|
| `zhtw` | 這個貼圖包太好笑了。 |
| `opencc-s2twp` | 這個表情包太好笑了。 |
| `zhconv-zh-tw` | 這個表情包太好笑了。 |

### regressions/regression_095 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：設備二次轉換不能變裝置
- Review：pending
- Notes：設備 target 冪等

| Engine | Output |
|--------|--------|
| `zhtw` | 設備二次轉換不能變裝置 |
| `opencc-s2twp` | 裝置二次轉換不能變裝置 |
| `zhconv-zh-tw` | 設備二次轉換不能變裝置 |

### wiki/wiki_055 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：區塊鏈透過分散式帳本記錄交易。
- Review：pending
- Notes：通过→透過，账本→帳本

| Engine | Output |
|--------|--------|
| `zhtw` | 區塊鏈透過分散式帳本記錄交易。 |
| `opencc-s2twp` | 區塊鏈透過分散式賬本記錄交易。 |
| `zhconv-zh-tw` | 區塊鏈通過分布式帳本記錄交易。 |

### regressions/regression_087 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：品質保證不是物體質量
- Review：pending
- Notes：品質/質量雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 品質保證不是物體質量 |
| `opencc-s2twp` | 質量保證不是物體質量 |
| `zhconv-zh-tw` | 質量保證不是物體質量 |

### social/social_095 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：選單選項太多我找不到。
- Review：pending
- Notes：菜单→選單

| Engine | Output |
|--------|--------|
| `zhtw` | 選單選項太多我找不到。 |
| `opencc-s2twp` | 選單選項太多我找不到。 |
| `zhconv-zh-tw` | 菜單選項太多我找不到。 |

### social/social_063 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：每週到公園散步一次。
- Review：pending
- Notes：每周到→每週到

| Engine | Output |
|--------|--------|
| `zhtw` | 每週到公園散步一次。 |
| `opencc-s2twp` | 每週到公園散步一次。 |
| `zhconv-zh-tw` | 每周到公園散步一次。 |

### tech/tech_096 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：持續整合管線已經通過。
- Review：pending
- Notes：CI 通過語境

| Engine | Output |
|--------|--------|
| `zhtw` | 持續整合管線已經通過。 |
| `opencc-s2twp` | 持續整合流水線已經透過。 |
| `zhconv-zh-tw` | 持續集成流水線已經通過。 |

### tech/tech_057 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：資料庫交易需要回滾。
- Review：pending
- Notes：事务→交易，回滚→回復

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫交易需要回滾。 |
| `opencc-s2twp` | 資料庫事務需要回滾。 |
| `zhconv-zh-tw` | 資料庫事務需要回滾。 |

### tech/tech_001 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：使用遞迴函式來解決這個問題。
- Review：pending
- Notes：递归→遞迴, 函数→函式

| Engine | Output |
|--------|--------|
| `zhtw` | 使用遞迴函式來解決這個問題。 |
| `opencc-s2twp` | 使用遞迴函式來解決這個問題。 |
| `zhconv-zh-tw` | 使用遞歸函數來解決這個問題。 |

### social/social_011 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：這家店的服務品質不錯。
- Review：pending
- Notes：这→這, 服务→服務, 服务质量→服務品質

| Engine | Output |
|--------|--------|
| `zhtw` | 這家店的服務品質不錯。 |
| `opencc-s2twp` | 這家店的服務質量不錯。 |
| `zhconv-zh-tw` | 這家店的服務質量不錯。 |

### social/social_066 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：我把影片上傳到雲端硬碟。
- Review：pending
- Notes：视频→影片

| Engine | Output |
|--------|--------|
| `zhtw` | 我把影片上傳到雲端硬碟。 |
| `opencc-s2twp` | 我把影片上傳到雲端硬碟。 |
| `zhconv-zh-tw` | 我把視頻上傳到雲端硬碟。 |

### regressions/regression_042 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：註銷公司登記
- Review：pending
- Notes：法律登記語境→註銷

| Engine | Output |
|--------|--------|
| `zhtw` | 註銷公司登記 |
| `opencc-s2twp` | 登出公司登記 |
| `zhconv-zh-tw` | 註銷公司登記 |

### wiki/wiki_003 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：雪梨歌劇院是澳大利亞的著名地標。
- Review：pending
- Notes：悉尼→雪梨, 剧→劇, 标→標

| Engine | Output |
|--------|--------|
| `zhtw` | 雪梨歌劇院是澳大利亞的著名地標。 |
| `opencc-s2twp` | 悉尼歌劇院是澳大利亞的著名地標。 |
| `zhconv-zh-tw` | 雪梨歌劇院是澳大利亞的著名地標。 |

### regressions/regression_078 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：傳訊息不是好消息
- Review：pending
- Notes：消息雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 傳訊息不是好消息 |
| `opencc-s2twp` | 發訊息不是好訊息 |
| `zhconv-zh-tw` | 發消息不是好消息 |

### regressions/regression_047 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：他默認了指控
- Review：pending
- Notes：一般默认→默認

| Engine | Output |
|--------|--------|
| `zhtw` | 他默認了指控 |
| `opencc-s2twp` | 他預設了指控 |
| `zhconv-zh-tw` | 他默認了指控 |

### tech/tech_031 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：容器映像檔需要重新建置。
- Review：pending
- Notes：镜像→映像，构建→建置

| Engine | Output |
|--------|--------|
| `zhtw` | 容器映像檔需要重新建置。 |
| `opencc-s2twp` | 容器映象需要重新構建。 |
| `zhconv-zh-tw` | 容器鏡像需要重新構建。 |

### social/social_006 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：這個軟體真的很好用，按讚。
- Review：pending
- Notes：软件→軟體, 点赞→按讚

| Engine | Output |
|--------|--------|
| `zhtw` | 這個軟體真的很好用，按讚。 |
| `opencc-s2twp` | 這個軟體真的很好用，點贊。 |
| `zhconv-zh-tw` | 這個軟體真的很好用，點讚。 |

### tech/tech_033 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：這個欄位允許為空字元串。
- Review：pending
- Notes：字段→欄位，字符串→字串

| Engine | Output |
|--------|--------|
| `zhtw` | 這個欄位允許為空字元串。 |
| `opencc-s2twp` | 這個欄位允許為空字串。 |
| `zhconv-zh-tw` | 這個欄位允許為空字符串。 |

### wiki/wiki_020 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：網際網路的發展改變了資訊傳播方式。
- Review：pending
- Notes：互联网→網際網路, 发展→發展, 信息→資訊, 传播→傳播

| Engine | Output |
|--------|--------|
| `zhtw` | 網際網路的發展改變了資訊傳播方式。 |
| `opencc-s2twp` | 網際網路的發展改變了資訊傳播方式。 |
| `zhconv-zh-tw` | 網際網路的發展改變了信息傳播方式。 |

### wiki/wiki_044 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：微處理器是現代電腦的核心元件。
- Review：pending
- Notes：微处理器→微處理器，组件→元件

| Engine | Output |
|--------|--------|
| `zhtw` | 微處理器是現代電腦的核心元件。 |
| `opencc-s2twp` | 微處理器是現代計算機的核心元件。 |
| `zhconv-zh-tw` | 微處理器是現代計算機的核心組件。 |

### wiki/wiki_099 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：遺傳演算法模擬自然選擇過程。
- Review：pending
- Notes：遗传算法→遺傳演算法

| Engine | Output |
|--------|--------|
| `zhtw` | 遺傳演算法模擬自然選擇過程。 |
| `opencc-s2twp` | 遺傳演算法模擬自然選擇過程。 |
| `zhconv-zh-tw` | 遺傳算法模擬自然選擇過程。 |

### social/social_054 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：這個貼圖包我笑到不行。
- Review：pending
- Notes：表情包→貼圖包

| Engine | Output |
|--------|--------|
| `zhtw` | 這個貼圖包我笑到不行。 |
| `opencc-s2twp` | 這個表情包我笑到不行。 |
| `zhconv-zh-tw` | 這個表情包我笑到不行。 |

### tech/tech_072 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：這個欄位預設允許為空。
- Review：pending
- Notes：字段→欄位

| Engine | Output |
|--------|--------|
| `zhtw` | 這個欄位預設允許為空。 |
| `opencc-s2twp` | 這個欄位預設允許為空。 |
| `zhconv-zh-tw` | 這個欄位默認允許為空。 |

### tech/tech_092 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：設定變更需要重新啟動服務。
- Review：pending
- Notes：配置→設定

| Engine | Output |
|--------|--------|
| `zhtw` | 設定變更需要重新啟動服務。 |
| `opencc-s2twp` | 配置變更需要重啟服務。 |
| `zhconv-zh-tw` | 配置變更需要重啟服務。 |

### wiki/wiki_051 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：神經網路由多個層組成。
- Review：pending
- Notes：神经网络→神經網路，层→層

| Engine | Output |
|--------|--------|
| `zhtw` | 神經網路由多個層組成。 |
| `opencc-s2twp` | 神經網路由多個層組成。 |
| `zhconv-zh-tw` | 神經網絡由多個層組成。 |

### regressions/regression_097 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：500公克巧克力蛋糕
- Review：pending
- Notes：數量克與巧克力

| Engine | Output |
|--------|--------|
| `zhtw` | 500公克巧克力蛋糕 |
| `opencc-s2twp` | 500克巧克力蛋糕 |
| `zhconv-zh-tw` | 500克巧克力蛋糕 |

### tech/tech_024 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：後端服務回傳 JSON 回應。
- Review：pending
- Notes：响应→回應，回传保持

| Engine | Output |
|--------|--------|
| `zhtw` | 後端服務回傳 JSON 回應。 |
| `opencc-s2twp` | 後端服務回傳 JSON 響應。 |
| `zhconv-zh-tw` | 後端服務回傳 JSON 響應。 |

### regressions/regression_068 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：戶籍登錄資料不能寫成登入
- Review：pending
- Notes：戶籍登錄保持登錄

| Engine | Output |
|--------|--------|
| `zhtw` | 戶籍登錄資料不能寫成登入 |
| `opencc-s2twp` | 戶籍登入資料不能寫成登入 |
| `zhconv-zh-tw` | 戶籍登錄資料不能寫成登入 |

### regressions/regression_010 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：註冊後請登出目前帳戶
- Review：pending
- Notes：注册→註冊, 后→後, 注销当前账户→登出目前帳戶

| Engine | Output |
|--------|--------|
| `zhtw` | 註冊後請登出目前帳戶 |
| `opencc-s2twp` | 註冊後請登出當前賬戶 |
| `zhconv-zh-tw` | 註冊後請註銷當前帳戶 |

### tech/tech_086 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：應用程式啟動後讀取設定。
- Review：pending
- Notes：应用程序→應用程式

| Engine | Output |
|--------|--------|
| `zhtw` | 應用程式啟動後讀取設定。 |
| `opencc-s2twp` | 應用程式啟動後讀取設定。 |
| `zhconv-zh-tw` | 應用程式啟動後讀取設置。 |

### news/news_032 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：民調顯示多數民眾支持改革。
- Review：pending
- Notes：民调→民調，民众→民眾

| Engine | Output |
|--------|--------|
| `zhtw` | 民調顯示多數民眾支持改革。 |
| `opencc-s2twp` | 民調顯示多數民眾支援改革。 |
| `zhconv-zh-tw` | 民調顯示多數民眾支持改革。 |

### wiki/wiki_025 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：資料結構包含陣列、連結串列與樹。
- Review：pending
- Notes：数据结构→資料結構，数组→陣列

| Engine | Output |
|--------|--------|
| `zhtw` | 資料結構包含陣列、連結串列與樹。 |
| `opencc-s2twp` | 資料結構包含陣列、連結串列與樹。 |
| `zhconv-zh-tw` | 數據結構包含數組、鍊表與樹。 |

### tech/tech_016 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：瀏覽器快取需要清除。
- Review：pending
- Notes：浏览器→瀏覽器, 缓存→快取

| Engine | Output |
|--------|--------|
| `zhtw` | 瀏覽器快取需要清除。 |
| `opencc-s2twp` | 瀏覽器快取需要清除。 |
| `zhconv-zh-tw` | 瀏覽器緩存需要清除。 |

### regressions/regression_077 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：追蹤頻道不是關注案件
- Review：pending
- Notes：社群追蹤與一般關注

| Engine | Output |
|--------|--------|
| `zhtw` | 追蹤頻道不是關注案件 |
| `opencc-s2twp` | 關注頻道不是關注案件 |
| `zhconv-zh-tw` | 關注頻道不是關注案件 |

### tech/tech_099 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：請確認網路介面是否啟用。
- Review：pending
- Notes：网络接口→網路介面

| Engine | Output |
|--------|--------|
| `zhtw` | 請確認網路介面是否啟用。 |
| `opencc-s2twp` | 請確認網路介面是否啟用。 |
| `zhconv-zh-tw` | 請確認網絡接口是否啟用。 |

### tech/tech_041 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：指令碼會清理暫存檔。
- Review：pending
- Notes：脚本→指令碼，文件依策略轉文件/檔案

| Engine | Output |
|--------|--------|
| `zhtw` | 指令碼會清理暫存檔。 |
| `opencc-s2twp` | 指令碼會清理臨時檔案。 |
| `zhconv-zh-tw` | 腳本會清理臨時文件。 |

### social/social_016 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：這個應用程式一直閃退。
- Review：pending
- Notes：应用一直闪退→應用程式一直閃退

| Engine | Output |
|--------|--------|
| `zhtw` | 這個應用程式一直閃退。 |
| `opencc-s2twp` | 這個應用一直閃退。 |
| `zhconv-zh-tw` | 這個應用一直閃退。 |

### regressions/regression_006 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：權限設定請聯絡管理員
- Review：pending
- Notes：权限→權限, 设置→設定, 联系→聯絡

| Engine | Output |
|--------|--------|
| `zhtw` | 權限設定請聯絡管理員 |
| `opencc-s2twp` | 許可權設定請聯絡管理員 |
| `zhconv-zh-tw` | 權限設置請聯繫管理員 |

### tech/tech_077 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：瀏覽器擴充功能需要重新安裝。
- Review：pending
- Notes：扩展→擴充功能

| Engine | Output |
|--------|--------|
| `zhtw` | 瀏覽器擴充功能需要重新安裝。 |
| `opencc-s2twp` | 瀏覽器擴充套件需要重新安裝。 |
| `zhconv-zh-tw` | 瀏覽器擴展需要重新安裝。 |

### tech/tech_082 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：用戶端快取已經失效。
- Review：pending
- Notes：客户端→用戶端

| Engine | Output |
|--------|--------|
| `zhtw` | 用戶端快取已經失效。 |
| `opencc-s2twp` | 客戶端快取已經失效。 |
| `zhconv-zh-tw` | 客戶端緩存已經失效。 |

### regressions/regression_031 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：前端元件需要支援深色模式
- Review：pending
- Notes：技術語境支持→支援

| Engine | Output |
|--------|--------|
| `zhtw` | 前端元件需要支援深色模式 |
| `opencc-s2twp` | 前端元件需要支援深色模式 |
| `zhconv-zh-tw` | 前端組件需要支持深色模式 |

### social/social_003 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：游泳之後去吃麵條，太爽了！
- Review：pending
- Notes：游泳保持游, 之后→之後, 面条→麵條

| Engine | Output |
|--------|--------|
| `zhtw` | 游泳之後去吃麵條，太爽了！ |
| `opencc-s2twp` | 游泳之後去吃麵條，太爽了！ |
| `zhconv-zh-tw` | 遊泳之後去吃麵條，太爽了！ |

### news/news_021 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：交通部公布春節疏運計畫。
- Review：pending
- Notes：公布保持公布，计划→計畫

| Engine | Output |
|--------|--------|
| `zhtw` | 交通部公布春節疏運計畫。 |
| `opencc-s2twp` | 交通部公佈春節疏運計劃。 |
| `zhconv-zh-tw` | 交通部公布春節疏運計劃。 |

### regressions/regression_014 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：登出帳戶後仍保留公司登記
- Review：pending
- Notes：注销账户→登出帳戶, 公司登记→公司登記

| Engine | Output |
|--------|--------|
| `zhtw` | 登出帳戶後仍保留公司登記 |
| `opencc-s2twp` | 登出賬戶後仍保留公司登記 |
| `zhconv-zh-tw` | 註銷帳戶後仍保留公司登記 |

### social/social_055 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：請把密碼設定得複雜一點。
- Review：pending
- Notes：密码→密碼，设置→設定

| Engine | Output |
|--------|--------|
| `zhtw` | 請把密碼設定得複雜一點。 |
| `opencc-s2twp` | 請把密碼設定得複雜一點。 |
| `zhconv-zh-tw` | 請把密碼設置得複雜一點。 |

### social/social_096 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：這個貼圖包我笑到不行。
- Review：pending
- Notes：表情包→貼圖包

| Engine | Output |
|--------|--------|
| `zhtw` | 這個貼圖包我笑到不行。 |
| `opencc-s2twp` | 這個表情包我笑到不行。 |
| `zhconv-zh-tw` | 這個表情包我笑到不行。 |

### tech/tech_054 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：持續部署會自動發布新版本。
- Review：pending
- Notes：持续部署→持續部署，发布→發布

| Engine | Output |
|--------|--------|
| `zhtw` | 持續部署會自動發布新版本。 |
| `opencc-s2twp` | 持續部署會自動釋出新版本。 |
| `zhconv-zh-tw` | 持續部署會自動發布新版本。 |

### news/news_083 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：財政部公布稅收統計。
- Review：pending
- Notes：公布保持公布

| Engine | Output |
|--------|--------|
| `zhtw` | 財政部公布稅收統計。 |
| `opencc-s2twp` | 財政部公佈稅收統計。 |
| `zhconv-zh-tw` | 財政部公布稅收統計。 |

### regressions/regression_096 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：網路協議定義設備之間的通訊規則
- Review：pending
- Notes：設備 target 冪等

| Engine | Output |
|--------|--------|
| `zhtw` | 網路協議定義設備之間的通訊規則 |
| `opencc-s2twp` | 網路協議定義裝置之間的通訊規則 |
| `zhconv-zh-tw` | 網絡協議定義設備之間的通信規則 |

### tech/tech_070 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：分支合併後觸發部署管線。
- Review：pending
- Notes：部署流水线→部署管線

| Engine | Output |
|--------|--------|
| `zhtw` | 分支合併後觸發部署管線。 |
| `opencc-s2twp` | 分支合併後觸發部署流水線。 |
| `zhconv-zh-tw` | 分支合併後觸發部署流水線。 |

### regressions/regression_057 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：里長在鄰里服務中心
- Review：pending
- Notes：里長與鄰里

| Engine | Output |
|--------|--------|
| `zhtw` | 里長在鄰里服務中心 |
| `opencc-s2twp` | 里長在鄰里服務中心 |
| `zhconv-zh-tw` | 裡長在鄰裡服務中心 |

### regressions/regression_015 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/samples.json`
- Corpus expected：500公克巧克力
- Review：pending
- Notes：數字語境克→公克，巧克力保持

| Engine | Output |
|--------|--------|
| `zhtw` | 500公克巧克力 |
| `opencc-s2twp` | 500克巧克力 |
| `zhconv-zh-tw` | 500克巧克力 |

### wiki/wiki_001 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/samples.json`
- Corpus expected：電腦科學是研究資訊與計算的理論基礎。
- Review：pending
- Notes：计算机→電腦, 信息→資訊

| Engine | Output |
|--------|--------|
| `zhtw` | 電腦科學是研究資訊與計算的理論基礎。 |
| `opencc-s2twp` | 電腦科學是研究資訊與計算的理論基礎。 |
| `zhconv-zh-tw` | 計算機科學是研究信息與計算的理論基礎。 |

### regressions/regression_053 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：看了下周遭的環境
- Review：pending
- Notes：下周不應吃掉周遭

| Engine | Output |
|--------|--------|
| `zhtw` | 看了下周遭的環境 |
| `opencc-s2twp` | 看了下週遭的環境 |
| `zhconv-zh-tw` | 看了下周遭的環境 |

### tech/tech_011 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：命令列工具會讀取環境變數。
- Review：pending
- Notes：命令行→命令列, 环境变量→環境變數

| Engine | Output |
|--------|--------|
| `zhtw` | 命令列工具會讀取環境變數。 |
| `opencc-s2twp` | 命令列工具會讀取環境變數。 |
| `zhconv-zh-tw` | 命令行工具會讀取環境變量。 |

### regressions/regression_071 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：檢查項目不是開源專案
- Review：pending
- Notes：項目/專案雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 檢查項目不是開源專案 |
| `opencc-s2twp` | 檢查專案不是開源專案 |
| `zhconv-zh-tw` | 檢查項目不是開源項目 |

### news/news_060 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：調查報告指出服務品質仍需改善。
- Review：pending
- Notes：服务质量→服務品質，调查→調查

| Engine | Output |
|--------|--------|
| `zhtw` | 調查報告指出服務品質仍需改善。 |
| `opencc-s2twp` | 調查報告指出服務質量仍需改善。 |
| `zhconv-zh-tw` | 調查報告指出服務質量仍需改善。 |

### tech/tech_038 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：單元測試需要模擬網路請求。
- Review：pending
- Notes：单元测试→單元測試，网络→網路

| Engine | Output |
|--------|--------|
| `zhtw` | 單元測試需要模擬網路請求。 |
| `opencc-s2twp` | 單元測試需要模擬網路請求。 |
| `zhconv-zh-tw` | 單元測試需要模擬網絡請求。 |

### news/news_002 — `zhtw_advantage`

- Source：`tests/data/corpus/news/samples.json`
- Corpus expected：國務院發布了最新的經濟數據。
- Review：pending
- Notes：发布→發布, 数据→數據

| Engine | Output |
|--------|--------|
| `zhtw` | 國務院發布了最新的經濟數據。 |
| `opencc-s2twp` | 國務院釋出了最新的經濟資料。 |
| `zhconv-zh-tw` | 國務院發布了最新的經濟數據。 |

### tech/tech_009 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/samples.json`
- Corpus expected：快取命中率會影響回應時間。
- Review：pending
- Notes：缓存→快取, 响应时间→回應時間

| Engine | Output |
|--------|--------|
| `zhtw` | 快取命中率會影響回應時間。 |
| `opencc-s2twp` | 快取命中率會影響響應時間。 |
| `zhconv-zh-tw` | 緩存命中率會影響響應時間。 |

### wiki/wiki_026 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27.json`
- Corpus expected：機率論是數學的重要分支。
- Review：pending
- Notes：概率→機率，数学→數學

| Engine | Output |
|--------|--------|
| `zhtw` | 機率論是數學的重要分支。 |
| `opencc-s2twp` | 機率論是數學的重要分支。 |
| `zhconv-zh-tw` | 概率論是數學的重要分支。 |

### wiki/wiki_075 — `zhtw_advantage`

- Source：`tests/data/corpus/wiki/expanded-2026-06-27-500.json`
- Corpus expected：機率分布描述隨機變數。
- Review：pending
- Notes：概率→機率

| Engine | Output |
|--------|--------|
| `zhtw` | 機率分布描述隨機變數。 |
| `opencc-s2twp` | 機率分佈描述隨機變數。 |
| `zhconv-zh-tw` | 概率分布描述隨機變量。 |

### regressions/regression_023 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：交通部公布春節疏運計畫
- Review：pending
- Notes：公布不應轉公佈

| Engine | Output |
|--------|--------|
| `zhtw` | 交通部公布春節疏運計畫 |
| `opencc-s2twp` | 交通部公佈春節疏運計劃 |
| `zhconv-zh-tw` | 交通部公布春節疏運計劃 |

### tech/tech_062 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：請在設定檔中新增環境變數。
- Review：pending
- Notes：配置文件→設定檔

| Engine | Output |
|--------|--------|
| `zhtw` | 請在設定檔中新增環境變數。 |
| `opencc-s2twp` | 請在配置檔案中新增環境變數。 |
| `zhconv-zh-tw` | 請在配置文件中新增環境變量。 |

### social/social_090 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：請聯絡管理員重設密碼。
- Review：pending
- Notes：联系管理员→聯絡管理員

| Engine | Output |
|--------|--------|
| `zhtw` | 請聯絡管理員重設密碼。 |
| `opencc-s2twp` | 請聯絡管理員重置密碼。 |
| `zhconv-zh-tw` | 請聯繫管理員重置密碼。 |

### regressions/regression_073 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：儲存檔案不是保存文化遺產
- Review：pending
- Notes：保存雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 儲存檔案不是保存文化遺產 |
| `opencc-s2twp` | 儲存檔案不是儲存文化遺產 |
| `zhconv-zh-tw` | 保存文件不是保存文化遺產 |

### social/social_075 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27-500.json`
- Corpus expected：登出帳號之前先備份資料。
- Review：pending
- Notes：注销账号→登出帳號

| Engine | Output |
|--------|--------|
| `zhtw` | 登出帳號之前先備份資料。 |
| `opencc-s2twp` | 登出賬號之前先備份資料。 |
| `zhconv-zh-tw` | 註銷帳號之前先備份資料。 |

### tech/tech_040 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：權限驗證失敗時返回錯誤資訊。
- Review：pending
- Notes：权限→權限，信息→資訊

| Engine | Output |
|--------|--------|
| `zhtw` | 權限驗證失敗時返回錯誤資訊。 |
| `opencc-s2twp` | 許可權驗證失敗時返回錯誤資訊。 |
| `zhconv-zh-tw` | 權限驗證失敗時返回錯誤信息。 |

### tech/tech_093 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：程式啟動參數寫在說明文件中。
- Review：pending
- Notes：程序→程式

| Engine | Output |
|--------|--------|
| `zhtw` | 程式啟動參數寫在說明文件中。 |
| `opencc-s2twp` | 程式啟動引數寫在說明檔案中。 |
| `zhconv-zh-tw` | 程序啟動參數寫在說明文件中。 |

### regressions/regression_062 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：已經透過 API 下載檔案
- Review：pending
- Notes：通过 API→透過 API

| Engine | Output |
|--------|--------|
| `zhtw` | 已經透過 API 下載檔案 |
| `opencc-s2twp` | 已經透過 API 下載檔案 |
| `zhconv-zh-tw` | 已經通過 API 下載文件 |

### social/social_008 — `zhtw_advantage`

- Source：`tests/data/corpus/social/samples.json`
- Corpus expected：這個影片太高畫質了。
- Review：pending
- Notes：视频→影片, 高清→高畫質

| Engine | Output |
|--------|--------|
| `zhtw` | 這個影片太高畫質了。 |
| `opencc-s2twp` | 這個影片太高畫質了。 |
| `zhconv-zh-tw` | 這個視頻太高清了。 |

### tech/tech_069 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：請重新建置專案並發布版本。
- Review：pending
- Notes：重新构建项目→重新建置專案

| Engine | Output |
|--------|--------|
| `zhtw` | 請重新建置專案並發布版本。 |
| `opencc-s2twp` | 請重新構建專案併發布版本。 |
| `zhconv-zh-tw` | 請重新構建項目並發布版本。 |

### regressions/regression_080 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：復原操作不是撤銷登記
- Review：pending
- Notes：撤銷/復原雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 復原操作不是撤銷登記 |
| `opencc-s2twp` | 撤銷操作不是撤銷登記 |
| `zhconv-zh-tw` | 撤銷操作不是撤銷登記 |

### regressions/regression_072 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：政府文件不是檔案系統
- Review：pending
- Notes：正式文件與檔案系統

| Engine | Output |
|--------|--------|
| `zhtw` | 政府文件不是檔案系統 |
| `opencc-s2twp` | 政府檔案不是檔案系統 |
| `zhconv-zh-tw` | 政府文件不是文件系統 |

### news/news_028 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：氣象部門發布豪雨特報。
- Review：pending
- Notes：气象→氣象，发布→發布

| Engine | Output |
|--------|--------|
| `zhtw` | 氣象部門發布豪雨特報。 |
| `opencc-s2twp` | 氣象部門釋出豪雨特報。 |
| `zhconv-zh-tw` | 氣象部門發布豪雨特報。 |

### tech/tech_063 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：資料庫連線失敗時會重試。
- Review：pending
- Notes：连接→連線

| Engine | Output |
|--------|--------|
| `zhtw` | 資料庫連線失敗時會重試。 |
| `opencc-s2twp` | 資料庫連線失敗時會重試。 |
| `zhconv-zh-tw` | 資料庫連接失敗時會重試。 |

### social/social_060 — `zhtw_advantage`

- Source：`tests/data/corpus/social/expanded-2026-06-27.json`
- Corpus expected：請聯絡管理員幫忙處理。
- Review：pending
- Notes：联系管理员→聯絡管理員

| Engine | Output |
|--------|--------|
| `zhtw` | 請聯絡管理員幫忙處理。 |
| `opencc-s2twp` | 請聯絡管理員幫忙處理。 |
| `zhconv-zh-tw` | 請聯繫管理員幫忙處理。 |

### tech/tech_027 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：對象序列化後寫入快取。
- Review：pending
- Notes：对象→物件，缓存→快取

| Engine | Output |
|--------|--------|
| `zhtw` | 對象序列化後寫入快取。 |
| `opencc-s2twp` | 物件序列化後寫入快取。 |
| `zhconv-zh-tw` | 對象序列化後寫入緩存。 |

### tech/tech_058 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：API 閘道會限制請求頻率。
- Review：pending
- Notes：请求频率→請求頻率

| Engine | Output |
|--------|--------|
| `zhtw` | API 閘道會限制請求頻率。 |
| `opencc-s2twp` | API 閘道器會限制請求頻率。 |
| `zhconv-zh-tw` | API 網關會限制請求頻率。 |

### news/news_052 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：政府補助中小企業升級設備。
- Review：pending
- Notes：补助→補助，企业→企業

| Engine | Output |
|--------|--------|
| `zhtw` | 政府補助中小企業升級設備。 |
| `opencc-s2twp` | 政府補助中小企業升級裝置。 |
| `zhconv-zh-tw` | 政府補助中小企業升級設備。 |

### regressions/regression_075 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：策略合作不是軍事戰略
- Review：pending
- Notes：策略/戰略雙語境

| Engine | Output |
|--------|--------|
| `zhtw` | 策略合作不是軍事戰略 |
| `opencc-s2twp` | 戰略合作不是軍事戰略 |
| `zhconv-zh-tw` | 戰略合作不是軍事戰略 |

### regressions/regression_086 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27-500.json`
- Corpus expected：通過審查後透過介面提交
- Review：pending
- Notes：通過審查，透過介面

| Engine | Output |
|--------|--------|
| `zhtw` | 通過審查後透過介面提交 |
| `opencc-s2twp` | 透過審查後透過介面提交 |
| `zhconv-zh-tw` | 通過審查後通過接口提交 |

### regressions/regression_021 — `zhtw_advantage`

- Source：`tests/data/corpus/regressions/expanded-2026-06-27.json`
- Corpus expected：每週到店一次
- Review：pending
- Notes：每周到不應被周到 identity 擋住

| Engine | Output |
|--------|--------|
| `zhtw` | 每週到店一次 |
| `opencc-s2twp` | 每週到店一次 |
| `zhconv-zh-tw` | 每周到店一次 |

### tech/tech_060 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27.json`
- Corpus expected：程式退出前會釋放資源。
- Review：pending
- Notes：程序→程式，资源→資源

| Engine | Output |
|--------|--------|
| `zhtw` | 程式退出前會釋放資源。 |
| `opencc-s2twp` | 程式退出前會釋放資源。 |
| `zhconv-zh-tw` | 程序退出前會釋放資源。 |

### news/news_073 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27-500.json`
- Corpus expected：旅遊業者期待國際旅客迴流。
- Review：pending
- Notes：旅游→旅遊

| Engine | Output |
|--------|--------|
| `zhtw` | 旅遊業者期待國際旅客迴流。 |
| `opencc-s2twp` | 旅遊業者期待國際旅客迴流。 |
| `zhconv-zh-tw` | 旅遊業者期待國際旅客回流。 |

### news/news_038 — `zhtw_advantage`

- Source：`tests/data/corpus/news/expanded-2026-06-27.json`
- Corpus expected：文化部宣布開放線上申請。
- Review：pending
- Notes：宣布保持宣布，线上→線上

| Engine | Output |
|--------|--------|
| `zhtw` | 文化部宣布開放線上申請。 |
| `opencc-s2twp` | 文化部宣佈開放線上申請。 |
| `zhconv-zh-tw` | 文化部宣布開放線上申請。 |

### tech/tech_088 — `zhtw_advantage`

- Source：`tests/data/corpus/tech/expanded-2026-06-27-500.json`
- Corpus expected：持續部署失敗後停止發布。
- Review：pending
- Notes：持续部署→持續部署

| Engine | Output |
|--------|--------|
| `zhtw` | 持續部署失敗後停止發布。 |
| `opencc-s2twp` | 持續部署失敗後停止釋出。 |
| `zhconv-zh-tw` | 持續部署失敗後停止發布。 |
