import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from sol_mcp.toolcall_bridge import definitions, dispatch, dispatch_openai_tool_call

class BridgeTest(unittest.TestCase):
    def test_allowlist(self):
        self.assertEqual(len(definitions()), 3)
        self.assertEqual(dispatch("run_shell", {"command": "whoami"})["error"], "NOT_ALLOWED")
        self.assertEqual(dispatch("sol_health", {"extra": 1})["error"], "INVALID_SCHEMA")
        self.assertEqual(dispatch("sol_inventory", {"limit": True})["error"], "INVALID_SCHEMA")
        self.assertEqual(dispatch("sol_sha256", "{bad")["error"], "INVALID_JSON")

    def test_openai_compatible(self):
        with tempfile.TemporaryDirectory() as folder:
            Path(folder, "a.txt").write_bytes(b"abc")
            with patch.dict(os.environ, {"SOL_MCP_ROOT": folder}):
                call = {"type": "function", "function": {"name": "sol_sha256",
                        "arguments": json.dumps({"relative_path": "a.txt"})}}
                result = dispatch_openai_tool_call(call)
                self.assertTrue(result["ok"])
                self.assertEqual(result["result"]["bytes"], 3)
                self.assertFalse(dispatch("sol_sha256", {"relative_path": "../escape"})["ok"])

if __name__ == "__main__":
    unittest.main()
