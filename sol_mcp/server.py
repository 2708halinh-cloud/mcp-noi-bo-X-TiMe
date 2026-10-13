"""SOL MCP clean core and evidence-first audit of authorized instructions."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file, root
from sol_mcp.sources import sources, detect_research_trigger
from sol_mcp.multi_agent import approach_source
from sol_mcp.instruction_audit import audit_files

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Return local root status."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List authorized local files."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Hash one authorized local file."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_registry_sources() -> dict:
    """Report configured integration sources."""
    return sources()

@mcp.tool()
def sol_research_route(command: str) -> dict:
    """Route Truy tìm requests as plans, not external execution."""
    return detect_research_trigger(command)

@mcp.tool()
def sol_source_approach(source: str) -> dict:
    """Plan five research roles for a new source."""
    return approach_source(source)

@mcp.tool()
def sol_instruction_audit(relative_files: list[str], workers: int = 5) -> dict:
    """Parallel scan of explicit files beneath authorized SOL_MCP_ROOT."""
    return audit_files(str(root()), relative_files, workers)

if __name__ == "__main__":
    mcp.run(transport="stdio")
