# Harness — Evals

Harness is only valuable if it is **trustworthy**, **repeatable**, and **operationally sane** (cost/latency/security).

This file defines evaluation surfaces that should eventually map into repo evals and CI gates.

## Eval dimensions (core)
### 1) Groundedness
- Are major claims supported by cited sources/chunks?
- Metrics (candidate):
  - % of major claims with citations
  - spot-check correctness of sampled claims against cited text
  - “citation quality” heuristics (avoid citing irrelevant chunks)

### 2) Consistency / Drift
- Are outputs stable under the same inputs/config?
- Metrics:
  - tag stability across reruns
  - schema stability (no missing required fields)
  - summarization drift checks (key facts preserved)

### 3) Usefulness / Actionability
- Does it produce outputs that can be acted on (projects that can be built, study plans that can be followed)?
- Metrics:
  - project spec completeness checklist score
  - success rate of “project runs” (even if mocked initially)
  - human rating rubric (later)

### 4) Reliability
- Does it behave predictably under failures/slow tools?
- Metrics:
  - tool failure rate handling (typed errors)
  - retry correctness and idempotency checks
  - degraded-mode behavior (partial outputs clearly labeled)

### 5) Efficiency (Cost/Latency)
- Does it stay inside budgets?
- Metrics:
  - token/cost per workflow
  - p95 latency per workflow stage
  - tool-call counts and cache hit rates

### 6) Security / Policy
- Does it resist prompt injection and protect secrets?
- Metrics:
  - retrieval injection test set pass rate
  - “no secrets in logs/artifacts” checks
  - allowlist enforcement checks

## Minimum eval artifacts (targets)
- Goldens:
  - `evals/harness/radar_goldens.jsonl`
  - `evals/harness/deepdive_goldens.jsonl`
  - `evals/harness/study_goldens.jsonl`
- Scoring:
  - rubric definitions (what counts as a “major claim”, what counts as “cited”)
  - a scoring script that emits a report suitable for CI
- CI:
  - fast offline gate (schema + citation structure + drift checks)
  - optional slow gate (full model runs, if applicable)

## Run artifacts as eval inputs
Every workflow should emit run artifacts that can be replayed and used for regression:
- inputs (source set, time window, artifact IDs)
- config (model/router settings, budgets)
- outputs (JSON + MD)
- traces/log pointers
- run ID
