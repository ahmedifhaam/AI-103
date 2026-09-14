# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟢 Day 2 — Foundry architecture checkpoint passed; authentication/security next
- **Completed checkpoints:** 2
- **Target readiness:** ≥85%

```text
Overall Readiness
████░░░░░░ 20%

Plan & Manage             ████░░░░░░ 20%
Generative AI             ███░░░░░░░ 15%
Agents                    ███░░░░░░░ 15%
Computer Vision           ░░░░░░░░░░ 0%
Text Analysis             ██░░░░░░░░ 10%
Information Extraction    ██░░░░░░░░ 10%

Hands-on                  ░░░░░░░░░░ 0%
Exam Questions            ███░░░░░░░ 15%
Retention                 ███░░░░░░░ 15%
```

> Progress is intentionally conservative. A topic is not considered mastered just because it was discussed.

## Daily Log

| Date | Topic | Quiz | Hands-on | Confidence | Weak area | Gate |
|---|---|---:|---|---:|---|---|
| 2026-09-14 | AI mental model: Traditional AI vs GenAI vs Agents, RAG, tool calling | 5/5 | Not yet | 5/5 | Agent runtime vs model responsibility | 🟢 |
| 2026-09-14 | Azure AI capability vs input type; RAG architecture; Foundry model/project/deployment/service map | 4/4 + architecture | Not yet | 4.5/5 | Capability vs input type; RAG retrieval component | 🟢 |

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
| 🟠 | RAG vs GenAI | Initially treated RAG as primarily GenAI | Revisit retrieval/search architecture | ⬜ |
| 🟠 | Agent model vs runtime responsibility | Minor conceptual distinction | Revisit during Agent architecture lesson | ⬜ |

## Next Learning Target

**Foundry authentication, identity, connections, and security**

Focus on:
- Microsoft Entra ID vs API keys
- Managed identity / keyless authentication
- Project connections and credentials
- RBAC at the right Azure resource scope
- Separating application identity from model/tool identity
- Exam scenarios involving secure access to Foundry resources

## Mock Exams

| Mock | Date | Score | Time | Weak domains | Action |
|---|---|---:|---:|---|---|
| #1 | Sep 30 | — | — | — | — |
| #2 | Oct 3 | — | — | — | — |

## Readiness Rule

Do not use the percentage as a vanity metric. Readiness is based on **retention + service selection + scenario reasoning + hands-on ability**.
