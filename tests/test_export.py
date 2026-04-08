"""Tests for export module."""

from __future__ import annotations


def test_export_data_schema():
    """Exported data must have correct top-level schema."""
    from zhtw.export import export_data

    data = export_data()

    assert "version" in data
    assert "exported_at" in data
    assert "stats" in data
    assert "charmap" in data
    assert "terms" in data

    assert "charmap_count" in data["stats"]
    assert "ambiguous_count" in data["stats"]
    assert "terms_cn_count" in data["stats"]
    assert "terms_hk_count" in data["stats"]

    assert "chars" in data["charmap"]
    assert "ambiguous" in data["charmap"]
    assert isinstance(data["charmap"]["chars"], dict)
    assert isinstance(data["charmap"]["ambiguous"], list)

    assert "cn" in data["terms"]
    assert "hk" in data["terms"]
    assert isinstance(data["terms"]["cn"], dict)
    assert isinstance(data["terms"]["hk"], dict)


def test_export_data_stats_match_content():
    """Stats counts must match actual content lengths."""
    from zhtw.export import export_data

    data = export_data()
    assert data["stats"]["charmap_count"] == len(data["charmap"]["chars"])
    assert data["stats"]["ambiguous_count"] == len(data["charmap"]["ambiguous"])
    assert data["stats"]["terms_cn_count"] == len(data["terms"]["cn"])
    assert data["stats"]["terms_hk_count"] == len(data["terms"]["hk"])


def test_export_data_version_matches_package():
    """Exported version must match __version__."""
    from zhtw import __version__
    from zhtw.export import export_data

    data = export_data()
    assert data["version"] == __version__


def test_export_data_cn_hk_separate():
    """CN and HK terms must not be merged — keys can differ."""
    from zhtw.export import export_data

    data = export_data()
    cn = data["terms"]["cn"]
    hk = data["terms"]["hk"]

    # CN should have simplified keys like 软件
    assert "软件" in cn
    # HK should have traditional keys like 軟件
    assert "軟件" in hk
    # They should not be identical dicts
    assert cn != hk


def test_export_data_source_filter():
    """--source cn should only export CN terms."""
    from zhtw.export import export_data

    data = export_data(sources=["cn"])
    assert "cn" in data["terms"]
    assert "hk" not in data["terms"]
    assert data["stats"]["terms_hk_count"] == 0


def test_golden_test_schema():
    """Golden test must have correct schema."""
    from zhtw.export import generate_golden_test

    golden = generate_golden_test()

    assert "version" in golden
    assert "description" in golden
    assert "convert" in golden
    assert "check" in golden
    assert "lookup" in golden
    assert isinstance(golden["convert"], list)
    assert isinstance(golden["check"], list)
    assert isinstance(golden["lookup"], list)


def test_golden_convert_cases():
    """Convert cases must have input/sources/expected fields."""
    from zhtw.export import generate_golden_test

    golden = generate_golden_test()

    for case in golden["convert"]:
        assert "input" in case
        assert "sources" in case
        assert "expected" in case
        assert isinstance(case["sources"], list)


def test_golden_check_has_full_matches():
    """Check cases must have expected_matches with start/end/source/target."""
    from zhtw.export import generate_golden_test

    golden = generate_golden_test()

    for case in golden["check"]:
        assert "input" in case
        assert "expected_matches" in case
        for m in case["expected_matches"]:
            assert "start" in m
            assert "end" in m
            assert "source" in m
            assert "target" in m


def test_golden_lookup_has_full_details():
    """Lookup cases must have expected_details with source/target/layer/position."""
    from zhtw.export import generate_golden_test

    golden = generate_golden_test()

    for case in golden["lookup"]:
        assert "input" in case
        assert "expected_output" in case
        assert "expected_changed" in case
        assert "expected_details" in case
        for d in case["expected_details"]:
            assert "source" in d
            assert "target" in d
            assert "layer" in d
            assert "position" in d


def test_golden_convert_matches_python_pipeline():
    """Golden convert expected values must match actual Python conversion."""
    from zhtw.charconv import get_translate_table
    from zhtw.converter import convert_text
    from zhtw.dictionary import load_dictionary
    from zhtw.export import generate_golden_test
    from zhtw.matcher import Matcher

    golden = generate_golden_test()

    for case in golden["convert"]:
        terms = load_dictionary(sources=case["sources"])
        matcher = Matcher(terms)
        char_table = get_translate_table() if "cn" in case["sources"] else None
        result_text, _ = convert_text(case["input"], matcher, fix=True, char_table=char_table)
        assert result_text == case["expected"], (
            f"Convert mismatch for {case['input']!r}: "
            f"golden={case['expected']!r}, actual={result_text!r}"
        )


def test_write_export_creates_files(tmp_path):
    """write_export() must create both JSON files."""
    from zhtw.export import write_export

    write_export(output_dir=tmp_path)

    data_path = tmp_path / "zhtw-data.json"
    golden_path = tmp_path / "golden-test.json"

    assert data_path.exists()
    assert golden_path.exists()

    # Verify they are valid JSON
    import json

    data = json.loads(data_path.read_text("utf-8"))
    golden = json.loads(golden_path.read_text("utf-8"))

    assert data["version"] == golden["version"]
    assert "terms" in data
    assert "convert" in golden


def test_write_export_deterministic_keys(tmp_path):
    """Exported JSON keys must be sorted for deterministic output."""
    import json

    from zhtw.export import write_export

    write_export(output_dir=tmp_path)

    data_path = tmp_path / "zhtw-data.json"
    raw = data_path.read_text("utf-8")
    data = json.loads(raw)

    # Charmap chars keys should be sorted
    chars_keys = list(data["charmap"]["chars"].keys())
    assert chars_keys == sorted(chars_keys)

    # Terms CN keys should be sorted
    cn_keys = list(data["terms"]["cn"].keys())
    assert cn_keys == sorted(cn_keys)
