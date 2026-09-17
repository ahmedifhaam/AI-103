# 04 — RAG Evaluation

## Objective
Understand how to evaluate a RAG pipeline by separating retrieval-side quality from generation-side quality, then connect the concepts to Azure AI Foundry evaluation workflows.

## Teaching Method
Visual pipeline diagrams, short definitions, boundary/cause-vs-symptom explanations, practical examples, Azure-specific mapping, and scenario-based checkpoints with immediate correction. New metrics were taught before being tested.

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

## Retrieval Metrics

### Recall@K
Asks whether the expected/relevant information was retrieved within the top K results.

Example: if the expected chunk appears in the top 5 for 82 of 100 questions, Recall@5 = 82%.

Mental model: **“Did I find what I needed within the top K?”**

### Precision@K
Asks how many of the top K retrieved results are relevant.

Example: if 3 of 5 retrieved chunks are relevant, Precision@5 = 60%.

Mental model: **“How much of what I retrieved was useful?”**

### Recall vs Precision
```text
RECALL                         PRECISION
“Did I find it?”               “Was what I found useful?”
     │                               │
Missing useful evidence?       Too much irrelevant noise?
```

A system can have high precision but low recall: the results it returns are mostly useful, but it misses other useful evidence.

## Azure AI Foundry Evaluation Workflow

```text
                 TEST DATASET
                      │
                      ▼
                RAG APPLICATION
                      │
             ┌────────┴────────┐
             ▼                 ▼
         Retrieval          Generation
             │                 │
             ▼                 ▼
       Retrieved chunks    Final answer
             │                 │
             └────────┬────────┘
                      ▼
                  Evaluation
```

### Process evaluation
Focuses on whether the retrieval/search process worked.

- **Retrieval:** evaluates whether retrieved context is relevant to the query.
- **Document Retrieval:** compares retrieved documents with ground-truth relevance information and can report search-quality metrics such as Fidelity, NDCG, XDCG, and Max Relevance.

Mental model: **Document Retrieval = retrieval + ground truth.**

### System evaluation
Focuses on the final generated response.

- **Groundedness:** whether the response is supported by the provided context.
- **Relevance:** whether the response addresses the user's question.
- **Response Completeness:** whether expected important information is missing from the response.

## Test Dataset Concepts

A RAG evaluation dataset can contain different forms of expected information:

```text
                 TEST DATASET
                      │
          ┌───────────┴───────────┐
          ▼                       ▼
   Retrieval ground truth     Answer ground truth
          │                       │
   Expected relevant docs/   Expected/reference
   chunks                    answer information
```

Retrieval ground truth is useful for evaluating search/retrieval performance. Answer ground truth is useful for evaluating final answer quality/correctness.

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
   - **Result:** Correct.

2. A RAG system retrieves the correct refund-policy document, but poor chunking separates the actual refund rules across multiple chunks and search often retrieves only one incomplete chunk.
   - **Answer:** Chunking strategy.
   - **Result:** Correct.

3. Correct refund-policy chunk says refunds are available within 30 days, but the LLM answers 60 days.
   - **Answer:** Grounding.
   - **Result:** Correct.

4. Query asks “How do I reset my password?” and retrieval returns four password-related chunks plus one username-change chunk.
   - **Answer:** Retrieval relevance.
   - **Result:** Correct.

5. Query asks for refund eligibility, number of days, and carry-over rules; the correct document is retrieved but only contains one part of the requested information.
   - **Answer:** Retrieval coverage.
   - **Result:** Correct.

6. Correct document says employees receive 20 annual leave days, but the model answers 25 days.
   - **Answer:** Groundedness.
   - **Result:** Correct.

7. Test set has 100 questions with expected evidence known; top 5 retrieval results are returned for each question. The set is primarily used to evaluate retrieval performance.
   - **Answer:** Retrieval performance.
   - **Result:** Correct.

8. RAG retrieves correct chunks 95% of the time, but generated answers are incomplete or unsupported.
   - **Answer:** Generation quality / groundedness.
   - **Result:** Correct.

9. Expected chunk appears in the top 5 results for 82 of 100 questions.
   - **Answer:** Recall@5 = 82%.
   - **Result:** Correct.

10. Five retrieved chunks contain three relevant chunks.
   - **Answer:** Precision@5 = 60%.
   - **Result:** Correct. This metric was taught immediately before the checkpoint.

11. Dataset contains questions, expected relevant documents, and actual retrieved documents; the goal is to evaluate how well the search system retrieved expected documents.
   - **Answer:** Azure AI Foundry Document Retrieval evaluator.
   - **Result:** Correct.

12. Query asks about parental leave, but retrieval returns parking, travel reimbursement, and expense documents. The final answer is also wrong.
   - **Answer:** Retrieval quality.
   - **Result:** Correct; retrieval is the first failed stage.

## Exam Rules
> Wrong/unrelated evidence → **Retrieval relevance/quality**.

> Relevant evidence is present but important requested information is missing → **Retrieval coverage**.

> Correct evidence is retrieved but the answer contradicts or ignores it → **Groundedness**.

> Poor chunking can be a **cause** of poor retrieval coverage; do not treat cause and evaluation dimension as synonyms.

> Related information is not automatically irrelevant. Relevance is judged by usefulness for answering the specific query, not exact word matching.

> **Recall@K** asks whether needed/relevant evidence appeared within the top K.

> **Precision@K** asks how much of the top K was relevant.

> **Document Retrieval** is the Foundry evaluator to use when evaluating retrieved documents against ground-truth relevance information.

> Trace RAG failures left-to-right: **question → retrieval → context → generation → answer**. Diagnose the first failed stage.

## Session Result
**Conceptual checks:** 12/12 recorded checks passed, including 6 original conceptual scenarios, retrieval/evaluation workflow checks, and newly taught Recall@5/Precision@5 checks.

**Hands-on:** Not yet completed.

**Gate:** 🟡 In progress. Conceptual evaluation understanding is established, but hands-on work and the repository's full topic-gate requirements remain incomplete.

## Next Learning Target
Continue Azure-specific RAG evaluation with ranking metrics such as NDCG and then cover common RAG failure modes and remediation choices. Do not test a new metric before teaching it.
