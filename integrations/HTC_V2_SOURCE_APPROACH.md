# Source approach: HTC-V2-inspired multi-agent planning

Upstream: https://github.com/05111975phamanhtuan-hue/H-th-ng-Multi-Agent-T-ng-h-a-Nghi-n-c-u-Khoa-h-c-v-Tri-n-khai-K-thu-t-T-ch-h-p

Readback on 2026-10-14: upstream contains only README.md and LICENSE (MIT).
README describes multi-agent debate, analysis, knowledge collection, implementation and testing.
There is **no upstream runnable orchestration code** to vendor or integrate.

SOL implementation: `sol_source_approach(source)` uses five logical roles:
provenance, structure, evidence, security, synthesis. It constructs a review plan
immediately when **the MCP tool is called**, before any third-party execution.
A separate host/orchestrator must explicitly call the tool for each new source;
GitHub hosting alone cannot detect a source automatically.

Safety: returns a deterministic plan only. No subagent process is spawned, no
repository is cloned and no network requests/commands are executed. All steps
remain `pending`, with a separate future carrier needed to execute them.
The earlier clean removal of legacy `sol_toolcall_dispatch` remains in effect.

Runtime test: `python -m unittest discover -s tests -v`, followed by MCP
`tools/list` and `sol_source_approach` readback on an authorized host.
