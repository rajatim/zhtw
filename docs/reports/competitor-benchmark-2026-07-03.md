<!-- zhtw:disable -->
# 競品 Benchmark 報告（2026-07-03）

## 摘要

本報告使用 `benchmarks/precision_cases.json` 的 26 筆人工標註 expected，比較 zhtw 與兩個可選競品轉換器。競品結果只作為候選問題偵測，不作為詞庫來源。

執行指令：

```bash
uv run --with opencc-python-reimplemented --with zhconv python scripts/competitor_benchmark.py --format json --output docs/reports/competitor-benchmark-2026-07-03.json
```

引擎：

| 引擎 | 版本 | 狀態 |
|------|------|------|
| zhtw | 4.4.1 | available |
| opencc-s2twp | 0.1.7 | available |
| zhconv-zh-tw | 1.4.3 | available |

結果：

| 分類 | 數量 | 判讀 |
|------|------|------|
| `candidate_gap` | 0 | 沒有發現「競品符合 expected、zhtw 不符合」的案例 |
| `zhtw_miss` | 0 | 沒有發現 zhtw 未符合人工 expected 的案例 |
| `zhtw_advantage` | 21 | zhtw 符合 expected，但至少一個競品不符合 |
| `all_match` | 5 | zhtw 與兩個競品都符合 expected |
| `zhtw_only` | 0 | 本次所有競品都可用 |

結論：這批案例目前不應導入任何競品詞條；更有價值的是把 `zhtw_advantage` 當作少錯轉與台灣 IT/UI 用語的差異化證據。

## 差異化案例

| ID | 領域 | 輸入 | expected | 競品差異摘要 |
|----|------|------|----------|--------------|
| `it-software-config-file` | it | 软件开发需要配置文件 | 軟體開發需要設定檔 | OpenCC 輸出「配置檔案」，zhconv 保留「配置文件」 |
| `it-login-system` | it | 请先登录系统 | 請先登入系統 | zhconv 輸出「登錄系統」 |
| `it-function-return-value` | it | 函数返回值 | 函式回傳值 | OpenCC 保留「返回值」，zhconv 保留「函數返回值」 |
| `it-file-system` | it | 文件系统损坏 | 檔案系統損壞 | zhconv 輸出「文件系統」 |
| `it-official-document` | formal | 政府发布官方文件 | 政府發布官方文件 | OpenCC 過度轉成「政府釋出官方檔案」 |
| `it-delete-this-document` | daily | 删除这个文件 | 刪除這個文件 | OpenCC 過度轉成「刪除這個檔案」 |
| `ui-save-file` | ui | 保存文件成功 | 儲存檔案成功 | zhconv 保留「保存文件」 |
| `daily-preserve-heritage` | daily | 保存文化遗产 | 保存文化遺產 | OpenCC 過度轉成「儲存文化遺產」 |
| `ui-favorites-folder` | ui | 收藏夹整理 | 我的最愛整理 | OpenCC/zhconv 都只做字形轉換成「收藏夾」 |
| `social-follow-channel` | social | 关注我们的频道 | 追蹤我們的頻道 | OpenCC/zhconv 都保留「關注」 |
| `quality-physical-mass` | science | 物体的质量是10千克 | 物體的質量是10公斤 | OpenCC/zhconv 都保留「10千克」 |
| `weight-grams` | daily | 500克糖 | 500公克糖 | OpenCC/zhconv 都保留「500克」 |
| `tech-network-protocol` | it | 网络协议定义设备之间的通信规则 | 網路協議定義設備之間的通訊規則 | OpenCC 將「設備」轉「裝置」，zhconv 保留「網絡/通信」 |
| `tech-frontend-component` | it | 前端组件需要支持深色模式 | 前端元件需要支援深色模式 | zhconv 保留「組件/支持」 |
| `tech-backend-status-code` | it | 后端服务返回状态码 | 後端服務回傳狀態碼 | OpenCC/zhconv 都保留「返回」 |
| `ui-detail-page` | ui | 查看详情页 | 查看詳情頁 | OpenCC 轉成「檢視詳情頁」 |
| `business-tsmc-process` | business | 台积电宣布扩大先进制程投资 | 台積電宣布擴大先進製程投資 | OpenCC 用「臺積電/宣佈」，zhconv 錯成「先進位程」 |
| `ui-disable-account` | ui | 禁用账号和禁用药物不同 | 停用帳號和禁用藥物不同 | OpenCC/zhconv 都未處理帳號語境的「停用」 |
| `ui-default-avatar` | ui | 默认头像太丑了 | 預設頭像太醜了 | zhconv 保留「默認」 |
| `daily-admit-accusation` | daily | 他默认了指控 | 他默認了指控 | OpenCC 過度轉成「他預設了指控」 |
| `it-programmer-haircut` | it | 长发程序员在理发店写程序 | 長髮程式設計師在理髮店寫程式 | zhconv 保留「長發/程序」；OpenCC 與 zhtw 一致 |

## 全工具一致案例

| ID | 領域 | 輸入 | expected |
|----|------|------|----------|
| `daily-collect-antiques` | daily | 他收藏古董 | 他收藏古董 |
| `formal-focus-case` | formal | 民众关注此案 | 民眾關注此案 |
| `quality-product` | daily | 产品的质量很好 | 產品的質量很好 |
| `food-chocolate` | daily | 巧克力蛋糕 | 巧克力蛋糕 |
| `tech-ai` | it | 人工智能发展 | 人工智慧發展 |

## 後續判斷

本次沒有 `candidate_gap`，所以沒有可直接排入詞庫修改的候選。下一步應擴充 benchmark 的探索來源，而不是從競品詞庫匯入：

- 從真實使用者回報與 `zhtw-test-corpus` 找 zhtw 尚未覆蓋的句子。
- 每個新增案例都先人工標註 expected，再跑競品比較。
- 若未來出現 `candidate_gap`，先補 golden/corpus regression，再按詞庫指南確認是否需要新增詞或 identity mapping。
