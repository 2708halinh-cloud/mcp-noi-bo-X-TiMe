import unittest
from sol_mcp.registry import sources, research_plan

class RegistryTest(unittest.TestCase):
    def test_registered(self):
        data = sources()
        self.assertEqual(len(data["sources"]), 8)
        self.assertTrue(all(not v["enabled"] for v in data["sources"].values()))
        self.assertFalse(data["automatic_external_execution"])

    def test_research_is_explicit(self):
        self.assertFalse(research_plan("Find", "test")["activated"])
        self.assertTrue(research_plan("Truy tìm", "evidence")["activated"])
        self.assertFalse(research_plan("Truy tìm", "evidence")["external_runtime_enabled"])
        with self.assertRaises(ValueError):
            research_plan("Truy tìm", "")

if __name__ == "__main__":
    unittest.main()
