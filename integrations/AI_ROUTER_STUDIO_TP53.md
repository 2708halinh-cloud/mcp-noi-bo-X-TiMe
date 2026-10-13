# AI Router Studio / SOL MCP — TP53 (P04637)

## Sources

- UniProtKB reviewed human p53 P04637: https://rest.uniprot.org/uniprotkb/P04637.json
- RCSB 1TUP (DNA-binding core complex, X-ray diffraction, 2.20 angstrom): https://www.rcsb.org/structure/1TUP
- AlphaFold Protein Structure Database model search: https://alphafold.ebi.ac.uk/search/text/P04637

## Evidence-aware separation

FACT: human TP53 accession P04637, 393-aa canonical reference, tumor-suppressing
transcription factor, apoptosis and cell-cycle regulation; experimental structure
1TUP is a partial DNA-binding-core complex, not full-length p53.

USER SUPPLIED: four requested intervals: TAD1 1-40, DNA-binding core 102-292,
tetramerization 325-356, C-terminal regulatory 363-393.
Only the 102-292 core range is corroborated directly by the RCSB source summary.
Other region boundaries are a convenient user-specific mapping and may differ
from annotation conventions in primary literature and structural databases.
All 4 intervals are inclusive. Together: 294 aa. Remaining: 99 aa. An unassigned
interval in this partial mapping does NOT imply that residues are functionless.

## SOL MCP tools

- sol_ai_router_tp53_profile(accession='P04637')
- sol_ai_router_tp53_residue(position=175)

The module is static local data and functions. It does not query UniProt or AlphaFold
on demand and does not expose a live external AI Router Studio deployment.
No medical diagnosis, mutation pathogenicity assessment, protein simulation
or molecular dynamics claims are made.

## Test

python -m unittest discover -s tests -v
Then verify host MCP tools/list and tools/call for both tools. No deployed runtime
has been confirmed by this GitHub source commit.
