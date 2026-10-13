"""SOL Tool_Call integration: source registry, normalized schemas and fail-closed routing.
No dependency on external processes; this is the audit/control plane.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

SOURCES = {
    "rubra": {"upstream": "https://github.com/rubra-ai/rubra", "role": "model", "runtime": "external", "enabled": False},
    "llm-toolcall-proxy": {"upstream": "https://github.com/ziozzang/llm-toolcall-proxy", "role": "format-converter", "runtime": "external", "enabled": False},
    "tanstack-ai": {"upstream": "https://github.com/TanStack/ai", "role": "typescript-client", "runtime": "external", "enabled": False},
    "rgb-fusion-tool": {"upstream": "https://github.com/tylerszabo/RGB-Fusion-Tool", "role": "hardware-adapter", "runtime": "windows", "enabled": False},
    "mcp-context-forge": {"upstream": "https://github.com/IBM/mcp-context-forge", "role": "gateway", "runtime": "external", "enabled": False},
}
READ_ONLY_TOOLS = frozenset({"sol_health", "sol_inventory", "sol_sha256"})

def registry() -> dict[str, Any]:
    return {"sources": SOURCES, "tool_call_runtime": "not_deployed", "external_execution_enabled": False,
            "supported_internal_tools": sorted(READ_ONLY_TOOLS)}

def normalize_call(payload: dict) -> dict[str, Any]:
    """Normalize OpenAI-style function calls to an auditable SOL envelope, without invoking them."""
    import json
    if not isinstance(payload, dict):
        raise ValueError("INVALID_CALL")
    f = payload.get("function")
    if not isinstance(f, dict):
        raise ValueError("FUNCTION_REQUIRED")
    name = f.get("name")
    if not isinstance(name, str) or name not in READ_ONLY_TOOLS:
        raise ValueError("TOOL_NOT_ALLOWLISTED")
    raw = f.get("arguments", "{}")
    args = json.loads(raw) if isinstance(raw, str) else raw
    if not isinstance(args, dict):
        raise ValueError("ARGUMENT_OBJECT_REQUIRED")
    return {"id": str(payload.get("id", ""))[:128], "tool": name, "arguments": args,
            "execution": "disabled_by_default", "source": "tool_call"}

def authorize_call(envelope: dict, approved_tools: set[str] | None = None) -> bool:
    """Explicit allowlist check only, not a substitute for MCP host authorization."""
    return bool(isinstance(envelope, dict) and envelope.get("tool") in (approved_tools or set())
                and envelope.get("tool") in READ_ONLY_TOOLS)
