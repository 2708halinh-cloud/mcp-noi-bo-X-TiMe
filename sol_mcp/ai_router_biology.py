"""TP53 reference profile for SOL AI Router Studio.

Static evidence-tagged biological knowledge, not a structural predictor.
"""
from __future__ import annotations
from copy import deepcopy

ACCESSION = "P04637"
LENGTH = 393
SOURCES = {
    "uniprot": "https://www.uniprot.org/uniprotkb/P04637/entry",
    "uniprot_api": "https://rest.uniprot.org/uniprotkb/P04637.json",
    "rcsb": "https://www.rcsb.org/structure/1TUP",
    "alphafold": "https://alphafold.ebi.ac.uk/search/text/P04637",
}
DOMAINS = (
    ("TAD1", "Transactivation 1", 1, 40, "user_supplied_interval"),
    ("DBD", "DNA-binding core", 102, 292, "user_supplied_and_RCSB_1TUP"),
    ("TET", "Tetramerization", 325, 356, "user_supplied_interval"),
    ("CTD", "C-terminal regulatory", 363, 393, "user_supplied_interval"),
)

def tp53_profile(accession: str = ACCESSION) -> dict:
    if accession != ACCESSION:
        raise ValueError("ONLY_TP53_P04637_SUPPORTED")
    domains = [
        {"id": key, "label": label, "start": start, "end": end,
         "length_aa": end - start + 1, "provenance": provenance}
        for key, label, start, end, provenance in DOMAINS
    ]
    return deepcopy({
        "module": "AI Router Studio",
        "protein": "p53",
        "gene": "TP53",
        "accession": ACCESSION,
        "species": "Homo sapiens",
        "length_aa": LENGTH,
        "function_vi": "Yếu tố phiên mã ức chế khối u: điều hòa ngừng chu kỳ, sửa chữa DNA hoặc apoptosis khi có stress hay tổn thương DNA.",
        "function_source": "UniProt reviewed P04637 FUNCTION",
        "domains": domains,
        "experimental_reference": {
            "pdb": "1TUP", "method": "X-RAY DIFFRACTION",
            "resolution_angstrom": 2.2, "covers": "DNA-binding core, not full-length p53"
        },
        "prediction_reference": {
            "provider": "AlphaFold DB", "accession": ACCESSION,
            "model_type": "predicted_not_experimental"
        },
        "sources": SOURCES,
        "coverage": {
            "annotated_amino_acids": sum(end-start+1 for _, _, start, end, _ in DOMAINS),
            "unassigned_in_this_four_domain_scheme": LENGTH - sum(end-start+1 for _, _, start, end, _ in DOMAINS)
        },
        "status": {"source_review_only": True, "live_external_router_connected": False},
        "limits": "User-provided intervals are one annotation convention, not authoritative experimental boundaries."
    })

def tp53_residue(position: int) -> dict:
    if type(position) is not int or not 1 <= position <= LENGTH:
        raise ValueError("RESIDUE_OUT_OF_RANGE")
    matches = [
        {"id": key, "label": label, "provenance": provenance}
        for key, label, start, end, provenance in DOMAINS
        if start <= position <= end
    ]
    return {
        "accession": ACCESSION, "position": position,
        "domains": matches,
        "annotated_in_current_scheme": bool(matches),
        "note": "No match means omitted by this four-domain scheme, not functionless."
    }
