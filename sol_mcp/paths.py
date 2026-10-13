"""Constrained, read-only SOL filesystem helpers."""
from __future__ import annotations
import hashlib
import os
from pathlib import Path

def _root():
    value = os.environ.get("SOL_MCP_ROOT", "").strip()
    if not value:
        raise ValueError("ROOT_NOT_CONFIGURED")
    p = Path(value).expanduser().resolve(strict=True)
    if not p.is_dir():
        raise ValueError("ROOT_NOT_DIR")
    return p

def _path(relative):
    if not isinstance(relative, str) or not relative:
        raise ValueError("INVALID_RELATIVE_PATH")
    candidate = Path(relative)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError("INVALID_RELATIVE_PATH")
    root = _root()
    p = (root / candidate).resolve(strict=True)
    if not p.is_relative_to(root):
        raise ValueError("OUTSIDE_ROOT")
    return p

def health():
    try:
        _root()
        ready = True
    except (ValueError, OSError):
        ready = False
    return {"server": "sol-mcp", "root_ready": ready, "read_only": True}

def inventory(relative_path=".", limit=100):
    if type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError("INVALID_LIMIT")
    directory = _path(relative_path)
    if not directory.is_dir():
        raise ValueError("NOT_DIRECTORY")
    entries = []
    with os.scandir(directory) as scan:
        for e in scan:
            if len(entries) >= limit:
                break
            if e.is_symlink():
                continue
            entries.append({"name": e.name,
                            "kind": "dir" if e.is_dir(follow_symlinks=False) else "file",
                            "bytes": e.stat(follow_symlinks=False).st_size if e.is_file(follow_symlinks=False) else None})
    entries.sort(key=lambda e: e["name"].casefold())
    return {"relative_path": relative_path, "entries": entries, "may_have_more": len(entries) >= limit}

def sha256_file(relative_path):
    p = _path(relative_path)
    if not p.is_file() or p.stat().st_size > 64 * 1024 * 1024:
        raise ValueError("NOT_A_FILE_OR_TOO_LARGE")
    h = hashlib.sha256()
    with p.open("rb") as stream:
        for block in iter(lambda: stream.read(1048576), b""):
            h.update(block)
    return {"path": relative_path, "bytes": p.stat().st_size, "sha256": h.hexdigest()}
