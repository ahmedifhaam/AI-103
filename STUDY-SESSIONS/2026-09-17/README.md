# 2026-09-17 — Agents, RAG, Search, Security

## Day Summary

Expanded the agent and RAG mental model, learned retrieval strategies and grounding, and continued with RAG evaluation. The session now covers retrieval relevance, retrieval coverage, groundedness, and answer correctness, including the distinction between an evaluation dimension and an underlying cause such as poor chunking.

## Topic Tree

```text
2026-09-17
├── 01-Agent-Tools-and-RAG.md
│   ├── Agents
│   ├── Tools
│   ├── Function calling
│   ├── OpenAPI/API tools
│   ├── RAG
│   ├── Chunking
│   ├── Embeddings
│   └── Vector search
│
├── 02-Search-Strategy-and-Grounding.md
│   ├── Keyword search
│   ├── Vector search
│   ├── Hybrid search
│   ├── Retrieval
│   ├── Chunking failure modes
│   └── Grounding
│
├── 03-Foundry-Authentication-Security.md
│   ├── API keys
│   ├── Entra ID
│   ├── Managed identity
│   ├── RBAC
│   ├── Project connections
│   └── Agent identity
│
└── 04-RAG-Evaluation.md
    ├── Retrieval relevance
    ├── Retrieval coverage
    ├── Groundedness
    ├── Answer correctness
    └── Chunking as a possible cause of coverage problems
```

## Root Summary

**Agent:** orchestration/decision-making component that can use a model, knowledge, tools, and state.

**Knowledge vs tools:** knowledge retrieves information; tools interact with systems or perform operations.

**RAG:** retrieve → augment context → generate grounded answer.

**Search:** keyword = exact terms; vector = semantic meaning; hybrid = both.

**Failure separation:** wrong results → retrieval; badly split context → chunking; unsupported answer despite correct evidence → grounding.

**RAG evaluation:** retrieval relevance asks whether retrieved evidence is useful; retrieval coverage asks whether enough required evidence was retrieved; groundedness asks whether the generated answer is supported by retrieved evidence; answer correctness asks whether the answer actually answers the question correctly.

**Cause vs evaluation:** poor chunking can contribute to poor retrieval coverage, but chunking and coverage are not synonyms. Relevance is contextual; semantically related information can still be relevant even when wording differs.

**Security:** authentication identifies the caller; authorization determines permissions. Managed identity uses Entra ID; RBAC grants permissions.

## Demonstrated Successfully

- Chose hybrid search when a query combines natural-language intent with an exact error code/identifier.
- Chose vector search when query wording differed from the knowledge-base wording but the meaning was similar.
- Distinguished retrieval problems from chunking problems.
- Correctly identified grounding failure when the right evidence was retrieved but the LLM produced an unsupported answer.
- Distinguished retrieval relevance from retrieval coverage.
- Recognized that password reset and forgotten-password material can be semantically related and therefore potentially relevant.
- Distinguished poor chunking as a possible cause of poor coverage from coverage as the observable retrieval outcome.
- Correctly identified groundedness when retrieved evidence contradicted the generated answer.

## Day Status

Conceptual checks are strong across the completed RAG branches. Hands-on work and some checkpoint requirements remain incomplete, so the relevant gates remain open.

## Next

**Azure AI Foundry RAG evaluation workflows** — connect the evaluation concepts to Azure-specific evaluation capabilities, then cover common RAG failure modes and remediation choices.
