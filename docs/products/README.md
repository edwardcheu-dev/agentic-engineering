# Products Registry (docs/products/)

Products are “vehicles” chosen because they exercise specific competencies.

Rule:
- A product exists to generate **evidence** and create **distillation opportunities**.
- If a product doesn’t clearly map to competency coverage, it is scope creep.

## Structure

Each product gets a folder:

- `docs/products/<product>/`
  - `README.md` — product overview + elevator pitch
  - `SCOPE.md` — goals, non-goals, constraints, personas
  - `ARCHITECTURE.md` — high-level architecture and major loops
  - `WORKFLOWS.md` — user journeys + CLI commands + examples
  - `DATA_MODEL.md` — storage objects/schemas, IDs, provenance
  - `TAXONOMY.md` — tagging system and rules for change/versioning
  - `EVALS.md` — how we measure groundedness/coverage/actionability/consistency
  - `ROADMAP.md` — phased plan + milestones
  - `RISKS.md` — what breaks without constraints (prompt injection, drift, cost)

Not every product must start with all files, but **the intent is to make the product legible**:
- What it is
- How it works
- How we know it works
- How it evolves without drifting

## Product selection rubric
Prefer products that:
- exercise multiple missing competencies (per TRACEABILITY gaps)
- can be advanced via small PRs
- have clear eval surfaces (offline tests/evals possible)
- create reusable KB patterns/templates

## Registry
| Product | Why it exists (competencies) | Docs | Status |
|---|---|---|---|
| Harness | Exercise a complete integrity-first agent system across all 14 domains, producing traceable run artifacts, evals, and KB distillations. | docs/products/harness/ | Planned |
