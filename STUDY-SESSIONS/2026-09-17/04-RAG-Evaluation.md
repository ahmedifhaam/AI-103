# 04 — RAG Evaluation

## Objective
Understand how to evaluate a RAG pipeline by separating retrieval-side quality from generation-side quality, with particular focus on relevance, coverage, groundedness, and answer correctness.

## Teaching Method
Visual pipeline diagrams, short definitions, boundary/cause-vs-symptom explanations, practical examples, and scenario-based checkpoints with immediate correction.

## Mental Model
```text
                    RAG EVALUATION
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
            RETRIEVAL             GENERATION
            QUALITY                QUALITY
                 │                   │
          ┌──────┴──────┐       ┌────┴────────┐
          ▼             ▼       ▼             ▼
      Relevance      Coverage  Groundedness  Correctness
          │             │       │             │
      Useful?       Enough?  Supported?   Answers the
                                          question correctly?
```

## Concepts

### Retrieval relevance
Asks whether retrieved information is useful for answering the specific user query. Exact wording is not required: semantically or contextually related information can still be relevant.

Example: for “I forgot my password,” a password-reset or credential-recovery document can be relevant even if it does not use the exact phrase “forgot password.”

### Retrieval coverage
Asks whether retrieval found enough of the information needed to answer the query. A result can be relevant but incomplete.

Example: a query asks for refund eligibility, amount, and exceptions, but retrieval only returns the eligibility section. The retrieved content is relevant, but coverage is incomplete.

### Groundedness
Asks whether the generated answer is supported by the retrieved evidence.

Example: retrieved evidence says refunds are available within 30 days, but the LLM answers 60 days. The primary RAG issue is grounding.

### Answer correctness
Asks whether the final answer actually answers the user's question correctly. This is broader than grounding: an answer can fail to provide the requested information even without explicitly contradicting retrieved evidence.

## Cause vs Evaluation Dimension

A key clarification from the session:

```text
Poor chunking
      ↓
Can make retrieval harder
      ↓
Can cause missing evidence
      ↓
Can produce poor retrieval coverage
```

Therefore, **incorrect chunking can be a cause of poor retrieval coverage**, but the two concepts are not interchangeable.

- Chunking = how source information is divided into retrievable units.
- Coverage = whether retrieval ultimately found enough information for the query.

When diagnosing a question, identify the observable failure first, then investigate possible causes.

## Scenario Questions

1. Query asks for the company's refund policy; the correct document exists in the index, but unrelated shipping/delivery documents are consistently returned.
   - **Answer:** Retrieval quality.
   - **Reasoning:** The system is returning the wrong evidence.
   - **Result:** Correct.

2. A RAG system retrieves the correct refund-policy document, but poor chunking separates the actual refund rules across multiple chunks and search often retrieves only one incomplete chunk.
   - **Answer:** Chunking strategy.
   - **Reasoning:** The scenario explicitly identifies poor division of source information as the problem.
   - **Result:** Correct.

3. Correct refund-policy chunk says refunds are available within 30 days, but the LLM answers 60 days.
   - **Answer:** Grounding.
   - **Reasoning:** Correct evidence was retrieved, but the generated answer contradicts it.
   - **Result:** Correct.

4. Query asks “How do I reset my password?” and retrieval returns four password-related chunks plus one username-change chunk.
   - **Answer:** Retrieval relevance.
   - **Reasoning:** Relevance asks whether retrieved information is useful for the query; semantically related password-recovery/reset material can remain relevant even when wording differs.
   - **Result:** Correct.

5. Query asks for refund eligibility, number of days, and carry-over rules; the correct annual/refund document is retrieved but only contains one part of the requested information.
   - **Answer:** Retrieval coverage.
   - **Reasoning:** The evidence is relevant but does not cover enough of the information required to answer the query.
   - **Result:** Correct.

6. Correct document says employees receive 20 annual leave days, but the model answers 25 days.
   - **Answer:** Groundedness.
   - **Reasoning:** The retrieved evidence is correct, but the generated answer contradicts it. The answer is also factually incorrect, but groundedness is the more specific RAG diagnosis.
   - **Result:** Correct.

## Exam Rules
> Wrong/unrelated evidence → **Retrieval relevance/quality**.

> Relevant evidence is present but important requested information is missing → **Retrieval coverage**.

> Correct evidence is retrieved but the answer contradicts or ignores it → **Groundedness**.

> Poor chunking can be a **cause** of poor retrieval coverage; do not treat cause and evaluation dimension as synonyms.

> Related information is not automatically irrelevant. Relevance is judged by usefulness for answering the specific query, not exact word matching.

## Session Result
**Conceptual checks:** 6/6 passed in this RAG evaluation branch.

**Hands-on:** Not yet completed.

**Gate:** 🟡 In progress. Conceptual evaluation understanding is established, but hands-on work and the repository's full topic-gate requirements remain incomplete.

## Next Learning Target
Connect RAG evaluation concepts to Azure AI Foundry evaluation workflows and then cover common RAG failure modes and remediation choices.
