"""Tests for export module."""

from __future__ import annotations

from click.testing import CliRunner

from zhtw.cli import main


def test_export_data_schema():
    """Exported data must have correct top-level schema."""
    from zhtw.export import export_data

    data = export_data()

    assert "version" in data
    assert "exported_at" not in data  # removed for deterministic output
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


def test_cli_export_default(tmp_path, monkeypatch):
    """CLI export writes files to sdk/data/ relative to CWD."""
    sdk_data = tmp_path / "sdk" / "data"
    sdk_data.mkdir(parents=True)
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    result = runner.invoke(main, ["export"])

    assert result.exit_code == 0
    assert (sdk_data / "zhtw-data.json").exists()
    assert (sdk_data / "golden-test.json").exists()


def test_cli_export_custom_output(tmp_path):
    """CLI export with --output writes to specified directory."""
    runner = CliRunner()
    result = runner.invoke(main, ["export", "--output", str(tmp_path)])

    assert result.exit_code == 0
    assert (tmp_path / "zhtw-data.json").exists()
    assert (tmp_path / "golden-test.json").exists()


def test_cli_export_missing_default_dir(tmp_path, monkeypatch):
    """CLI export fails gracefully when sdk/data/ doesn't exist."""
    monkeypatch.chdir(tmp_path)

    runner = CliRunner()
    result = runner.invoke(main, ["export"])

    assert result.exit_code != 0
    assert "--output" in result.output


def test_cli_export_source_filter(tmp_path):
    """CLI export with --source cn only exports CN terms and consistent golden."""
    import json

    runner = CliRunner()
    result = runner.invoke(main, ["export", "--output", str(tmp_path), "--source", "cn"])

    assert result.exit_code == 0
    data = json.loads((tmp_path / "zhtw-data.json").read_text("utf-8"))
    assert "cn" in data["terms"]
    assert "hk" not in data["terms"]

    # Golden test must also be filtered — no HK cases
    golden = json.loads((tmp_path / "golden-test.json").read_text("utf-8"))
    for case in golden["convert"]:
        assert "hk" not in case["sources"], f"HK case leaked into CN-only golden: {case}"
    for case in golden["lookup"]:
        assert "hk" not in case["sources"], f"HK case leaked into CN-only golden: {case}"


def test_write_export_byte_stable(tmp_path):
    """Two consecutive exports must produce identical bytes."""
    from zhtw.export import write_export

    dir1 = tmp_path / "a"
    dir2 = tmp_path / "b"
    dir1.mkdir()
    dir2.mkdir()

    write_export(output_dir=dir1)
    write_export(output_dir=dir2)

    assert (dir1 / "zhtw-data.json").read_bytes() == (dir2 / "zhtw-data.json").read_bytes()
    assert (dir1 / "golden-test.json").read_bytes() == (dir2 / "golden-test.json").read_bytes()


def test_cli_export_verbose(tmp_path):
    """CLI export --verbose shows stats."""
    runner = CliRunner()
    result = runner.invoke(main, ["export", "--output", str(tmp_path), "--verbose"])

    assert result.exit_code == 0
    assert "charmap" in result.output.lower() or "字元" in result.output
