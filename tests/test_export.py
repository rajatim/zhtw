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
