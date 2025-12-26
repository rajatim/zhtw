"""Prompt templates for LLM operations."""

VALIDATE_TERM_PROMPT = """判斷以下簡體/港式中文轉換為台灣繁體是否正確：

來源詞：{source}
目標詞：{target}

請判斷這個轉換是否正確。考慮：
1. 來源詞是否為簡體中文或港式用語
2. 目標詞是否為正確的台灣繁體用語
3. 轉換是否保留原意

請用以下 JSON 格式回答（只回答 JSON，不要其他文字）：
{{"correct": true/false, "reason": "原因說明", "suggestion": "建議的替代詞或null"}}
"""

DISCOVER_TERM_PROMPT = """分析以下中文詞彙，判斷是否需要轉換為台灣繁體：

詞彙：{term}
上下文：{context}

請判斷這個詞彙是否為：
1. 簡體中文（需要轉換）
2. 港式用語（需要轉換）
3. 已經是台灣繁體（不需轉換）

請用以下 JSON 格式回答（只回答 JSON，不要其他文字）：
{{"needs_conversion": true/false, "target": "建議詞彙", "confidence": 0.0-1.0, "reason": "原因"}}
"""

BATCH_VALIDATE_PROMPT = """批量驗證以下簡體/港式中文轉台灣繁體的轉換是否正確：

{terms_list}

請用以下 JSON 格式回答每個轉換（只回答 JSON 陣列，不要其他文字）：
[
  {{"source": "來源詞", "target": "目標詞", "correct": true/false, "reason": "原因"}},
  ...
]
"""
