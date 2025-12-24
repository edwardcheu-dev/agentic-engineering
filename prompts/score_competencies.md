# Score Competencies (0–3)

This prompt guides the agent to update competency maturity scores based on new evidence.

## Input Context
- `docs/competency/TRACEABILITY.md` (The Source of Truth for scores 0-3)
- `docs/competency/SCORECARD.md` (The Domain Summary)
- Recent PRs or work sessions (Evidence)

## Workflow

### 1. Update Traceability (Granular Scoring)
For each competency that was exercised:
1.  **Locate** the ID in `TRACEABILITY.md` (e.g., `ACW-03`).
2.  **Verify Evidence**: Ensure specific file paths or PR links are listed in the Evidence column.
3.  **Verify KB**: Ensure a KB artifact is linked (if claiming Score 2+).
4.  **Update Score (0-3)**:
    - **0**: Missing.
    - **1**: Ad-hoc (evidence exists, but no standard doc).
    - **2**: Standardized (KB artifact exists + evidence).
    - **3**: Automated (CI/Tooling enforced).

### 2. Update Scorecard (Domain Aggregation)
For any domain where a competency score changed:
1.  **Calculate Domain Score**: `Ceiling(Average(Competency Scores))`
    - Example: (2 + 0 + 0 + 0 + 0) / 5 = 0.4 -> Ceiling = **1**
2.  **Update `SCORECARD.md`**: Update the "Aggregate Score" and "Notes" for that domain.

## Output Format

### 1. Proposed `TRACEABILITY.md` Changes
(List the rows to be updated with new scores/evidence)

### 2. Proposed `SCORECARD.md` Changes
(List the domain rows to be updated with new aggregates)

### 3. Verification
- Confirm that every Score > 0 has Evidence linked.
- Confirm that every Score > 1 has a KB artifact linked.

### 4. Next Steps
- Propose quick wins, if any, to improve scores or coverage (e.g., add standard doc if evidence exists).

Do not modify `COMPETENCY_MAP.md` except to fix obvious typos; treat it as canonical. Only update SCORECARD/TRACEABILITY/KB and link to evidence.
