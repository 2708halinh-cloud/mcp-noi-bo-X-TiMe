# SOL ToolRegistry rebuild

**Order:** Prior SOL Tool_Call dispatchers removed on this branch; now integrate a new native MCP tool registry.
The old implementation remains recoverable in Git history. This does not change ChatGPT's internal tool calls.

**Sổ tay**: [Oaklight ToolRegistry](https://github.com/Oaklight/ToolRegistry) for protocol-agnostic tool registration and permissions. In this stage the Python-only native FastMCP interface remains the actual registry; Oaklight's package has not yet been installed, so do not claim its runtime is active.

- [mcp-cmd](https://github.com/developit/mcp-cmd): optional persistent CLI; Node.js dependency, not installed.
- [MindGeniusAI](https://github.com/xianjianlf2/MindGeniusAI): editable mind maps from PDF, self-hosted. BSL 1.1; avoid vendoring.
- [OGAM](https://github.com/off-grid-ai/OGAM): mobile/on-device client; no APK built.
- [bbd2api](https://github.com/N1nEmAn/bbd2api): Backboard proxy (Claude/OpenAI schemas), CC BY-NC-SA 4.0, not started. Avoid browser credential/cookie proxying.
- [zeroboot](https://github.com/zerobootdev/zeroboot): VM isolation backend reference. No VM booted.
- [AOrchestra](https://github.com/FoundationAgents/AOrchestra): multi-agent orchestration reference. No agents spawned.
- [deep-research](https://github.com/Cranot/deep-research): recursive research worker; **only considered upon exact user trigger "Truy tìm"**. The MCP sol_research_plan tool is deliberately plan-only.

## Existing SOL native MCP endpoints

sol_health, sol_inventory, sol_sha256, sol_registry, sol_research_plan.
Only the first three touch local files; they remain scoped to SOL_MCP_ROOT and read-only. Registering upstreams never authorizes them to execute.

## Verification gates
1. Run: python -m unittest discover -s tests -v
2. Install Python MCP SDK and start: python -m sol_mcp.server
3. From a compatible host, verify tools/list and tools/call.
4. VM, API proxy, research service, UI client require separate setup and runtime evidence.
