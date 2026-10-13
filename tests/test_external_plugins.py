import json
import unittest
from sol_mcp.external_plugins import plugin_catalog
from sol_mcp.apify_rag import normalize_rag_result

class PluginIntegrationTest(unittest.TestCase):
    def test_catalog_is_not_installed(self):
        data = plugin_catalog()
        self.assertEqual(len(data["plugins"]), 4)
        self.assertFalse(data["remote_tools_list_verified"])
        self.assertTrue(all(not p["runtime_verified"] for p in data["plugins"].values()))
    def test_apify_mapping(self):
        data = [{"metadata": {"url": "https://example.com", "title": "Example"},
                 "searchResult": {"resultType": "ORGANIC"}, "markdown": "# Test"}]
        parsed = normalize_rag_result(json.dumps(data))
        self.assertEqual(parsed["count"], 1)
        doc = parsed["documents"][0]
        self.assertEqual(doc["metadata"]["title"], "Example")
        self.assertEqual(doc["searchResult"]["resultType"], "ORGANIC")
        self.assertEqual(doc["markdown"], "# Test")
        self.assertFalse(doc["trusted"])
    def test_invalid_inputs(self):
        for bad in ("{x", "123", '"abc"'):
            with self.assertRaises(ValueError):
                normalize_rag_result(bad)
        with self.assertRaises(ValueError):
            normalize_rag_result("[]", 999)
    def test_clips_untrusted_markdown(self):
        doc = normalize_rag_result(json.dumps({"metadata": {"url": "file:///sensitive"},
                "markdown": "A" * 7000}))["documents"][0]
        self.assertIsNone(doc["metadata"]["url"])
        self.assertTrue(doc["markdown_truncated"])
if __name__ == "__main__":
    unittest.main()
