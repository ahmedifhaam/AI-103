# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟢 RAG + Agent tools fundamentals learned; Keyword vs Vector vs Hybrid Search next
- **Completed checkpoints:** 3
- **Target readiness:** ≥85%

```text
Overall Readiness
█████░░░░░ 25%

Plan & Manage             ████░░░░░░ 20%
Generative AI             █████░░░░░ 25%
Agents                    █████░░░░░ 25%
Computer Vision           ░░░░░░░░░░ 0%
Text Analysis             ██░░░░░░░ 10%
Information Extraction    ██░░░░░░░ 10%

Hands-on                  ░░░░░░░░░░ 0%
Exam Questions            ████░░░░░░ 20%
Retention                 ████░░░░░░ 20%
```

> Progress is intentionally conservative. A topic is not considered mastered just because it was discussed.

## Daily Log

| Date | Topic | Quiz | Hands-on | Confidence | Weak area | Gate |
|---|---|---:|---|---:|---|---|
| 2026-09-14 | AI mental model: Traditional AI vs GenAI vs Agents, RAG, tool calling | 5/5 | Not yet | 5/5 | Agent runtime vs model responsibility | 🟢 |
| 2026-09-14 | Azure AI capability vs input type; RAG architecture; Foundry model/project/deployment/service map | 4/4 + architecture | Not yet | 4.5/5 | Capability vs input type; RAG retrieval component | 🟢 |
| 2026-09-17 | Agent fundamentals, tools, function calling, OpenAPI/API tools, RAG, chunking, embeddings, vector search | Multiple scenario checks: passed | Not yet | 5/5 | Search strategy comparison still in progress | 🟡 |

## Day 1 — Foundation

**Result:** 5/5 — PASS

### Strengths
- Correctly distinguished application-controlled traditional AI from LLM-centric generative AI.
- Correctly understood the model's reasoning/decision-making role in an agent.
- Correctly understood tools as capabilities for retrieving information or performing actions.
- Correctly recognized RAG as a retrieval pattern.
- Correctly identified API-based customer-order lookup as an agent/tool-calling scenario.

### Refinement to retain

> **The model reasons; the agent/runtime executes and manages the workflow.**

An LLM is not automatically an agent simply because it can call a tool.

## Day 2 — Service Selection / Foundry Architecture

**Result:** 4/4 scenario questions correct + strong architecture diagram.

### Strong points
- Correctly recognized model catalog, deployment, endpoint, and RAG/search scenarios.
- Correctly understood that the model catalog is outside the project boundary; deployments are the project-level model resource used by the application/agent.
- Correctly separated the user's business/application API from Foundry itself.
- Correctly understood that Azure AI Search is an external Azure resource connected to the Foundry project.
- Correctly understood that the agent can decide whether to retrieve from Search, call an API, use another tool, or answer directly.

### Architecture refinement — final mental model

```text
                     MODEL CATALOG
                           │
                      deployment
                           │
                           ▼
┌───────────────────────────────────────────────────────┐
│                  MICROSOFT FOUNDRY                    │
│                                                       │
│  ┌─────────────────────────────────────────────────┐  │
│  │                  PROJECT                        │  │
│  │                                                 │  │
│  │   Model Deployment                              │  │
│  │          │                                      │  │
│  │          ▼                                      │  │
│  │        AGENT                                    │  │
│  │          │                                      │  │
│  │          ├──► Search Connection ───────────────┼────► Azure AI Search
│  │          │                                      │  │
│  │          └──► API Tool ─────────────────────────┼────► Your API
│  │                                                 │  │
│  └─────────────────────────────────────────────────┘  │
│                                                       │
└──────────────────────────┬────────────────────────────┘
                           │
                           ▼
                     APPLICATION
                           │
                           ▼
                          USER
```

### Important correction from discussion

Do **not** memorize “Search and API are inside Foundry.” Instead:

> The **Foundry project contains the agent, deployments, and connections/tool configuration**. The actual Azure AI Search resource and your business API can remain external resources.

Also retain:

> **RAG is a retrieval pattern; an agent is an orchestration/decision-making component.** An agent may use RAG, but RAG does not imply an agent.

And:

> **The model reasons; the runtime executes the selected tool/workflow.**

## 2026-09-17 — Agent Tools + RAG Fundamentals

### Learned
- **Agent** is the orchestration component that coordinates a model with instructions, tools, knowledge, and conversation/workflow state.
- An **agent uses a model deployment**; the agent is not the model itself.
- **Tools** give an agent capabilities to retrieve live information or perform operations.
- **Function calling** lets a model request a specific function with structured arguments; the application/runtime executes the function and returns the result.
- **OpenAPI/API tools** are appropriate when exposing an existing REST API with documented operations to an agent.
- **Knowledge/RAG** is primarily a retrieval/grounding pattern, while tools can interact with live external systems or perform actions.
- **RAG pipeline:** documents → chunks → embeddings/index → retrieval → LLM → grounded answer.
- **Chunking** breaks large documents into smaller retrievable units.
- **Embeddings** represent text as vectors so semantic similarity can be measured.
- **Vector search** can retrieve semantically similar content even when exact words do not match.
- At indexing time, documents are prepared/indexed; at query time, the question is embedded, relevant content is retrieved, and the LLM generates the response.

### Checkpoints passed
- Correctly selected **Agent** for orchestrating a model, tools, search, and instructions.
- Correctly selected **Knowledge + API/tool** when answering a user-specific HR question could require both policy and live employee data.
- Correctly selected **OpenAPI/API tool** for an existing REST API used to check inventory and place an order.
- Correctly selected the standard **RAG pipeline** for answering questions from a large set of technical manuals.
- Correctly explained why vector search can retrieve semantically similar documents without exact keyword matches.

### Refinements to retain

> **Knowledge retrieves information; tools interact with systems or perform operations.**

> **Function calling describes/request a callable operation; the runtime/application actually executes it.**

> **RAG adds retrieved external knowledge to the model's context; it is not the same thing as fine-tuning.**

> **Vector search is semantic matching using embeddings; keyword search is useful for exact terms such as identifiers and error codes.**

### Current topic

**Keyword vs Vector vs Hybrid Search** — next lesson/checkpoint.

## Topic Gate

A topic is green only when all are true:

- [ ] I can draw the architecture/flow from memory.
- [ ] I can explain the core concept in simple terms.
- [ ] I can choose the appropriate Azure service for a scenario.
- [ ] I completed the hands-on task.
- [ ] I scored ≥80% on the quick check.
- [ ] I can answer at least one variation of the scenario without notes.

## Weak Area Queue

| Priority | Topic | Why weak? | Remediation | Status |
|---|---|---|---|---|
| 🟠 | Capability vs input type | Initially answered with the input type rather than the capability | Repeat service-selection scenarios | ⬜ |
| 🟠 | RAG vs GenAI | Initially treated RAG as primarily GenAI | Revisit retrieval/search architecture | 🟡 Improved |
| 🟠 | Agent model vs runtime responsibility | Minor conceptual distinction | Revisit during Agent architecture lesson | 🟡 Improved |
| 🟠 | Keyword vs vector vs hybrid search | Not yet completed | Compare retrieval signals and complete scenario gate | ⬜ |

## Next Learning Target

**Keyword vs Vector vs Hybrid Search**

Focus on:
- Keyword/full-text search
- Vector search and semantic similarity
- Embeddings and vector representations
- Hybrid search
- When exact identifiers/codes favor keyword retrieval
- When natural-language meaning favors vector retrieval
- Combining retrieval signals for RAG

After this, continue through the scheduled RAG retrieval/evaluation material, then agents and agent architecture while preserving the hands-on and topic-gate requirements.

## Mock Exams

| Mock | Date | Score | Time | Weak domains | Action |
|---|---|---:|---:|---|---|
| #1 | Sep 30 | — | — | — | — |
| #2 | Oct 3 | — | — | — | — |

## Readiness Rule

Do not use the percentage as a vanity metric. Readiness is based on **retention + service selection + scenario reasoning + hands-on ability**.
