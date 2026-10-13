# ToolGen and CatGPT-Gateway — SOL Tool_Call

## Sources and semantics
- [Reason-Wang/ToolGen](https://github.com/Reason-Wang/ToolGen) — ICLR 2025 ToolGen research; learns a tool vocabulary as tokens. Example: `<<Service&&operation>>`. It is not an MCP server; ToolBench/StableToolBench, trained models and runtime dependencies are required for live use.
- [GautamVhavle/CatGPT-Gateway](https://github.com/GautamVhavle/CatGPT-Gateway) — OpenAI-compatible API gateway implemented using a logged-in browser session and automated page interaction. Tool calls are parsed from structured model output. It is not a native MCP server. Browser-session reuse and provider policy compliance require separate review.

## Integration implemented
- `sol_mcp/toolcall_addons.py`: source catalog and format-boundary functions.
- CatGPT: normalize OpenAI-compatible calls through SOL's existing strict allowlist.
- ToolGen: parse proposed virtual tokens as untrusted *candidates* (no implicit authorization).
- Unit tests in `tests/test_toolcall_addons.py`.

## Explicitly not enabled
Neither upstream is cloned, installed, executed, authenticated, or deployed. No browser cookies/passwords are read; no HTTP endpoint is opened. No third-party model output may directly invoke filesystem or hardware actions.

To activate any provider later: review its license/terms, select an approved transport, authenticate through the provider's own supported login flow, implement an explicit tool-name map, verify MCP tools/list, and test tools/call with a read-only fixture.
