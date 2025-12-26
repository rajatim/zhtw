"""Import terms from external sources."""

import json
import re
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class ImportResult:
    """Result of an import operation."""

    total: int = 0
    valid: int = 0
    invalid: int = 0
    duplicates: int = 0
    conflicts: int = 0
    errors: list = field(default_factory=list)
    terms: dict = field(default_factory=dict)


class ImportError(Exception):
    """Error during import."""

    pass


def get_pending_dir() -> Path:
    """Get the pending terms directory."""
    # Get the data directory relative to this file
    data_dir = Path(__file__).parent / "data" / "terms" / "pending"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir


def is_simplified_chinese(char: str) -> bool:
    """Check if a character is likely simplified Chinese.

    This is a simple heuristic based on Unicode ranges.
    """
    # Common simplified-only characters
    simplified_chars = set(
        "与专业东两严个丰临为丽举义乐习书买乱争亏云产亲亿仅从仓仪众优会"
        "伟传伤伦伪体余佣侠侣侥侦侧侨侬俊俏俐俣俦俨俩俪俭债倾偻偿傥傧储"
        "兑兖关兴养兽冁冯冲决况冻净凄准凉减凑凛凤凫凭凯击凿刍划刘则刚创"
        "删别刬刭刮刹剀剂剐剑剥剧劝办务劢动励劲劳势勋勚匀匦匮区医华协单"
        "卖卢卤卫却卷厂厅历厉压厌厍厐厕厘厢厣厦厨厩厮县叁参双变叙叠只台"
        "叶号叹吁后吓吕吗吨听启吴呐呒呓呕呖呗员呙呛呜咏咙咛咝咤咴咸哒哓"
        "哔哕哗哙哜哝哟唛唝唠唡唢唣唤啧啬啭啮啰啴啸喷喽喾嗫嗳嘘嘤嘱噜噼"
        "嚣囊囔囵国图圆圣圹场坂坏块坚坛坜坝坞坟坠垄垅垆垒垦垧垩垫垭垱垲"
        "垴埘埙埚埝域埯堑堕堙塆墙壮声壳壶壸处备复够头夸夹夺奁奂奋奖套奥"
    )
    return char in simplified_chars


def validate_term(source: str, target: str, existing_terms: dict) -> tuple[bool, Optional[str]]:
    """Validate a term pair.

    Returns:
        (is_valid, error_message)
    """
    # Check empty
    if not source or not target:
        return False, "來源或目標為空"

    # Check same
    if source == target:
        return False, "來源與目標相同"

    # Check length
    if len(source) > 20 or len(target) > 20:
        return False, "詞彙過長（超過 20 字元）"

    # Check for non-Chinese characters (allow some punctuation)
    chinese_pattern = re.compile(r"^[\u4e00-\u9fff\u3400-\u4dbf]+$")
    if not chinese_pattern.match(source):
        return False, "來源包含非中文字元"
    if not chinese_pattern.match(target):
        return False, "目標包含非中文字元"

    # Check for conflicts with existing terms
    if source in existing_terms:
        if existing_terms[source] != target:
            return False, f"與現有詞庫衝突：{source} → {existing_terms[source]}"

    return True, None


def load_from_url(url: str) -> dict:
    """Load terms from a URL.

    Returns:
        Dict of source -> target terms
    """
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "zhtw/2.0"},
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            data = json.loads(content)

            # Handle different formats
            if isinstance(data, dict):
                if "terms" in data:
                    return data["terms"]
                return data
            elif isinstance(data, list):
                # List of {"source": ..., "target": ...}
                return {item["source"]: item["target"] for item in data if "source" in item}

            raise ImportError(f"無法識別的格式: {type(data)}")

    except urllib.error.URLError as e:
        raise ImportError(f"無法載入 URL: {e.reason}")
    except json.JSONDecodeError as e:
        raise ImportError(f"JSON 解析錯誤: {e}")


def load_from_file(path: Path) -> dict:
    """Load terms from a local file.

    Returns:
        Dict of source -> target terms
    """
    if not path.exists():
        raise ImportError(f"檔案不存在: {path}")

    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)

            # Handle different formats
            if isinstance(data, dict):
                if "terms" in data:
                    return data["terms"]
                return data
            elif isinstance(data, list):
                return {item["source"]: item["target"] for item in data if "source" in item}

            raise ImportError(f"無法識別的格式: {type(data)}")

    except json.JSONDecodeError as e:
        raise ImportError(f"JSON 解析錯誤: {e}")


def import_terms(
    source: str, existing_terms: Optional[dict] = None, validate: bool = True
) -> ImportResult:
    """Import terms from a URL or file path.

    Args:
        source: URL or file path
        existing_terms: Existing terms dict for conflict detection
        validate: Whether to validate terms

    Returns:
        ImportResult with import statistics and validated terms
    """
    result = ImportResult()
    existing = existing_terms or {}

    # Load terms
    if source.startswith("http://") or source.startswith("https://"):
        raw_terms = load_from_url(source)
    else:
        raw_terms = load_from_file(Path(source))

    result.total = len(raw_terms)

    # Validate each term
    seen = set()
    for src, tgt in raw_terms.items():
        # Check duplicates within this import
        if src in seen:
            result.duplicates += 1
            result.errors.append(f"重複: {src}")
            continue
        seen.add(src)

        if validate:
            is_valid, error = validate_term(src, tgt, existing)
            if not is_valid:
                result.invalid += 1
                if "衝突" in error:
                    result.conflicts += 1
                result.errors.append(f"{src} → {tgt}: {error}")
                continue

        result.valid += 1
        result.terms[src] = tgt

    return result


def save_to_pending(terms: dict, name: str) -> Path:
    """Save terms to pending directory for review.

    Args:
        terms: Dict of source -> target terms
        name: Name for the pending file

    Returns:
        Path to the saved file
    """
    pending_dir = get_pending_dir()

    # Clean up name
    clean_name = re.sub(r"[^\w\-]", "_", name)
    if not clean_name.endswith(".json"):
        clean_name += ".json"

    path = pending_dir / clean_name

    data = {
        "version": "1.0",
        "description": f"匯入於 {__import__('datetime').datetime.now().isoformat()}",
        "status": "pending",
        "terms": terms,
    }

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return path


def list_pending() -> list[dict]:
    """List all pending term files.

    Returns:
        List of dicts with file info
    """
    pending_dir = get_pending_dir()
    results = []

    for path in sorted(pending_dir.glob("*.json")):
        try:
            with open(path, encoding="utf-8") as f:
                data = json.load(f)
                results.append(
                    {
                        "path": path,
                        "name": path.name,
                        "terms_count": len(data.get("terms", {})),
                        "description": data.get("description", ""),
                        "status": data.get("status", "pending"),
                    }
                )
        except (json.JSONDecodeError, IOError):
            continue

    return results


def load_pending(name: str) -> dict:
    """Load a pending term file.

    Args:
        name: Name of the pending file

    Returns:
        Dict with file data including terms
    """
    pending_dir = get_pending_dir()

    if not name.endswith(".json"):
        name += ".json"

    path = pending_dir / name

    if not path.exists():
        raise ImportError(f"待審核檔案不存在: {name}")

    with open(path, encoding="utf-8") as f:
        return json.load(f)


def delete_pending(name: str) -> None:
    """Delete a pending term file.

    Args:
        name: Name of the pending file
    """
    pending_dir = get_pending_dir()

    if not name.endswith(".json"):
        name += ".json"

    path = pending_dir / name

    if path.exists():
        path.unlink()
