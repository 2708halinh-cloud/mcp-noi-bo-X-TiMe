import unittest
from sol_mcp.registry import catalog, require_registered

class RegistryTests(unittest.TestCase):
    def test_four_sources_are_disabled(self):
        c = catalog()
        self.assertEqual(len(c["sources"]), 4)
        self.assertFalse(c["external_runtime_active"])
        self.assertTrue(all(s["enabled"] is False for s in c["sources"]))

    def test_requires_registered_identity(self):
        self.assertEqual(require_registered("toolregistry")["id"], "toolregistry")
        with self.assertRaises(ValueError):
            require_registered("unknown")

    def test_no_legacy_dispatch(self):
        from sol_mcp import server
        self.assertFalse(hasattr(server, "sol_toolcall_dispatch"))
if __name__ == "__main__":
    unittest.main()
