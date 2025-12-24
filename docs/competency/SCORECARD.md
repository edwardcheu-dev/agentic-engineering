# Scorecard (0–3 maturity)

This file tracks the current maturity score for each competency.

Rubric:
- **0 — Missing:** not present / not practiced
- **1 — Ad-hoc:** exists, but inconsistent and not repeatable
- **2 — Standardized:** documented, repeatable, and used by default
- **3 — Automated/Enforced:** CI gates, tooling, and templates enforce it

Update discipline:
- Scores should be conservative.
- Add evidence links when increasing scores.
- Prefer “raise one competency by one level” over sweeping re-scores.

Last updated: 2025-12-24 (initial scaffold; scores are placeholders)

> NOTE: Detailed link coverage (KB + evidence + product usage) lives in `docs/competency/TRACEABILITY.md`.

## Domain-level summary (optional, coarse)
| Domain | Goal | Current level (0–3) | Notes |
|---|---|---:|---|
| ACW | Agentic Coding Workflow | 2 | Standardized with prompts/commit_package.md and PR workflow guide |
| CTX | Context Engineering | 0 | Not started |
| MCP | Tooling & Protocol Interop (MCP) | 0 | Not started |
| AGT | Agent Architecture | 0 | Not started |
| MAS | Multi-Agent Systems | 0 | Not started |
| A2A | Agent-to-Agent Interfaces | 0 | Not started |
| DKE | Data & Knowledge Engineering | 0 | Not started |
| EVAL | Evaluation & Evals Ops | 1 | Basic unit tests / CI exist |
| REL | Reliability | 0 | Not started |
| OBS | Observability | 0 | Not started |
| SEC | Security / Prompt Injection Defense | 1 | Public-repo posture started; needs standardization |
| CLP | Cost/Latency/Performance | 0 | Not started |
| OPS | Deployment/Ops/Release | 2 | CI pipeline + guides (CI/CD, Tagging) are standardized |
| GOV | Governance / Enterprise Readiness | 0 | Not started |
