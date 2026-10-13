import hashlib
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from sol_mcp.paths import health, inventory, sha256_file

class ScopedToolsTest(unittest.TestCase):
    def test_missing_configuration(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(health()["root_ready"])

    def test_tools(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / "example.txt").write_bytes(b"abc")
            (p / "nested").mkdir()
            with patch.dict(os.environ, {"SOL_MCP_ROOT": d}):
                self.assertEqual(len(inventory()["entries"]), 2)
                self.assertEqual(sha256_file("example.txt")["sha256"], hashlib.sha256(b"abc").hexdigest())
                with self.assertRaises(ValueError):
                    sha256_file("../outside")
                with self.assertRaises(ValueError):
                    inventory(".", 201)

if __name__ == "__main__":
    unittest.main()
