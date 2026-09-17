# 2026-09-17 — Agents, RAG, Search, Security

## Day Summary

Expanded the agent and RAG mental model, learned retrieval strategies and grounding, then moved into Foundry authentication and security.

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

**Security:** authentication identifies the caller; authorization determines permissions. Managed identity uses Entra ID; RBAC grants permissions.

## Day Status

Conceptual checks were strong. Hands-on work and some checkpoint questions remain incomplete, so the relevant gates remain open.
