"""SOL external integration catalog and explicit Vietnamese research trigger.

Catalog does not spawn processes, fetch secrets or execute third-party code.
"""
from __future__ import annotations

SOURCES = {"mcp-cmd":{"url":"https://github.com/developit/mcp-cmd","role":"persistent-mcp-cli","carrier":"node-optional","mode":"manual-only","installed":False,"live_verified":False},"MindGeniusAI":{"url":"https://github.com/xianjianlf2/MindGeniusAI","role":"document-to-editable-mindmap","carrier":"separate-app","mode":"disabled","installed":False,"live_verified":False},"ToolRegistry":{"url":"https://github.com/Oaklight/ToolRegistry","role":"tool-catalog-python","carrier":"optional-local","mode":"registry-only","installed":False,"live_verified":False},"OGAM":{"url":"https://github.com/off-grid-ai/OGAM","role":"mobile-offline-ai","carrier":"mobile-app","mode":"disabled","installed":False,"live_verified":False},"bbd2api":{"url":"https://github.com/N1nEmAn/bbd2api","role":"external-model-api-proxy","carrier":"external-http","mode":"disabled","installed":False,"live_verified":False},"zeroboot":{"url":"https://github.com/zerobootdev/zeroboot","role":"kvm-firecracker-isolated-sandbox","carrier":"linux-kvm","mode":"disabled","installed":False,"live_verified":False},"AOrchestra":{"url":"https://github.com/FoundationAgents/AOrchestra","role":"subagent-orchestration","carrier":"optional-local","mode":"disabled","installed":False,"live_verified":False},"deep-research":{"url":"https://github.com/Cranot/deep-research","role":"recursive-research","carrier":"optional-local","mode":"trigger-only","installed":False,"live_verified":False}}

def sources():
    return {"registry": "Oaklight/ToolRegistry", "providers": SOURCES,
            "external_runtime": "not_verified", "automatic_execution": False}

def detect_research_trigger(command: str):
    if not isinstance(command, str):
        raise ValueError("COMMAND_MUST_BE_STRING")
    clean = command.strip()
    if not clean:
        return {"matched": False, "action": "none"}
    matched = clean.casefold().startswith("truy tìm")
    return {"matched": matched, "action": "request_deep_research" if matched else "none",
            "provider": "Cranot/deep-research" if matched else None,
            "execution": "pending_authorized_runtime" if matched else "none"}
