# SOL MCP integration — ToolRegistry-led architecture

## Mandatory order
1. Reset prior SOL application-level TOOL_CALL on branch feat/sol-registry-replace-toolcall-20261014.
2. Preserve native MCP tools/list + tools/call for protocol compatibility.
3. Record upstreams in a read-only registry (this commit).
4. Install or launch individually only after explicit transport, license, platform, permission and credential verification.

## Sources
- [developit/mcp-cmd](https://github.com/developit/mcp-cmd) — persistent-session MCP CLI. It is a separate Node.js CLI client, not part of this Python MCP server; no install.
- [xianjianlf2/MindGeniusAI](https://github.com/xianjianlf2/MindGeniusAI) — PDF/RAG mind-map UI with tool interaction. Separate application; no install.
- [Oaklight/ToolRegistry](https://github.com/Oaklight/ToolRegistry) — protocol-independent tool management concept; basis of catalog and source registration, not automatically imported as a dependency.
- [off-grid-ai/OGAM](https://github.com/off-grid-ai/OGAM) — offline AI on supported mobile/Mac platforms, with tool-call capabilities. No runtime binding or model deployment.

The additional `sol_registry` MCP tool reports provenance and disabled source states.
`sol_health`, `sol_inventory` and `sol_sha256` remain the only active domain functions.

## Verification
Run `python -m unittest discover -s tests -v`.
With SOL_MCP_ROOT pointing to a safe directory, start `python -m sol_mcp.server` in a supported host.
Verify `tools/list`, call `sol_health` and `sol_registry`. Runtime has NOT been verified on the user host.

## Boundary
No Node install, no Docker, no HTTP exposure, no executing downloaded repos,
no credential collection, and no host-device modification.
