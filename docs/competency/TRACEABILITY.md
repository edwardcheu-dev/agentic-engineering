# Traceability (competency ↔ KB ↔ evidence ↔ products)

This file is the **coverage contract** for “done”.

A competency is not “done” until it has all three:
1) **KB artifact** (docs/kb/...) that teaches it
2) **Evidence** (code/tests/evals/docs/ADRs) proving it works
3) **Product usage** (docs/products/...) showing it was exercised

## Status definitions
Use these statuses consistently:
- **Not started** — no links yet
- **In progress** — some work exists, but links are incomplete
- **KB only** — KB exists, missing evidence and/or product usage
- **Evidence only** — evidence exists, missing KB and/or product usage
- **Product only** — used in a product, missing KB and/or evidence
- **Complete** — KB + evidence + product usage all linked

## Link conventions
- **KB**: `docs/kb/...`
- **Evidence**: link to PR(s) and/or file paths (tests, eval reports, ADRs)
- **Product**: link to `docs/products/<product>/...` and optionally code path

Tip: Keep links short and concrete. Prefer file paths over vague descriptions.

---

## ACW — Agentic Coding Workflow (Control Plane)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| ACW-01 | Session bootstrap discipline (goal → AC → plan → verify) |  |  |  | Not started |  |
| ACW-02 | Context discipline (what to load, what not to load) |  |  |  | Not started |  |
| ACW-03 | Small diffs + incremental commits | `docs/kb/acw/acw-03/pr_workflow.md` | This repo history |  | KB + Evidence |  |
| ACW-04 | Failure triage loop (capture failing output, minimal fix, re-verify) |  |  |  | Not started |  |
| ACW-05 | Prompt/tooling hygiene for the CLI itself (macros, reusable prompts) |  |  |  | Not started |  |

---

## CTX — Context Engineering (prompt, memory, compression, grounding)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| CTX-01 | Instruction hierarchy & policy separation (system/dev/task) |  |  |  | Not started |  |
| CTX-02 | Context packing strategy (what goes in, ordering, truncation plan) |  |  |  | Not started |  |
| CTX-03 | Memory: short-term vs long-term vs episodic (and when to write) |  |  |  | Not started |  |
| CTX-04 | Summarization/compression with fidelity checks (avoid “summary drift”) |  |  |  | Not started |  |
| CTX-05 | Retrieval-informed context (RAG) with citation policy |  |  |  | Not started |  |
| CTX-06 | Anti-injection context filtering (don’t promote retrieved text to instructions) |  |  |  | Not started |  |
| CTX-07 | Reproducibility: “re-run this with same context pack” |  |  |  | Not started |  |

---

## MCP — Tooling & Protocol Interop (MCP + tool contracts)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| MCP-01 | Tool schema/contracts (inputs/outputs, types, error model) |  |  |  | Not started |  |
| MCP-02 | MCP client usage patterns (capabilities discovery, tool selection) |  |  |  | Not started |  |
| MCP-03 | MCP server authoring patterns (wrappers/adapters, versioning) |  |  |  | Not started |  |
| MCP-04 | Permissioning & least-privilege tool access |  |  |  | Not started |  |
| MCP-05 | Tool sandboxing boundaries (filesystem/network) |  |  |  | Not started |  |
| MCP-06 | Tool reliability: timeouts/retries/idempotency |  |  |  | Not started |  |
| MCP-07 | Tool testing strategy (fake servers, contract tests) |  |  |  | Not started |  |

---

## AGT — Agent Architecture (single-agent systems done well)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| AGT-01 | Explicit state machine / stages (plan → act → observe → reflect) |  |  |  | Not started |  |
| AGT-02 | Separation of concerns: planner vs executor vs critic/judge |  |  |  | Not started |  |
| AGT-03 | Deterministic core + probabilistic edges (where randomness is allowed) |  |  |  | Not started |  |
| AGT-04 | Tool-use constraints (allowed tools per stage) |  |  |  | Not started |  |
| AGT-05 | Stop conditions and bounded loops (no infinite “thinking”) |  |  |  | Not started |  |
| AGT-06 | Human-in-the-loop checkpoints (approval steps when needed) |  |  |  | Not started |  |

---

## MAS — Multi-Agent Systems (MAS) & Coordination

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| MAS-01 | Role design (specialists, router, coordinator) |  |  |  | Not started |  |
| MAS-02 | Task decomposition strategy (when/why to split) |  |  |  | Not started |  |
| MAS-03 | Coordination protocol (handoffs, escalation, consensus rules) |  |  |  | Not started |  |
| MAS-04 | Shared memory design (blackboard vs per-agent memory) |  |  |  | Not started |  |
| MAS-05 | Conflict resolution (disagreement handling, tie-breakers) |  |  |  | Not started |  |
| MAS-06 | Efficiency controls (caps, budgets, termination) |  |  |  | Not started |  |
| MAS-07 | Eval strategy for MAS (end-to-end + per-role metrics) |  |  |  | Not started |  |

---

## A2A — Agent-to-Agent (A2A) Interfaces & Messaging

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| A2A-01 | Message schemas (task requests, results, evidence, confidence) |  |  |  | Not started |  |
| A2A-02 | Provenance passing (sources, citations, run IDs) |  |  |  | Not started |  |
| A2A-03 | Capability negotiation (what an agent can/can’t do) |  |  |  | Not started |  |
| A2A-04 | Trust boundaries (what you accept from another agent) |  |  |  | Not started |  |
| A2A-05 | Robustness to partial failure (agent unavailable, stale results) |  |  |  | Not started |  |
| A2A-06 | Versioning & compatibility for agent protocols |  |  |  | Not started |  |

---

## DKE — Data & Knowledge Engineering (corpora, pipelines, labeling)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| DKE-01 | Corpus ingestion pipeline (repeatable, logged) |  |  |  | Not started |  |
| DKE-02 | Data versioning & provenance |  |  |  | Not started |  |
| DKE-03 | Chunking strategy + benchmarks |  |  |  | Not started |  |
| DKE-04 | Metadata strategy (source, time, permissions, sensitivity) |  |  |  | Not started |  |
| DKE-05 | Feedback loop: collect hard examples, label, add to evals |  |  |  | Not started |  |

---

## EVAL — Evaluation, Testing & Evals Ops (LLM + agents)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| EVAL-01 | Unit tests for deterministic components |  |  |  | Not started |  |
| EVAL-02 | Offline eval sets (goldens, scoring rubrics) |  |  |  | Not started |  |
| EVAL-03 | Simulation harness for agents (controlled environments) |  |  |  | Not started |  |
| EVAL-04 | LLM-judge usage guidelines (when allowed, how to stabilize) |  |  |  | Not started |  |
| EVAL-05 | CI gating strategy (fast offline + optional slow online) |  |  |  | Not started |  |
| EVAL-06 | Eval reporting & trend tracking (quality, latency, cost) |  |  |  | Not started |  |

---

## REL — Reliability & Resilience Engineering

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| REL-01 | Timeouts, retries, idempotency, circuit breakers |  |  |  | Not started |  |
| REL-02 | Backpressure/rate limiting |  |  |  | Not started |  |
| REL-03 | Degradation modes (cached answers, partial outputs) |  |  |  | Not started |  |
| REL-04 | Error taxonomy + user-facing error messaging |  |  |  | Not started |  |
| REL-05 | Determinism controls (seeds/temperature policies where relevant) |  |  |  | Not started |  |

---

## OBS — Observability & Run Artifacts (debugging at scale)

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| OBS-01 | Structured logging + correlation IDs |  |  |  | Not started |  |
| OBS-02 | Trace-like step logs for agent stages/tool calls |  |  |  | Not started |  |
| OBS-03 | Run artifact persistence (inputs/outputs/context pack metadata) |  |  |  | Not started |  |
| OBS-04 | Metrics: latency, error rates, token/cost, tool usage |  |  |  | Not started |  |
| OBS-05 | Redaction policy (don’t leak sensitive data) |  |  |  | Not started |  |

---

## SEC — Security, Privacy & Prompt-Injection Defense

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| SEC-01 | Threat model for RAG + tools (prompt injection) |  |  |  | Not started |  |
| SEC-02 | Instruction/data boundary enforcement |  |  |  | Not started |  |
| SEC-03 | Secrets management & no-secret logging |  |  |  | Not started |  |
| SEC-04 | Sandboxing tools (filesystem/network) + allowlists |  |  |  | Not started |  |
| SEC-05 | Data handling policy (PII, retention, redaction) |  |  |  | Not started |  |
| SEC-06 | Supply chain hygiene (deps, lockfiles, audits) |  |  |  | Not started |  |

---

## CLP — Cost, Latency & Performance Engineering

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| CLP-01 | Budgeting (per run/per user/per workflow) |  |  |  | Not started |  |
| CLP-02 | Caching (prompt/result/retrieval caches) + invalidation strategy |  |  |  | Not started |  |
| CLP-03 | Model routing (small vs large, fallback policies) |  |  |  | Not started |  |
| CLP-04 | Profiling + performance baselines |  |  |  | Not started |  |

---

## OPS — Deployment, Ops & Release Engineering

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| OPS-01 | CI/CD pipeline and release versioning | `docs/kb/ops/ops-01/ci_cd.md`, `docs/kb/ops/ops-01/git_tagging.md` | `.github/workflows/ci.yml` |  | KB + Evidence |  |
| OPS-02 | Environment config strategy (dev/stage/prod) |  |  |  | Not started |  |
| OPS-03 | Rollbacks and safe migrations |  |  |  | Not started |  |
| OPS-04 | On-call basics / incident handling (even if “solo on-call”) |  |  |  | Not started |  |
| OPS-05 | Dependency upgrades cadence |  |  |  | Not started |  |

---

## GOV — Governance / Enterprise Readiness

| ID | Competency | KB artifact(s) | Evidence | Product usage | Status | Notes |
|---|---|---|---|---|---|---|
| GOV-01 | Auditability (who ran what, when, with what inputs/config) |  |  |  | Not started |  |
| GOV-02 | Policy enforcement (allowed models/tools/data sources) |  |  |  | Not started |  |
| GOV-03 | Data retention/deletion workflows |  |  |  | Not started |  |
| GOV-04 | Vendor/model risk notes (where applicable) |  |  |  | Not started |  |
| GOV-05 | Compliance hooks (as needed: SOC2-ish controls, etc.) |  |  |  | Not started |  |
