"""Additional Tool_Call source adapters: normalization ONLY, no remote calls.
Both upstream projects are optional and never imported or started here.
"""
from __future__ import annotations
import json
from typing import Any
from sol_mcp.toolcall import normalize_call

REGISTERED_SOURCES = {
    "toolgen": {"url": "https://github.com/Reason-Wang/ToolGen", "role": "tool-retrieval", "enabled": False},
    "catgpt-gateway": {"url": "https://github.com/GautamVhavle/CatGPT-Gateway",
                       "role": "openai-compatible-browser-gateway", "enabled": False},
}

def catalog() -> dict[str, Any]:
    return {"sources": REGISTERED_SOURCES, "executables_started": False,
            "auth_or_browser_sessions_forwarded": False}

def normalize_catgpt_tool_call(tool_call: dict[str, Any]) -> dict[str, Any]:
    """Accept only a single OpenAI-compatible function-call item.

    No tool execution here; downstream MCP authorization remains mandatory.
    """
    if not isinstance(tool_call, dict) or tool_call.get("type") != "function":
        raise ValueError("FUNCTION_CALL_REQUIRED")
    return normalize_call(tool_call)

def parse_toolgen_candidates(raw: str) -> dict[str, Any]:
    """Parse virtual tool tokens as untrusted candidates, never as permission.

    ToolGen emits tokens similar to <<Service&&operation>>.
    Do not map arbitrary service names to capabilities automatically.
    """
    if not isinstance(raw, str) or len(raw) > 1024:
        raise ValueError("INVALID_TOOLGEN_TOKEN")
    if not (raw.startswith("<<") and raw.endswith(">>") and raw.count("&&") == 1):
        raise ValueError("INVALID_TOOLGEN_TOKEN")
    service, operation = raw[2:-2].split("&&", 1)
    if not service or not operation or any(ch in service + operation for ch in "<>\r\n"):
        raise ValueError("INVALID_TOOLGEN_TOKEN")
    return {"source": "toolgen", "service": service, "operation": operation,
            "authorized": False, "executed": False}
