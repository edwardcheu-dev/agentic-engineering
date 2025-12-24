# Competency Map (canonical)

This is the canonical competency map for the Learning Factory.

Structure:
- **Domains (14):** stable categories
- **Competencies:** concrete, ID’d targets within each domain

Scoring rubric is defined in `docs/competency/SCORECARD.md` (0–3).

---

## Domain 1 — Agentic Coding Workflow (Control Plane)
**Goal:** Reliably ship changes using CLI agents without chaos.

- ACW-01 Session bootstrap discipline (goal → AC → plan → verify)
- ACW-02 Context discipline (what to load, what not to load)
- ACW-03 Small diffs + incremental commits
- ACW-04 Failure triage loop (capture failing output, minimal fix, re-verify)
- ACW-05 Prompt/tooling hygiene for the CLI itself (macros, reusable prompts)

---

## Domain 2 — Context Engineering (prompt, memory, compression, grounding)
**Goal:** Design context flows that are stable, scalable, and safe.

- CTX-01 Instruction hierarchy & policy separation (system/dev/task)
- CTX-02 Context packing strategy (what goes in, ordering, truncation plan)
- CTX-03 Memory: short-term vs long-term vs episodic (and when to write)
- CTX-04 Summarization/compression with fidelity checks (avoid “summary drift”)
- CTX-05 Retrieval-informed context (RAG) with citation policy
- CTX-06 Anti-injection context filtering (don’t promote retrieved text to instructions)
- CTX-07 Reproducibility: “re-run this with same context pack”

---

## Domain 3 — Tooling & Protocol Interop (MCP + tool contracts)
**Goal:** Expose/consume tools in a standardized, testable way.

- MCP-01 Tool schema/contracts (inputs/outputs, types, error model)
- MCP-02 MCP client usage patterns (capabilities discovery, tool selection)
- MCP-03 MCP server authoring patterns (wrappers/adapters, versioning)
- MCP-04 Permissioning & least-privilege tool access
- MCP-05 Tool sandboxing boundaries (filesystem/network)
- MCP-06 Tool reliability: timeouts/retries/idempotency
- MCP-07 Tool testing strategy (fake servers, contract tests)

---

## Domain 4 — Agent Architecture (single-agent systems done well)
**Goal:** Build an agent loop that’s understandable, testable, and safe.

- AGT-01 Explicit state machine / stages (plan → act → observe → reflect)
- AGT-02 Separation of concerns: planner vs executor vs critic/judge
- AGT-03 Deterministic core + probabilistic edges (where randomness is allowed)
- AGT-04 Tool-use constraints (allowed tools per stage)
- AGT-05 Stop conditions and bounded loops (no infinite “thinking”)
- AGT-06 Human-in-the-loop checkpoints (approval steps when needed)

---

## Domain 5 — Multi-Agent Systems (MAS) & Coordination
**Goal:** Design multi-agent systems that don’t collapse into chatter.

- MAS-01 Role design (specialists, router, coordinator)
- MAS-02 Task decomposition strategy (when/why to split)
- MAS-03 Coordination protocol (handoffs, escalation, consensus rules)
- MAS-04 Shared memory design (blackboard vs per-agent memory)
- MAS-05 Conflict resolution (disagreement handling, tie-breakers)
- MAS-06 Efficiency controls (caps, budgets, termination)
- MAS-07 Eval strategy for MAS (end-to-end + per-role metrics)

---

## Domain 6 — Agent-to-Agent (A2A) Interfaces & Messaging
**Goal:** Agents communicate with explicit contracts, not vibes.

- A2A-01 Message schemas (task requests, results, evidence, confidence)
- A2A-02 Provenance passing (sources, citations, run IDs)
- A2A-03 Capability negotiation (what an agent can/can’t do)
- A2A-04 Trust boundaries (what you accept from another agent)
- A2A-05 Robustness to partial failure (agent unavailable, stale results)
- A2A-06 Versioning & compatibility for agent protocols

---

## Domain 7 — Data & Knowledge Engineering (corpora, pipelines, labeling)
**Goal:** Knowledge inputs are high-quality, versioned, and testable.

- DKE-01 Corpus ingestion pipeline (repeatable, logged)
- DKE-02 Data versioning & provenance
- DKE-03 Chunking strategy + benchmarks
- DKE-04 Metadata strategy (source, time, permissions, sensitivity)
- DKE-05 Feedback loop: collect hard examples, label, add to evals

---

## Domain 8 — Evaluation, Testing & Evals Ops (LLM + agents)
**Goal:** Detect regressions and improve quality systematically.

- EVAL-01 Unit tests for deterministic components
- EVAL-02 Offline eval sets (goldens, scoring rubrics)
- EVAL-03 Simulation harness for agents (controlled environments)
- EVAL-04 LLM-judge usage guidelines (when allowed, how to stabilize)
- EVAL-05 CI gating strategy (fast offline + optional slow online)
- EVAL-06 Eval reporting & trend tracking (quality, latency, cost)

---

## Domain 9 — Reliability & Resilience Engineering
**Goal:** The system fails gracefully and predictably.

- REL-01 Timeouts, retries, idempotency, circuit breakers
- REL-02 Backpressure/rate limiting
- REL-03 Degradation modes (cached answers, partial outputs)
- REL-04 Error taxonomy + user-facing error messaging
- REL-05 Determinism controls (seeds/temperature policies where relevant)

---

## Domain 10 — Observability & Run Artifacts (debugging at scale)
**Goal:** Answer “what happened, why, and how often?”

- OBS-01 Structured logging + correlation IDs
- OBS-02 Trace-like step logs for agent stages/tool calls
- OBS-03 Run artifact persistence (inputs/outputs/context pack metadata)
- OBS-04 Metrics: latency, error rates, token/cost, tool usage
- OBS-05 Redaction policy (don’t leak sensitive data)

---

## Domain 11 — Security, Privacy & Prompt-Injection Defense
**Goal:** Treat the agent as an attacker-facing system.

- SEC-01 Threat model for RAG + tools (prompt injection)
- SEC-02 Instruction/data boundary enforcement
- SEC-03 Secrets management & no-secret logging
- SEC-04 Sandboxing tools (filesystem/network) + allowlists
- SEC-05 Data handling policy (PII, retention, redaction)
- SEC-06 Supply chain hygiene (deps, lockfiles, audits)

---

## Domain 12 — Cost, Latency & Performance Engineering
**Goal:** Control and predict spend and user experience.

- CLP-01 Budgeting (per run/per user/per workflow)
- CLP-02 Caching (prompt/result/retrieval caches) + invalidation strategy
- CLP-03 Model routing (small vs large, fallback policies)
- CLP-04 Profiling + performance baselines

---

## Domain 13 — Deployment, Ops & Release Engineering
**Goal:** Shipping and operating is routine, not scary.

- OPS-01 CI/CD pipeline and release versioning
- OPS-02 Environment config strategy (dev/stage/prod)
- OPS-03 Rollbacks and safe migrations
- OPS-04 On-call basics / incident handling (even if “solo on-call”)
- OPS-05 Dependency upgrades cadence

---

## Domain 14 — Governance / Enterprise Readiness
**Goal:** The system can meet organizational constraints.

- GOV-01 Auditability (who ran what, when, with what inputs/config)
- GOV-02 Policy enforcement (allowed models/tools/data sources)
- GOV-03 Data retention/deletion workflows
- GOV-04 Vendor/model risk notes (where applicable)
- GOV-05 Compliance hooks (as needed: SOC2-ish controls, etc.)

---

## Changing the map (governance)
- Prefer keeping IDs stable once introduced.
- If a competency needs renaming, keep the ID and change the label.
- If we add competencies, add them under the appropriate domain using the same ID pattern.
