# AI-103 Progress Dashboard

## Overall

- **Start:** 2026-09-14
- **Exam:** 2026-10-05
- **Core deadline:** 2026-09-30
- **Current status:** 🟢 Day 1 — Foundation passed
- **Current completed gates:** 2
- **Target readiness:** ≥85%

```text
Overall Readiness
███░░░░░░░ 15%

Plan & Manage             ███░░░░░░░ 15%
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
- Correctly identified the model's reasoning/decision-making role in an agent.
- Correctly understood tools as capabilities for retrieving information or performing actions.
- Correctly recognized RAG.
- Correctly identified API-based customer-order lookup as an agent/tool-calling scenario.

### Refinement to retain

> **The model reasons; the agent/runtime executes and manages the workflow.**

An LLM is not automatically an agent simply because it can call a tool.

## Day 1 — Service Selection / Foundry

**Result:** 4/4 scenario questions correct + strong architecture diagram.

### Strong points
- Correctly recognized model catalog, deployment, endpoint, and RAG/search scenarios.
- Correctly placed API and Search as capabilities available to an agent.
- Correctly understood that the agent can decide whether retrieval or an API call is needed.

### Diagram refinement

The user's diagram had the right components and boundaries, but the **request flow was drawn in reverse**. Conceptually:

```text
User → Application → Agent → Tools/Search/API → Model/Reasoning → Application → User
```

Also retain:

> A model deployment belongs to the Foundry project context; the application consumes the deployed model/agent through the appropriate project/agent endpoint.

Current Microsoft documentation describes Foundry projects, project endpoints, project connections, model deployments, and Search connections in this architecture. citeturn0search1turn0search2turn0search9

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

## Mock Exams

| Mock | Date | Score | Time | Weak domains | Action |
|---|---|---:|---:|---|---|
| #1 | Sep 30 | — | — | — | — |
| #2 | Oct 3 | — | — | — | — |

## Readiness Rule

Do not use the percentage as a vanity metric. Readiness is based on **retention + service selection + scenario reasoning + hands-on ability**.
