import unittest
from sol_mcp.ai_router_biology import tp53_profile, tp53_residue

class TP53ProfileTests(unittest.TestCase):
    def test_domain_lengths_and_coverage(self):
        item = tp53_profile()
        self.assertEqual(item["length_aa"], 393)
        self.assertEqual([d["length_aa"] for d in item["domains"]], [40,191,32,31])
        self.assertEqual(item["coverage"]["annotated_amino_acids"], 294)
        self.assertEqual(item["coverage"]["unassigned_in_this_four_domain_scheme"], 99)
        self.assertEqual(item["experimental_reference"]["pdb"], "1TUP")

    def test_boundaries(self):
        for residue, expected in [(1,"TAD1"),(40,"TAD1"),(102,"DBD"),
                                  (292,"DBD"),(325,"TET"),(356,"TET"),
                                  (363,"CTD"),(393,"CTD")]:
            self.assertEqual(tp53_residue(residue)["domains"][0]["id"], expected)
        self.assertEqual(tp53_residue(41)["domains"], [])
        self.assertEqual(tp53_residue(357)["domains"], [])

    def test_range_and_accession(self):
        for position in (0,394,True,"100"):
            with self.assertRaises(ValueError):
                tp53_residue(position)
        with self.assertRaises(ValueError):
            tp53_profile("P04638")

if __name__ == "__main__":
    unittest.main()
