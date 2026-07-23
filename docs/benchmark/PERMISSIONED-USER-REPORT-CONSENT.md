# Permissioned User Report Consent v1

Version ID: `permissioned-user-report-v1`

本流程只收集簡體中文原句，用於 zhtw 公開 benchmark 的評估與報告。不得提交
expected、可接受答案、任何轉換器輸出，或根據轉換結果挑選的句子。

## 提交者聲明

送出 GitHub issue 前，提交者必須逐項確認：

1. 提交者是文字的原作者或有權依 CC0 提供該文字；內容不是從受著作權保護的
   私人郵件、聊天、文件、網站或客戶資料直接複製。
2. 提交者在其可處分權利範圍內，對提交文字適用
   [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)，允許公眾
   複製、修改、散布、翻譯與公開使用。CC0 的正式法律文字優先於本說明。
3. 提交內容與 GitHub 帳號、issue、時間及同意紀錄都會公開保存，並可能出現在
   zhtw 的 benchmark、測試資料、報告及衍生版本中。
4. 內容不含真實姓名、電子郵件、電話、地址、帳號、客戶編號、身分證明、密碼、
   API key、token、私鑰、內部網址參數、未公開商業資料或其他敏感資訊。
5. 提交內容是 input-only，沒有 expected 或 converter output，也不是因為某個
   轉換器轉錯而特別挑選。

CC0 原則上不可撤回。Maintainer 可在 benchmark freeze 前依請求移除尚未發布的案例，
但不保證能從既有 Git 歷史、fork、下載內容或已發布衍生資料中刪除。

## 專案處理規則

- 自動檢查只降低風險，不能保證偵測所有個資或秘密。
- 偵測到敏感內容時整筆拒絕，要求提交者提供已自行去識別的新句子；工具不得靜默
  遮罩或改寫原句。
- Issue 中的情境說明不會匯入 benchmark，也不會直接決定 domain、risk 或 expected。
- 收集批次必須滿 100 筆、通過 schema 與敏感資料檢查後，才可標記
  `ready_for_import`。
- 匯入後仍須依 Codex、Gemini、maintainer 與 exact/near-dedupe gate 審查。

本文件是專案資料治理說明，不是法律意見。
