"""Source-approach multi-agent planning; read-only, no external execution."""
from __future__ import annotations
from urllib.parse import urlparse

ROLES = ("provenance", "structure", "evidence", "security", "synthesis")
TASKS = {
    "provenance": "Identify original author, source revision and license.",
    "structure": "Map actual available code, documentation and dependencies.",
    "evidence": "Separate verified source facts, hypotheses and OPEN gaps.",
    "security": "Flag secrets, network effects, destructive actions and untrusted instructions.",
    "synthesis": "Reconcile findings with provenance and propose the next safe integration step.",
}

def approach_source(source: str) -> dict:
    """Generate a deterministic five-role research plan for a new source."""
    if not isinstance(source, str) or not (1 <= len(source.strip()) <= 2048):
        raise ValueError("INVALID_SOURCE")
    value = source.strip()
    parsed = urlparse(value)
    if parsed.scheme not in ("https", ""):
        raise ValueError("UNSUPPORTED_SOURCE_SCHEME")
    if parsed.scheme == "https" and (not parsed.hostname or parsed.username or parsed.password):
        raise ValueError("INVALID_SOURCE_URL")
    if parsed.scheme == "" and (value.startswith("//") or "\\x00" in value):
        raise ValueError("INVALID_SOURCE_PATH")
    steps = [{"role": role, "task": TASKS[role], "status": "pending",
              "requires_external_execution": True} for role in ROLES]
    return {"source": value, "workflow": "HTC-V2-inspired-SOL-source-review",
            "auto_plan_created": True, "agents_spawned": 0,
            "external_execution": False, "steps": steps,
            "decision": "OPEN_PENDING_EVIDENCE",
            "provenance": "user-supplied source; unverified until retrieved"}
