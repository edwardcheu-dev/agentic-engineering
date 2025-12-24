# Harness — Scope

Harness is intentionally broad: it is the repo’s primary product vehicle for generating end-to-end evidence across the full competency map.

## Goals
Harness should:

- **Radar**
  - ingest a bounded, allowlisted set of sources
  - normalize and dedupe
  - tag via stable taxonomy
  - produce a digest with citations and “why it matters”

- **Deep dive**
  - ingest a single artifact (PDF/repo/page)
  - chunk with provenance and stable IDs
  - produce a structured breakdown grounded to chunk IDs
  - record run artifacts for reproduction

- **Guided learning**
  - produce a learning path (lessons/quizzes/labs/projects)
  - tie each lesson to source material (chunk IDs)
  - generate project ladders with explicit evaluation criteria

- **System integrity**
  - enforce schemas/contracts
  - enforce budgets (cost/latency/tool calls)
  - support observability and auditability

## Non-goals (for now)
- Unbounded browsing across arbitrary websites.
- “General research” without explicit sources and selection criteria.
- A complex multi-agent society before single-agent integrity is proven.
- Shipping UI polish before evals/traceability exist.

## Constraints (product-level contracts)
- **Boundedness:** every workflow must have stop conditions and explicit budgets.
- **Traceability:** outputs must link back to sources (citations) and runs (run IDs).
- **Policy separation:** system/developer instructions are never overwritten by retrieved text.
- **Controlled taxonomy drift:** tag set is versioned and repo-owned.

## Success criteria (acceptance)
Harness is “working” when:
1) A run can be re-executed with the same inputs/config and yields comparable outputs.
2) Outputs include citations for major claims, and citation checks pass.
3) Taxonomy tags remain stable across reruns (measurable).
4) Evals can catch regressions in groundedness and usefulness.
5) Run artifacts make debugging straightforward (you can see what happened).
