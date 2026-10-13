import unittest
from sol_mcp.multi_agent import approach_source, ROLES

class AutoPlanningTest(unittest.TestCase):
    def test_approach_source(self):
        result = approach_source("https://github.com/example/repo")
        self.assertTrue(result["auto_plan_created"])
        self.assertEqual([x["role"] for x in result["steps"]], list(ROLES))
        self.assertEqual(result["agents_spawned"], 0)
        self.assertFalse(result["external_execution"])
    def test_unsafe_urls(self):
        for source in ("file:///etc/passwd", "https://user:pass@example.com/path", ""):
            with self.assertRaises(ValueError):
                approach_source(source)
if __name__ == "__main__":
    unittest.main()
