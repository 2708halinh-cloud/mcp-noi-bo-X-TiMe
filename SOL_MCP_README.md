# SOL MCP server — read-only source

Following https://modelcontextprotocol.io/docs/2026-07-28/develop/build-server

Python >= 3.10 and MCP SDK >= 2.0. No Node.js. Three tools:
sol_health, sol_inventory, sol_sha256.

### Local start

1. Clone branch feat/sol-mcp-server-20261014 of https://github.com/2708halinh-cloud/mcp-noi-bo-X-TiMe
2. cd mcp-noi-bo-X-TiMe
3. uv sync
4. Set SOL_MCP_ROOT to an existing, explicitly authorized directory that has no credentials.
5. uv run python -m sol_mcp.server
6. Configure the MCP host using mcp.client.example.json with absolute paths.
7. Run tests: uv run python -m unittest discover -s tests -v.
8. From the MCP host, verify tools/list and call sol_health.

### Guarantees and limits

STDIO transport only. No filesystem write tools, no shell execution, no external network access.
Paths must remain under SOL_MCP_ROOT, symlink directory entries are skipped.
SHA-256 limited to 64 MiB per file. Files are not uploaded to GitHub.
Do not store tokens or OAuth callback codes in this repo.
GitHub hosts the source code, not an always-running server. Runtime and host
connection must be independently verified.
