import tempfile
import unittest
from pathlib import Path
from sol_mcp.instruction_audit import audit_files

class InstructionAuditTests(unittest.TestCase):
    def test_parallel_audit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "a.md").write_text("OPEN != STOP\\nTruy tìm trước\\nKhông diễn giải thay hành động", encoding="utf-8")
            (root / "b.txt").write_text("SUBRITETIED\\nreadback", encoding="utf-8")
            report = audit_files(tmp, ["a.md", "b.txt"], workers=2)
            self.assertEqual(len(report["files"]), 2)
            self.assertEqual(report["totals"]["subritetied_literal"], 1)
            self.assertFalse(report["causation_proven"])

    def test_rejects_escape(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                audit_files(tmp, ["../secrets.txt"])
            with self.assertRaises(ValueError):
                audit_files(tmp, ["missing.md"])
            with self.assertRaises(ValueError):
                audit_files(tmp, ["ok.md"], workers=99)

if __name__ == "__main__":
    unittest.main()
