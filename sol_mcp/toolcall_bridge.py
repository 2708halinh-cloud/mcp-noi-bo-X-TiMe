"""Allowlisted OpenAI/Rubra/TanStack tool-call bridge (no model-side privilege)."""
import json
from sol_mcp.paths import health, inventory, sha256_file

_HANDLERS = {
    "sol_health": (health, frozenset(), frozenset()),
    "sol_inventory": (inventory, frozenset(("relative_path", "limit")), frozenset()),
    "sol_sha256": (sha256_file, frozenset(("relative_path",)), frozenset(("relative_path",))),
}

def definitions():
    def wrap(name, desc, properties, required):
        return {"type": "function", "function": {"name": name, "description": desc,
                "parameters": {"type": "object", "properties": properties,
                               "required": required, "additionalProperties": False}}}
    return [
        wrap("sol_health", "Read-only health check", {}, []),
        wrap("sol_inventory", "List authorized directory entries", {
             "relative_path": {"type": "string"}, "limit": {"type": "integer", "minimum": 1, "maximum": 200}}, []),
        wrap("sol_sha256", "Hash one authorized file (max 64 MiB)", {
             "relative_path": {"type": "string"}}, ["relative_path"]),
    ]

def dispatch(name, arguments=None):
    if name not in _HANDLERS:
        return {"ok": False, "error": "NOT_ALLOWED"}
    if arguments is None:
        arguments = {}
    if isinstance(arguments, str):
        try:
            arguments = json.loads(arguments)
        except (ValueError, TypeError):
            return {"ok": False, "error": "INVALID_JSON"}
    if not isinstance(arguments, dict):
        return {"ok": False, "error": "INVALID_ARGUMENTS"}
    fn, allowed, required = _HANDLERS[name]
    if not required.issubset(arguments) or not set(arguments).issubset(allowed):
        return {"ok": False, "error": "INVALID_SCHEMA"}
    if "relative_path" in arguments and not isinstance(arguments["relative_path"], str):
        return {"ok": False, "error": "INVALID_SCHEMA"}
    if "limit" in arguments and (type(arguments["limit"]) is not int or not 1 <= arguments["limit"] <= 200):
        return {"ok": False, "error": "INVALID_SCHEMA"}
    try:
        return {"ok": True, "result": fn(**arguments)}
    except (OSError, ValueError, TypeError):
        return {"ok": False, "error": "OPERATION_REJECTED"}

def dispatch_openai_tool_call(tool_call):
    if not isinstance(tool_call, dict):
        return {"ok": False, "error": "INVALID_TOOL_CALL"}
    func = tool_call.get("function")
    if tool_call.get("type") != "function" or not isinstance(func, dict):
        return {"ok": False, "error": "INVALID_TOOL_CALL"}
    return dispatch(func.get("name"), func.get("arguments"))
