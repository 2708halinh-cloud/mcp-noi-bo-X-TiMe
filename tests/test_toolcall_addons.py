import unittest
from sol_mcp.toolcall_addons import (
    catalog, normalize_catgpt_tool_call, parse_toolgen_candidates
)

class IntegrationBoundaryTests(unittest.TestCase):
    def test_sources_disabled(self):
        c = catalog()
        self.assertEqual(len(c["sources"]), 2)
        self.assertTrue(all(not x["enabled"] for x in c["sources"].values()))

    def test_catgpt_normalize(self):
        a = normalize_catgpt_tool_call({"type": "function", "id": "1",
            "function": {"name": "sol_health", "arguments": "{}"}})
        self.assertEqual(a["tool"], "sol_health")
        self.assertEqual(a["execution"], "disabled_by_default")

    def test_catgpt_denies_shell(self):
        with self.assertRaises(ValueError):
            normalize_catgpt_tool_call({"type":"function",
                "function":{"name":"bash","arguments":"{}"}})

    def test_toolgen_token_only(self):
        r = parse_toolgen_candidates("<<Weather&&current>>")
        self.assertFalse(r["authorized"])
        self.assertFalse(r["executed"])

    def test_toolgen_bad_format(self):
        for raw in ("", "shell", "<<foo&&>>", "<<a&&b&&c>>"):
            with self.assertRaises(ValueError):
                parse_toolgen_candidates(raw)

if __name__ == "__main__":
    unittest.main()
