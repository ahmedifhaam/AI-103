# 2026-09-17 — Agents, RAG, Search, Security

## Day Summary

Expanded the agent and RAG mental model, learned retrieval strategies and grounding, and continued the session with scenario-based checks. The latest part of the conversation specifically clarified grounding because it had not previously been taught explicitly.

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
└── 03-Foundry-Authentication-Security.md
    ├── API keys
    ├── Entra ID
    ├── Managed identity
    ├── RBAC
    ├── Project connections
    └── Agent identity
```

## Root Summary

**Agent:** orchestration/decision-making component that can use a model, knowledge, tools, and state.

**Knowledge vs tools:** knowledge retrieves information; tools interact with systems or perform operations.

**RAG:** retrieve → augment context → generate grounded answer.

**Search:** keyword = exact terms; vector = semantic meaning; hybrid = both.

**Failure separation:** wrong results → retrieval; badly split context → chunking; unsupported answer despite correct evidence → grounding.

**Grounding clarification:** grounding was explicitly taught in this session after the user noticed it had not yet been covered. The key distinction is retrieval = find evidence; grounding = keep the generated answer supported by that evidence.

**Security:** authentication identifies the caller; authorization determines permissions. Managed identity uses Entra ID; RBAC grants permissions.

## Demonstrated Successfully

- Chose hybrid search when a query combines natural-language intent with an exact error code/identifier.
- Chose vector search when query wording differed from the knowledge-base wording but the meaning was similar.
- Distinguished retrieval problems from chunking problems.
- Correctly identified grounding failure when the right evidence was retrieved but the LLM produced an unsupported answer.
- Corrected/clarified the final answer from an accidental option C to intended option B while preserving the correct reasoning.

## Day Status

Conceptual checks were strong. Hands-on work and some checkpoint requirements remain incomplete, so the relevant gates remain open.

## Next

**RAG retrieval + evaluation** — retrieval quality, groundedness, evaluation concepts, and common RAG failure modes.
