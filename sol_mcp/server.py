"""SOL read-only MCP (stdio). Third-party Tool_Call sources are registry-only."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file
from sol_mcp.toolcall import registry, normalize_call

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Report server readiness without credentials."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """Read-only listing under explicitly configured SOL_MCP_ROOT."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Compute SHA-256 for an authorized file up to 64 MiB."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_toolcall_sources() -> dict:
    """Read-only provenance/availability for five Tool_Call sources."""
    return registry()

@mcp.tool()
def sol_toolcall_normalize(function_call_json: str) -> dict:
    """Parse and validate a tool call WITHOUT running it or any external software."""
    import json
    return normalize_call(json.loads(function_call_json))

if __name__ == "__main__":
    mcp.run(transport="stdio")
