"""Clean SOL MCP core, without the former platform Tool_Call dispatcher."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Local root readiness without revealing credentials."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List direct children inside SOL_MCP_ROOT (read only)."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """SHA256 a file under the authorized root; limit 64 MiB."""
    return sha256_file(relative_path)

if __name__ == "__main__":
    mcp.run(transport="stdio")
