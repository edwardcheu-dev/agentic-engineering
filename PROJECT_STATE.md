# PROJECT_STATE (source of truth)

Keep this file current. It is the fastest way to resume work.

## Current focus (as of 2025-12-24)
**PR1 (doc-only): Learning Factory control plane + canonical competency map**

Goal: eliminate inconsistent “old roadmap” signals so Gemini (and future readers) understand:
- this is a long-lived public repo
- progress is measured by competency coverage
- every competency needs evidence + KB distillation + product usage

## Repo invariants (do not drift)
- Public repo forever mindset.
- No secrets in git (ever).
- Keep diffs small; prefer incremental PRs.
- Prefer: acceptance criteria → tests/evidence → implementation → verification.
- Unit tests never make network calls.

## Canonical navigation (the 3 pillars)
1) Competency Map (North Star): `docs/competency/`
2) Products (Vehicles): `docs/products/`
3) Knowledge Base (Blueprint): `docs/kb/` (most important)

Supporting:
- ADRs: `docs/decisions/`
- Weekly raw notes: `docs/weeks/`

## Resume order (when coming back later)
1. `AGENT_CONTEXT.md`
2. `PROJECT_STATE.md`
3. `docs/competency/COMPETENCY_MAP.md`
4. `docs/competency/TRACEABILITY.md`
5. `docs/kb/index.md`
6. `docs/products/README.md`
7. `LEARNING_LOG.md`
8. `docs/weeks/`
9. `GEMINI.md`

## PR1 acceptance checklist (doc-only)
Control plane skeleton:
- [ ] Add `AGENT_CONTEXT.md`
- [ ] Add `docs/competency/`:
  - [ ] `README.md`
  - [ ] `COMPETENCY_MAP.md` (canonical map: ACW/CTX/MCP/AGT/MAS/A2A/DKE/EVAL/REL/OBS/SEC/CLP/OPS/GOV)
  - [ ] `SCORECARD.md` (0–3 rubric)
  - [ ] `TRACEABILITY.md` (competency ↔ KB ↔ evidence ↔ products)
  - [ ] `ROADMAP.md` (iterative “next deltas”, optional)
- [ ] Add `docs/products/README.md` (product registry + selection rubric)
- [ ] Add `docs/kb/README.md`, `docs/kb/index.md`, `docs/kb/START_HERE.md`
- [ ] Add `docs/weeks/README.md` (weekly notes conventions)
- [ ] Add `docs/decisions/ADR-0000-template.md` (ADR template)

Repo memory alignment:
- [ ] Update `README.md` to describe the Learning Factory and link to canonical docs
- [ ] Update `ROADMAP.md` (root) to deprecate the 52-week plan and point to canonical docs
- [ ] Update `LEARNING_LOG.md` to track competency IDs + evidence + distillation
- [ ] Update `GEMINI.md` so the agent:
  - [ ] loads `AGENT_CONTEXT.md` + competency/traceability first
  - [ ] always ties work to competency IDs
  - [ ] enforces evidence + distillation

Macro prompts (stubs are OK in PR1):
- [ ] Add:
  - [ ] `prompts/session_bootstrap.md`
  - [ ] `prompts/score_competencies.md`
  - [ ] `prompts/distill_to_kb.md`
  - [ ] `prompts/create_adr.md`
  - [ ] `prompts/migrate_three_pillars.md`

Verification:
- [ ] `just verify-docs` passes

## Next actions (do these in order)
1. Create/update branch (doc-only):
   - `git checkout -b docs/migration-01-gemini-awareness`

2. Apply the doc changes in this PR1 checklist.

3. Verify:
   - `just verify-docs`

4. Open PR, merge.

5. After merge:
   - Run first calibration pass:
     - update `docs/competency/SCORECARD.md` honestly (0/1 is fine)
     - fill 5–10 rows in `docs/competency/TRACEABILITY.md` (start small)
