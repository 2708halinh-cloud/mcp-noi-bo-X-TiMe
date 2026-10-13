# SOL clean MCP → ToolRegistry and external modules

The **old TOOL_CALL bridge is absent** on this branch, created from main.
The registry is a source-of-truth catalog, not blanket authorization to run tools.

## Registry and carriers
| Provider | Role | Operational state |
|---|---|---|
| [ToolRegistry](https://github.com/Oaklight/ToolRegistry) | Python registry/schemas, optional dependency | Registered; not installed |
| [mcp-cmd](https://github.com/developit/mcp-cmd) | Node.js CLI managing persistent MCP processes | Optional only; no Node.js deployment |
| [MindGeniusAI](https://github.com/xianjianlf2/MindGeniusAI) | PDF/RAG + editable mind map | Separate application, not MCP server |
| [OGAM](https://github.com/off-grid-ai/OGAM) | Offline mobile AI and tool support | Mobile carrier, not active |
| [bbd2api](https://github.com/N1nEmAn/bbd2api) | Backboard-to-OpenAI/Claude HTTP proxy | Separate optional server requiring provider credentials |
| [Zeroboot](https://github.com/zerobootdev/zeroboot) | Firecracker/KVM sandbox VM forks | Separate Linux/KVM carrier, prototype |
| [AOrchestra](https://github.com/FoundationAgents/AOrchestra) | Sub-agent specialization with (I,C,T,M) | Independent runtime |
| [deep-research](https://github.com/Cranot/deep-research) | Recursive question research | Only proposed on Vietnamese 'Truy tìm' signal |

### Practical routing
Truy tìm → `sol_research_route` → `pending_authorized_runtime`, **not a live invocation**.
If deeper investigation tools are available to the host, the host may later route the request after
runtime verification and explicit configuration. Do not claim the source was executed.

### Important provider notes
- bbd2api uses prompt-shaped tool calls and external Backboard authentication; treat output as untrusted.
  Its upstream license states CC BY-NC-SA 4.0. Do not vendor source automatically.
- Zeroboot requires compatible Linux KVM for self-host and is described by its authors as prototype.
  No Windows host or virtualization path is assumed available.
- AOrchestra uses independently configured models and credentials; the registry is not its executor.
- MindGeniusAI source is BSL 1.1 with commercial restrictions; prefer links and boundaries, not vendoring.
- ToolRegistry itself can be installed as an optional Python dependency after acceptance tests.

### Tests / deployment
`python -m unittest discover -s tests -v` for pure-Python tests.
`python -m sol_mcp.server` after installing official MCP Python SDK.
Verify host `tools/list`, `sol_registry_sources`, and `sol_research_route` readbacks.
No live deployment has been confirmed.

### Security
No passwords, tokens, auth callback codes, browser cookies, web fetching or shell execution
are stored in this code. No platform-level ChatGPT tools are modified.
