"""SOL source registry (Python-only; no implicit tool invocation)."""
from __future__ import annotations

REGISTRY = {
    "toolregistry": {"url": "https://github.com/Oaklight/ToolRegistry", "role": "registration_authority", "enabled": False},
    "mcp-cmd": {"url": "https://github.com/developit/mcp-cmd", "role": "optional_mcp_cli", "enabled": False},
    "mindgeniusai": {"url": "https://github.com/xianjianlf2/MindGeniusAI", "role": "mindmap_client", "enabled": False},
    "ogam": {"url": "https://github.com/off-grid-ai/OGAM", "role": "offline_mobile_client", "enabled": False},
    "bbd2api": {"url": "https://github.com/N1nEmAn/bbd2api", "role": "api_format_proxy", "enabled": False},
    "zeroboot": {"url": "https://github.com/zerobootdev/zeroboot", "role": "sandbox_vm_backend", "enabled": False},
    "aorchestra": {"url": "https://github.com/FoundationAgents/AOrchestra", "role": "multiagent_orchestration", "enabled": False},
    "deep-research": {"url": "https://github.com/Cranot/deep-research", "role": "research_worker", "enabled": False},
}

def sources():
    return {"registry_version": 1, "sources": REGISTRY, "automatic_external_execution": False}

def research_plan(trigger: str, question: str):
    """Gating for a research request; never starts external services."""
    if not isinstance(trigger, str) or not isinstance(question, str):
        raise ValueError("INVALID_RESEARCH_REQUEST")
    if trigger.strip().casefold() != "truy tìm":
        return {"activated": False, "reason": "TRIGGER_NOT_MATCHED"}
    if not question.strip():
        raise ValueError("EMPTY_QUESTION")
    return {"activated": True, "mode": "plan_only",
            "worker": "deep-research", "external_runtime_enabled": False,
            "question": question[:2000]}
