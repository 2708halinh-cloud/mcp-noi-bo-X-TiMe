"""SOL MCP core: read-only scoped tools. No legacy Tool_Call dispatcher."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Report the local SOL MCP server state."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List authorized directory entries without reading their contents."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Compute SHA-256 of an authorized file under the size limit."""
    return sha256_file(relative_path)

if __name__ == "__main__":
    mcp.run(transport="stdio")
