# Learning Log — agentic-engineering

## What this log is
A time-based record of what changed (PRs, outcomes, and what we learned).

## What “progress” means in this repo
Progress is competency-driven and traceable:
- Competency Map: `docs/competency/COMPETENCY_MAP.md`
- Scores: `docs/competency/SCORECARD.md`
- Traceability (competency ↔ KB ↔ evidence ↔ products): `docs/competency/TRACEABILITY.md`

## Recommended entry format (per week or per merged PR)
- Dates (ISO week is preferred)
- PR link(s)
- Competency IDs touched
- Evidence updated (tests/evals/docs/ADRs)
- KB distillation created/updated
- 3 takeaways

---

## 2025-W52 — Repo scaffold + baseline checks (legacy Week 01)

- Dates: 2025-12-22 to 2025-12-28
- PR: (link)
- Notes (legacy): docs/week-01/notes.md
- Notes (target, later): docs/weeks/2025-W52/

### Competency IDs touched (retro-mapped to the canonical v0 map)
Agentic workflow:
- ACW-01 Session bootstrap discipline
- ACW-02 Context discipline
- ACW-03 Small diffs + incremental commits
- ACW-04 Failure triage loop
- ACW-05 Prompt/tooling hygiene for CLI

Evals / quality / ops:
- EVAL-01 Unit tests for deterministic components
- OPS-01 CI/CD pipeline and release versioning

Security posture:
- SEC-03 Secrets management & no-secret logging

### Evidence updated
- Local quality gates and verification loop (`ruff` / `pyright` / `pytest`, plus `just verify*`)
- CI baseline on GitHub Actions
- Engineering docs for CI/CD + PR workflow

### KB distillation
- Initial repo documentation exists, but KB is not yet established as a navigable blueprint.
- Next PR creates the Learning Factory control plane and KB skeleton.

### Commands run (copy/paste)
- just check
- just doctor
- just verify-code
- just verify-docs

### Gemini CLI muscle drills
- Ran /memory show
- Used @README.md in a prompt
- Ran !uv run pytest -q from inside Gemini CLI
- Verified checkpointing + /restore exists

### Takeaways
1. Verification loop discipline (fast local + CI) prevents drift.
2. Public repo safety must be explicit everywhere (docs + agent rules), not assumed.
3. Without traceability (competencies ↔ evidence ↔ KB), “learning” feels endless; the control plane fixes that.

### Next
- PR1 (doc-only): Learning Factory control plane + canonical competency map + traceability skeleton.
