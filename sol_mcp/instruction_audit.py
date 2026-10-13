"""Parallel, evidence-first audit of user-authorized local text files.

No private platform instructions, network access or subprocess execution.
Results are indicators to investigate, not findings of causation.
"""
from __future__ import annotations
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
import os
import re

PATTERNS = {
    "memory_context": r"\\b(memory|context|forget|reset|amnesia)\\b|ký ức|mất trí nhớ|quên ngữ cảnh",
    "subritetied_literal": r"subritetied",
    "open_nonterminal": r"\\bOPEN\\b|truy tìm trước|chưa đủ bằng chứng",
    "apology_explanation": r"nhận lỗi|xin lỗi|diễn giải|giải thích|\\b(apologize|sorry|explain)\\b",
    "action_readback": r"readback|kiểm chứng|xác minh|thực hiện|\\b(action|receipt|execute)\\b",
}
COMPILED = {key: re.compile(value, re.IGNORECASE) for key, value in PATTERNS.items()}
EXTENSIONS = frozenset({".md", ".txt", ".toml", ".yaml", ".yml", ".json", ".py"})
LIMIT_FILES = 200
LIMIT_BYTES = 2 * 1024 * 1024
MAX_WORKERS = 5

def _scan_one(path: Path, allowed_root: Path) -> dict:
    # Recheck the root immediately before reading; reject symbolic links.
    if path.is_symlink() or not path.resolve(strict=True).is_relative_to(allowed_root):
        return {"path": path.name, "status": "SKIPPED_PATH"}
    try:
        if path.stat().st_size > LIMIT_BYTES:
            return {"path": path.relative_to(allowed_root).as_posix(), "status": "SKIPPED_SIZE"}
        data = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return {"path": path.name, "status": "UNREADABLE"}
    lines = data.splitlines()
    matches = {key: [] for key in COMPILED}
    for number, line in enumerate(lines, 1):
        for key, expression in COMPILED.items():
            if expression.search(line):
                matches[key].append(number)
    return {"path": path.relative_to(allowed_root).as_posix(), "status": "SCANNED",
            "line_count": len(lines), "indicators": {key: {"count": len(value), "lines": value[:50]} for key, value in matches.items()}}

def audit_files(root: str, relative_files: list[str], workers: int = 5) -> dict:
    """Scan explicit user-controlled file paths in parallel. Never crawls arbitrary filesystem."""
    if not isinstance(relative_files, list) or not 1 <= len(relative_files) <= LIMIT_FILES:
        raise ValueError("FILES_OUT_OF_RANGE")
    if type(workers) is not int or not 1 <= workers <= MAX_WORKERS:
        raise ValueError("WORKER_LIMIT")
    base = Path(root).expanduser().resolve(strict=True)
    if not base.is_dir():
        raise ValueError("INVALID_ROOT")
    paths = []
    for name in relative_files:
        if not isinstance(name, str) or not name or ".." in Path(name).parts or Path(name).is_absolute():
            raise ValueError("INVALID_FILE_NAME")
        candidate = base / name
        if candidate.is_symlink() or not candidate.is_file() or candidate.suffix.lower() not in EXTENSIONS:
            raise ValueError("UNSUPPORTED_OR_MISSING_FILE")
        if not candidate.resolve(strict=True).is_relative_to(base):
            raise ValueError("OUTSIDE_ROOT")
        paths.append(candidate)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        results = list(pool.map(lambda item: _scan_one(item, base), paths))
    totals = {category: sum(item.get("indicators", {}).get(category, {}).get("count", 0) for item in results) for category in COMPILED}
    return {"status": "EVIDENCE_INDICATORS_ONLY", "files": results, "totals": totals,
            "no_platform_hidden_instructions_access": True, "causation_proven": False,
            "execution": "read_only_parallel_thread_scan"}
