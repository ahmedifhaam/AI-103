# 02 — Service Selection + Microsoft Foundry Architecture

## Objective
Learn to identify the AI capability from a scenario and map model catalog, deployment, endpoint, project, Search, API tools, and agent responsibilities.

## Teaching Method
Short scenario questions, service-selection comparisons, ASCII architecture, and clarification of project boundaries.

## Questions / Evidence

1. **Sentiment analysis of reviews — which capability?**
   - **User answer:** Text.
   - **Correction:** The expected capability is **Language / sentiment analysis**; “text” describes the input type rather than the service capability.

2. **Identify cars, trucks, and pedestrians — which capability?**
   - **User answer:** Vision.
   - **Result:** Correct.

3. **Extract vendor, invoice number, and total from an invoice — which capability?**
   - **User answer:** Document Intelligence / information extraction.
   - **Result:** Correct.

4. **Answer questions using 50,000 company documents — which approach?**
   - **User answer:** GenAI.
   - **Correction:** The scenario points to **RAG + retrieval/search + GenAI**, not GenAI alone.

5. **Customer-support assistant with knowledge-base retrieval and optional order-status API — architecture?**
   - **User answer:** `User → Application → Agent → RAG → Agent → optional API → Agent → User`, with the agent deciding whether clarification, retrieval, or API access is needed.
   - **Correction/refinement:** Do not memorize RAG → Agent → API as a fixed sequence. The agent decides which tool/knowledge source to use and in what order.
   - **Result:** Strong architecture reasoning.

## Foundry Architecture Check

- **Q1:** Model catalog = model discovery/catalog.
  - **User answer:** B — correct.
- **Q2:** Deployment = making a model available for application use.
  - **User answer:** A — correct.
- **Q3:** Endpoint = how the application reaches a deployed capability.
  - **User answer:** B — correct.
- **Q4:** RAG architecture scenario.
  - **User answer:** C — correct.
- **Q5:** User drew Model and API outside the Foundry project, with Deployment, Agent, and Search-related configuration in the project.
  - **Reasoning:** Model catalog is shared/outside the project; the business API is an external application resource; Azure AI Search is an external resource connected to the project.
  - **Result:** Architecture reasoning was strong; later refined for exact project/resource wording.

## Final Mental Model

```text
MODEL CATALOG
     │
 deployment
     ▼
FOUNDRY PROJECT
 ├── Model Deployment
 ├── Agent
 ├── Connections / Tool configuration
 │      ├──► Azure AI Search (external)
 │      └──► Your API (external)
 └── project context
          │
          ▼
     APPLICATION
          │
          ▼
         USER
```

## Exam Rules
> **RAG is a retrieval pattern; an agent is an orchestration/decision-making component.**

> **The model reasons; the runtime executes the selected tool/workflow.**

> A Foundry project can contain/manage the agent, model deployments, and connections/tool configuration; connected Azure resources such as Search can remain external.

## Weak Areas
- Capability vs input type — initially confused; needs repeated service-selection scenarios.
- RAG vs GenAI — initially too broad; refined to RAG + retrieval + GenAI.

## Gate
Conceptual architecture checkpoint passed. Full gate remains open because hands-on work was not completed.
