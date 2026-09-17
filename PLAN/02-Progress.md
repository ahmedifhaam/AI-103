# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟡 Foundry authentication/security taught; checkpoint questions pending
- **Completed checkpoints:** 4
- **Target readiness:** ≥85%

```text
Overall Readiness
█████░░░░░ 25%

Plan & Manage             ████░░░░░░ 20%
Generative AI             ██████░░░░ 30%
Agents                    █████░░░░░ 25%
Computer Vision           ░░░░░░░░░░ 0%
Text Analysis             ██░░░░░░░ 10%
Information Extraction    ██░░░░░░░ 10%

Hands-on                  ░░░░░░░░░░ 0%
Exam Questions            █████░░░░░ 25%
Retention                 ████░░░░░░ 20%
```

> Progress is intentionally conservative. A topic is not considered mastered just because it was discussed.

## Study Session Tree

Detailed session evidence is now stored under [`STUDY-SESSIONS/`](../STUDY-SESSIONS/README.md).

```text
STUDY-SESSIONS/
├── 2026-09-14/
│   ├── README.md
│   ├── 01-AI-Mental-Model.md
│   └── 02-Service-Selection-Foundry.md
│
└── 2026-09-17/
    ├── README.md
    ├── 01-Agent-Tools-and-RAG.md
    ├── 02-Search-Strategy-and-Grounding.md
    └── 03-Foundry-Authentication-Security.md
```

## Session Index

| Date | Session | Result | Hands-on | Gate | Details |
|---|---|---|---|---|---|
| 2026-09-14 | AI mental model | 5/5 | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-14/01-AI-Mental-Model.md) |
| 2026-09-14 | Service selection + Foundry architecture | 4/4 + architecture | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-14/02-Service-Selection-Foundry.md) |
| 2026-09-17 | Agent tools + RAG fundamentals | Multiple scenario checks passed | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/01-Agent-Tools-and-RAG.md) |
| 2026-09-17 | Search strategy + grounding | 5/5 | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/02-Search-Strategy-and-Grounding.md) |
| 2026-09-17 | Foundry authentication + security | 6 questions pending | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/03-Foundry-Authentication-Security.md) |

## Current Learning Tree

```text
AI-103
├── Plan & Manage
│   └── Microsoft Foundry
│       ├── Architecture ✓ conceptual
│       ├── Projects ✓ conceptual
│       ├── Model catalog / deployments ✓ conceptual
│       └── Authentication & Security 🟡
│           ├── API keys ✓ taught
│           ├── Entra ID ✓ taught
│           ├── Managed identity ✓ taught
│           ├── RBAC ✓ taught
│           ├── Project connections ✓ taught
│           └── Agent identity ✓ taught
│
└── Generative AI / Agents
    ├── Agent fundamentals ✓ conceptual
    ├── Tools / function calling ✓ conceptual
    ├── RAG ✓ conceptual
    │   ├── Chunking ✓
    │   ├── Embeddings ✓
    │   └── Vector search ✓
    ├── Search strategies ✓ conceptual
    │   ├── Keyword ✓
    │   ├── Vector ✓
    │   └── Hybrid ✓
    └── Grounding ✓ conceptual
        └── RAG evaluation ⬜ next
```

## Weak Area Queue

| Priority | Topic | Why weak? | Remediation | Status |
|---|---|---|---|---|
| 🟠 | Capability vs input type | Initially answered with the input type rather than the capability | Repeat service-selection scenarios | ⬜ |
| 🟠 | RAG vs GenAI | Initially treated RAG as primarily GenAI | Revisit retrieval/search architecture | 🟡 Improved |
| 🟠 | Agent model vs runtime responsibility | Minor conceptual distinction | Revisit during agent architecture | 🟡 Improved |
| 🟠 | Keyword vs vector vs hybrid search | Newly learned; more evaluation practice needed | Continue retrieval/evaluation scenarios | 🟡 In progress |
| 🟠 | RAG evaluation | Not yet covered | Learn retrieval quality, groundedness, evaluation, and failure modes | ⬜ |
| 🟠 | Authentication/security checkpoint | Concepts taught but six checkpoint questions unanswered | Complete checkpoint + hands-on | 🟡 Open |

## Next Learning Target

**Complete Foundry Authentication/Security checkpoint → RBAC + project roles → RAG evaluation.**

## Topic Gate

A topic is green only when all are true:

- [ ] Draw architecture/flow from memory
- [ ] Explain the core concept simply
- [ ] Choose the appropriate Azure service for a scenario
- [ ] Complete the hands-on task
- [ ] Score ≥80% on the quick check
- [ ] Answer a scenario variation without notes

## Mock Exams

| Mock | Date | Score | Time | Weak domains | Action |
|---|---|---:|---:|---|---|
| #1 | Sep 30 | — | — | — | — |
| #2 | Oct 3 | — | — | — | — |

## Readiness Rule

Do not use the percentage as a vanity metric. Readiness is based on **retention + service selection + scenario reasoning + hands-on ability**.
