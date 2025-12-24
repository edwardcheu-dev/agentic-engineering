# Competency System (docs/competency/)

This folder is the **control plane** for the Learning Factory.

## Canonical files
- `COMPETENCY_MAP.md` — definitions + IDs (the North Star)
- `SCORECARD.md` — current maturity scores (0–3) + evidence links
- `TRACEABILITY.md` — coverage contract:
  competency ↔ KB artifact ↔ evidence ↔ product usage
- `ROADMAP.md` — optional “next deltas” list; iterative (not time-based)

## Scoring rubric (0–3)
We use a simple maturity rubric:
- **0 — Missing:** not present / not practiced
- **1 — Ad-hoc:** exists, but inconsistent and not repeatable
- **2 — Standardized:** documented, repeatable, and used by default
- **3 — Automated/Enforced:** CI gates, tooling, and templates enforce it

## Coverage contract (definition of done per competency)
A competency is “done” only when TRACEABILITY links to:
1) a **KB artifact** (playbook/pattern/reference) that teaches it
2) **evidence** (code/tests/evals/docs/ADRs) proving it works
3) **product usage** showing a product exercised it

If any of the three links are missing, it remains “in progress.”

## How this stays finite (“enterprise-complete-enough”)
The competency map is intentionally bounded (domains + concrete competencies).
We evolve it iteratively, but we keep IDs stable once introduced.

Progress is not word count; it is traceability coverage.
