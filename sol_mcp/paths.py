"""Read-only file helpers bounded by explicitly configured SOL_MCP_ROOT."""
from __future__ import annotations
import hashlib
import os
from pathlib import Path

def root() -> Path:
    value = os.environ.get("SOL_MCP_ROOT", "").strip()
    if not value:
        raise ValueError("SOL_MCP_ROOT_NOT_CONFIGURED")
    candidate = Path(value).expanduser().resolve(strict=True)
    if not candidate.is_dir():
        raise ValueError("ROOT_NOT_DIRECTORY")
    return candidate

def safe(relative: str) -> Path:
    allowed = root()
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError("INVALID_RELATIVE_PATH")
    target = (allowed / relative).resolve(strict=True)
    if not target.is_relative_to(allowed):
        raise ValueError("OUTSIDE_ROOT_DENIED")
    return target

def health() -> dict:
    try:
        root()
        ready = True
    except (OSError, ValueError):
        ready = False
    return {"name": "sol-mcp", "root_ready": ready, "read_only": True}

def inventory(relative_path: str = ".", limit: int = 100) -> dict:
    if type(limit) is not int or not 1 <= limit <= 200:
        raise ValueError("LIMIT_OUT_OF_RANGE")
    directory = safe(relative_path)
    if not directory.is_dir():
        raise ValueError("NOT_A_DIRECTORY")
    children = []
    with os.scandir(directory) as iterator:
        for entry in iterator:
            if len(children) >= limit:
                break
            if entry.is_symlink():
                continue
            children.append({"name": entry.name, "kind": "directory" if entry.is_dir(follow_symlinks=False) else "file",
                             "bytes": entry.stat(follow_symlinks=False).st_size if entry.is_file(follow_symlinks=False) else None})
    children.sort(key=lambda x: x["name"].casefold())
    return {"entries": children, "possibly_truncated": len(children) == limit}

def sha256_file(relative_path: str) -> dict:
    file = safe(relative_path)
    if not file.is_file() or file.stat().st_size > 64 * 1024 * 1024:
        raise ValueError("NOT_FILE_OR_TOO_LARGE")
    digest = hashlib.sha256()
    with file.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return {"relative_path": relative_path, "bytes": file.stat().st_size, "sha256": digest.hexdigest()}
