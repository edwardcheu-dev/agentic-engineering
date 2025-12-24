# Harness — Architecture (high level)

Harness is built as a small number of pipelines (“loops”) that all terminate in the same integrity layer:
**schema validation, citation checks, run artifacts, budgets, and observability**.

## Core data objects (conceptual)
- **Source**: allowlisted feed/API/repo list entry + policy metadata
- **Item**: one ingested unit (paper, post, repo release, etc.)
- **Artifact**: a fetched document/repo snapshot used for deep dives/study
- **Chunk**: an addressable span of text with provenance (source → artifact → chunk)
- **Run**: a reproducible record of one execution (inputs/config/outputs/log pointers)
- **Output**: digest / breakdown / study plan / project ladder (JSON + Markdown view)

## Loop A: Radar (scan → tag → cluster → digest)
1) Acquire from allowlisted sources
2) Normalize metadata
3) Dedupe
4) Tag via taxonomy (deterministic first; LLM fallback only with constraints)
5) Cluster by tags/themes
6) Generate digest **with citations** to items

Outputs:
- Digest artifact (MD/JSON)
- Backlog of deep-dive candidates
- Run record

## Loop B: Deep dive (artifact → chunks → grounded breakdown)
1) Acquire artifact (PDF/repo/page snapshot)
2) Extract/parse
3) Chunk with stable IDs + metadata
4) Summarize (map) at chunk/group level with citations
5) Synthesize (reduce) into a structured breakdown
6) Verification pass:
   - schema validation
   - citation checks (“major claims cite chunk IDs”)

Outputs:
- Breakdown object (JSON + MD view)
- Chunk store entries
- Run record + trace

## Loop C: Guided learning (outline → lessons → quizzes → projects)
1) Build outline/dependency graph from artifact + chunks
2) Create lessons with objectives and reading chunk references
3) Generate quizzes and mini-labs tied to lesson objectives
4) Generate project ladder aligned to lessons (with eval criteria)
5) Track progress; schedule review

Outputs:
- Study plan + progress state
- Quiz/lab/project specs
- Run record

## Tooling / protocol layer (MCP-oriented)
Harness is expected to use tools via explicit contracts:
- tool schemas (inputs/outputs)
- typed errors
- timeouts/retries/idempotency boundaries
- least-privilege permissions

This layer is deliberately designed to be “swappable” across providers/tools.

## Observability layer (always-on)
- structured logs with correlation IDs
- step traces for agent stages and tool calls
- run artifact persistence
- metrics: latency, cost, error rates, tool-call counts

## Security/governance layer (always-on)
- instruction/data boundary enforcement (anti-injection)
- source allowlists + provenance metadata
- redaction rules for logs/artifacts
- audit hooks: who ran what and with what config
- retention/deletion policy (future)
