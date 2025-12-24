# Harness — Workflows (contracts)

Command names are placeholders. The behavior is the contract.

## Workflow 1: Weekly radar digest
**Goal:** “What mattered this week?” with explicit selection criteria and citations.

Inputs:
- time window
- source allowlist
- budgets (cost/latency/tool calls)

Outputs:
- `digest.md` + `digest.json`
- run record (run ID + config + stats)

Contract:
- every “why it matters” claim must cite at least one item
- digest includes tags from the taxonomy only
- run record includes source list, time window, and model/tool configuration

## Workflow 2: Deep dive a single artifact
**Goal:** produce a structured breakdown grounded to chunk IDs.

Inputs:
- artifact reference (URL/arXiv ID/repo)
- parsing/chunking config
- budgets

Outputs:
- breakdown JSON + MD view
- chunk store entries with stable chunk IDs
- run record + trace

Contract:
- major claims cite chunk IDs
- breakdown conforms to schema
- verification step runs and records pass/fail

## Workflow 3: Turn a long artifact into guided study + projects
**Goal:** reading becomes skill accumulation.

Inputs:
- artifact + topic tag(s)
- learner profile (optional; bounded memory policy)

Outputs:
- study plan (lessons, objectives, references)
- quizzes + labs
- project ladder (beginner → intermediate → advanced → capstone)
- progress state + run record

Contract:
- each lesson links to chunk IDs
- each project includes: requirements, constraints, evaluation criteria, stretch goals
- outputs remain within budgets and stop conditions

## Workflow 4: Taxonomy change (controlled drift)
**Goal:** evolve categories without breaking history.

Inputs:
- proposed taxonomy changes

Outputs:
- taxonomy version bump + migration notes
- report on impacted tags/items

Contract:
- no silent tag drift across runs
- taxonomy changes are reviewed and recorded like API changes
