#!/usr/bin/env python3
"""
從 Unicode Unihan 資料庫生成安全的一對一簡繁字元對映表。

用法：
    python scripts/generate_charmap.py
    python scripts/generate_charmap.py --output src/zhtw/data/charmap/safe_chars.json
    python scripts/generate_charmap.py --report  # 顯示審核報告

資料來源：Unicode Unihan kTraditionalVariant / kSimplifiedVariant
"""

from __future__ import annotations

import argparse
import io
import json
import sys
import zipfile
from pathlib import Path
from urllib.request import urlopen

# Unicode Unihan 資料庫 URL
UNIHAN_URL = "https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip"

# 預設輸出路徑
DEFAULT_OUTPUT = (
    Path(__file__).parent.parent / "src" / "zhtw" / "data" / "charmap" / "safe_chars.json"
)

# 現有詞庫路徑（用於交叉比對）
TERMS_DIR = Path(__file__).parent.parent / "src" / "zhtw" / "data" / "terms"

# ============================================================
# 人工審核覆寫
# ============================================================

# Unihan 標記為一對一，但實際上在繁體中有語義歧義的字。
# 這些字在簡體中是「合併簡化」的結果，在繁體中原字仍有獨立語義。
# 例如：後 是 後 的簡化字，但「後」（皇后）在繁體中也存在。
FORCE_EXCLUDE = {
    "後",  # 後(behind) vs 後(empress)
    "面",  # 麵(noodle) vs 面(face)
    "鹹",  # 鹹(salty) vs 鹹(all)
    "冬",  # 鼕(drum sound) vs 冬(winter)
    "朱",  # 硃(cinnabar) vs 朱(vermilion)
    "余",  # 餘(remaining) vs 余(I, archaic)
    "谷",  # 穀(grain) vs 谷(valley)
    "丰",  # 豐(abundant) vs 丰(graceful)
    "醜",  # 醜(ugly) vs 醜(earthly branch)
    "斗",  # 鬥(fight) vs 斗(dipper)
    "几",  # 幾(how many) vs 几(small table)
    "卜",  # 蔔(radish) vs 卜(divination)
    "仆",  # 僕(servant) vs 仆(fall forward)
    "了",  # 瞭(understand) vs 了(particle)
    "千",  # 韆(swing) vs 千(thousand)
    "才",  # 才(just now) vs 才(talent)
    "出",  # 齣(act of play) vs 出(exit)
    "曲",  # 麯(yeast) vs 曲(song/curve)
    "公公克",  # 剋(overcome) vs 公公克(gram)
    "奸",  # 姦(adultery) vs 奸(treacherous)
    "征",  # 徵(levy/sign) vs 征(expedition)
    "折",  # 摺(fold) vs 折(break)
    "採",  # 採(pick) vs 採(style)
    "志",  # 誌(record) vs 志(ambition)
    "注",  # 註(note) vs 注(pour)
    "制",  # 製(manufacture) vs 制(system)
    "准",  # 準(standard) vs 准(approve)
    "布",  # 佈(spread) vs 布(cloth)
    "板",  # 闆(boss) vs 板(board)
    "松",  # 鬆(loose) vs 松(pine)
    "表",  # 錶(watch) vs 表(table/surface)
    "捨",  # 捨(abandon) vs 捨(house)
    "別",  # 彆(awkward) vs 別(separate)
    "向",  # 嚮(towards) vs 向(direction)
    "回",  # 迴(detour) vs 回(return)
    "困",  # 睏(sleepy) vs 困(trapped)
    "吊",  # 弔(condole) vs 吊(hang)
    "冲",  # 衝(rush) vs 沖(rinse)
    "御",  # 禦(defend) vs 御(royal)
    "借",  # 藉(by means of) vs 借(borrow)
    "劃",  # 劃(plan) vs 劃(row boat)
    "占",  # 佔(occupy) vs 占(divine)
    "游",  # 遊(travel) vs 游(swim)
    "闢",  # 闢(open) vs 闢(king's order)
    "朴",  # 樸(simple) vs 朴(a surname/tree)
    "家",  # 傢(furniture) vs 家(home)
    "致",  # 緻(fine) vs 致(cause)
    "栗",  # 慄(tremble) vs 栗(chestnut)
    "杰",  # 傑(outstanding) vs 杰(hero)
    "卷",  # 捲(roll) vs 卷(scroll)
    "秋",  # 鞦(swing) vs 秋(autumn)
    "尸",  # 屍(corpse) vs 尸(preside over)
    "同",  # 衕(alley) vs 同(same)
    "升",  # 昇(rise) vs 升(liter)
    "累",  # 纍(archaic) vs 累(tired/accumulate) — Taiwan uses 累
    "合",  # 閤(door/archaic) vs 合(combine) — Taiwan uses 合
    "灶",  # 竈(archaic) vs 灶(stove) — Taiwan uses 灶
    "𬮤",  # CJK Ext-F, maps to archaic 閤 — too rare and archaic
}

# Unihan 標記為一對多，但實際上某個變體是明確標準的字。
# 通常是 Unihan 列出了一個罕用異體字，但標準形式是確定的。
FORCE_INCLUDE = {
    "說": "說",  # 説 是 說 的異體字，說 是標準
    "為": "為",  # 為 是 為 的異體字
    "兩": "兩",  # 兩 不是繁體字
    "個": "個",  # 個 不是繁體字
    "產": "產",  # 産 是 產 的異體字
    "義": "義",  # 義 不是繁體字
    "乐": "樂",  # 乐 不是繁體字
    "亂": "亂",  # 亂 不是繁體字
    "争": "爭",  # 争 不是繁體字
    "虧": "虧",  # 虧 不是繁體字
    "雲": "雲",  # 雲(to say) 在現代中文幾乎不用
    "僅": "僅",  # 僅 不是繁體字
    "從": "從",  # 從 不是繁體字
    "仪": "儀",  # 仪 不是繁體字
    "价": "價",  # 价 不是繁體字
    "優": "優",  # 優 不是繁體字
    "會": "會",  # 會 不是繁體字
    "伤": "傷",  # 伤 不是繁體字
    "體": "體",  # 體 不是繁體字
    "單": "單",  # 單 不是繁體字
    "儿": "兒",  # 儿 不是繁體字
    "内": "內",  # 内 是 內 的異體字，內 是標準
    "凤": "鳳",  # 凤 不是繁體字
    "凭": "憑",  # 凭 不是繁體字
    "劉": "劉",  # 劉 不是繁體字
    "創": "創",  # 創 不是繁體字
    "删": "刪",  # 删 不是繁體字
    "動": "動",  # 動 不是繁體字
    "劝": "勸",  # 劝 不是繁體字
    "辦": "辦",  # 辦 不是繁體字
    "励": "勵",  # 励 不是繁體字
    "勞": "勞",  # 勞 不是繁體字
    "勢": "勢",  # 勢 不是繁體字
    "区": "區",  # 区 不是繁體字
    "醫": "醫",  # 醫 不是繁體字
    "號": "號",  # 號 不是繁體字
    "聽": "聽",  # 聽 不是繁體字
    "吓": "嚇",  # 吓 不是繁體字
    "圖": "圖",  # 圖 不是繁體字
    "壞": "壞",  # 壞 不是繁體字
    "塊": "塊",  # 塊 不是繁體字
    "壮": "壯",  # 壮 不是繁體字
    "聲": "聲",  # 聲 不是繁體字
    "頭": "頭",  # 頭 不是繁體字
    "誇": "誇",  # 誇 不是繁體字（誇父的誇用法極罕）
    "寧": "寧",  # 寧 不是繁體字
    "寶": "寶",  # 寶 不是繁體字
    "實": "實",  # 實 不是繁體字
    "對": "對",  # 對 不是繁體字
    "宾": "賓",  # 宾 不是繁體字
    "尔": "爾",  # 尔 不是繁體字
    "盡": "盡",  # 「儘」是「盡」的用法分化，盡 是主體
    "屆": "屆",  # 屆 不是繁體字
    "屬": "屬",  # 屬 不是繁體字
    "歲": "歲",  # 歲 不是繁體字
    "師": "師",  # 師 不是繁體字
    "幫": "幫",  # 幫 不是繁體字
    "廣": "廣",  # 廣(shelter) 幾乎不用
    "應": "應",  # 應 不是繁體字
    "庙": "廟",  # 庙 不是繁體字
    "開": "開",  # 開 不是繁體字
    "棄": "棄",  # 棄 不是繁體字
    "弯": "彎",  # 弯 不是繁體字
    "弹": "彈",  # 弹 不是繁體字
    "歸": "歸",  # 歸 不是繁體字
    "錄": "錄",  # 錄 不是繁體字
    "怀": "懷",  # 怀 不是繁體字
    "怜": "憐",  # 怜 不是繁體字
    "恋": "戀",  # 恋 不是繁體字
    "惡": "惡",  # 噁 是口語用法
    "恼": "惱",  # 恼 不是繁體字
    "惧": "懼",  # 惧 不是繁體字
    "惩": "懲",  # 惩 不是繁體字
    "願": "願",  # 願 不是繁體字
    "戲": "戲",  # 戲 不是繁體字
    "战": "戰",  # 战 不是繁體字
    "戶": "戶",  # 戶 是 戶 的異體字
    "執": "執",  # 執 不是繁體字
    "扑": "撲",  # 扑 不是繁體字
    "報": "報",  # 報 不是繁體字
    "担": "擔",  # 担 不是繁體字
    "擋": "擋",  # 擋 不是繁體字
    "據": "據",  # 據 不是繁體字
    "掷": "擲",  # 掷 不是繁體字
    "携": "攜",  # 携 不是繁體字
    "摊": "攤",  # 摊 不是繁體字
    "數": "數",  # 數 不是繁體字
    "无": "無",  # 无 不是繁體字
    "時": "時",  # 時 不是繁體字
    "機": "機",  # 機 不是繁體字
    "權": "權",  # 權 不是繁體字
    "極": "極",  # 極 不是繁體字
    "構": "構",  # 構 不是繁體字
    "標": "標",  # 標 不是繁體字
    "楼": "樓",  # 楼 不是繁體字
    "歡": "歡",  # 歡 不是繁體字
    "氣": "氣",  # 氣 不是繁體字
    "沪": "滬",  # 沪 不是繁體字
    "泪": "淚",  # 泪 不是繁體字
    "洒": "灑",  # 洒 不是繁體字
    "浅": "淺",  # 浅 不是繁體字
    "涛": "濤",  # 涛 不是繁體字
    "湾": "灣",  # 湾 不是繁體字
    "滨": "濱",  # 滨 不是繁體字
    "滩": "灘",  # 滩 不是繁體字
    "灯": "燈",  # 灯 不是繁體字
    "炉": "爐",  # 炉 不是繁體字
    "點": "點",  # 點 不是繁體字
    "烛": "燭",  # 烛 不是繁體字
    "熱": "熱",  # 熱 不是繁體字
    "犹": "猶",  # 犹 不是繁體字
    "獨": "獨",  # 獨 不是繁體字
    "豬": "豬",  # 豬 不是繁體字
    "貓": "貓",  # 貓 不是繁體字
    "獻": "獻",  # 獻 不是繁體字
    "環": "環",  # 環 不是繁體字
    "琼": "瓊",  # 琼 不是繁體字
    "電": "電",  # 電 不是繁體字
    "画": "畫",  # 画 不是繁體字
    "確": "確",  # 確 不是繁體字
    "礼": "禮",  # 礼 不是繁體字
    "種": "種",  # 種 不是繁體字
    "稱": "稱",  # 稱 不是繁體字
    "穩": "穩",  # 穩 不是繁體字
    "窮": "窮",  # 窮 不是繁體字
    "窃": "竊",  # 窃 不是繁體字
    "筆": "筆",  # 筆 不是繁體字
    "線": "線",  # 綫 是異體
    "凫": "鳧",  # 鳬 是鳧的異體字
    "坝": "壩",  # 垻 極罕
    "竖": "豎",  # 竪 是豎的異體字
    "绣": "繡",  # 鏽=rust 是不同字，不構成歧義
    "绷": "繃",  # 無真實替代
    "蕴": "蘊",  # 縕/緼 是古字
    "谣": "謠",  # 諑 極罕
    "赃": "贓",  # 無真實替代
    "酝": "醞",  # 無真實替代
    "锈": "鏽",  # 銹 是鏽的異體字
    "颓": "頹",  # 穨 是古字
    "鳄": "鱷",  # 無真實替代
    "網": "網",  # 網 不是繁體字
    "羅": "羅",  # 羅 不是繁體字
    "職": "職",  # 職 不是繁體字
    "聯": "聯",  # 聯 不是繁體字
    "膽": "膽",  # 膽 不是繁體字
    "脚": "腳",  # 脚 不是繁體字（脚 是 腳 的俗字）
    "髒": "髒",  # 臟(organ) 由詞庫層處理
    "艳": "艷",  # 艳 不是繁體字
    "芦": "蘆",  # 芦 不是繁體字
    "榮": "榮",  # 榮 不是繁體字
    "藥": "藥",  # 葯 是罕用異體
    "萝": "蘿",  # 萝 不是繁體字
    "蠻": "蠻",  # 蠻 不是繁體字
    "補": "補",  # 補 不是繁體字
    "譽": "譽",  # 譽 不是繁體字
    "辭": "辭",  # 辭 不是繁體字
    "邊": "邊",  # 邊 不是繁體字
    "迁": "遷",  # 迁 不是繁體字
    "過": "過",  # 過 不是繁體字
    "還": "還",  # 還 不是繁體字
    "這": "這",  # 這 不是繁體字
    "遠": "遠",  # 遠 不是繁體字
    "適": "適",  # 適 不是繁體字
    "選": "選",  # 選 不是繁體字
    "遞": "遞",  # 遞 不是繁體字
    "邏": "邏",  # 邏 不是繁體字
    "郑": "鄭",  # 郑 不是繁體字
    "际": "際",  # 际 不是繁體字
    "隨": "隨",  # 隨 不是繁體字
    "隱": "隱",  # 隱 不是繁體字
    "隶": "隸",  # 隶 不是繁體字
    "難": "難",  # 難 不是繁體字
    "風": "風",  # 風 不是繁體字
    "骂": "罵",  # 骂 不是繁體字
    "龜": "龜",  # 龜 不是繁體字
    "党": "黨",  # 党 不是繁體字
    "廠": "廠",  # 廣 的同類
    "歷": "歷",  # 曆(calendar) 由詞庫處理
    "厉": "厲",  # 厉 不是繁體字
    "壓": "壓",  # 壓 不是繁體字
    "厕": "廁",  # 厕 不是繁體字
    "厨": "廚",  # 厨 不是繁體字
    "雙": "雙",  # 雙 不是繁體字
    "葉": "葉",  # 葉 不是繁體字
    "吴": "吳",  # 吴 不是繁體字
    "園": "園",  # 園 不是繁體字
    "墙": "牆",  # 牆 是標準
    "壳": "殼",  # 殼 是標準
    "夠": "夠",  # 夠 不是繁體字
    "孫": "孫",  # 孫 不是繁體字
    "姜": "薑",  # 姜(surname) 幾乎只在姓名用，薑 是標準
    "娇": "嬌",  # 娇 不是繁體字
    "層": "層",  # 層 不是繁體字
    "當": "當",  # 噹 由詞庫處理
    "發": "發",  # 髮 由詞庫處理（頭髮→頭髮）
    "蓋": "蓋",  # 蓋 不是繁體字
    "著": "著",  # 著 是 著 的俗寫
    "矫": "矯",  # 矫 不是繁體字
    "粮": "糧",  # 粮 不是繁體字
    # 繁: identity → 不加入對映（跳過）
    # 累: 纍 是異體，累 在繁體中通用 → 不加入對映（跳過）
    "劇": "劇",  # 劇 不是繁體字
    "郁": "鬱",  # 鬱 是標準
    "霉": "黴",  # 黴 是標準
    "烟": "煙",  # 菸 由詞庫處理
    "簽": "簽",  # 籤 由詞庫處理
    "叙": "敘",  # 叙 不是繁體字
    "叠": "疊",  # 叠 不是繁體字
    "减": "減",  # 减 不是繁體字
    "凉": "涼",  # 凉 是 涼 的異體字
    "沈": "瀋",  # 沈(surname) 也存在但瀋(Shenyang) 是主要用法
    "涂": "塗",  # 塗 是標準
    "範": "範",  # 範(surname) 也存在但範 是標準
    "強": "強",  # 強 是 強 的異體
    "侠": "俠",  # 侠 不是繁體字
    "岩": "巖",  # 巖 是標準
    "庄": "莊",  # 莊 是標準
    "彦": "彥",  # 彥 是標準
    "恒": "恆",  # 恆 是標準
    "晋": "晉",  # 晉 是標準
    "晒": "曬",  # 曬 是標準
    "栖": "棲",  # 棲 是標準
    "梦": "夢",  # 夢 是標準
    "渊": "淵",  # 淵 是標準
    "温": "溫",  # 溫 是標準
    "滚": "滾",  # 滾 是標準
    "皱": "皺",  # 皺 是標準
    "礙": "礙",  # 礙 是標準
    "窝": "窩",  # 窩 是標準
    "篱": "籬",  # 籬 是標準
    "絕": "絕",  # 絕 是標準（絶 是異體）
    "绿": "綠",  # 綠 是標準
    "罢": "罷",  # 罷 是標準
    "勝": "勝",  # 勝 不是繁體字
    "脉": "脈",  # 脈 是標準
    "蘇": "蘇",  # 蘇 是標準
    "苹": "蘋",  # 蘋 是標準
    "荐": "薦",  # 薦 是標準
    "荡": "蕩",  # 蕩 是標準（盪 由詞庫處理）
    "獲": "獲",  # 獲 是標準（穫 是罕用）
    "虫": "蟲",  # 虫 在繁體中幾乎不單用
    "蚕": "蠶",  # 蠶 是標準（蠺 也存在）
    "蜡": "蠟",  # 蠟 是標準
    "迹": "跡",  # 跡 和 蹟 都用，跡 較標準
    "靜": "靜",  # 靜 是標準
    "須": "須",  # 須 是標準（鬚 由詞庫處理）
    "韵": "韻",  # 韻 是標準
    "饥": "飢",  # 飢 是標準
    "黃": "黃",  # 黃 是標準
}


def download_unihan() -> bytes:
    """下載 Unihan.zip。"""
    print("📥 下載 Unicode Unihan 資料庫...")
    with urlopen(UNIHAN_URL) as resp:
        data = resp.read()
    print(f"   下載完成 ({len(data) / 1024 / 1024:.1f} MB)")
    return data


def parse_unihan_variants(zip_data: bytes) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    """
    解析 Unihan_Variants.txt，提取 kTraditionalVariant 和 kSimplifiedVariant。

    Returns:
        (traditional_map, simplified_map)
        traditional_map: {simplified_char: [traditional_chars]}
        simplified_map: {traditional_char: [simplified_chars]}
    """
    traditional_map: dict[str, list[str]] = {}
    simplified_map: dict[str, list[str]] = {}

    with zipfile.ZipFile(io.BytesIO(zip_data)) as zf:
        # 找到 Unihan_Variants.txt
        variant_files = [n for n in zf.namelist() if "Variants" in n]
        if not variant_files:
            raise FileNotFoundError("Unihan_Variants.txt not found in archive")

        with zf.open(variant_files[0]) as f:
            for raw_line in f:
                line = raw_line.decode("utf-8").strip()
                if not line or line.startswith("#"):
                    continue

                parts = line.split("\t")
                if len(parts) < 3:
                    continue

                codepoint_str, field, values_str = parts[0], parts[1], parts[2]

                # 解析 Unicode codepoint (U+XXXX)
                char = chr(int(codepoint_str.replace("U+", ""), 16))

                # 解析目標字元清單
                targets = []
                for val in values_str.split():
                    if val.startswith("U+"):
                        # 去除可能的附加標記（如 U+4E94<kMatthews）
                        hex_str = val[2:]  # 移除 "U+"
                        # 只取純十六進位部分
                        clean_hex = ""
                        for c in hex_str:
                            if c in "0123456789ABCDEFabcdef":
                                clean_hex += c
                            else:
                                break
                        if clean_hex:
                            targets.append(chr(int(clean_hex, 16)))

                if not targets:
                    continue

                if field == "kTraditionalVariant":
                    traditional_map[char] = targets
                elif field == "kSimplifiedVariant":
                    simplified_map[char] = targets

    return traditional_map, simplified_map


def load_existing_term_chars() -> set[str]:
    """載入現有詞庫中所有涉及的簡體單字對映，用於交叉比對。"""
    chars = set()
    for source_dir in ["cn", "hk"]:
        src_path = TERMS_DIR / source_dir
        if not src_path.exists():
            continue
        for json_file in src_path.glob("*.json"):
            try:
                with open(json_file, encoding="utf-8") as f:
                    data = json.load(f)
                terms = data.get("terms", data)
                for source_term in terms:
                    if source_term.startswith("_"):
                        continue
                    # 記錄所有單字的來源字
                    if len(source_term) == 1:
                        chars.add(source_term)
            except (json.JSONDecodeError, KeyError):
                continue
    return chars


def generate_charmap(
    traditional_map: dict[str, list[str]],
    simplified_map: dict[str, list[str]],
) -> tuple[dict[str, str], list[str]]:
    """
    從 Unihan 資料生成安全的一對一對映。

    策略：
    1. 只取 kTraditionalVariant 恰好有 1 個目標的字（一對一）
    2. 排除自身對映（簡體 == 繁體）
    3. 排除一對多的歧義字

    Returns:
        (safe_chars, ambiguous_excluded)
    """
    safe_chars: dict[str, str] = {}
    ambiguous_excluded: list[str] = []

    for simplified, traditional_list in sorted(traditional_map.items()):
        # Step 1: 人工強制排除（Unihan 說一對一但實際有語義歧義）
        if simplified in FORCE_EXCLUDE:
            ambiguous_excluded.append(simplified)
            continue

        # Step 2: 人工強制包含（Unihan 說一對多但實際有明確標準）
        if simplified in FORCE_INCLUDE:
            safe_chars[simplified] = FORCE_INCLUDE[simplified]
            continue

        # Step 3: 過濾掉自身引用（Unihan 常把字元本身也列為 variant）
        real_targets = [t for t in traditional_list if t != simplified]

        if not real_targets:
            # 所有 variant 都是自身 → 無差異，跳過
            continue
        elif len(real_targets) == 1:
            # 一對一安全對映
            safe_chars[simplified] = real_targets[0]
        else:
            # 一對多歧義字（去除自身後仍有多個）
            ambiguous_excluded.append(simplified)

    # 按 Unicode 碼位排序
    safe_chars = dict(sorted(safe_chars.items(), key=lambda x: ord(x[0])))
    ambiguous_excluded.sort(key=ord)

    return safe_chars, ambiguous_excluded


def print_report(
    safe_chars: dict[str, str],
    ambiguous: list[str],
    traditional_map: dict[str, list[str]],
    existing_single_chars: set[str],
) -> None:
    """列印審核報告。"""
    print("\n" + "=" * 60)
    print("📊 字元對映生成報告")
    print("=" * 60)

    print(f"\n✅ 安全一對一對映: {len(safe_chars)} 個")
    print(f"⚠️  一對多歧義字:   {len(ambiguous)} 個")
    print(f"📚 現有詞庫單字:   {len(existing_single_chars)} 個")

    # 新增字元（不在現有詞庫中的）
    new_chars = {k for k in safe_chars if k not in existing_single_chars}
    overlap_chars = {k for k in safe_chars if k in existing_single_chars}
    print(f"\n🆕 新增字元（現有詞庫未覆蓋）: {len(new_chars)} 個")
    print(f"🔄 重疊字元（現有詞庫已有）:   {len(overlap_chars)} 個")

    print(f"\n{'─' * 60}")
    print("⚠️  一對多歧義字清單（已排除，由詞庫層處理）：")
    print("─" * 60)
    for char in ambiguous:
        targets = traditional_map.get(char, [])
        targets_str = "/".join(targets)
        print(f"  {char} → {targets_str}")

    print(f"\n{'─' * 60}")
    print("🆕 新增字元範例（前 50 個）：")
    print("─" * 60)
    for i, (s, t) in enumerate(safe_chars.items()):
        if s not in existing_single_chars:
            print(f"  {s} → {t}", end="")
            if (i + 1) % 8 == 0:
                print()
        if i >= 50:
            print("\n  ...")
            break
    print()


def main():
    parser = argparse.ArgumentParser(description="生成安全的簡繁字元對映表")
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"輸出 JSON 路徑 (預設: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--report",
        "-r",
        action="store_true",
        help="顯示詳細審核報告",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只分析，不寫入檔案",
    )
    args = parser.parse_args()

    # 1. 下載 Unihan 資料
    zip_data = download_unihan()

    # 2. 解析
    print("🔍 解析 Unihan_Variants.txt...")
    traditional_map, simplified_map = parse_unihan_variants(zip_data)
    print(f"   kTraditionalVariant: {len(traditional_map)} 筆")
    print(f"   kSimplifiedVariant:  {len(simplified_map)} 筆")

    # 3. 生成對映
    print("⚙️  生成安全對映表...")
    safe_chars, ambiguous = generate_charmap(traditional_map, simplified_map)

    # 4. 載入現有詞庫比對
    existing = load_existing_term_chars()

    # 5. 報告
    if args.report:
        print_report(safe_chars, ambiguous, traditional_map, existing)

    print("\n📊 總結:")
    print(f"   安全一對一對映: {len(safe_chars)} 個")
    print(f"   一對多歧義字:   {len(ambiguous)} 個（已排除）")
    total = len(safe_chars) + len(ambiguous)
    pct = total / max(len(traditional_map), 1) * 100
    print(f"   覆蓋率:         {total} / {len(traditional_map)} ({pct:.1f}%)")

    # 6. 寫入
    if not args.dry_run:
        output_data = {
            "version": "1.0",
            "description": "安全一對一簡繁字元對映（排除一對多歧義字）",
            "source": "Unicode Unihan kTraditionalVariant（自動生成 + 人工審核）",
            "stats": {
                "safe_chars": len(safe_chars),
                "ambiguous_excluded": len(ambiguous),
                "unihan_total": len(traditional_map),
            },
            "ambiguous_excluded": ambiguous,
            "chars": safe_chars,
        }

        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)

        print(f"\n✅ 已寫入: {args.output}")
        print(f"   檔案大小: {args.output.stat().st_size / 1024:.1f} KB")
    else:
        print("\n⏭️  Dry-run 模式，未寫入檔案")

    return 0


if __name__ == "__main__":
    sys.exit(main())
