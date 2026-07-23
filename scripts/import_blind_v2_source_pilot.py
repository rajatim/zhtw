#!/usr/bin/env python3
# zhtw:disable  # 來源 parser 的簡體錨點不可被轉換
"""Import a pinned Simplified Chinese source as a Blind-v2 input-only pilot."""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import re
import sys
import tarfile
import unicodedata
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker
from pypdf import PdfReader

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.benchmark_metrics import canonical_json_bytes  # noqa: E402
from scripts.import_ud_gsd_benchmark import parse_conllu  # noqa: E402
from scripts.validate_permissioned_user_reports import validate_collection  # noqa: E402

ACCURACY_ROOT = PROJECT_ROOT / "benchmarks" / "accuracy"
PILOT_SCHEMA = ACCURACY_ROOT / "blind-v2.source-pilot.schema.json"
PROJECT_SOURCE_SCHEMA = ACCURACY_ROOT / "blind-v2.project-original-source.schema.json"
SUPPORTED_SOURCES = {
    "flores-200-zho-hans-v1": "flores",
    "ud-chinese-cfl-v1": "ud_cfl",
    "cdc-stacks-111808-v1": "cdc_pdf",
    "cdc-stacks-120024-v1": "cdc_pdf",
    "cdc-stacks-116683-v1": "cdc_pdf",
    "zhtw-project-ui-i18n-v1": "project_original_json",
    "zhtw-project-llm-product-v1": "project_original_json",
    "zhtw-project-it-api-cli-v1": "project_original_json",
    "zhtw-project-formal-llm-semantic-v1": "project_original_json",
    "massive-1-0-zh-cn-v1": "massive",
    "ftc-small-business-simplified-v1": "ftc_pdf",
    "ftc-heads-up-simplified-v1": "ftc_heads_up_pdf",
    "nps-essential-acadia-simplified-v1": "nps_acadia_html",
    "ready-gov-floods-zh-hans-v1": "ready_gov_html",
    "ready-gov-hurricanes-zh-hans-v1": "ready_gov_html",
    "ready-gov-earthquakes-zh-hans-v1": "ready_gov_html",
    "osha-electrical-safety-simplified-v1": "osha_pdf",
    "osha-chainsaw-safety-simplified-v1": "osha_pdf",
    "osha-work-zone-traffic-simplified-v1": "osha_pdf",
    "osha-disaster-falls-simplified-v1": "osha_pdf",
    "osha-small-business-consultation-simplified-v1": "osha_pdf",
    "osha-disaster-cleanup-simplified-v1": "osha_pdf",
    "osha-fallen-workers-family-simplified-v1": "osha_pdf",
    "vscode-loc-zh-hans-v1": "vscode_loc_json",
}
READY_GOV_SOURCE_ANCHORS = {
    "ready-gov-floods-zh-hans-v1": ("洪水", "10/22/2025"),
    "ready-gov-hurricanes-zh-hans-v1": ("飓风", "07/09/2026"),
    "ready-gov-earthquakes-zh-hans-v1": ("地震", "10/22/2025"),
}
OSHA_SOURCE_CONFIG = {
    "osha-electrical-safety-simplified-v1": (2, (2,), "用电安全指南"),
    "osha-chainsaw-safety-simplified-v1": (2, (2,), "链锯安全指南"),
    "osha-work-zone-traffic-simplified-v1": (2, (2,), "作业区交通安全指南"),
    "osha-disaster-falls-simplified-v1": (2, (2,), "避免滑倒、绊倒和跌倒"),
    "osha-small-business-consultation-simplified-v1": (
        2,
        (1, 2),
        "小型企业可信赖的安全及健康建议",
    ),
    "osha-disaster-cleanup-simplified-v1": (
        2,
        (1, 2),
        "在灾后清理以及重建时确保工人安全",
    ),
    "osha-fallen-workers-family-simplified-v1": (2, (1, 2), "亲人在工作中离世"),
}
OSHA_IGNORED_LINES = {
    "速览卡",
    "用电安全指南",
    "链锯安全指南",
    "启动链锯之前",
    "为链锯加油",
    "作业区交通安全指南",
    "救灾期间保护救援人员",
    "避免滑倒、绊倒和跌倒",
    "防止滑倒、绊倒和跌倒的方法",
    "请牢记",
    "小型企业可信赖的安全及健康建议",
    "现场咨询项目",
    "请求咨询的好处",
    "节省资金",
    "调动劳动力",
    "告诉我们您的安全顾虑 — 咨询会帮您找出解决方案",
    "方式",
    "咨询访问是什么样的呢?",
    "初次会议",
    "详解",
    "结束会议以及后续跟进",
    "纠正安全隐患",
    "顾问是谁?",
    "请求服务",
    "亲人在工作",
    "中离世",
    "联系方式",
    "记住...",
    "帮助你应对哀伤情绪的建议:",
    "向牺牲的员工致敬",
    "家庭资源",
    "机构组织",
    "联系您的区域OSHA办公室",
    "你不是孤单的那个人",
    "须知和期望",
    "索取检查档案",
}


def sha256_bytes(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON must be an object")
    return value


def normalize_input(text: str) -> str:
    return " ".join(unicodedata.normalize("NFC", text).split())


def read_raw_source(manifest: dict[str, Any], source_file: Path | None = None) -> tuple[str, bytes]:
    raw_sha256 = manifest["raw_sha256"]
    markers = {
        "flores-200-zho-hans-v1": "flores200_dataset.tar.gz",
        "ud-chinese-cfl-v1": "zh_cfl-ud-test.conllu",
        "vscode-loc-zh-hans-v1": "main.i18n.json",
    }
    marker = markers.get(manifest["id"])
    data_urls = [url for url in raw_sha256 if marker and url.endswith(marker)]
    if not data_urls and len(raw_sha256) == 1:
        data_urls = list(raw_sha256)
    if len(data_urls) != 1:
        raise ValueError("source pilot manifest must identify exactly one source data file")
    data_url = data_urls[0]
    data_content: bytes | None = None
    for url, expected_hash in raw_sha256.items():
        if source_file is not None:
            if url != data_url:
                continue
            content = source_file.read_bytes()
        else:
            if "://" in url:
                request = urllib.request.Request(
                    url,
                    headers={
                        "User-Agent": (
                            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                            "AppleWebKit/537.36 Chrome/136.0 Safari/537.36"
                        )
                    },
                )
                with urllib.request.urlopen(request, timeout=120) as response:
                    content = response.read()
            else:
                source_path = (PROJECT_ROOT / url).resolve()
                try:
                    source_path.relative_to(PROJECT_ROOT)
                except ValueError as exc:
                    raise ValueError(f"raw source path escapes project root: {url}") from exc
                content = source_path.read_bytes()
        actual_hash = sha256_bytes(content)
        if actual_hash != expected_hash:
            raise ValueError(f"raw sha256 mismatch for {url}: {actual_hash}")
        if url == data_url:
            data_content = content
    if data_content is None:
        raise ValueError("source data file was not read")
    return data_url, data_content


def parse_flores(content: bytes) -> list[tuple[str, str, str]]:
    rows: list[tuple[str, str, str]] = []
    members = (
        ("dev", "./flores200_dataset/dev/zho_Hans.dev"),
        ("devtest", "./flores200_dataset/devtest/zho_Hans.devtest"),
    )
    with tarfile.open(fileobj=io.BytesIO(content), mode="r:gz") as archive:
        for split, member_name in members:
            member = archive.getmember(member_name)
            extracted = archive.extractfile(member)
            if extracted is None:
                raise ValueError(f"FLORES archive member is not a file: {member_name}")
            lines = extracted.read().decode("utf-8").splitlines()
            rows.extend(
                (split, f"{split}-{index:04d}", text) for index, text in enumerate(lines, 1)
            )
    return rows


def parse_ud_cfl(content: bytes) -> list[tuple[str, str, str]]:
    sentences = parse_conllu(content.decode("utf-8"), source="UD Chinese-CFL")
    return [("test", sent_id, sentence.text) for sent_id, sentence in sorted(sentences.items())]


def parse_massive(content: bytes) -> list[tuple[str, str, str]]:
    member_name = "1.0/data/zh-CN.jsonl"
    with tarfile.open(fileobj=io.BytesIO(content), mode="r:gz") as archive:
        extracted = archive.extractfile(member_name)
        if extracted is None:
            raise ValueError(f"MASSIVE archive member is not a file: {member_name}")
        lines = extracted.read().decode("utf-8").splitlines()

    rows: list[tuple[str, str, str]] = []
    seen_ids: set[str] = set()
    for line_number, line in enumerate(lines, 1):
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"MASSIVE line {line_number}: invalid JSON") from exc
        if not isinstance(row, dict):
            raise ValueError(f"MASSIVE line {line_number}: row must be an object")
        source_case_id = row.get("id")
        partition = row.get("partition")
        utterance = row.get("utt")
        if (
            not isinstance(source_case_id, str)
            or not isinstance(utterance, str)
            or partition not in {"train", "dev", "test"}
            or row.get("locale") != "zh-CN"
        ):
            raise ValueError(f"MASSIVE line {line_number}: invalid required fields")
        if source_case_id in seen_ids:
            raise ValueError(f"MASSIVE line {line_number}: duplicate id {source_case_id}")
        seen_ids.add(source_case_id)
        rows.append((partition, source_case_id, utterance))
    return rows


def parse_vscode_loc(content: bytes) -> list[tuple[str, str, str]]:
    """Extract stable input-only UI strings from the pinned VS Code language pack."""
    try:
        source = json.loads(content)
    except json.JSONDecodeError as exc:
        raise ValueError("VS Code localization source is not valid JSON") from exc
    if not isinstance(source, dict) or set(source) != {"", "contents", "version"}:
        raise ValueError("VS Code localization source has unexpected root fields")
    metadata = source[""]
    if (
        source["version"] != "1.0.0"
        or not isinstance(metadata, list)
        or not all(isinstance(line, str) for line in metadata)
        or "Copyright (c) Microsoft Corporation. All rights reserved." not in metadata
        or "Do not edit this file. It is machine generated." not in metadata
    ):
        raise ValueError("VS Code localization source has unexpected metadata")
    contents = source["contents"]
    if not isinstance(contents, dict):
        raise ValueError("VS Code localization contents must be an object")

    rows: list[tuple[str, str, str]] = []
    seen_ids: set[str] = set()
    for module_name in sorted(contents):
        messages = contents[module_name]
        if not isinstance(module_name, str) or not isinstance(messages, dict):
            raise ValueError("VS Code localization module must be a string/object pair")
        for message_key in sorted(messages):
            raw_text = messages[message_key]
            if not isinstance(message_key, str) or not isinstance(raw_text, str):
                raise ValueError("VS Code localization message must be a string/string pair")
            text = normalize_input(raw_text)
            han_count = len(re.findall(r"[\u3400-\u9fff]", text))
            if (
                "\n" in raw_text
                or not 4 <= len(text) <= 240
                or han_count < 2
                or re.search(r"(?:https?://|www\.|[\w.+-]+@[\w.-]+)", text, re.I)
                or re.search(r"(?:`|<[^>]+>|\[[^]]+]\([^)]*\))", text)
                or not re.sub(r"\{\d+\}", "", text).strip(" ()[]{}，。！？、：；,.!?:;-/")
            ):
                continue
            source_key = f"{module_name}\0{message_key}"
            source_case_id = "entry-" + hashlib.sha256(source_key.encode()).hexdigest()[:16]
            if source_case_id in seen_ids:
                raise ValueError(f"VS Code localization source ID collision: {source_case_id}")
            seen_ids.add(source_case_id)
            rows.append(("language_pack", source_case_id, text))
    return rows


def normalize_pdf_text(text: str) -> str:
    """Collapse PDF layout whitespace without changing Chinese wording."""
    text = unicodedata.normalize("NFC", text).replace("\xa0", " ")
    text = " ".join(text.split())
    cjk = "\u3400-\u9fff"
    punctuation = "，。！？、：；（）《》“”"
    text = re.sub(rf"(?<=[{cjk}{punctuation}]) +(?=[{cjk}{punctuation}])", "", text)
    text = re.sub(r" +(?=[，。！？、：；）])", "", text)
    text = re.sub(r"(?<=（) +", "", text)
    return re.sub(r"(?<=\d) +(?=\d)", "", text)


def complete_chinese_sentences(text: str, *, minimum_length: int = 4) -> list[str]:
    sentences = []
    for match in re.finditer(r"[^。！？]*[。！？]", normalize_pdf_text(text)):
        sentence = match.group().strip(" •\t")
        if len(sentence) >= minimum_length and re.search(r"[\u3400-\u9fff]", sentence):
            sentences.append(sentence)
    return sentences


def anchored_region(text: str, start: str, end: str | None = None) -> str:
    normalized = normalize_pdf_text(text)
    start_index = normalized.find(start)
    if start_index < 0:
        raise ValueError(f"CDC PDF extraction anchor not found: {start!r}")
    if end is None:
        return normalized[start_index:]
    end_index = normalized.find(end, start_index)
    if end_index < 0:
        raise ValueError(f"CDC PDF extraction anchor not found: {end!r}")
    return normalized[start_index:end_index]


def parse_cdc_pages(source_id: str, pages: list[str]) -> list[tuple[str, str, str]]:
    """Extract conservative, complete sentences from verified CDC Stacks PDFs."""
    selected: list[tuple[int, str]] = []
    if source_id == "cdc-stacks-111808-v1":
        if len(pages) != 2:
            raise ValueError(f"{source_id}: expected 2 PDF pages, found {len(pages)}")
        selected = [
            (1, anchored_region(pages[0], "佩戴口罩。", "可访问版本")),
            (2, anchored_region(pages[1], "请勿与家里的其他人共用", "如果某人出现")),
            (2, anchored_region(pages[1], "呼吸困难。")),
        ]
    elif source_id == "cdc-stacks-120024-v1":
        if len(pages) != 7:
            raise ValueError(f"{source_id}: expected 7 PDF pages, found {len(pages)}")
        selected = [
            (1, anchored_region(pages[0], "美国疾病控制和预防中心")),
            (2, anchored_region(pages[1], "记得每天用含氟牙膏")),
            (3, anchored_region(pages[2], "保护你的牙齿")),
            (4, anchored_region(pages[3], "记得每天用牙线")),
            (5, anchored_region(pages[4], "你是否能在图片中")),
            (6, anchored_region(pages[5], "你知道你应该")),
            (7, anchored_region(pages[6], "每天刷两次牙！", "以下是我学到的")),
        ]
    elif source_id == "cdc-stacks-116683-v1":
        if len(pages) != 9:
            raise ValueError(f"{source_id}: expected 9 PDF pages, found {len(pages)}")
        selected = [
            (1, anchored_region(pages[0], "实现健康平等", "项目重点")),
            (1, anchored_region(pages[0], "目的：开发", "支持公共卫生")),
            (1, anchored_region(pages[0], "支持公共卫生", "项目介绍：")),
        ]
        for page_number, page in enumerate(pages[2:8], 3):
            normalized = normalize_pdf_text(page)
            for match in re.finditer(r"目的：(.+?)(?=合作伙伴：)", normalized):
                selected.append((page_number, "目的：" + match.group(1)))
    else:
        raise ValueError(f"unsupported CDC Stacks source: {source_id}")

    rows: list[tuple[str, str, str]] = []
    sequence_by_page: Counter[int] = Counter()
    for page_number, region in selected:
        for sentence in complete_chinese_sentences(region):
            if sentence.startswith(("关于", "查阅更多", "请访问")):
                continue
            sequence_by_page[page_number] += 1
            source_case_id = f"p{page_number:02d}-{sequence_by_page[page_number]:03d}"
            rows.append(("document", source_case_id, sentence))
    return rows


def parse_cdc_pdf(source_id: str, content: bytes) -> list[tuple[str, str, str]]:
    reader = PdfReader(io.BytesIO(content))
    pages = [page.extract_text() or "" for page in reader.pages]
    return parse_cdc_pages(source_id, pages)


FTC_SMALL_BUSINESS_HEADINGS = {
    "培训员工",
    "验证支票和付款",
    "甄别技术手段型诈骗",
    "了解和你打交道的对方",
    "伪造的发票和未订购的商品",
    "在线名录和广告诈骗",
    "伪装成企业和政府的诈骗",
    "技术支持型诈骗",
    "社会工程、网络钓鱼和勒索软件",
    "企业辅导型诈骗",
    "变更网络评价",
    "信用卡处理和设备租赁诈骗",
    "虚假支票诈骗",
    "关于 FTC",
}


def parse_ftc_small_business_pages(pages: list[str]) -> list[tuple[str, str, str]]:
    """Extract complete prose sentences from the pinned FTC Simplified booklet."""
    if len(pages) != 10:
        raise ValueError(f"FTC booklet: expected 10 PDF pages, found {len(pages)}")
    if "诈骗与你的小型企业" not in pages[0] or "Federal Trade Commission" in pages[0]:
        raise ValueError("FTC booklet: Simplified Chinese title anchor not found")

    lines: list[str] = []
    for page in pages[1:9]:
        for raw_line in page.splitlines():
            line = raw_line.strip()
            if (
                not line
                or line == "诈骗与你的小型企业: 企业指南"
                or line.isdigit()
                or line.startswith("►")
                or line in FTC_SMALL_BUSINESS_HEADINGS
            ):
                continue
            lines.append(re.sub(r"^[●\s]+", "", line))

    text = " ".join(lines).replace("（千万不要这样做。）", "千万不要这样做。")
    sentences = complete_chinese_sentences(text, minimum_length=8)
    rows: list[tuple[str, str, str]] = []
    for sentence in sentences:
        if re.search(r"(?:https?://|\b[\w.-]+\.(?:gov|org)\b)", sentence, re.I):
            continue
        if re.search(r"\d{3}-\d{3}-\d{4}|按\s*#?\d", sentence):
            continue
        if sentence.startswith(("有关如何", "如需")):
            continue
        rows.append(("booklet", f"sentence-{len(rows) + 1:03d}", sentence))
    return rows


def parse_ftc_small_business_pdf(content: bytes) -> list[tuple[str, str, str]]:
    reader = PdfReader(io.BytesIO(content))
    metadata = reader.metadata
    if metadata is None or metadata.author != "Federal Trade Commission":
        raise ValueError("FTC booklet: unexpected PDF author metadata")
    pages = [page.extract_text() or "" for page in reader.pages]
    return parse_ftc_small_business_pages(pages)


FTC_HEADS_UP_IGNORED_LINES = {
    "谨慎分享",
    "友善为先",
    "防范网络欺凌",
    "保护交流",
    "经过思考后再分享",
    "关注你发贴的人",
    "可能",
    "比你想象的多。",
    "一旦在网上发布内容，",
    "就无法将其收回",
    "关于社交媒体的注意事项",
    "礼貌很重要",
    "不要冒充他人",
    "直言相告",
    "要注意礼仪！",
    "保护自己的隐私",
    "保护自己的信息",
    "保护自己的账户",
    "保护自己的设备",
    "从些步骤着手：",
    "如果有人在网上骚扰你，采取以下做法：",
    "下面的方法用于在网上保护自己的信息：",
}


def parse_ftc_heads_up_pages(pages: list[str]) -> list[tuple[str, str, str]]:
    """Extract complete Chinese prose from the pinned FTC online-safety booklet."""
    if len(pages) != 15:
        raise ValueError(f"FTC Heads Up: expected 15 PDF pages, found {len(pages)}")
    if "要在生活中帮助您的孩子安全上网" not in normalize_pdf_text(pages[1]):
        raise ValueError("FTC Heads Up: Simplified Chinese content anchor not found")
    if "This booklet helps kids socialize safely online" not in pages[14]:
        raise ValueError("FTC Heads Up: English back-cover anchor not found")

    chinese_page_two = pages[1].split("To help kids", 1)[0]
    selected_pages = [chinese_page_two, *pages[2:14]]
    lines: list[str] = []
    for page in selected_pages:
        for raw_line in page.splitlines():
            line = normalize_pdf_text(raw_line)
            if not line or line.isdigit() or line == "?" or line in FTC_HEADS_UP_IGNORED_LINES:
                continue
            lines.append(line)

    text = normalize_pdf_text(" ".join(lines))
    rows: list[tuple[str, str, str]] = []
    for match in re.finditer(r"[^。！？]*[。！？](?:[”」』])?", text):
        sentence = match.group().strip(" •\t")
        if len(sentence) < 8 or not re.search(r"[\u3400-\u9fff]", sentence):
            continue
        if re.search(r"(?:https?://|www\.|\b[\w.-]+\.(?:gov|org)\b)", sentence, re.I):
            continue
        rows.append(("booklet", f"sentence-{len(rows) + 1:03d}", sentence))
    return rows


def parse_ftc_heads_up_pdf(content: bytes) -> list[tuple[str, str, str]]:
    reader = PdfReader(io.BytesIO(content))
    metadata = reader.metadata
    if metadata is None or metadata.author != "Federal Trade Commission":
        raise ValueError("FTC Heads Up: unexpected PDF author metadata")
    pages = [page.extract_text() or "" for page in reader.pages]
    return parse_ftc_heads_up_pages(pages)


def parse_osha_pdf(source_id: str, content: bytes) -> list[tuple[str, str, str]]:
    """Extract input-only sentences from a pinned OSHA Simplified Chinese PDF."""
    expected_pages, selected_pages, title_anchor = OSHA_SOURCE_CONFIG[source_id]
    reader = PdfReader(io.BytesIO(content))
    if len(reader.pages) != expected_pages:
        raise ValueError(
            f"{source_id}: expected {expected_pages} PDF pages, found {len(reader.pages)}"
        )
    metadata = reader.metadata
    if metadata is None or metadata.author not in {None, "OSHA"}:
        raise ValueError(f"{source_id}: unexpected PDF author metadata")

    pages = [page.extract_text() or "" for page in reader.pages]
    selected_text = "\n".join(pages[page_number - 1] for page_number in selected_pages)
    if title_anchor not in normalize_pdf_text(selected_text):
        raise ValueError(f"{source_id}: Simplified Chinese title anchor not found")

    rows: list[tuple[str, str, str]] = []
    for page_number in selected_pages:
        kept_lines = []
        for raw_line in pages[page_number - 1].splitlines():
            if normalize_pdf_text(raw_line) in OSHA_IGNORED_LINES:
                continue
            kept_lines.append(re.sub(r"^\s*(?:[y•●]|[–-](?=\s))\s*", "", raw_line))
        page = "\n".join(kept_lines)
        for sentence in complete_chinese_sentences(page, minimum_length=8):
            if source_id == "osha-small-business-consultation-simplified-v1" and re.search(
                r"(?:EWP|Mark St|ESCO Manufacturing|现场顾问项目合作帮我们|赔偿保险费降低)",
                sentence,
            ):
                continue
            if re.search(
                r"(?:https?://|www\.|\b[\w.-]+\.(?:gov|org)\b|"
                r"[\w.+-]+@[\w.-]+|\(?\d{3}\)?[ -]\d{3}[ -]\d{4}|"
                r"1-800-321-OSHA|\b(?:911|988)\b)",
                sentence,
                re.I,
            ):
                continue
            rows.append(("document", f"sentence-{len(rows) + 1:03d}", sentence))
    return rows


class NpsArticleParagraphParser(HTMLParser):
    """Collect paragraph text only from the NPS article content container."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.div_depth = 0
        self.article_depth: int | None = None
        self.in_paragraph = False
        self.paragraphs: list[str] = []
        self._parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "div":
            self.div_depth += 1
            classes = (attributes.get("class") or "").split()
            if self.article_depth is None and "Article__Content" in classes:
                self.article_depth = self.div_depth
        elif tag == "p" and self.article_depth is not None:
            self.in_paragraph = True
            self._parts = []
        elif tag == "br" and self.in_paragraph:
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag == "p" and self.in_paragraph:
            self.paragraphs.append("".join(self._parts))
            self.in_paragraph = False
            self._parts = []
        elif tag == "div":
            if self.article_depth == self.div_depth:
                self.article_depth = None
            self.div_depth -= 1

    def handle_data(self, data: str) -> None:
        if self.in_paragraph:
            self._parts.append(data)


def parse_nps_acadia_html(content: bytes) -> list[tuple[str, str, str]]:
    """Extract complete prose sentences from the pinned NPS Acadia article."""
    text = content.decode("utf-8")
    if (
        '<h1 class="page-title">Essential Acadia: Simplified Chinese</h1>' not in text
        or "Last updated: October 6, 2023" not in text
    ):
        raise ValueError("NPS Acadia article: expected title or revision anchor not found")

    parser = NpsArticleParagraphParser()
    parser.feed(text)
    sentences = [
        sentence
        for paragraph in parser.paragraphs
        for line in paragraph.splitlines()
        for sentence in complete_chinese_sentences(line, minimum_length=8)
    ]
    return [
        ("article", f"sentence-{index:03d}", sentence)
        for index, sentence in enumerate(sentences, 1)
    ]


class ReadyGovMainTextParser(HTMLParser):
    """Collect paragraph and list-item text from the Ready.gov main element."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.in_main = False
        self.block_tag: str | None = None
        self.skip_depth = 0
        self._parts: list[str] = []
        self.blocks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "main":
            self.in_main = True
        elif self.in_main and tag in {"script", "style"}:
            self.skip_depth += 1
        elif self.in_main and self.block_tag is None and tag in {"p", "li"}:
            self.block_tag = tag
            self._parts = []
        elif self.block_tag is not None and tag == "br":
            self._parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_depth and tag in {"script", "style"}:
            self.skip_depth -= 1
        elif self.block_tag == tag:
            self.blocks.append("".join(self._parts))
            self.block_tag = None
            self._parts = []
        elif tag == "main":
            self.in_main = False

    def handle_data(self, data: str) -> None:
        if self.block_tag is not None and not self.skip_depth:
            self._parts.append(data)


def parse_ready_gov_html(source_id: str, content: bytes) -> list[tuple[str, str, str]]:
    """Extract complete FEMA-authored prose from a pinned Simplified Chinese page."""
    title, revision = READY_GOV_SOURCE_ANCHORS[source_id]
    text = content.decode("utf-8")
    if (
        '<html lang="zh-hans"' not in text
        or f"<title>{title} | Ready.gov</title>" not in text
        or f"Last Updated: {revision}" not in text
    ):
        raise ValueError(f"{source_id}: expected language, title, or revision anchor not found")

    parser = ReadyGovMainTextParser()
    parser.feed(text)
    sentences: list[str] = []
    seen: set[str] = set()
    for block in parser.blocks:
        for sentence in complete_chinese_sentences(block, minimum_length=8):
            if re.search(
                r"(?:https?://|\b[\w.-]+\.(?:gov|org)\b|\(?\d{3}\)?[ -]\d{3}[ -]\d{4}|9-1-1)",
                sentence,
                re.I,
            ):
                continue
            if sentence not in seen:
                seen.add(sentence)
                sentences.append(sentence)
    return [
        ("article", f"sentence-{index:03d}", sentence)
        for index, sentence in enumerate(sentences, 1)
    ]


def parse_project_original(source_id: str, content: bytes) -> list[tuple[str, str, str]]:
    source = json.loads(content.decode("utf-8"))
    schema = load_json(PROJECT_SOURCE_SCHEMA)
    errors = sorted(
        Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(source),
        key=lambda item: list(item.path),
    )
    if errors:
        detail = "; ".join(f"{error.json_path}: {error.message}" for error in errors)
        raise ValueError(f"invalid project-original source: {detail}")
    if source["id"] != source_id:
        raise ValueError(
            f"project-original source id {source['id']!r} does not match manifest {source_id!r}"
        )
    case_ids = [case["id"] for case in source["cases"]]
    if len(case_ids) != len(set(case_ids)):
        raise ValueError("project-original source contains duplicate case ids")
    return [("project_original", case["id"], case["input"]) for case in source["cases"]]


def parse_permissioned_user_reports(source_id: str, content: bytes) -> list[tuple[str, str, str]]:
    source = json.loads(content.decode("utf-8"))
    if not isinstance(source, dict):
        raise ValueError("permissioned user-report source must be an object")
    if source.get("id") != source_id:
        raise ValueError(
            f"permissioned source id {source.get('id')!r} does not match manifest {source_id!r}"
        )
    errors = validate_collection(source, require_ready=True)
    if errors:
        raise ValueError("invalid permissioned user-report source: " + "; ".join(errors))
    return [("permissioned_user_report", case["id"], case["input"]) for case in source["cases"]]


def build_dataset(manifest: dict[str, Any], *, source_file: Path | None = None) -> dict[str, Any]:
    source_kind = SUPPORTED_SOURCES.get(manifest["id"])
    if source_kind is None and re.fullmatch(
        r"permissioned-user-report-batch-[0-9]{3}", manifest["id"]
    ):
        source_kind = "permissioned_user_report_json"
    if source_kind is None:
        raise ValueError(f"unsupported Blind-v2 source pilot: {manifest['id']}")
    raw_url, content = read_raw_source(manifest, source_file)
    if source_kind == "flores":
        raw_rows = parse_flores(content)
    elif source_kind == "ud_cfl":
        raw_rows = parse_ud_cfl(content)
    elif source_kind == "project_original_json":
        raw_rows = parse_project_original(manifest["id"], content)
    elif source_kind == "massive":
        raw_rows = parse_massive(content)
    elif source_kind == "vscode_loc_json":
        raw_rows = parse_vscode_loc(content)
    elif source_kind == "ftc_pdf":
        raw_rows = parse_ftc_small_business_pdf(content)
    elif source_kind == "ftc_heads_up_pdf":
        raw_rows = parse_ftc_heads_up_pdf(content)
    elif source_kind == "nps_acadia_html":
        raw_rows = parse_nps_acadia_html(content)
    elif source_kind == "ready_gov_html":
        raw_rows = parse_ready_gov_html(manifest["id"], content)
    elif source_kind == "osha_pdf":
        raw_rows = parse_osha_pdf(manifest["id"], content)
    elif source_kind == "permissioned_user_report_json":
        raw_rows = parse_permissioned_user_reports(manifest["id"], content)
    else:
        raw_rows = parse_cdc_pdf(manifest["id"], content)

    cases: list[dict[str, Any]] = []
    exclusions = Counter()
    seen_inputs: set[str] = set()
    by_split = Counter()
    for split, source_case_id, raw_text in raw_rows:
        text = normalize_input(raw_text)
        if not text:
            exclusions["empty_after_normalization"] += 1
            continue
        if text in seen_inputs:
            exclusions["exact_duplicate_within_source"] += 1
            continue
        seen_inputs.add(text)
        by_split[split] += 1
        cases.append(
            {
                "id": f"{manifest['id']}/{source_case_id}",
                "input": text,
                "provenance": {
                    "raw_url": raw_url,
                    "source_case_id": source_case_id,
                    "split": split,
                },
                "classification": {
                    "domain": None,
                    "risk": None,
                    "status": "needs_input_only_review",
                },
            }
        )

    return {
        "version": 1,
        "id": manifest["id"],
        "dataset": "blind-v2",
        "purpose": "candidate_source_pilot",
        "input_only": True,
        "converter_output_used": False,
        "source_class": manifest.get("source_class", "permissive_license"),
        "license": manifest["output_license"],
        "attribution": manifest["attribution"],
        "modification_notice": manifest["modification_notice"],
        "upstream_revision": manifest["upstream_revision"],
        "review_policy": "domain_and_risk_must_be_assigned_from_input_only",
        "stats": {
            "raw_cases": len(raw_rows),
            "eligible_pending_review": len(cases),
            "by_split": dict(sorted(by_split.items())),
            "exclusions": dict(sorted(exclusions.items())),
        },
        "cases": cases,
    }


def validate_dataset(dataset: dict[str, Any]) -> list[str]:
    schema = load_json(PILOT_SCHEMA)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(dataset), key=lambda item: list(item.path))
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--source-file", type=Path)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    manifest = load_json(args.manifest)
    output = args.output or PROJECT_ROOT / manifest["normalized_path"]
    dataset = build_dataset(manifest, source_file=args.source_file)
    errors = validate_dataset(dataset)
    if errors:
        raise ValueError("invalid source pilot: " + "; ".join(errors))
    content = canonical_json_bytes(dataset)
    if args.check:
        if not output.is_file() or output.read_bytes() != content:
            print(f"normalized source pilot is stale: {output}", file=sys.stderr)
            return 1
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_bytes(content)
    print(
        f"{manifest['id']}: {dataset['stats']['eligible_pending_review']} input-only cases; "
        f"sha256={sha256_bytes(content)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
