# Break from legacy TOOL_CALL

On 2026-10-14 the clean branch `feat/sol-mcp-toolregistry-clean-20261014` was
created **from main**, rather than from the earlier Tool_Call feature branch.
The first code commit contains **no** `sol_mcp/toolcall.py`,
`sol_mcp/toolcall_bridge.py`, `sol_mcp/toolcall_addons.py`,
or `sol_toolcall_dispatch` MCP endpoint. This is the clean-slate cutover.

The former feature branch stays intact as rollback provenance; it is not
merged or activated. No ChatGPT platform internals are modified.

This repo is a source host, not a deployed MCP server.
