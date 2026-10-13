"""SOL read-only file inventory, bounded to SOL_MCP_ROOT."""
import hashlib
import os
from pathlib import Path

def root():
    value = os.environ.get("SOL_MCP_ROOT", "").strip()
    if not value:
        raise ValueError("SOL_MCP_ROOT_NOT_CONFIGURED")
    path = Path(value).expanduser().resolve(strict=True)
    if not path.is_dir():
        raise ValueError("ROOT_NOT_DIRECTORY")
    return path

def safe(relative):
    r = root()
    p = Path(relative)
    if not relative or p.is_absolute() or ".." in p.parts:
        raise ValueError("INVALID_RELATIVE_PATH")
    target = (r / p).resolve(strict=True)
    if not target.is_relative_to(r):
        raise ValueError("OUTSIDE_ROOT_DENIED")
    return target

def health():
    try:
        root()
        ready = True
    except (ValueError, OSError):
        ready = False
    return {"name": "sol-mcp", "root_ready": ready, "read_only": True, "transport": "stdio"}

def inventory(relative_path=".", limit=100):
    if not (1 <= limit <= 200):
        raise ValueError("LIMIT_OUT_OF_RANGE")
    r = root()
    directory = safe(relative_path)
    if not directory.is_dir():
        raise ValueError("NOT_A_DIRECTORY")
    output = []
    with os.scandir(directory) as stream:
        for entry in stream:
            if len(output) >= limit:
                break
            if entry.is_symlink():
                continue
            output.append({"name": entry.name,
                           "kind": "directory" if entry.is_dir(follow_symlinks=False) else "file",
                           "bytes": entry.stat(follow_symlinks=False).st_size if entry.is_file(follow_symlinks=False) else None})
    return {"path": str(directory.relative_to(r)), "entries": sorted(output, key=lambda e: e["name"].casefold()),
            "possibly_truncated": len(output) == limit}

def sha256_file(relative_path):
    f = safe(relative_path)
    if not f.is_file() or f.stat().st_size > 64 * 1024 * 1024:
        raise ValueError("NOT_FILE_OR_TOO_LARGE")
    h = hashlib.sha256()
    with f.open("rb") as inp:
        for chunk in iter(lambda: inp.read(1024 * 1024), b""):
            h.update(chunk)
    return {"path": relative_path, "sha256": h.hexdigest(), "bytes": f.stat().st_size}
