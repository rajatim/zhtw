#!/usr/bin/env python3
"""
從 Unicode Unihan 資料庫生成安全的一對一簡繁字元映射表。

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
# 例如：后 是 後 的簡化字，但「后」（皇后）在繁體中也存在。
FORCE_EXCLUDE = {
    "后",  # 後(behind) vs 后(empress)
    "面",  # 麵(noodle) vs 面(face)
    "咸",  # 鹹(salty) vs 咸(all)
    "冬",  # 鼕(drum sound) vs 冬(winter)
    "朱",  # 硃(cinnabar) vs 朱(vermilion)
    "余",  # 餘(remaining) vs 余(I, archaic)
    "谷",  # 穀(grain) vs 谷(valley)
    "丰",  # 豐(abundant) vs 丰(graceful)
    "丑",  # 醜(ugly) vs 丑(earthly branch)
    "斗",  # 鬥(fight) vs 斗(dipper)
    "几",  # 幾(how many) vs 几(small table)
    "卜",  # 蔔(radish) vs 卜(divination)
    "仆",  # 僕(servant) vs 仆(fall forward)
    "了",  # 瞭(understand) vs 了(particle)
    "千",  # 韆(swing) vs 千(thousand)
    "才",  # 纔(just now) vs 才(talent)
    "出",  # 齣(act of play) vs 出(exit)
    "曲",  # 麯(yeast) vs 曲(song/curve)
    "克",  # 剋(overcome) vs 克(gram)
    "奸",  # 姦(adultery) vs 奸(treacherous)
    "征",  # 徵(levy/sign) vs 征(expedition)
    "折",  # 摺(fold) vs 折(break)
    "采",  # 採(pick) vs 采(style)
    "志",  # 誌(record) vs 志(ambition)
    "注",  # 註(note) vs 注(pour)
    "制",  # 製(manufacture) vs 制(system)
    "准",  # 準(standard) vs 准(approve)
    "布",  # 佈(spread) vs 布(cloth)
    "板",  # 闆(boss) vs 板(board)
    "松",  # 鬆(loose) vs 松(pine)
    "表",  # 錶(watch) vs 表(table/surface)
    "舍",  # 捨(abandon) vs 舍(house)
    "别",  # 彆(awkward) vs 別(separate)
    "向",  # 嚮(towards) vs 向(direction)
    "回",  # 迴(detour) vs 回(return)
    "困",  # 睏(sleepy) vs 困(trapped)
    "吊",  # 弔(condole) vs 吊(hang)
    "冲",  # 衝(rush) vs 沖(rinse)
    "御",  # 禦(defend) vs 御(royal)
    "借",  # 藉(by means of) vs 借(borrow)
    "划",  # 劃(plan) vs 划(row boat)
    "占",  # 佔(occupy) vs 占(divine)
    "游",  # 遊(travel) vs 游(swim)
    "辟",  # 闢(open) vs 辟(king's order)
    "朴",  # 樸(simple) vs 朴(a surname/tree)
    "家",  # 傢(furniture) vs 家(home)
    "致",  # 緻(fine) vs 致(cause)
    "栗",  # 慄(tremble) vs 栗(chestnut)
    "杰",  # 傑(outstanding) vs 杰(hero)
    "卷",  # 捲(roll) vs 卷(scroll)
    "秋",  # 鞦(swing) vs 秋(autumn)
    "帘",  # 簾(curtain) vs 帘(wine shop sign)
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
    "说": "說",  # 説 是 說 的異體字，說 是標準
    "为": "為",  # 爲 是 為 的異體字
    "两": "兩",  # 两 不是繁體字
    "个": "個",  # 个 不是繁體字
    "产": "產",  # 産 是 產 的異體字
    "义": "義",  # 义 不是繁體字
    "乐": "樂",  # 乐 不是繁體字
    "乱": "亂",  # 乱 不是繁體字
    "争": "爭",  # 争 不是繁體字
    "亏": "虧",  # 亏 不是繁體字
    "云": "雲",  # 云(to say) 在現代中文幾乎不用
    "仅": "僅",  # 仅 不是繁體字
    "从": "從",  # 从 不是繁體字
    "仪": "儀",  # 仪 不是繁體字
    "价": "價",  # 价 不是繁體字
    "优": "優",  # 优 不是繁體字
    "会": "會",  # 会 不是繁體字
    "伤": "傷",  # 伤 不是繁體字
    "体": "體",  # 体 不是繁體字
    "单": "單",  # 单 不是繁體字
    "儿": "兒",  # 儿 不是繁體字
    "内": "內",  # 内 是 內 的異體字，內 是標準
    "凤": "鳳",  # 凤 不是繁體字
    "凭": "憑",  # 凭 不是繁體字
    "刘": "劉",  # 刘 不是繁體字
    "创": "創",  # 创 不是繁體字
    "删": "刪",  # 删 不是繁體字
    "动": "動",  # 动 不是繁體字
    "劝": "勸",  # 劝 不是繁體字
    "办": "辦",  # 办 不是繁體字
    "励": "勵",  # 励 不是繁體字
    "劳": "勞",  # 劳 不是繁體字
    "势": "勢",  # 势 不是繁體字
    "区": "區",  # 区 不是繁體字
    "医": "醫",  # 医 不是繁體字
    "号": "號",  # 号 不是繁體字
    "听": "聽",  # 听 不是繁體字
    "吓": "嚇",  # 吓 不是繁體字
    "图": "圖",  # 图 不是繁體字
    "坏": "壞",  # 坏 不是繁體字
    "块": "塊",  # 块 不是繁體字
    "壮": "壯",  # 壮 不是繁體字
    "声": "聲",  # 声 不是繁體字
    "头": "頭",  # 头 不是繁體字
    "夸": "誇",  # 夸 不是繁體字（夸父的夸用法極罕）
    "宁": "寧",  # 宁 不是繁體字
    "宝": "寶",  # 宝 不是繁體字
    "实": "實",  # 实 不是繁體字
    "对": "對",  # 对 不是繁體字
    "宾": "賓",  # 宾 不是繁體字
    "尔": "爾",  # 尔 不是繁體字
    "尽": "盡",  # 「儘」是「盡」的用法分化，盡 是主體
    "届": "屆",  # 届 不是繁體字
    "属": "屬",  # 属 不是繁體字
    "岁": "歲",  # 岁 不是繁體字
    "师": "師",  # 师 不是繁體字
    "帮": "幫",  # 帮 不是繁體字
    "广": "廣",  # 广(shelter) 幾乎不用
    "应": "應",  # 应 不是繁體字
    "庙": "廟",  # 庙 不是繁體字
    "开": "開",  # 开 不是繁體字
    "弃": "棄",  # 弃 不是繁體字
    "弯": "彎",  # 弯 不是繁體字
    "弹": "彈",  # 弹 不是繁體字
    "归": "歸",  # 归 不是繁體字
    "录": "錄",  # 录 不是繁體字
    "怀": "懷",  # 怀 不是繁體字
    "怜": "憐",  # 怜 不是繁體字
    "恋": "戀",  # 恋 不是繁體字
    "恶": "惡",  # 噁 是口語用法
    "恼": "惱",  # 恼 不是繁體字
    "惧": "懼",  # 惧 不是繁體字
    "惩": "懲",  # 惩 不是繁體字
    "愿": "願",  # 愿 不是繁體字
    "戏": "戲",  # 戏 不是繁體字
    "战": "戰",  # 战 不是繁體字
    "户": "戶",  # 户 是 戶 的異體字
    "执": "執",  # 执 不是繁體字
    "扑": "撲",  # 扑 不是繁體字
    "报": "報",  # 报 不是繁體字
    "担": "擔",  # 担 不是繁體字
    "挡": "擋",  # 挡 不是繁體字
    "据": "據",  # 据 不是繁體字
    "掷": "擲",  # 掷 不是繁體字
    "携": "攜",  # 携 不是繁體字
    "摊": "攤",  # 摊 不是繁體字
    "数": "數",  # 数 不是繁體字
    "无": "無",  # 无 不是繁體字
    "时": "時",  # 时 不是繁體字
    "机": "機",  # 机 不是繁體字
    "权": "權",  # 权 不是繁體字
    "极": "極",  # 极 不是繁體字
    "构": "構",  # 构 不是繁體字
    "标": "標",  # 标 不是繁體字
    "楼": "樓",  # 楼 不是繁體字
    "欢": "歡",  # 欢 不是繁體字
    "气": "氣",  # 气 不是繁體字
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
    "点": "點",  # 点 不是繁體字
    "烛": "燭",  # 烛 不是繁體字
    "热": "熱",  # 热 不是繁體字
    "犹": "猶",  # 犹 不是繁體字
    "独": "獨",  # 独 不是繁體字
    "猪": "豬",  # 猪 不是繁體字
    "猫": "貓",  # 猫 不是繁體字
    "献": "獻",  # 献 不是繁體字
    "环": "環",  # 环 不是繁體字
    "琼": "瓊",  # 琼 不是繁體字
    "电": "電",  # 电 不是繁體字
    "画": "畫",  # 画 不是繁體字
    "确": "確",  # 确 不是繁體字
    "礼": "禮",  # 礼 不是繁體字
    "种": "種",  # 种 不是繁體字
    "称": "稱",  # 称 不是繁體字
    "稳": "穩",  # 稳 不是繁體字
    "穷": "窮",  # 穷 不是繁體字
    "窃": "竊",  # 窃 不是繁體字
    "笔": "筆",  # 笔 不是繁體字
    "线": "線",  # 綫 是異體
    "网": "網",  # 网 不是繁體字
    "罗": "羅",  # 罗 不是繁體字
    "职": "職",  # 职 不是繁體字
    "联": "聯",  # 联 不是繁體字
    "胆": "膽",  # 胆 不是繁體字
    "脚": "腳",  # 脚 不是繁體字（脚 是 腳 的俗字）
    "脏": "髒",  # 臟(organ) 由詞庫層處理
    "艳": "艷",  # 艳 不是繁體字
    "芦": "蘆",  # 芦 不是繁體字
    "荣": "榮",  # 荣 不是繁體字
    "药": "藥",  # 葯 是罕用異體
    "萝": "蘿",  # 萝 不是繁體字
    "蛮": "蠻",  # 蛮 不是繁體字
    "补": "補",  # 补 不是繁體字
    "誉": "譽",  # 誉 不是繁體字
    "辞": "辭",  # 辞 不是繁體字
    "边": "邊",  # 边 不是繁體字
    "迁": "遷",  # 迁 不是繁體字
    "过": "過",  # 过 不是繁體字
    "还": "還",  # 还 不是繁體字
    "这": "這",  # 这 不是繁體字
    "远": "遠",  # 远 不是繁體字
    "适": "適",  # 适 不是繁體字
    "选": "選",  # 选 不是繁體字
    "递": "遞",  # 递 不是繁體字
    "逻": "邏",  # 逻 不是繁體字
    "郑": "鄭",  # 郑 不是繁體字
    "际": "際",  # 际 不是繁體字
    "随": "隨",  # 随 不是繁體字
    "隐": "隱",  # 隐 不是繁體字
    "隶": "隸",  # 隶 不是繁體字
    "难": "難",  # 难 不是繁體字
    "风": "風",  # 风 不是繁體字
    "骂": "罵",  # 骂 不是繁體字
    "龟": "龜",  # 龟 不是繁體字
    "党": "黨",  # 党 不是繁體字
    "厂": "廠",  # 广 的同類
    "历": "歷",  # 曆(calendar) 由詞庫處理
    "厉": "厲",  # 厉 不是繁體字
    "压": "壓",  # 压 不是繁體字
    "厕": "廁",  # 厕 不是繁體字
    "厨": "廚",  # 厨 不是繁體字
    "双": "雙",  # 双 不是繁體字
    "叶": "葉",  # 叶 不是繁體字
    "吴": "吳",  # 吴 不是繁體字
    "园": "園",  # 园 不是繁體字
    "墙": "牆",  # 牆 是標準
    "壳": "殼",  # 殼 是標準
    "够": "夠",  # 够 不是繁體字
    "孙": "孫",  # 孙 不是繁體字
    "姜": "薑",  # 姜(surname) 幾乎只在姓名用，薑 是標準
    "娇": "嬌",  # 娇 不是繁體字
    "层": "層",  # 层 不是繁體字
    "当": "當",  # 噹 由詞庫處理
    "发": "發",  # 髮 由詞庫處理（头发→頭髮）
    "盖": "蓋",  # 盖 不是繁體字
    "着": "著",  # 着 是 著 的俗寫
    "矫": "矯",  # 矫 不是繁體字
    "粮": "糧",  # 粮 不是繁體字
    # 繁: identity → 不加入映射（跳過）
    # 累: 纍 是異體，累 在繁體中通用 → 不加入映射（跳過）
    "剧": "劇",  # 剧 不是繁體字
    "郁": "鬱",  # 鬱 是標準
    "霉": "黴",  # 黴 是標準
    "烟": "煙",  # 菸 由詞庫處理
    "签": "簽",  # 籤 由詞庫處理
    "叙": "敘",  # 叙 不是繁體字
    "叠": "疊",  # 叠 不是繁體字
    "减": "減",  # 减 不是繁體字
    "凉": "涼",  # 凉 是 涼 的異體字
    "沈": "瀋",  # 沈(surname) 也存在但瀋(Shenyang) 是主要用法
    "涂": "塗",  # 塗 是標準
    "范": "範",  # 范(surname) 也存在但範 是標準
    "强": "強",  # 强 是 強 的異體
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
    "碍": "礙",  # 礙 是標準
    "窝": "窩",  # 窩 是標準
    "篱": "籬",  # 籬 是標準
    "绝": "絕",  # 絕 是標準（絶 是異體）
    "绿": "綠",  # 綠 是標準
    "罢": "罷",  # 罷 是標準
    "胜": "勝",  # 胜 不是繁體字
    "脉": "脈",  # 脈 是標準
    "苏": "蘇",  # 蘇 是標準
    "苹": "蘋",  # 蘋 是標準
    "荐": "薦",  # 薦 是標準
    "荡": "蕩",  # 蕩 是標準（盪 由詞庫處理）
    "获": "獲",  # 獲 是標準（穫 是罕用）
    "虫": "蟲",  # 虫 在繁體中幾乎不單用
    "蚕": "蠶",  # 蠶 是標準（蠺 也存在）
    "蜡": "蠟",  # 蠟 是標準
    "迹": "跡",  # 跡 和 蹟 都用，跡 較標準
    "静": "靜",  # 靜 是標準
    "须": "須",  # 須 是標準（鬚 由詞庫處理）
    "韵": "韻",  # 韻 是標準
    "饥": "飢",  # 飢 是標準
    "黄": "黃",  # 黃 是標準
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

                # 解析目標字元列表
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
    """載入現有詞庫中所有涉及的簡體單字映射，用於交叉比對。"""
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
    從 Unihan 資料生成安全的一對一映射。

    策略：
    1. 只取 kTraditionalVariant 恰好有 1 個目標的字（一對一）
    2. 排除自身映射（簡體 == 繁體）
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
            # 一對一安全映射
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
    print("📊 字元映射生成報告")
    print("=" * 60)

    print(f"\n✅ 安全一對一映射: {len(safe_chars)} 個")
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
    parser = argparse.ArgumentParser(description="生成安全的簡繁字元映射表")
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

    # 3. 生成映射
    print("⚙️  生成安全映射表...")
    safe_chars, ambiguous = generate_charmap(traditional_map, simplified_map)

    # 4. 載入現有詞庫比對
    existing = load_existing_term_chars()

    # 5. 報告
    if args.report:
        print_report(safe_chars, ambiguous, traditional_map, existing)

    print("\n📊 總結:")
    print(f"   安全一對一映射: {len(safe_chars)} 個")
    print(f"   一對多歧義字:   {len(ambiguous)} 個（已排除）")
    total = len(safe_chars) + len(ambiguous)
    pct = total / max(len(traditional_map), 1) * 100
    print(f"   覆蓋率:         {total} / {len(traditional_map)} ({pct:.1f}%)")

    # 6. 寫入
    if not args.dry_run:
        output_data = {
            "version": "1.0",
            "description": "安全一對一簡繁字元映射（排除一對多歧義字）",
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
