"""Tests for dictionary module."""
# zhtw:disable  # 測試案例需要簡體字輸入

import json
import tempfile
from pathlib import Path

import pytest

from zhtw.dictionary import (
    load_builtin,
    load_builtin_catalog,
    load_custom,
    load_dictionary,
    load_dictionary_catalog,
    load_json_file,
    load_rule_file,
)
from zhtw.rules import ReviewStatus, RuleCatalogError, RuleClass, TrustLevel


class TestDictionary:
    """Test dictionary loading functions."""

    def test_load_builtin_cn(self):
        """Test loading CN (Simplified) dictionary."""
        terms = load_builtin(sources=["cn"])

        assert len(terms) > 0
        assert "软件" in terms
        assert terms["软件"] == "軟體"

    def test_load_builtin_hk(self):
        """Test loading HK dictionary."""
        terms = load_builtin(sources=["hk"])

        assert len(terms) > 0

    def test_load_builtin_all(self):
        """Test loading all built-in dictionaries."""
        terms = load_builtin()

        # Should have terms from both cn and hk
        assert len(terms) > 0

    def test_load_dictionary_default(self):
        """Test load_dictionary with defaults."""
        terms = load_dictionary()

        assert len(terms) > 0
        assert "软件" in terms

    def test_load_custom_simple_format(self):
        """Test loading custom dictionary with simple format."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump({"自定义": "自訂"}, f, ensure_ascii=False)
            f.flush()

            terms = load_custom(Path(f.name))

        assert terms == {"自定义": "自訂"}

    def test_load_custom_with_terms_key(self):
        """Test loading custom dictionary with terms key."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            data = {
                "version": "1.0",
                "terms": {"自定义": "自訂"},
            }
            json.dump(data, f, ensure_ascii=False)
            f.flush()

            terms = load_custom(Path(f.name))

        assert terms == {"自定义": "自訂"}

    def test_legacy_custom_keeps_applying_with_hk_only(self, tmp_path):
        """Legacy custom files had no locale and must preserve that behavior."""
        custom = tmp_path / "custom.json"
        custom.write_text('{"自定义": "自訂"}', encoding="utf-8")

        terms = load_dictionary(sources=["hk"], custom_path=custom)

        assert terms["自定义"] == "自訂"

    def test_wrapped_format_excludes_underscore_metadata(self):
        """Section comments inside `terms` are not runtime conversion rules."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            data = {
                "version": "1.0",
                "terms": {
                    "_comment_ui": "UI section",
                    "软件": "軟體",
                },
            }
            json.dump(data, f, ensure_ascii=False)
            f.flush()

            terms = load_custom(Path(f.name))

        assert terms == {"软件": "軟體"}

    def test_load_dictionary_with_custom(self):
        """Test load_dictionary merges custom terms."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump({"自定义": "自訂"}, f, ensure_ascii=False)
            f.flush()

            terms = load_dictionary(custom_path=Path(f.name))

        # Should have both builtin and custom
        assert "软件" in terms
        assert "自定义" in terms

    def test_load_custom_extended_entry_without_target_is_skipped(self):
        """Test malformed extended entries don't leak dict objects into replacements."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(
                {
                    "version": "1.0",
                    "terms": {
                        "测试": {"category": "bad"},
                        "软件": {"target": "軟體", "category": "it"},
                    },
                },
                f,
                ensure_ascii=False,
            )
            f.flush()

            terms = load_custom(Path(f.name))

        assert "测试" not in terms
        assert terms["软件"] == "軟體"

    def test_load_nonexistent_file(self):
        """Test loading non-existent file returns empty dict."""
        terms = load_json_file(Path("/nonexistent/path.json"))

        assert terms == {}

    def test_legacy_flat_format_excludes_metadata_keys(self):
        """Legacy flat-format JSON files (no `terms` wrapper) must NOT load
        reserved metadata keys (version/description/source/...) as term
        mappings. Regression: a previous loader treated `data.get("terms",
        data)` as a fallback, leaking metadata into the dictionary and
        corrupting English text like `version = "x.y.z"` → `1.0 = "x.y.z"`.
        """
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(
                {
                    "version": "1.0",
                    "description": "Some metadata",
                    "source": "External provider",
                    "license": "Apache-2.0",
                    "_comment_source": "Not a conversion rule",
                    # Real entries (legacy flat format)
                    "软件": "軟體",
                    "数据": "資料",
                },
                f,
                ensure_ascii=False,
            )
            f.flush()

            terms = load_json_file(Path(f.name))

        # Real terms loaded
        assert terms["软件"] == "軟體"
        assert terms["数据"] == "資料"
        # Metadata MUST NOT appear as term keys
        assert "version" not in terms
        assert "description" not in terms
        assert "source" not in terms
        assert "license" not in terms
        assert "_comment_source" not in terms

    def test_schema_v2_loads_only_approved_rules(self, tmp_path):
        path = tmp_path / "rules.json"
        path.write_text(
            json.dumps(
                {
                    "schema_version": 2,
                    "rules": [
                        {
                            "id": "rule:cn:it:approved",
                            "source_locale": "cn",
                            "source": "软件",
                            "target": "軟體",
                            "rule_class": "custom",
                            "domain": "it",
                            "trust_level": "custom",
                            "priority": 400,
                            "context": [],
                            "evidence_source": "maintainer-review-2026-08-27",
                            "review_status": "approved",
                        },
                        {
                            "id": "rule:cn:it:pending",
                            "source_locale": "cn",
                            "source": "测试",
                            "target": "測試",
                            "rule_class": "custom",
                            "domain": "it",
                            "trust_level": "custom",
                            "priority": 400,
                            "context": [],
                            "evidence_source": None,
                            "review_status": "pending",
                        },
                    ],
                },
                ensure_ascii=False,
            ),
            encoding="utf-8",
        )

        result = load_rule_file(path)

        assert result.terms == {"软件": "軟體"}
        assert len(result.catalog) == 2
        assert result.catalog[1].review_status is ReviewStatus.PENDING

    def test_schema_v2_filters_explicit_source_locale(self, tmp_path):
        path = tmp_path / "rules.json"
        rule = {
            "id": "rule:hk:it:approved",
            "source_locale": "hk",
            "source": "軟件",
            "target": "軟體",
            "rule_class": "custom",
            "domain": "it",
            "trust_level": "custom",
            "priority": 400,
            "context": [],
            "evidence_source": "maintainer-review-2026-08-27",
            "review_status": "approved",
        }
        path.write_text(
            json.dumps({"schema_version": 2, "rules": [rule]}, ensure_ascii=False),
            encoding="utf-8",
        )

        assert (
            load_dictionary(sources=["cn"], custom_path=path, include_builtin=False).get("軟件")
            is None
        )
        assert (
            load_dictionary(sources=["hk"], custom_path=path, include_builtin=False)["軟件"]
            == "軟體"
        )

    @pytest.mark.parametrize("version", [3, True, "2"])
    def test_schema_v2_rejects_unknown_version(self, tmp_path, version):
        path = tmp_path / "rules.json"
        path.write_text(
            json.dumps({"schema_version": version, "rules": []}),
            encoding="utf-8",
        )

        with pytest.raises(RuleCatalogError, match="unsupported dictionary schema_version"):
            load_rule_file(path)

    def test_schema_v2_rejects_rule_class_mismatch(self, tmp_path):
        path = tmp_path / "rules.json"
        payload = {
            "schema_version": 2,
            "rules": [
                {
                    "id": "rule:cn:it:wrong-class",
                    "source_locale": "cn",
                    "source": "软件",
                    "target": "軟體",
                    "rule_class": "curated",
                    "domain": "it",
                    "trust_level": "curated",
                    "priority": 300,
                    "context": [],
                    "evidence_source": "maintainer-review-2026-08-27",
                    "review_status": "approved",
                }
            ],
        }
        path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

        with pytest.raises(RuleCatalogError, match="rule_class does not match"):
            load_rule_file(path)

    def test_builtin_catalog_preserves_effective_terms_and_precedence_metadata(self):
        result = load_builtin_catalog(["cn"])

        assert result.terms == load_builtin(["cn"])
        assert {record.rule_class for record in result.catalog} == {
            RuleClass.BULK,
            RuleClass.GENERATED_GUARD,
            RuleClass.CURATED,
        }
        priorities = {record.rule_class: record.priority for record in result.catalog}
        assert priorities == {
            RuleClass.BULK: 100,
            RuleClass.GENERATED_GUARD: 200,
            RuleClass.CURATED: 300,
        }
        trusts = {record.rule_class: record.trust_level for record in result.catalog}
        assert trusts == {
            RuleClass.BULK: TrustLevel.IMPORTED,
            RuleClass.GENERATED_GUARD: TrustLevel.GENERATED,
            RuleClass.CURATED: TrustLevel.CURATED,
        }

    def test_dictionary_catalog_matches_legacy_runtime_map(self):
        result = load_dictionary_catalog()

        assert result.terms == load_dictionary()
        assert len(result.catalog) >= len(result.terms)
