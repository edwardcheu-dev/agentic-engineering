# 52-Week Roadmap — agentic-engineering

This roadmap is designed for **muscle memory**. Every week:
1) ship a small PR
2) practice 1–2 Gemini CLI drills
3) update notes + state

## The weekly ritual (non-negotiable)
- Pick 1 tiny deliverable (1–3 hours scope)
- Plan → implement → verify (ruff/pyright/pytest)
- Write weekly notes
- Open PR (even solo), merge, tag the week in LEARNING_LOG

## Core Gemini CLI drills (we rotate these)
- Context control: `@path` and minimal context
- Tight loop: `!uv run pytest -q` inside CLI
- Memory sanity: `/memory show`
- Safety: checkpointing + `/restore`
- Automation later: headless `gemini -p ... --output-format json`

## Week-by-week plan (high level)
| Week | Theme | Ship (minimum) | Gemini CLI drill |
|---:|---|---|---|
| 01 | Cockpit setup | Repo scaffold + tooling passes | `/memory show` + `@README.md` |
| 02 | Inner loop | `ae doctor` + tests | `!uv run pytest -q` |
| 03 | Tests-first habit | Add a small utility + tests | Ask for a plan before edits |
| 04 | LLM adapter boundary | `LLMClient` interface + FakeLLM | `/restore` practice (intentional) |
| 05 | Structured output | Pydantic schema output + tests | Use `@src/` selectively |
| 06 | RAG 0 (offline) | chunk + retrieve (toy corpus) | `.geminiignore` sanity check |
| 07 | RAG 1 | embeddings abstraction (fake in unit tests) | `/chat save` snapshot habit |
| 08 | RAG 2 | retrieval + citations contract | `@docs/` + targeted Qs |
| 09 | FastAPI 0 | health endpoint + app skeleton | Review diffs via headless prompt |
| 10 | DB 0 | Postgres model + migration | `!` commands for db/test runs |
| 11 | Integration tests | docker compose test harness | “plan then run” discipline |
| 12 | CI PR gating | GitHub Actions for lint/type/test | Explain gating in notes |
| 13 | Nightly skeleton | scheduled workflow placeholder | Separate fast vs slow checks |
| 14 | Real LLM smoke test 0 | 1–2 tiny live calls (budgeted) | headless JSON output |
| 15 | RAG eval harness 0 | small labeled dataset + scorer | store artifacts in /docs |
| 16 | Observability 0 | structured logs + trace IDs | ask agent to add logging carefully |
| 17 | Tool calling 0 | one tool contract + tests | prompt for tool schema review |
| 18 | Agent loop 0 | planner/executor minimal | compare runs + note drift |
| 19 | Reliability 0 | retries/timeouts + tests | verify failure modes |
| 20 | Prompt/versioning 0 | prompt templates + changelog | keep prompts diffable |
| 21 | Security 0 | prompt injection basics (RAG) | add guardrails checklist |
| 22 | Data hygiene | document corpus rules | practice minimal context |
| 23 | Performance 0 | caching strategy | measure latency + tokens |
| 24 | Cost controls | budgets + caps | enforce in code/tests |
| 25 | CI hardening | matrix + caching | keep PR gating fast |
| 26 | Nightly evals | run dataset nightly | store weekly trend |
| 27 | Streaming | stream endpoint + tests | debug via targeted context |
| 28 | Concurrency | async boundaries | write concurrency tests |
| 29 | Deployment 0 | simple deploy doc | “runbook” writing |
| 30 | Monitoring 0 | metrics + alerts doc | verify logs/traces |
| 31 | Incident drills | simulate failure | write postmortem |
| 32 | Authn/Authz basics | API keys for service | threat-model notes |
| 33 | Tool ecosystem | add one MCP server (optional) | tool inventory discipline |
| 34 | Multi-agent 0 | 2-agent coordination | compare to single-agent |
| 35 | Memory 0 | session memory vs repo memory | document tradeoffs |
| 36 | Evaluation depth | regression thresholds | define “quality gates” |
| 37 | Refactor sprint | pay down tech debt | use checkpoints more |
| 38 | DX improvements | dev scripts + docs | headless helpers |
| 39 | Product polish | better CLI UX | keep tests stable |
| 40 | Capstone plan | pick final capstone | write spec + milestones |
| 41 | Capstone build 1 | core pipeline | PR gating strict |
| 42 | Capstone build 2 | RAG + citations | eval improvements |
| 43 | Capstone build 3 | tools + agent loop | reliability checks |
| 44 | Capstone build 4 | UI/API polish | docs/runbook |
| 45 | Security review | threat model + fixes | least-privilege |
| 46 | Load/perf | basic load test | cost/perf notes |
| 47 | Observability | dashboards doc | incident runbook |
| 48 | Release prep | versioning + changelog | automate checks |
| 49 | Open source polish | CONTRIBUTING + issues | community-ready |
| 50 | Final eval pass | baseline + improvements | compare trends |
| 51 | “Zero → hero” write-up | long blog/guide | summarize learnings |
| 52 | Graduation | demo + retrospective | plan next year |

> This plan can evolve, but we keep it updated in Git so the repository remains our shared memory.