# SOL Tool_Call integration matrix

This branch provides a bounded OpenAI-compatible function-tool adapter in
`sol_mcp/toolcall_bridge.py`. It is a library entry point to be used by an
authorized model-tool orchestration host; it does not automatically intercept
ChatGPT or launch external software.

| Source | Integration surface | Status |
|---|---|---|
| [Rubra](https://github.com/rubra-ai/rubra) | Model may emit OpenAI-compatible function tool calls | Adapter source |
| [llm-toolcall-proxy](https://github.com/ziozzang/llm-toolcall-proxy) | Optional model-format conversion proxy upstream of tool dispatcher | Configuration reference, not deployed |
| [TanStack AI](https://github.com/TanStack/ai) | TypeScript SDK can consume the same tool definitions with a separate client implementation | Contract reference, not installed |
| [RGB-Fusion-Tool](https://github.com/tylerszabo/RGB-Fusion-Tool) | Gigabyte RGB hardware control | Source reference only; device control deliberately NOT exposed |
| [IBM MCP Context Forge](https://github.com/IBM/mcp-context-forge) | Optional MCP registry/gateway before SOL MCP | Architecture reference, not deployed |

## Tool Call boundary

```text
Rubra / model server -> optional llm-toolcall-proxy
  -> OpenAI-compatible function tool call
  -> sol_mcp.toolcall_bridge.dispatch_openai_tool_call
  -> allowlisted read-only SOL tools -> structured response
```

The Python MCP server is a separate `stdio` MCP endpoint. Calls from
TanStack AI or a gateway require a configured, authenticated orchestration
host; tool definitions alone do not create a live bridge.

## Local verification

```sh
python -m unittest discover -s tests -v
```

Use `SOL_MCP_ROOT` only for a directory intentionally authorized for
inventory and hashing. No model request can execute arbitrary processes,
write files, change RGB devices, or receive credentials through this adapter.

## Next independent acceptance gates

1. Validate tests and actual MCP SDK import on a Python machine.
2. Start MCP host; confirm `tools/list`.
3. If desired, install a local inference backend and the tool-call proxy,
   pin versions and verify its output format with an explicit dummy tool.
4. For Context Forge, deploy separately with proper authentication and
   do NOT expose a raw unprotected stdio server to the internet.
5. RGB control requires Windows Gigabyte hardware/driver verification,
   device-specific permissions and explicit action approval.

**Source on GitHub is not evidence of a running service.**
