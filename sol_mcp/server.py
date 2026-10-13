"""SOL clean MCP core with source review, Apify normalization, and TP53 biology."""
from mcp.server.fastmcp import FastMCP
from sol_mcp.paths import health, inventory, sha256_file, root
from sol_mcp.sources import sources, detect_research_trigger
from sol_mcp.multi_agent import approach_source
from sol_mcp.instruction_audit import audit_files
from sol_mcp.external_plugins import plugin_catalog
from sol_mcp.apify_rag import normalize_rag_result
from sol_mcp.ai_router_biology import tp53_profile, tp53_residue

mcp = FastMCP("sol-mcp")

@mcp.tool()
def sol_health() -> dict:
    """Return readiness without credentials."""
    return health()

@mcp.tool()
def sol_inventory(relative_path: str = ".", limit: int = 100) -> dict:
    """List authorized directory entries."""
    return inventory(relative_path, limit)

@mcp.tool()
def sol_sha256(relative_path: str) -> dict:
    """Hash one authorized file."""
    return sha256_file(relative_path)

@mcp.tool()
def sol_registry_sources() -> dict:
    """Return external integration catalog."""
    return sources()

@mcp.tool()
def sol_research_route(command: str) -> dict:
    """Identify Truy tìm requests without executing them."""
    return detect_research_trigger(command)

@mcp.tool()
def sol_source_approach(source: str) -> dict:
    """Prepare five-role source analysis plan."""
    return approach_source(source)

@mcp.tool()
def sol_instruction_audit(relative_files: list[str], workers: int = 5) -> dict:
    """Audit explicit local files in limited read-only threads."""
    return audit_files(str(root()), relative_files, workers)

@mcp.tool()
def sol_plugin_catalog() -> dict:
    """Read-only IDA, Redmine, Apify and Haystack integration status."""
    return plugin_catalog()

@mcp.tool()
def sol_apify_rag_normalize(dataset_json: str, max_results: int = 10) -> dict:
    """Normalize untrusted JSON from Apify without calling remote actors."""
    return normalize_rag_result(dataset_json, max_results)

@mcp.tool()
def sol_ai_router_tp53_profile(accession: str = "P04637") -> dict:
    """Return provenance-tagged human TP53 biological/domain profile."""
    return tp53_profile(accession)

@mcp.tool()
def sol_ai_router_tp53_residue(position: int) -> dict:
    """Locate a TP53 residue in the supplied four-domain annotation scheme."""
    return tp53_residue(position)

if __name__ == "__main__":
    mcp.run(transport="stdio")
