import unittest
from sol_mcp.sources import sources, detect_research_trigger

class CatalogTest(unittest.TestCase):
    def test_all_sources_present_but_disabled(self):
        data = sources()
        self.assertEqual(len(data["providers"]), 8)
        self.assertFalse(data["automatic_execution"])
        self.assertTrue(all(not x["installed"] and not x["live_verified"]
                            for x in data["providers"].values()))
    def test_research_gate(self):
        event = detect_research_trigger("Truy tìm lịch sử gốc")
        self.assertTrue(event["matched"])
        self.assertEqual(event["execution"], "pending_authorized_runtime")
        self.assertFalse(detect_research_trigger("đồng bộ tệp")["matched"])
    def test_invalid(self):
        with self.assertRaises(ValueError):
            detect_research_trigger(None)
if __name__ == "__main__":
    unittest.main()
