import json
import unittest
from sol_mcp.toolcall import registry, normalize_call, authorize_call

class ToolCallTest(unittest.TestCase):
    def test_sources_fail_closed(self):
        r = registry()
        self.assertEqual(len(r["sources"]), 5)
        self.assertFalse(r["external_execution_enabled"])
        self.assertTrue(all(not source["enabled"] for source in r["sources"].values()))

    def test_normalize_does_not_execute(self):
        call = {"id": "abc", "type": "function",
                "function": {"name": "sol_inventory", "arguments": json.dumps({"relative_path": "."})}}
        envelope = normalize_call(call)
        self.assertEqual(envelope["tool"], "sol_inventory")
        self.assertEqual(envelope["arguments"]["relative_path"], ".")
        self.assertFalse(authorize_call(envelope))
        self.assertTrue(authorize_call(envelope, {"sol_inventory"}))

    def test_blocks_hardware_and_shell(self):
        for name in ("rgb_set_color", "execute_shell", "posthog_admin"):
            with self.assertRaises(ValueError):
                normalize_call({"function": {"name": name, "arguments": "{}"}})

    def test_argument_validation(self):
        with self.assertRaises(ValueError):
            normalize_call({"function": {"name": "sol_health", "arguments": "[]"}})
        with self.assertRaises(ValueError):
            normalize_call({"function": {"name": "sol_health", "arguments": "not-json"}})

if __name__ == "__main__":
    unittest.main()
