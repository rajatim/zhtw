"""
ZHTW - Simplified/HK Traditional to Taiwan Traditional Chinese Converter

tim Insight 出品 🇹🇼
"""

# zhtw:disable - Python identifiers must not be converted
__version__ = "4.3.0"
__author__ = "tim Insight"

from .converter import VALID_SOURCES, convert, convert_file, convert_text
from .dictionary import load_dictionary
from .export import export_data, write_export
from .lookup import ConversionDetail, LookupResult, lookup_word, lookup_words
from .matcher import Matcher

__all__ = [
    "__version__",
    "VALID_SOURCES",
    "convert",
    "convert_file",
    "convert_text",
    "load_dictionary",
    "export_data",
    "write_export",
    "ConversionDetail",
    "LookupResult",
    "lookup_word",
    "lookup_words",
    "Matcher",
]
# zhtw:enable
