# Harness — Roadmap (small PR friendly)

Harness is a long-lived product vehicle; the roadmap is structured to produce **evidence early** and expand capability without losing integrity.

## Phase 0: Product integrity scaffolding (docs + schemas)
Deliverables:
- product docs exist (this folder)
- initial output schemas drafted (digest/breakdown/study plan)
- run artifact format drafted (run record schema)

Primary domains exercised:
ACW, CTX, GOV (contracts), EVAL (rubrics)

## Phase 1: Radar MVP (bounded + reproducible)
Deliverables:
- allowlisted sources ingestion + normalization + dedupe
- taxonomy tagging (strict)
- digest generation (MD + JSON) with citations
- run artifacts + structured logs

Primary domains exercised:
DKE, CTX, EVAL, OBS, REL, CLP, SEC (source boundaries)

## Phase 2: Deep dive MVP (chunk-grounded breakdown)
Deliverables:
- artifact acquisition + parsing
- chunk store + provenance
- breakdown generator with chunk citations
- verification pass (schema + citation checks)

Primary domains exercised:
DKE, CTX, AGT, EVAL, OBS, SEC, REL

## Phase 3: Guided learning + project ladder MVP
Deliverables:
- study plan from an artifact
- quizzes/labs/projects tied to chunk IDs
- progress tracking state (minimal)

Primary domains exercised:
AGT, DKE, EVAL, CTX, GOV (auditability), CLP (budgets)

## Phase 4: Tool contracts + MCP hardening
Deliverables:
- tool schemas + typed error model
- contract tests and fake tool servers
- permissioning boundaries

Primary domains exercised:
MCP, SEC, REL, OPS, OBS

## Phase 5: MAS/A2A expansion (optional, after integrity is strong)
Deliverables:
- role decomposition (radar specialist, deep dive specialist, evaluator)
- message schemas + provenance passing
- per-role evals

Primary domains exercised:
MAS, A2A, EVAL, OBS
