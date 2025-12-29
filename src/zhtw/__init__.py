"""
ZHTW - Simplified/HK Traditional to Taiwan Traditional Chinese Converter

rajatim 出品 🇹🇼
"""

__version__ = "2.5.0"
__author__ = "rajatim"

from .converter import convert_file, convert_text
from .dictionary import load_dictionary
from .matcher import Matcher

__all__ = [
    "__version__",
    "convert_file",
    "convert_text",
    "load_dictionary",
    "Matcher",
]
