# 01 — AI Mental Model

## Objective
Build the mental model needed to distinguish traditional AI, generative AI, agentic AI, tools, and RAG.

## Teaching Method
Visual-first explanations, short definitions, architecture thinking, scenario questions, and immediate corrections.

## Mental Model

```text
Traditional AI
App controls workflow → model performs inference

Generative AI
App → LLM → generated content

Agentic AI
App/User → Agent/Runtime ↔ Model
                    ↙     ↘
                 Knowledge  Tools
```

## Concepts Learned
- Traditional AI is generally application-controlled; the model is a component performing inference.
- Generative AI places an LLM more centrally in producing content/reasoning.
- Agentic AI adds orchestration: the model can help decide the next action while the runtime executes and manages the workflow.
- Tools provide retrieval or action capabilities.
- RAG retrieves external knowledge and adds it to model context before generation.

## Exam Rules
> **The model reasons; the agent/runtime executes and manages the workflow.**

> An LLM is not automatically an agent just because it can call a tool.

> RAG is a retrieval pattern; it does not imply an agent.

## Questions / Evidence

### Q1 — What distinguishes traditional AI, GenAI, and agents?
- **User answer:** Correctly distinguished application-controlled AI from LLM-centric GenAI and agent orchestration.
- **Result:** Correct.

### Q2 — What is the model's role in an agent?
- **User answer:** Correctly identified the model's reasoning/decision-making role.
- **Result:** Correct.

### Q3 — What are tools?
- **User answer:** Correctly recognized tools as retrieval/action capabilities.
- **Result:** Correct.

### Q4 — What is RAG?
- **User answer:** Correctly recognized RAG as a retrieval pattern.
- **Result:** Correct.

### Q5 — API lookup scenario
- **User answer:** Correctly identified an API lookup as an agent/tool-calling scenario.
- **Result:** Correct.

## Session Result
**Quiz:** 5/5 — PASS

**Confidence:** 5/5

**Hands-on:** Not yet completed.

**Gate:** Conceptual checkpoint passed; full topic gate remains dependent on hands-on and remaining requirements.

## Weak Area
Agent model vs runtime responsibility. This was later refined to: **the model reasons; the runtime executes/manages the workflow.**
