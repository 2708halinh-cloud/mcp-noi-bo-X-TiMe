"""SOL MCP server: native FastMCP tools, no legacy Tool_Call dispatcher."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file
from sol_mcp.registry import sources, research_plan

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Read-only status check."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List files inside the authorized directory."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Hash an authorized file."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_registry() -> dict:
    """Read ToolRegistry-based inventory of approved upstream integrations."""
    return sources()

@mcp.tool()
def sol_research_plan(trigger: str, question: str) -> dict:
    """Prepare research only when explicitly asked 'Truy tìm'. Does not run the worker."""
    return research_plan(trigger, question)

if __name__ == "__main__":
    mcp.run(transport="stdio")
