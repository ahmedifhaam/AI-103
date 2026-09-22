# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟡 RAG evaluation/remediation concepts are strong and scenario performance is consistent. Hands-on work has now started with a real Microsoft Azure RAG sample. The Foundry authentication/security checkpoint remains open.
- **Completed checkpoints:** 7
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

Hands-on                  █░░░░░░░░░ 5%
Exam Questions            ██████░░░░ 30%
Retention                 ████░░░░░░ 20%
```

> Progress is intentionally conservative. A topic is not considered mastered just because it was discussed.

## Study Session Tree

Detailed session evidence is stored under [STUDY-SESSIONS/](../STUDY-SESSIONS/README.md).

```text
STUDY-SESSIONS/
├── 2026-09-14/
│   ├── README.md
│   ├── 01-AI-Mental-Model.md
│   └── 02-Service-Selection-Foundry.md
│
├── 2026-09-17/
│   ├── README.md
│   ├── 01-Agent-Tools-and-RAG.md
│   ├── 02-Search-Strategy-and-Grounding.md
│   ├── 03-Foundry-Authentication-Security.md
│   └── 04-RAG-Evaluation.md
│
└── 2026-09-18/
    ├── README.md
    └── 01-RAG-Evaluation-Remediation.md
```

## Hands-On Tree

Detailed practical work is stored separately under [HANDS-ON/](../HANDS-ON/README.md).

```text
HANDS-ON/
├── README.md
└── RAG/
    ├── README.md
    ├── SOURCES.md
    ├── data/
    │   └── README.md
    ├── evaluation/
    │   └── README.md
    └── experiments/
        └── README.md
```

## Session Index

| Date | Session | Result | Hands-on | Gate | Details |
|---|---|---|---|---|---|
| 2026-09-14 | AI mental model | 5/5 | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-14/01-AI-Mental-Model.md) |
| 2026-09-14 | Service selection + Foundry architecture | 4/4 + architecture | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-14/02-Service-Selection-Foundry.md) |
| 2026-09-17 | Agent tools + RAG fundamentals | Multiple scenario checks passed | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/01-Agent-Tools-and-RAG.md) |
| 2026-09-17 | Search strategy + grounding | 6/6 meaningful scenarios | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/02-Search-Strategy-and-Grounding.md) |
| 2026-09-17 | Foundry authentication + security | 6 questions pending | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/03-Foundry-Authentication-Security.md) |
| 2026-09-17 | RAG evaluation | 12/12 recorded checks | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-17/04-RAG-Evaluation.md) |
| 2026-09-18 | RAG evaluation + remediation | NDCG + 5/5 remediation checks | Not yet | 🟡 | [Session](../STUDY-SESSIONS/2026-09-18/01-RAG-Evaluation-Remediation.md) |
| 2026-09-22 | RAG hands-on setup | Real Microsoft sample selected; lab structure created | 🟡 Started | 🟡 | [Hands-on lab](../HANDS-ON/RAG/README.md) |

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
    ├── Grounding ✓ conceptual
    └── RAG evaluation 🟡 in progress
        ├── Retrieval relevance ✓
        ├── Retrieval coverage ✓
        ├── Recall@K ✓ taught
        ├── Precision@K ✓ taught
        ├── NDCG ✓ scenario checkpoint passed
        ├── Groundedness ✓
        ├── Answer correctness ✓
        ├── Foundry process/system evaluation ✓ taught
        ├── Document Retrieval evaluator ✓ taught
        └── Failure modes + remediation 🟡
            ├── Semantic/vector retrieval ✓
            ├── Hybrid retrieval ✓
            ├── Chunking remediation ✓
            ├── Ranking/reranking ✓
            └── Precision / Top-K / filtering ✓
        └── Hands-on lab 🟡
            ├── Real sample selected ✓
            ├── Lab structure ✓
            ├── Source corpus identified ✓
            ├── Ingestion/indexing ⬜
            ├── Retrieval experiments ⬜
            └── Evaluation experiments ⬜
```

## Weak Area Queue

| Priority | Topic | Why weak? | Remediation | Status |
|---|---|---|---|---|
| 🟠 | Capability vs input type | Initially answered with the input type rather than the capability | Repeat service-selection scenarios | ⬜ |
| 🟠 | RAG vs GenAI | Initially treated RAG as primarily GenAI | Revisit retrieval/search architecture | 🟡 Improved |
| 🟠 | Agent model vs runtime responsibility | Minor conceptual distinction | Revisit during agent architecture | 🟡 Improved |
| 🟠 | Keyword vs vector vs hybrid search | Newly learned; more evaluation practice needed | Continue retrieval/evaluation scenarios | 🟡 In progress |
| 🟠 | RAG evaluation | Ranking and remediation now demonstrated; hands-on remains | Complete hands-on + multi-symptom scenarios | 🟡 In progress |
| 🟠 | Authentication/security checkpoint | Concepts taught but six checkpoint questions unanswered | Complete checkpoint + hands-on | 🟡 Open |

## Next Learning Target

**RAG hands-on evaluation using a real Microsoft sample.** Start with the source corpus, inspect ingestion/chunking, then run baseline retrieval before changing search strategies. Connect each experiment back to the evaluation concepts already learned.

The Foundry authentication/security checkpoint remains an open parallel checkpoint and should not be treated as mastered until its questions and hands-on gate are completed.

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
