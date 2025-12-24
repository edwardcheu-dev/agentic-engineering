# Harness

Harness is the repo’s **end-to-end research + learning harness**: an integrity-first agentic system that ingests sources, detects trends, performs grounded deep dives, and turns long documents into guided study and project ladders.

Harness exists explicitly as a **competency exercise vehicle**: it is broad on purpose, so we can generate traceable evidence across the full system lifecycle (data → tools → agent loop → evals → ops → governance).

Optional in-chat persona name: **Hans** (the “voice” of Harness). The product is Harness; Hans is a presentation layer choice.

## Integrity invariants (non-negotiables)
Harness outputs are only “valid” if they satisfy:

1) **Groundedness:** major claims must cite sources (or chunk IDs).
2) **Reproducibility:** every run writes a run record (inputs, config, versions, outputs).
3) **Stable taxonomy:** tags come from a versioned taxonomy; no ad-hoc categories.
4) **Budgeted execution:** explicit caps (time/token/tool calls); bounded loops.
5) **Tool contracts:** tool inputs/outputs validated; failures are typed and logged.
6) **Security boundaries:** retrieved content never becomes instructions; secrets never logged.
7) **Auditability:** “who ran what, when, with what config” is answerable from artifacts.

These invariants are the “integrity of what Harness is”. Features that violate them are out of scope.

## What Harness produces (minimal product surface)
- **Radar digest:** “what mattered” for a bounded source set and time window, with citations.
- **Deep dive:** structured breakdown for one artifact (paper/repo/page), grounded to chunk IDs.
- **Guided study:** a curriculum (lessons/quizzes/labs) with a project ladder and evaluation criteria.
- **Run artifacts:** durable records for debugging, audit, and regression testing.

## Competency coverage (14 domains)
Harness is intended to generate evidence for **every domain**, not just a few:

| Domain | How Harness exercises it (examples) | Typical evidence outputs |
|---|---|---|
| **ACW** | disciplined loop: goal → acceptance criteria → plan → implement → verify → reflect | PRs with small diffs; checklists; runbooks |
| **CTX** | context packing, retrieval boundaries, summarization fidelity, memory policy | prompts/templates; context pack logs; drift tests |
| **MCP** | tool contracts: schema validation, error model, timeouts, capability discovery | tool schema tests; contract tests; tool adapters |
| **AGT** | explicit agent loop with stop conditions + bounded retries | state machine code + tests; run traces |
| **MAS** | (later phase) role decomposition for radar vs deep dive vs evaluator | coordination logs; per-role evals |
| **A2A** | (later phase) message schemas between roles/agents; provenance passing | schema definitions; compatibility tests |
| **DKE** | ingestion, normalization, chunking, metadata/provenance | dataset snapshots; chunking benchmarks |
| **EVAL** | goldens, scoring rubrics, regression gates, judge policy | eval sets; scoring scripts; CI reports |
| **REL** | retries/idempotency/backpressure/degraded modes | fault-injection tests; reliability metrics |
| **OBS** | structured logs, traces, run artifact persistence, metrics | run records; dashboards (later); log schema |
| **SEC** | injection defenses; allowlists; redaction; secrets hygiene | threat model doc; redaction tests; policy checks |
| **CLP** | cost/latency budgets; caching; routing policy | budget tests; perf baselines; router config |
| **OPS** | CI/CD, environment configs, releases | pipelines; release notes; deployment docs |
| **GOV** | auditability, retention, policy enforcement hooks | audit logs; retention policy docs; approvals |

> Note: MAS/A2A are intentionally “later phase” coverage, but Harness still provides the *place* they belong without changing the product identity.

## Pointer docs
- Scope: `SCOPE.md`
- Architecture: `ARCHITECTURE.md`
- Workflows: `WORKFLOWS.md`
- Taxonomy: `TAXONOMY.md`
- Evals: `EVALS.md`
- Roadmap: `ROADMAP.md`
- Risks: `RISKS.md`
