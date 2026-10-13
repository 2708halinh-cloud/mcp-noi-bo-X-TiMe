"""SOL MCP core. No application-level TOOL_CALL foundation or execution router."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Readiness of the read-only MCP core."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List immediate entries below SOL_MCP_ROOT."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Hash file in SOL_MCP_ROOT (64 MiB maximum)."""
    return sha256_file(relative_path)

if __name__ == "__main__":
    mcp.run(transport="stdio")
