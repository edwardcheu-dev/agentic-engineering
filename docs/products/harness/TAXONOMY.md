# Harness — Taxonomy

Harness requires a **stable, versioned taxonomy** to prevent category drift and to make “trend” and “learning progression” meaningful over time.

## Rules (contract)
- The taxonomy is **repo-owned** (not invented ad-hoc during runs).
- Tagging must use taxonomy keys exactly.
- Adding/removing/renaming tags requires:
  - an explicit proposal
  - a version bump
  - migration notes (what changes and why)
- If an output contains unknown tags, the run fails verification (or the tags are rejected and logged).

## Why this exists
If the model invents new categories every run:
- tags become incomparable across time
- trend detection becomes meaningless
- evals regress silently
- learning modules don’t accumulate coherently

## Initial taxonomy (draft; contextual scaffold)
This draft exists to anchor early work and vocabulary. The “real” source-of-truth can later move to a versioned file (e.g., `taxonomy.json`) once stable.

Top-level categories (illustrative):

- **Content Engineering**
  - dataset design
  - synthetic data
  - instruction design
  - rubric design
  - prompt/program structure

- **Agentic Patterns**
  - plan-execute
  - reflect/verify
  - tool use
  - self-critique

- **Multi-Agent Systems**
  - role specialization
  - debate/consensus
  - blackboard
  - routing

- **MCP / Tooling**
  - tool servers
  - auth/secrets
  - schemas/contracts

- **Memory**
  - episodic vs semantic
  - retrieval strategy
  - summarization/memory compression

- **Evaluation**
  - groundedness
  - task success metrics
  - regression tests
  - human eval protocols

- **Infra**
  - cost/latency
  - caching
  - observability

## Future direction (not required now)
- represent taxonomy as a machine-readable versioned artifact
- add governance around deprecations and migrations
- attach allowed tags to specific workflows (radar vs deep dive vs study)
