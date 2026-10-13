"""SOL MCP clean core with read-only ToolRegistry/source discovery."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file
from sol_mcp.sources import sources, detect_research_trigger

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Read-only local readiness check."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List direct children under SOL_MCP_ROOT."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """SHA256 an authorized file; size limit 64 MiB."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_registry_sources() -> dict:
    """Read-only catalog of external integrations and their true activation status."""
    return sources()

@mcp.tool()
def sol_research_route(command: str) -> dict:
    """Recognize 'Truy tìm' without executing external software."""
    return detect_research_trigger(command)

if __name__ == "__main__":
    mcp.run(transport="stdio")
