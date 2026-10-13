import ast
from pathlib import Path
import unittest

class SourceContractTest(unittest.TestCase):
    def test_server_python_syntax_and_registration(self):
        p = Path(__file__).resolve().parents[1] / "sol_mcp" / "server.py"
        tree = ast.parse(p.read_text(encoding="utf-8"))
        fnames = {n.name for n in ast.walk(tree) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))}
        self.assertTrue({"sol_health", "sol_inventory", "sol_sha256", "sol_toolcall_dispatch"}.issubset(fnames))

if __name__ == "__main__":
    unittest.main()
