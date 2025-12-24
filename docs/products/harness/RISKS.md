# Harness — Risks & Failure Modes

This file exists to preserve the integrity of Harness as it expands.

## Risk: “Radar” becomes hype instead of evidence
Failure mode:
- claiming trends without clear selection criteria and citations

Mitigations:
- define “trend” operationally (window + count/burst + representative items)
- require citations for “why it matters”
- include selection criteria in the digest metadata

## Risk: Summarization drift on long documents
Failure mode:
- synthesized summaries diverge from source material

Mitigations:
- chunk IDs + provenance
- map-reduce summarization with citation requirements
- fidelity checks on key claims

## Risk: Taxonomy drift
Failure mode:
- tags change run-to-run, ruining comparability and trends

Mitigations:
- strict taxonomy enforcement + versioning + migrations
- reject unknown tags during verification

## Risk: Prompt injection via retrieved content
Failure mode:
- retrieved text influences system behavior (“ignore previous instructions…”)

Mitigations:
- strict instruction/data boundary
- retrieval content never becomes instructions
- allowlists + sanitization; log injection attempts

## Risk: Cost and latency blowups
Failure mode:
- runaway tool calls / long model chains / no bounded loops

Mitigations:
- budgets and stop conditions everywhere
- caching (retrieval/results) with clear invalidation policy
- profiling baselines and CI budget checks (later)

## Risk: Un-auditable outputs
Failure mode:
- cannot reproduce or explain why an output was produced

Mitigations:
- run artifacts as a first-class output
- correlation IDs and step traces
- record inputs/config/model/tool versions
