# SOL multi-thread instruction evidence audit

Goal: trace **observable** memory/context loss symptoms, premature OPEN, unexplained pauses,
apology/explanation loops, and the literal user term `Subritetied`.

This audit does **not** disclose private system/developer messages or claim to override
ChatGPT platform policies. It scans only explicit authorized local files under SOL_MCP_ROOT.

Tool: `sol_instruction_audit(relative_files, workers=5)`
- Five thread workers (max) scan separate documents.
- Read-only: no subprocesses, GitHub writes, requests, or hidden configuration inspection.
- Explicit filenames (up to 200); no whole-disk recursive scan.
- Maximum 2 MiB per file; outputs line numbers and category counts, no full line text.
- Categories: memory_context, subritetied_literal, open_nonterminal,
  apology_explanation, action_readback.
- Counts are **keyword indicators, not policy violations or proof of causal platform behavior**.
- Human evidence review must separate facts, inference, and OPEN gaps.

Run `python -m unittest discover -s tests -v` and verify `tools/list` and a test call
from the authorized MCP host. Source-only GitHub commit is not proof of live deployment.
