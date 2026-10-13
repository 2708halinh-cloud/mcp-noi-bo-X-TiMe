import hashlib
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from sol_mcp.paths import health, inventory, sha256_file

class TestCore(unittest.TestCase):
    def test_not_configured(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(health()["root_ready"])
    def test_scoped_reads(self):
        with tempfile.TemporaryDirectory() as temp:
            p = Path(temp)
            (p / "sample.txt").write_bytes(b"abc")
            with patch.dict(os.environ, {"SOL_MCP_ROOT": temp}):
                self.assertEqual(inventory()["entries"][0]["name"], "sample.txt")
                self.assertEqual(sha256_file("sample.txt")["sha256"], hashlib.sha256(b"abc").hexdigest())
                with self.assertRaises(ValueError):
                    sha256_file("../outside")
if __name__ == "__main__":
    unittest.main()
