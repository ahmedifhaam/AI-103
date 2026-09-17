# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟢 RAG retrieval fundamentals + grounding learned; RAG evaluation next
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

## Daily Log

| Date | Topic | Quiz | Hands-on | Confidence | Weak area | Gate |
|---|---|---:|---|---:|---|---|
| 2026-09-14 | AI mental model: Traditional AI vs GenAI vs Agents, RAG, tool calling | 5/5 | Not yet | 5/5 | Agent runtime vs model responsibility | 🟢 |
| 2026-09-14 | Azure AI capability vs input type; RAG architecture; Foundry model/project/deployment/service map | 4/4 + architecture | Not yet | 4.5/5 | Capability vs input type; RAG retrieval component | 🟢 |
| 2026-09-17 | Agent fundamentals, tools, function calling, OpenAPI/API tools, RAG, chunking, embeddings, vector search | Multiple scenario checks: passed | Not yet | 5/5 | Search strategy comparison still in progress | 🟡 |
| 2026-09-17 | Keyword vs vector vs hybrid search; retrieval vs chunking; grounding | 5/5 | Not yet | 5/5 | RAG evaluation not yet covered | 🟡 |

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

## 2026-09-17 — Search Strategy + Grounding

### How this session was taught
- Visual-first ASCII diagrams showing the RAG pipeline and the three retrieval strategies.
- Short definitions followed by concrete scenarios.
- Exam-trap comparisons: exact terms vs semantic meaning vs mixed requirements.
- Immediate feedback after each answer, with a correction when needed.
- A final mental model was used to distinguish retrieval, chunking, and grounding failures.

### Concepts learned
- **Keyword search** is strong for exact words, IDs, codes, product numbers, and other identifiers.
- **Vector search** is strong when the user's wording differs from the wording in the knowledge base but the meaning is similar.
- **Hybrid search** combines keyword and vector retrieval signals and is useful when a query contains both natural-language intent and exact identifiers.
- **Retrieval** determines which chunks/documents are returned as candidate evidence.
- **Chunking** affects retrieval quality by determining how information is divided into retrievable units; poorly split chunks can lose context.
- **Grounding** means keeping the generated answer supported by trusted retrieved context rather than unsupported model knowledge.

### Scenario questions and responses

1. **Question:** A technical knowledge base contains natural-language documentation plus product names, model numbers, and error codes. Users search using natural language, but exact identifiers must also be found reliably. Which approach: keyword, vector, hybrid, or fine-tuning?
   - **Answer:** Hybrid search.
   - **Reasoning:** Natural-language meaning benefits from vector search while exact identifiers benefit from keyword search.
   - **Result:** Correct.

2. **Question:** A user asks “What is the process for resetting a forgotten password?” while the knowledge base uses terms such as “credential recovery” and “account access restoration.” Which approach is most directly useful?
   - **Answer:** Vector search.
   - **Reasoning:** The wording may not share the same keywords, but the semantic meaning is similar.
   - **Result:** Correct.

3. **Question:** A knowledge base contains product names, error codes, and natural-language explanations. The user asks why they are getting error `E1042` when connecting to the server. Which retrieval strategy?
   - **Answer:** Hybrid search.
   - **Reasoning:** `E1042` requires reliable exact-term matching while the surrounding natural-language intent benefits from semantic retrieval.
   - **Result:** Correct.

4. **Question:** A RAG system retrieves 10 chunks but only 3 are relevant. Which part should be investigated first?
   - **Answer:** Retrieval.
   - **Reasoning:** The immediate issue is which chunks are being returned. Chunking can influence retrieval quality, but the stated failure is the retrieval result.
   - **Result:** Correct.

5. **Question:** The system retrieves the correct document, but the LLM gives an answer unsupported by the retrieved content. What failed?
   - **Answer:** Grounding.
   - **Reasoning:** The evidence was retrieved successfully; the generated answer did not stay supported by that evidence.
   - **Result:** Correct.

### Exam rules to retain

```text
Keyword  → exact terms / IDs / codes
Vector   → semantic meaning / different wording
Hybrid   → exact identifiers + semantic meaning

Retrieval → find the evidence
Chunking  → divide the evidence into useful retrievable units
Grounding → keep the generated answer supported by the evidence
```

### Important clarification

Chunking is important to retrieval quality, but these are different failure modes:

> **Wrong/unrelated chunks returned → Retrieval issue.**

> **Relevant information split into poor fragments → Chunking issue.**

> **Correct evidence retrieved but unsupported answer generated → Grounding issue.**

### Session result

**Quiz:** 5/5 — PASS

**Confidence:** 5/5

**Hands-on:** Not yet completed.

**Topic gate:** 🟡 In progress. Conceptual checks passed, but hands-on work and the repository's full gate requirements remain incomplete.

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
| 🟠 | Keyword vs vector vs hybrid search | Newly learned; more evaluation practice needed | Complete RAG retrieval/evaluation scenarios | 🟡 In progress |
| 🟠 | RAG evaluation | Not yet covered | Learn retrieval quality, groundedness, and evaluation concepts | ⬜ |

## Next Learning Target

**RAG Retrieval + Evaluation**

Focus on:
- Retrieval quality
- Groundedness / grounding
- Evaluating retrieved context and generated answers
- Common RAG failure modes
- Improving retrieval and grounding

After this, continue through the scheduled RAG evaluation material, then agents and agent architecture while preserving the hands-on and topic-gate requirements.

## Mock Exams

| Mock | Date | Score | Time | Weak domains | Action |
|---|---|---:|---:|---|---|
| #1 | Sep 30 | — | — | — | — |
| #2 | Oct 3 | — | — | — | — |

## Readiness Rule

Do not use the percentage as a vanity metric. Readiness is based on **retention + service selection + scenario reasoning + hands-on ability**.
