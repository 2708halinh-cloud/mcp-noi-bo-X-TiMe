"""Cross-host plugin inventory. No installation, execution or credential handling."""
PLUGINS = {
    "meloader": {
        "repo": "https://github.com/embedi/meloader",
        "host": "IDA Pro",
        "purpose": "Intel ME firmware loader",
        "install_target": "<IDA_INSTALL>/loaders/",
        "mcp_server": False, "installed": False, "runtime_verified": False
    },
    "redmine_evm": {
        "repo": "https://github.com/imaginary-cloud/redmine_evm",
        "host": "Redmine / Rails",
        "purpose": "Earned Value Management baseline, cost and performance",
        "install_target": "<REDMINE_ROOT>/plugins/redmine_evm/",
        "mcp_server": False, "installed": False, "runtime_verified": False
    },
    "apify-mcp": {
        "endpoint": "https://mcp.apify.com/",
        "host": "Remote MCP host",
        "purpose": "Apify actors, documentation, runs, storage, tasks, schedules, builds, source, api, rag-web-browser and web-fetch",
        "credentials": "APIFY_API_TOKEN via host secret store",
        "mcp_server": True, "installed": False, "runtime_verified": False
    },
    "haystack-apify-cookbook": {
        "url": "https://haystack.deepset.ai/cookbook/apify_haystack_rag_web_browser",
        "host": "Haystack",
        "purpose": "RAG web browser cookbook / mapping reference",
        "mcp_server": False, "installed": False, "runtime_verified": False
    }
}

def plugin_catalog() -> dict:
    return {"plugins": PLUGINS, "source_catalog_only": True,
            "outside_runtime_started": False, "remote_tools_list_verified": False}
