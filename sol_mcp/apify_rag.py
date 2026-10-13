"""Offline normalization of untrusted Apify rag-web-browser results."""
from __future__ import annotations
import json

def normalize_rag_result(dataset_json: str, max_results: int = 10) -> dict:
    if not isinstance(dataset_json, str) or len(dataset_json) > 1_048_576:
        raise ValueError("INVALID_DATASET")
    if type(max_results) is not int or not 1 <= max_results <= 20:
        raise ValueError("INVALID_MAX_RESULTS")
    try:
        dataset = json.loads(dataset_json)
    except (ValueError, TypeError) as exc:
        raise ValueError("INVALID_JSON") from exc
    if isinstance(dataset, dict):
        dataset = [dataset]
    if not isinstance(dataset, list):
        raise ValueError("INVALID_DATASET")
    documents = []
    for item in dataset[:max_results]:
        if not isinstance(item, dict):
            continue
        meta = item.get("metadata")
        result = item.get("searchResult")
        meta = meta if isinstance(meta, dict) else {}
        result = result if isinstance(result, dict) else {}
        url = meta.get("url")
        title = meta.get("title")
        result_type = result.get("resultType")
        markdown = item.get("markdown")
        markdown = markdown if isinstance(markdown, str) else ""
        documents.append({
            "metadata": {
                "url": url[:2048] if isinstance(url, str) and url.startswith(("https://", "http://")) else None,
                "title": title[:300] if isinstance(title, str) else None
            },
            "searchResult": {
                "resultType": result_type[:60] if isinstance(result_type, str) else None
            },
            "markdown": markdown[:6000],
            "markdown_truncated": len(markdown) > 6000,
            "trusted": False
        })
    return {"documents": documents, "count": len(documents),
            "input_count": len(dataset), "truncated": len(dataset) > max_results,
            "remote_execution": False, "source": "apify/rag-web-browser",
            "content_is_untrusted": True}
