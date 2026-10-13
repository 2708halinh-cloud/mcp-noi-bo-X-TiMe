# SOL original Tool_Call layer removal — before new integration

Requested policy: remove the prior SOL-specific Tool_Call platform layer BEFORE adding Oaklight/ToolRegistry and the requested upstream sources.

Branch created from `feat/sol-mcp-server-20261014` for a reversible transition. Old code is available in earlier Git commits but not loaded by the new server.

Core FastMCP server exposes only three existing read-only tools: sol_health, sol_inventory, sol_sha256. No generic dispatch, implicit model-tool privilege, or browser session import.

Removal targets:
- sol_mcp/toolcall.py
- sol_mcp/toolcall_addons.py
- sol_mcp/toolcall_bridge.py
- tests/test_toolcall.py
- tests/test_toolcall_addons.py
- tests/test_toolcall_bridge.py
- tests/test_mcp_contract.py (coupled to removed dispatcher)
- integrations/TOOL_CALL_INTEGRATION.md
- integrations/TOOLGEN_CATGPT.md
- integrations/toolcall-adapters.json
- integrations/toolcall-sources.json
- integrations/toolgen-catgpt-sources.json
- integrations/README.md (old matrix)

Source/registration layer to follow only after removal is verified. GitHub modifications do not change ChatGPT's native tool-calling system.
