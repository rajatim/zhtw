"""
ZHTW - Simplified/HK Traditional to Taiwan Traditional Chinese Converter

tim Insight 出品 🇹🇼
"""

__version__ = "3.3.0"
__author__ = "tim Insight"

from .converter import convert_file, convert_text
from .dictionary import load_dictionary
from .lookup import ConversionDetail, LookupResult, lookup_word, lookup_words
from .matcher import Matcher

__all__ = [
    "__version__",
    "convert_file",
    "convert_text",
    "load_dictionary",
    "ConversionDetail",
    "LookupResult",
    "lookup_word",
    "lookup_words",
    "Matcher",
]
