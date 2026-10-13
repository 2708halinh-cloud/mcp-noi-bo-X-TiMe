# SOL Tool_Call — integration boundary

Sources: Rubra, ziozzang/llm-toolcall-proxy, TanStack/ai,
tylerszabo/RGB-Fusion-Tool, IBM/mcp-context-forge.

## Architecture

Client (optional TanStack AI) -> model (optional Rubra) -> tool-call normalization
(optional ziozzang proxy) -> SOL MCP tool registry -> (optional IBM ContextForge gateway).
RGB Fusion is **hardware-specific**, not an MCP provider, and is DISABLED until explicitly
installed on a supported Gigabyte Windows device with an approved per-action tool.

## Included in this commit
- Source/provenance manifest, five registry references.
- Two MCP tool interfaces: sol_toolcall_sources and sol_toolcall_normalize.
- OpenAI function-call envelope parsing and strict three-tool allowlist, no execution.
- Unit tests against unknown tool names, malformed arguments, and disabled sources.
- Fixes main server import to Python SDK FastMCP.

## Not claimed
- Not vendoring, cloning, building or launching the upstreams.
- Not installing the TanStack JS toolchain in this Python-only server.
- Not starting ContextForge or a remote HTTP MCP endpoint.
- Not launching RGB device executables or granting hardware write access.
- Not authenticating a model gateway or calling live upstream APIs.

## Use
With the source branch checked out and Python MCP SDK installed:
run `python -m unittest discover -s tests -v`, then start
`python -m sol_mcp.server` with an explicitly permitted SOL_MCP_ROOT.
Verify MCP tools/list and call sol_toolcall_sources. No tokens go to Git.

## Provenance
https://github.com/rubra-ai/rubra
https://github.com/ziozzang/llm-toolcall-proxy
https://github.com/TanStack/ai
https://github.com/tylerszabo/RGB-Fusion-Tool
https://github.com/IBM/mcp-context-forge
