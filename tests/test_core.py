import hashlib
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from sol_mcp.paths import health, inventory, sha256_file

class CoreTests(unittest.TestCase):
    def test_no_root(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(health()["root_ready"])

    def test_scoped_tools(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "a.txt").write_bytes(b"abc")
            with patch.dict(os.environ, {"SOL_MCP_ROOT": temp}):
                self.assertEqual(inventory()["entries"][0]["name"], "a.txt")
                self.assertEqual(sha256_file("a.txt")["sha256"], hashlib.sha256(b"abc").hexdigest())
                with self.assertRaises(ValueError):
                    sha256_file("../secret")
                with self.assertRaises(ValueError):
                    inventory(".", 201)
if __name__ == "__main__":
    unittest.main()
