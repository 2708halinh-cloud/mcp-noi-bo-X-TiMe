# SOL — expanded Apify MCP, IDA meloader and Redmine EVM

## Remote Apify MCP URL

https://mcp.apify.com/?tools=actors,docs,runs,storage,tasks,schedules,builds,source,api,apify/rag-web-browser,apify/web-fetch

Eleven tool-family selectors are passed through unchanged. Confirm support using the actual MCP host tools/list.
Keep APIFY_API_TOKEN in the MCP host's secret manager, never in Git or chat.
The supplied npx mcp-remote example is valid for a Node-capable MCP host; this Python-first SOL repository
does not launch Node.js. Configure a remote Streamable HTTP MCP host directly if available.
Actor runs, storage, tasks, schedules, builds and other operations may affect state or incur cost;
only invoke explicitly authorized operations after validating the real tool schema.

## RAG data contract — Apify + Haystack

Reference: https://haystack.deepset.ai/cookbook/apify_haystack_rag_web_browser
Offline normalizer sol_apify_rag_normalize accepts JSON with metadata.url, metadata.title,
searchResult.resultType (if provided), and markdown. It clips results and treats text as untrusted.
No network fetch or actor execution is performed by the normalizer.

## Distinct plugin runtimes

embedi/meloader is an Intel ME firmware loader for IDA, tested on ME 9.x according to its README.
It belongs in an IDA installation's loaders directory, not in ChatGPT/MCP plugins.
Source: https://github.com/embedi/meloader

imaginary-cloud/redmine_evm is a Redmine Earned Value Management plugin with legacy Rails dependencies.
It belongs under redmine_root/plugins/redmine_evm and requires compatibility review before migrations.
Source: https://github.com/imaginary-cloud/redmine_evm

## Status

Source integration only; no IDA plugin or Redmine plugin installed; no Apify expanded MCP connection
verified at this exact URL; no live tools/list, paid actor run, browser crawl or remote write performed.
Validate local Python tests, then run an authorized MCP handshake in the intended host.
