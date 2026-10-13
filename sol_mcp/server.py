"""SOL MCP core: no platform Tool_Call dispatch or proxy."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Return readiness without secrets."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List immediate entries within the configured SOL_MCP_ROOT."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Calculate SHA-256 of an authorized file."""
    return sha256_file(relative_path)

if __name__ == "__main__":
    mcp.run(transport="stdio")
