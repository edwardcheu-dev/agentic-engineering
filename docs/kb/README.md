# Knowledge Base (docs/kb/)

The KB is the repo’s **blueprint layer**: distilled knowledge that should still be true in 6 months.

## Structure (Strict 1:1 Mapping)
The KB mirrors the [Competency Map](../competency/COMPETENCY_MAP.md) exactly.
Every artifact must live in: `docs/kb/<DOMAIN>/<COMPETENCY_ID>/`

**Example:**
- Domain: `ACW` (Agentic Coding Workflow)
- Competency: `ACW-03` (Small diffs)
- Path: `docs/kb/acw/acw-03/pr_workflow.md`

## What belongs here
- **Distilled Blueprints**: Playbooks, patterns, templates, and reference guides that explain *how* to satisfy a competency.
- **Traceable Knowledge**: Every file here must link back to a Competency ID in `TRACEABILITY.md`.

## What does NOT belong here
- Raw session notes (those belong in `docs/weeks/`)
- One-off experiments without a generalized takeaway
- Generic "misc" folders (no `engineering/`, no `scripts/`)

## How KB proves progress
A KB page proves you have "learned" a competency. It must reference:
- The **Competency ID** it supports.
- The **Evidence** (tests/evals/PRs) that validates it.
