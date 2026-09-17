# 01 — Agent, Tools + RAG Fundamentals

## Objective
Understand agent orchestration, tools, function calling, OpenAPI/API tools, and the RAG pipeline.

## Teaching Method
Visual pipelines, short definitions, concrete scenarios, immediate correction, and architecture reasoning.

## Mental Model
```text
User
  ↓
Application / Agent Runtime
  ↓
Agent ↔ Model
  ├── Knowledge / RAG
  ├── Tools
  └── Conversation / workflow state
```

RAG pipeline:
```text
Documents → Chunks → Embeddings / Index → Retrieval → LLM → Grounded answer
```

## Concepts
- Agent coordinates model, instructions, tools, knowledge, and state.
- Agent uses a model deployment; agent is not the model itself.
- Tools retrieve live information or perform operations.
- Function calling lets the model request a function with structured arguments; runtime executes it.
- OpenAPI/API tools are useful for existing documented REST APIs.
- Chunking creates smaller retrievable units.
- Embeddings represent text as vectors for semantic similarity.
- Vector search can find semantically similar content despite different wording.
- Indexing prepares knowledge; query-time retrieval finds relevant content for generation.

## Scenario Checkpoints
- Agent for orchestration of model + tools + search + instructions — **correct**.
- Knowledge + API/tool for HR policy plus live employee data — **correct**.
- OpenAPI/API tool for an existing inventory/order REST API — **correct**.
- Standard RAG pipeline for technical manuals — **correct**.
- Vector search for semantically similar wording — **correct**.

## Exam Rules
> **Knowledge retrieves information; tools interact with systems or perform operations.**

> **Function calling requests/describes an operation; the runtime executes it.**

> **RAG is retrieval + grounding, not fine-tuning.**

> **The model reasons; the runtime executes the selected tool/workflow.**

## Gate
Conceptual checkpoints passed. Hands-on not completed; full gate remains open.
