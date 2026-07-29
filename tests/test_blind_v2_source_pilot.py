"""Tests for pinned Blind-v2 input-only source pilots."""
# zhtw:disable  # 測試來源必須保持簡體

from __future__ import annotations

import hashlib
import io
import json
import tarfile
from pathlib import Path
from typing import Any

import pytest

from scripts.benchmark_metrics import canonical_json_bytes
from scripts.import_blind_v2_source_pilot import (
    build_dataset,
    normalize_input,
    parse_aosp_strings,
    parse_cdc_pages,
    parse_census_newsroom_archive,
    parse_census_newsroom_html,
    parse_chromium_xtb,
    parse_cisa_cyber_hygiene_pages,
    parse_cisa_personal_security_pages,
    parse_ftc_heads_up_pages,
    parse_ftc_how_to_avoid_scam_pages,
    parse_ftc_identity_theft_pages,
    parse_ftc_small_business_pages,
    parse_kubernetes_markdown,
    parse_kubernetes_markdown_archive,
    parse_massive,
    parse_nps_acadia_html,
    parse_osha_pdf,
    parse_project_original,
    parse_ready_gov_guide_pages,
    parse_ready_gov_html,
    parse_vscode_loc,
    validate_dataset,
)
from scripts.validate_benchmark_assets import validate_manifest

ROOT = Path(__file__).resolve().parents[1]
ACCURACY_ROOT = ROOT / "benchmarks" / "accuracy"
MANIFESTS = ACCURACY_ROOT / "manifests"
EXTERNAL = ACCURACY_ROOT / "external"
FORBIDDEN_KEYS = {"expected", "acceptable", "annotation", "output", "normalized_output"}


def flores_archive(dev: list[str], devtest: list[str]) -> bytes:
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        for name, lines in (
            ("./flores200_dataset/dev/zho_Hans.dev", dev),
            ("./flores200_dataset/devtest/zho_Hans.devtest", devtest),
        ):
            content = ("\n".join(lines) + "\n").encode()
            info = tarfile.TarInfo(name)
            info.size = len(content)
            archive.addfile(info, io.BytesIO(content))
    return buffer.getvalue()


def manifest(source_id: str, source: Path) -> dict[str, Any]:
    return {
        "id": source_id,
        "raw_sha256": {
            "https://example.test/source": hashlib.sha256(source.read_bytes()).hexdigest()
        },
        "normalized_path": "unused.json",
        "output_license": "CC BY-SA 4.0",
        "attribution": "Fixture contributors.",
        "modification_notice": "Input-only fixture extraction.",
        "upstream_revision": "fixture-revision",
    }


def find_forbidden_keys(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, child in value.items():
            if key in FORBIDDEN_KEYS:
                found.add(key)
            found.update(find_forbidden_keys(child))
    elif isinstance(value, list):
        for child in value:
            found.update(find_forbidden_keys(child))
    return found


def test_flores_import_is_deterministic_input_only_and_deduplicated(tmp_path: Path) -> None:
    source = tmp_path / "flores.tar.gz"
    source.write_bytes(flores_archive(["开发  工具", "重复句"], ["重复句", "用户界面"]))
    fixture = manifest("flores-200-zho-hans-v1", source)

    first = build_dataset(fixture, source_file=source)
    second = build_dataset(fixture, source_file=source)

    assert first["stats"] == {
        "raw_cases": 4,
        "eligible_pending_review": 3,
        "by_split": {"dev": 2, "devtest": 1},
        "exclusions": {"exact_duplicate_within_source": 1},
    }
    assert first["cases"][0]["input"] == "开发 工具"
    assert first["cases"][0]["classification"] == {
        "domain": None,
        "risk": None,
        "status": "needs_input_only_review",
    }
    assert find_forbidden_keys(first) == set()
    assert validate_dataset(first) == []
    assert canonical_json_bytes(first) == canonical_json_bytes(second)


def test_source_file_override_only_reads_selected_data_source(tmp_path: Path) -> None:
    source = tmp_path / "flores.tar.gz"
    source.write_bytes(flores_archive(["开发工具"], ["用户界面"]))
    fixture = manifest("flores-200-zho-hans-v1", source)
    data_hash = fixture["raw_sha256"].pop("https://example.test/source")
    fixture["raw_sha256"] = {
        "https://example.test/metadata.json": "0" * 64,
        "https://example.test/flores200_dataset.tar.gz": data_hash,
    }

    dataset = build_dataset(fixture, source_file=source)

    assert dataset["stats"]["eligible_pending_review"] == 2


def test_ud_cfl_import_rejects_incomplete_conllu(tmp_path: Path) -> None:
    source = tmp_path / "cfl.conllu"
    source.write_text(
        "# sent_id = missing-text\n1\t文字\t_\tX\t_\t_\t0\troot\t_\t_\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing sent_id or text"):
        build_dataset(manifest("ud-chinese-cfl-v1", source), source_file=source)


def test_normalization_does_not_convert_script() -> None:
    assert normalize_input("开发  软件\r\n接口") == "开发 软件 接口"


def test_census_newsroom_parser_is_anchored_and_excludes_contact_details() -> None:
    content = """<!doctype html><html><head>
    <meta name=\"DC.creator\" content=\"US Census Bureau\">
    <meta name=\"DC.language\" scheme=\"DCTERMS.RFC1766\" content=\"zh-hans\">
    </head><body>Chinese (Simplified) / 中文(简体)
    <div class=\"uscb-text-image-text other\"><p>
    人口普查局今天发布新的统计资料。这些资料将用于改善公共服务。
    </p><li>请致电 301-763-3030 了解更多信息。</li></div>
    <footer><p>这段页脚文字不应被收集。</p></footer>
    </body></html>""".encode()

    assert parse_census_newsroom_html(content) == [
        ("press_release", "sentence-001", "人口普查局今天发布新的统计资料。"),
        ("press_release", "sentence-002", "这些资料将用于改善公共服务。"),
    ]

    with pytest.raises(ValueError, match="creator or language anchor"):
        parse_census_newsroom_html(content.replace(b"zh-hans", b"en"))


def test_census_newsroom_archive_preserves_page_provenance() -> None:
    page = """<meta name="DC.creator" content="US Census Bureau">
    <meta name="DC.language" scheme="DCTERMS.RFC1766" content="zh-hans">
    Chinese (Simplified) / 中文(简体)
    <div class="uscb-text-image-text"><p>人口普查局发布新的统计资料。</p></div>
    """.encode()
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        info = tarfile.TarInfo("census-1.html")
        info.size = len(page)
        archive.addfile(info, io.BytesIO(page))
    fixture = {
        "source_urls": [
            "https://www.census.gov/newsroom/press-releases/example.html",
            "https://www.copyright.gov/title17/92chap1.html#105",
        ]
    }

    assert parse_census_newsroom_archive(fixture, buffer.getvalue()) == [
        (
            "press_release_01",
            "page-01-sentence-001",
            "人口普查局发布新的统计资料。",
            "https://www.census.gov/newsroom/press-releases/example.html",
        )
    ]


def test_kubernetes_markdown_parser_excludes_translation_comments_and_code() -> None:
    content = """---
title: Example
content_type: concept
---
<!-- This English sentence must not be collected. -->
## Heading

Kubernetes 使用对象来表示集群的状态。

```yaml
message: 这段代码不应被收集。
```

[用户可以通过标签筛选需要的资源。](https://example.test)
""".encode()

    assert parse_kubernetes_markdown(content) == [
        (
            "documentation",
            "sentence-0001",
            "Kubernetes 使用对象来表示集群的状态。",
        ),
        (
            "documentation",
            "sentence-0002",
            "用户可以通过标签筛选需要的资源。",
        ),
    ]


def test_kubernetes_markdown_archive_preserves_page_provenance() -> None:
    page = (
        "---\ntitle: Example\ncontent_type: concept\n---\n"
        "用户可以查看集群中当前运行的所有工作负载。\n"
    ).encode()
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        for member_name in (
            "01-names.md",
            "02-object-management.md",
            "03-pod-lifecycle.md",
            "04-service.md",
        ):
            info = tarfile.TarInfo(member_name)
            info.size = len(page)
            archive.addfile(info, io.BytesIO(page))
    urls = [f"https://raw.githubusercontent.test/content/zh-cn/{number}.md" for number in range(4)]

    rows = parse_kubernetes_markdown_archive({"source_urls": urls}, buffer.getvalue())

    assert len(rows) == 4
    assert rows[0][0:3] == (
        "documentation_01",
        "page-01-sentence-0001",
        "用户可以查看集群中当前运行的所有工作负载。",
    )
    assert rows[0][3] == urls[0]


def test_cisa_cyber_hygiene_parser_is_anchored_and_excludes_page_furniture() -> None:
    page = """
    CISA Region 4 做网络聪明：把你的“盾牌举起”
    网络骗局已不是新事物了。每天都要更新软件。
    以下是四个简单的步骤，你今天就可以开始： • 使用多因素身份验证。
    避免在不同账户上使用同一个密码。欲了解更多信息，请访问：example.gov
    """

    assert parse_cisa_cyber_hygiene_pages([page]) == [
        ("guide", "sentence-001", "网络骗局已不是新事物了。"),
        ("guide", "sentence-002", "每天都要更新软件。"),
        ("guide", "sentence-003", "避免在不同账户上使用同一个密码。"),
    ]

    with pytest.raises(ValueError, match="title anchor"):
        parse_cisa_cyber_hygiene_pages(["网络骗局已不是新事物了。"])


def test_cisa_personal_security_parser_is_anchored_and_excludes_references() -> None:
    pages = [
        "关键基础设施员工个人安全考虑与行动指南 在当今的威胁环境中，请保持警惕。1 ProtectUK",
        "人身安全 您可以考虑采取许多简单的措施，以保护您和您的家。枪械袭击 3 联邦调查局",
        "态势感知 抗议和示威如果局势变得不稳定，您也要保持冷静。5 美国国土安全部",
        (
            "如果您在公共场所/环境中感到担忧，请靠近人群。"
            "请查看 CISA 指南，了解更多信息。关键基础设施员工个人安全考虑与行动指南"
        ),
        (
            "及时更新软件，让攻击者无法利用漏洞。机动车辆和旅行请始终保持安全驾驶。"
            "匿名电话和威胁6 网络安全请勿从未知来源下载应用程序。"
            "在您的网络浏览器中 6 联邦调查局"
        ),
        "移动设备和网络可以保存各种个人资料。8 联邦通信委员会",
        (
            "在网上发布信息时，请务必注意发布的内容和方式。"
            "如果您需要帮助，请访问 example.gov。11 国土安全部 识别并报告网络钓鱼"
        ),
        "资源",
    ]

    assert parse_cisa_personal_security_pages(pages) == [
        ("guide", "sentence-001", "在当今的威胁环境中，请保持警惕。"),
        ("guide", "sentence-002", "您可以考虑采取许多简单的措施，以保护您和您的家。"),
        ("guide", "sentence-003", "如果局势变得不稳定，您也要保持冷静。"),
        ("guide", "sentence-004", "如果您在公共场所/环境中感到担忧，请靠近人群。"),
        ("guide", "sentence-005", "及时更新软件，让攻击者无法利用漏洞。"),
        ("guide", "sentence-006", "请始终保持安全驾驶。"),
        ("guide", "sentence-007", "请勿从未知来源下载应用程序。"),
        ("guide", "sentence-008", "在网上发布信息时，请务必注意发布的内容和方式。"),
    ]

    with pytest.raises(ValueError, match="expected 8 PDF pages"):
        parse_cisa_personal_security_pages(pages[:-1])


def test_massive_parser_extracts_only_input_provenance_fields() -> None:
    rows = [
        {
            "id": "7",
            "locale": "zh-CN",
            "partition": "train",
            "scenario": "audio",
            "intent": "audio_volume_mute",
            "utt": "暂停十秒钟",
            "annot_utt": "暂停 [time : 十秒钟]",
            "worker_id": "35",
            "judgments": [{"worker_id": "0", "grammar_score": 4}],
        }
    ]
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        content = ("\n".join(json.dumps(row, ensure_ascii=False) for row in rows)).encode()
        info = tarfile.TarInfo("1.0/data/zh-CN.jsonl")
        info.size = len(content)
        archive.addfile(info, io.BytesIO(content))

    assert parse_massive(buffer.getvalue()) == [("train", "7", "暂停十秒钟")]


def test_vscode_loc_parser_keeps_structured_ui_text_only() -> None:
    source = {
        "": [
            "Copyright (c) Microsoft Corporation. All rights reserved.",
            "Do not edit this file. It is machine generated.",
        ],
        "version": "1.0.0",
        "contents": {
            "module/two": {
                "url": "请前往 https://example.test 查看。",
                "placeholder": "{0}",
                "multiline": "第一行\n第二行",
            },
            "module/one": {
                "open": "打开辅助视图",
                "error": "无法保存文件: {0}",
            },
        },
    }

    rows = parse_vscode_loc(json.dumps(source, ensure_ascii=False).encode())

    assert [row[2] for row in rows] == ["无法保存文件: {0}", "打开辅助视图"]
    assert all(row[0] == "language_pack" for row in rows)
    assert all(row[1].startswith("entry-") for row in rows)


def test_chromium_xtb_parser_keeps_variable_free_ui_text() -> None:
    content = """<?xml version="1.0" ?>
<!DOCTYPE translationbundle>
<translationbundle lang="zh-CN">
  <translation id="1">继续安装</translation>
  <translation id="2">Chromium 建议您检查此扩展程序</translation>
  <translation id="3">请<ph name="BEGIN_LINK" />登录<ph name="END_LINK" />。</translation>
  <translation id="4">请访问 https://example.test</translation>
  <translation id="5">设置</translation>
  <translation id="6">{COUNT,plural, =1{一个标签页}other{多个标签页}}</translation>
</translationbundle>
""".encode()

    assert parse_chromium_xtb(content) == [
        ("browser_ui", "translation-1", "继续安装"),
        ("browser_ui", "translation-2", "Chromium 建议您检查此扩展程序"),
    ]


def test_chromium_xtb_parser_requires_zh_cn_bundle_and_numeric_unique_ids() -> None:
    with pytest.raises(ValueError, match="zh-CN translationbundle"):
        parse_chromium_xtb(b'<translationbundle lang="zh-TW" />')

    duplicate = """<translationbundle lang="zh-CN">
<translation id="1">继续安装</translation><translation id="1">重新启动</translation>
</translationbundle>""".encode()
    with pytest.raises(ValueError, match="duplicate translation id"):
        parse_chromium_xtb(duplicate)


def test_aosp_parser_keeps_stable_single_line_ui_strings() -> None:
    content = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2006, The Android Open Source Project
Licensed under the Apache License, Version 2.0 -->
<resources xmlns:xliff="urn:oasis:names:tc:xliff:document:1.2">
  <string name="save" msgid="1">"保存文件"</string>
  <string name="retry" msgid="2"
    >"无法连接。请在 <xliff:g id="SECONDS">%1$d</xliff:g> 秒后重试。"</string>
  <string name="url" msgid="3">"请访问 https://example.test"</string>
  <string name="short" msgid="4">"未知"</string>
  <string name="escaped_newline" msgid="5">"第一行\\n第二行"</string>
  <string name="bare_domain" msgid="6">"请访问 google.com"</string>
</resources>""".encode()

    rows = parse_aosp_strings(content)

    assert [row[2] for row in rows] == ["保存文件", "无法连接。请在 %1$d 秒后重试。"]
    assert all(row[0] == "framework_ui" for row in rows)
    assert all(row[1].startswith("string-") for row in rows)


def test_cdc_pdf_parser_joins_layout_wraps_and_keeps_complete_sentences() -> None:
    pages = [
        "标题 佩戴口罩。 与其他人保持至少 6 英尺的距离。 可访问版本：https://example.test",
        (
            "标题 请勿与家里的其他人共用 碗 碟 、水 杯。"
            " 遵循当地 卫生部门的指示。 如果某人出现 呼吸困难。"
        ),
    ]

    rows = parse_cdc_pages("cdc-stacks-111808-v1", pages)

    assert [row[2] for row in rows] == [
        "佩戴口罩。",
        "与其他人保持至少 6 英尺的距离。",
        "请勿与家里的其他人共用碗碟、水杯。",
        "遵循当地卫生部门的指示。",
        "呼吸困难。",
    ]


def test_ftc_parser_removes_layout_navigation_and_joins_cross_page_sentence() -> None:
    pages = ["诈骗与你的小型企业: 企业指南"] + [""] * 9
    pages[1] = (
        "诈骗与你的小型企业: 企业指南\n1\n► 诈骗犯的伎俩\n"
        "● 诈骗犯会营造一种紧迫感，甚至施以威胁。\n"
        "请前往 ftc.gov/example 查阅更多信息。\n"
        "他们会要求你将企"
    )
    pages[2] = "诈骗与你的小型企业: 企业指南\n2\n业资料交给对方。"

    rows = parse_ftc_small_business_pages(pages)

    assert [row[2] for row in rows] == [
        "诈骗犯会营造一种紧迫感，甚至施以威胁。",
        "他们会要求你将企业资料交给对方。",
    ]


def test_ftc_heads_up_parser_excludes_english_and_preserves_quoted_questions() -> None:
    pages = [""] * 15
    pages[1] = (
        "要在生活中帮助您的孩子安全上网。\n"
        "每次都扪心自问： “这个应用软件需要知道我的位置吗？ ”\n"
        "如果不需要， 关闭位置\n"
        "To help kids in your life be safe online."
    )
    pages[2] = "3\n共享。\n谨慎分享\n网上的行为会产生真实的后果。"
    pages[14] = "This booklet helps kids socialize safely online."

    rows = parse_ftc_heads_up_pages(pages)

    assert [row[2] for row in rows] == [
        "要在生活中帮助您的孩子安全上网。",
        "每次都扪心自问：“这个应用软件需要知道我的位置吗？”",
        "如果不需要，关闭位置共享。",
        "网上的行为会产生真实的后果。",
    ]


def test_ftc_scam_parser_removes_pdf_bullets_and_contact_instructions() -> None:
    pages = [
        (
            "骗局的四大迹象 诈骗者假装来自于您知道 的组织。사 "
            "他们使用技术来更改来电显示上的电话号码。 Simplified Chinese"
        ),
        (
            "如何避免骗局 \uf07d 屏蔽骚扰电话和短信。 \uf07d 顶住立即采取行动的压力。 "
            "向美国联邦贸易委员会（FTC）举报骗局 请致电 877-382-4357。"
        ),
    ]

    rows = parse_ftc_how_to_avoid_scam_pages(pages)

    assert [row[2] for row in rows] == [
        "诈骗者假装来自于您知道的组织。",
        "他们使用技术来更改来电显示上的电话号码。",
        "屏蔽骚扰电话和短信。",
        "顶住立即采取行动的压力。",
    ]


def test_ftc_identity_theft_parser_removes_embedded_list_fragments() -> None:
    pages = [
        (
            "什么是身份盗窃？ 身份盗窃是指有人未经许可使用您的个人信息。 "
            "用途： ⊲ 用您的信用卡购物 ⊲ 找工作。 获取您的信用报告"
        ),
        (
            "如何保护自己免遭身份盗窃？ 身份盗窃可能发生在任何人身上。 "
            "⊲ 使用难以猜到的密码。 如何以我的首选语言举报身份盗窃"
        ),
    ]

    rows = parse_ftc_identity_theft_pages(pages)

    assert [row[2] for row in rows] == [
        "身份盗窃是指有人未经许可使用您的个人信息。",
        "身份盗窃可能发生在任何人身上。",
        "使用难以猜到的密码。",
    ]


def test_nps_parser_keeps_only_complete_article_paragraph_sentences() -> None:
    content = """<!doctype html><html><body>
    <nav><p>导航噪音。</p></nav>
    <h1 class="page-title">Essential Acadia: Simplified Chinese</h1>
    <div class="Article__Content"><div><p>
    欢迎来到阿卡迪亚国家公园。<br />
    请不要将手机当作地图或手电筒。
    请在 <a href="https://example.test">example.test</a> 上查看当前状
    </p></div></div>
    <footer><p>页脚噪音。</p></footer>
    <p>Last updated: October 6, 2023</p></body></html>""".encode()

    rows = parse_nps_acadia_html(content)

    assert [row[2] for row in rows] == [
        "\u6b22\u8fce\u6765\u5230\u963f\u5361\u8fea\u4e9a\u56fd\u5bb6\u516c\u56ed\u3002",
        "\u8bf7\u4e0d\u8981\u5c06\u624b\u673a\u5f53\u4f5c\u5730\u56fe\u6216\u624b\u7535\u7b52\u3002",
    ]


def test_ready_gov_parser_keeps_main_prose_and_excludes_phone_and_navigation() -> None:
    content = """<!doctype html><html lang="zh-hans"><head>
    <title>洪水 | Ready.gov</title></head><body>
    <nav><p>导航噪音。</p></nav><main>
    <p>洪水可能导致严重损害。</p>
    <ul><li><strong>收到警报后立即撤离。</strong></li>
    <li>如遇紧急情况，打 9-1-1。</li></ul>
    <p>Last Updated: 10/22/2025</p></main>
    <footer><p>页脚噪音。</p></footer></body></html>""".encode()

    rows = parse_ready_gov_html("ready-gov-floods-zh-hans-v1", content)

    assert [row[2] for row in rows] == ["洪水可能导致严重损害。", "收到警报后立即撤离。"]


def test_ready_gov_guide_parser_uses_only_body_and_excludes_contact_text() -> None:
    pages = [""] * 28
    pages[0] = "您做好准备了吗？\nP-2157 | 2020 年 9 月"
    pages[3] = "目录中的句子不应纳入。"
    pages[4] = (
        "1 Ready .gov\n防灾准备\n灾难发生前应先了解家庭面对的风险。\n"
        "请访问 Ready.gov 查看更多信息。"
    )
    pages[26] = (
        "23 Ready .gov\n保护自己不受与灾害有关的欺诈和诈骗\n"
        "联邦工作人员不会索求或者接受钱财。\n"
        "请拨打 866-720-5721 举报可疑活动。"
    )
    pages[27] = "目录编号。这个句子也不应纳入。"

    rows = parse_ready_gov_guide_pages(pages)

    assert [row[2] for row in rows] == [
        "防灾准备灾难发生前应先了解家庭面对的风险。",
        "保护自己不受与灾害有关的欺诈和诈骗联邦工作人员不会索求或者接受钱财。",
    ]


def test_osha_parser_keeps_only_selected_simplified_pages(monkeypatch: pytest.MonkeyPatch) -> None:
    class Page:
        def __init__(self, text: str) -> None:
            self.text = text

        def extract_text(self) -> str:
            return self.text

    class Reader:
        pages = [Page("Electrical Safety."), Page("这是用电安全指南。切勿接触掉落的架空电线。")]
        metadata = type("Metadata", (), {"author": "OSHA"})()

    monkeypatch.setattr("scripts.import_blind_v2_source_pilot.PdfReader", lambda _: Reader())

    rows = parse_osha_pdf("osha-electrical-safety-simplified-v1", b"pdf")

    assert [row[2] for row in rows] == ["这是用电安全指南。", "切勿接触掉落的架空电线。"]


def test_source_class_is_copied_from_manifest(tmp_path: Path) -> None:
    source = tmp_path / "flores.tar.gz"
    source.write_bytes(flores_archive(["公共资料"], []))
    fixture = manifest("flores-200-zho-hans-v1", source)
    fixture["source_class"] = "public_domain"

    assert build_dataset(fixture, source_file=source)["source_class"] == "public_domain"


def test_project_original_import_validates_input_only_schema(tmp_path: Path) -> None:
    source = tmp_path / "project-source.json"
    source.write_text(
        json.dumps(
            {
                "version": 1,
                "id": "zhtw-project-ui-i18n-v1",
                "created_date": "2026-07-23",
                "authorship": "Codex-drafted input-only fixture pending review.",
                "input_only": True,
                "converter_output_used": False,
                "cases": [{"id": "ui-001", "input": "用户界面"}],
            }
        ),
        encoding="utf-8",
    )
    fixture = manifest("zhtw-project-ui-i18n-v1", source)
    fixture["source_class"] = "project_original"

    dataset = build_dataset(fixture, source_file=source)

    assert dataset["stats"]["by_split"] == {"project_original": 1}
    assert dataset["cases"][0]["input"] == "用户界面"
    assert find_forbidden_keys(dataset) == set()


def test_project_original_source_rejects_expected_text() -> None:
    source = {
        "version": 1,
        "id": "zhtw-project-ui-i18n-v1",
        "created_date": "2026-07-23",
        "authorship": "Input-only fixture.",
        "input_only": True,
        "converter_output_used": False,
        "cases": [{"id": "ui-001", "input": "用户界面", "expected": "使用者介面"}],
    }

    with pytest.raises(ValueError, match="invalid project-original source"):
        parse_project_original(source["id"], json.dumps(source).encode())


@pytest.mark.parametrize(
    ("source_id", "expected_cases"),
    (
        ("flores-200-zho-hans-v1", 2009),
        ("ud-chinese-cfl-v1", 451),
        ("cdc-stacks-111808-v1", 18),
        ("cdc-stacks-120024-v1", 22),
        ("cdc-stacks-116683-v1", 22),
        ("zhtw-project-ui-i18n-v1", 50),
        ("zhtw-project-llm-product-v1", 50),
        ("zhtw-project-it-api-cli-v1", 100),
        ("zhtw-project-formal-llm-semantic-v1", 100),
        ("zhtw-project-formal-entity-guard-v1", 100),
        ("zhtw-project-it-llm-ui-guard-v1", 100),
        ("zhtw-project-balanced-baseline-guard-v1", 100),
        ("zhtw-project-formal-llm-balance-v1", 100),
        ("zhtw-project-competitor-risk-taxonomy-v1", 80),
        ("zhtw-project-llm-domain-balance-v1", 100),
        ("zhtw-project-llm-social-baseline-v1", 100),
        ("zhtw-project-it-llm-social-guard-v1", 100),
        ("zhtw-project-llm-it-ui-baseline-v1", 100),
        ("zhtw-project-it-ui-llm-formal-guard-v1", 100),
        ("zhtw-project-formal-llm-overconversion-guard-v1", 80),
        ("zhtw-project-formal-llm-context-guard-v1", 100),
        ("zhtw-project-formal-llm-evidence-guard-v1", 100),
        ("zhtw-project-ui-social-baseline-guard-v1", 100),
        ("zhtw-project-llm-formal-reasoning-guard-v1", 100),
        ("zhtw-project-llm-formal-operations-guard-v1", 100),
        ("massive-1-0-zh-cn-v1", 15619),
        ("ftc-small-business-simplified-v1", 81),
        ("ftc-heads-up-simplified-v1", 117),
        ("ftc-how-to-avoid-scam-simplified-v1", 34),
        ("ftc-identity-theft-simplified-v1", 20),
        ("nps-essential-acadia-simplified-v1", 32),
        ("ready-gov-floods-zh-hans-v1", 53),
        ("ready-gov-hurricanes-zh-hans-v1", 53),
        ("ready-gov-earthquakes-zh-hans-v1", 48),
        ("ready-gov-drought-zh-hans-v1", 73),
        ("ready-gov-home-fires-zh-hans-v1", 86),
        ("ready-gov-landslides-debris-flow-zh-hans-v1", 61),
        ("ready-gov-radiation-zh-hans-v1", 64),
        ("ready-gov-tornadoes-zh-hans-v1", 34),
        ("ready-gov-winter-weather-zh-hans-v1", 56),
        ("ready-gov-kids-tornadoes-zh-hans-v1", 43),
        ("ready-gov-campus-zh-hans-v1", 6),
        ("ready-gov-evacuation-zh-hans-v1", 49),
        ("ready-gov-cybersecurity-zh-hans-v1", 55),
        ("ready-gov-are-you-ready-guide-simplified-v1", 576),
        ("osha-electrical-safety-simplified-v1", 14),
        ("osha-chainsaw-safety-simplified-v1", 20),
        ("osha-work-zone-traffic-simplified-v1", 16),
        ("osha-disaster-falls-simplified-v1", 14),
        ("osha-small-business-consultation-simplified-v1", 22),
        ("osha-disaster-cleanup-simplified-v1", 76),
        ("osha-fallen-workers-family-simplified-v1", 23),
        ("vscode-loc-zh-hans-v1", 15618),
        ("chromium-strings-zh-cn-v1", 535),
        ("aosp-framework-zh-rcn-v1", 1697),
        ("cisa-cyber-hygiene-zh-hans-v1", 24),
        ("cisa-personal-security-zh-hans-v1", 134),
        ("census-newsroom-zh-hans-v1", 235),
        ("kubernetes-docs-zh-cn-v1", 679),
    ),
)
def test_committed_source_pilots_are_pinned_and_input_only(
    source_id: str, expected_cases: int
) -> None:
    manifest_path = MANIFESTS / f"{source_id}.json"
    dataset_path = EXTERNAL / f"{source_id}.json"
    source_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    dataset = json.loads(dataset_path.read_text(encoding="utf-8"))

    assert validate_manifest(manifest_path) == []
    assert (
        hashlib.sha256(dataset_path.read_bytes()).hexdigest()
        == source_manifest["normalized_sha256"]
    )
    assert dataset["input_only"] is True
    assert dataset["converter_output_used"] is False
    assert dataset["stats"]["eligible_pending_review"] == len(dataset["cases"]) == expected_cases
    assert find_forbidden_keys(dataset) == set()
    assert all(case["classification"]["domain"] is None for case in dataset["cases"])
    assert all(case["classification"]["risk"] is None for case in dataset["cases"])
