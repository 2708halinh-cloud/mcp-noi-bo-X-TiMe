"""SOL source registry. This is NOT an application-level TOOL_CALL executor."""
from __future__ import annotations
import json
from pathlib import Path

APPROVED_PROTOCOL_TOOLS = ("sol_health", "sol_inventory", "sol_sha256")
SOURCES = (
    {"id": "mcp-cmd", "repository": "https://github.com/developit/mcp-cmd", "role": "MCP client CLI", "enabled": False},
    {"id": "mindgeniusai", "repository": "https://github.com/xianjianlf2/MindGeniusAI", "role": "PDF RAG / mind map UI", "enabled": False},
    {"id": "toolregistry", "repository": "https://github.com/Oaklight/ToolRegistry", "role": "Protocol-agnostic catalog", "enabled": False},
    {"id": "ogam", "repository": "https://github.com/off-grid-ai/OGAM", "role": "Offline inference on supported devices", "enabled": False},
)

def catalog():
    """Return provenance; external tools are references until installed and verified."""
    return {"schema": "sol.mcp.registry.v1", "sources": [dict(x) for x in SOURCES],
            "native_mcp_tools": list(APPROVED_PROTOCOL_TOOLS), "external_runtime_active": False}

def require_registered(source: str) -> dict:
    """Validate identity, not authority to call or execute tools."""
    for row in SOURCES:
        if row["id"] == source:
            return dict(row)
    raise ValueError("UNREGISTERED_SOURCE")
