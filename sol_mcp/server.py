"""SOL local read-only MCP server with allowlisted Tool_Call bridge."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file
from sol_mcp.toolcall_bridge import dispatch

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Report read-only SOL MCP server state."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List a directory inside the explicitly authorized root."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Compute file SHA-256 beneath root; max 64 MiB."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_toolcall_dispatch(name: str, arguments_json: str = "{}") -> dict:
    """Invoke one of the three read-only SOL functions by OpenAI-compatible name."""
    return dispatch(name, arguments_json)

if __name__ == "__main__":
    mcp.run(transport="stdio")
