"""SOL MCP: native protocol tools with a read-only provenance catalog."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file
from sol_mcp.registry import catalog

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Inspect readiness of the SOL MCP server."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List directory under SOL_MCP_ROOT (read-only)."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Hash permitted file under SOL_MCP_ROOT (64 MiB cap)."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_registry() -> dict:
    """Show ToolRegistry-aligned upstream inventory without running third-party code."""
    return catalog()

if __name__ == "__main__":
    mcp.run(transport="stdio")
