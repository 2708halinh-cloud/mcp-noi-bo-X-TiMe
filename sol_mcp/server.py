"""SOL MCP 2026 tutorial implementation, read-only stdio."""
from mcp.server import MCPServer
from sol_mcp.paths import health, inventory, sha256_file

mcp = MCPServer("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Report server state without exposing credentials."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List a directory under the authorized root; never read file contents."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Compute SHA-256 of a file under the authorized root (64 MiB limit)."""
    return sha256_file(relative_path)

if __name__ == "__main__":
    mcp.run(transport="stdio")
