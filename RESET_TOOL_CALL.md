# Phase 1: replace platform TOOL_CALL scaffold (completed in this branch)

Created from the repository's main branch, not the earlier feature branch. The previous SOL-specific TOOL_CALL layer is deliberately **not brought forward**:
- sol_mcp/toolcall.py
- sol_mcp/toolcall_bridge.py
- sol_mcp/toolcall_addons.py
- sol_toolcall_dispatch MCP tool
- old integrations/toolcall* metadata and tests

The MCP protocol's native tools/list and tools/call cannot be removed without breaking MCP, and have NOT been removed. This reset targets only the custom application-level dispatcher. Old commits remain in Git history for provenance but are not in this branch's tree.

This branch's baseline provides only sol_health, sol_inventory and sol_sha256, using the Python MCP SDK. No command execution, device access, remote HTTP endpoint or credentials.

Run: python -m unittest discover -s tests -v
Host: SOL_MCP_ROOT=/authorized/path python -m sol_mcp.server
