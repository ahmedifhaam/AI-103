# 02 — Search Strategy + Grounding

## Objective
Distinguish keyword, vector, and hybrid search and separate retrieval, chunking, and grounding failures.

## Teaching Method
ASCII diagrams, short definitions, comparison scenarios, exam-trap distinctions, and immediate feedback.

## Mental Model
```text
Keyword → exact terms / IDs / codes
Vector  → semantic meaning / different wording
Hybrid  → exact identifiers + semantic meaning

Retrieval → find evidence
Chunking  → divide evidence into useful retrievable units
Grounding → keep answer supported by evidence
```

## Scenario Questions

1. Natural-language documentation + model numbers + error codes; both semantic intent and exact identifiers matter.
   - **Answer:** Hybrid.
   - **Reasoning:** Vector handles meaning; keyword handles identifiers.
   - **Result:** Correct.

2. User says “reset forgotten password”; KB says “credential recovery” / “account access restoration.”
   - **Answer:** Vector.
   - **Reasoning:** Meaning matches even though wording differs.
   - **Result:** Correct.

3. User asks about error `E1042` with surrounding natural-language explanation.
   - **Answer:** Hybrid.
   - **Reasoning:** Exact code + semantic context.
   - **Result:** Correct.

4. RAG retrieves 10 chunks but only 3 are relevant.
   - **Answer:** Retrieval should be investigated first.
   - **Result:** Correct.

5. Correct document is retrieved but generated answer is unsupported.
   - **Answer:** Grounding failed.
   - **Result:** Correct.

## Exam Rules
> Wrong/unrelated chunks returned → **retrieval issue**.

> Relevant information split into poor fragments → **chunking issue**.

> Correct evidence retrieved but unsupported answer generated → **grounding issue**.

## Session Result
**Quiz:** 5/5 — PASS

**Confidence:** 5/5

**Hands-on:** Not yet completed.

**Gate:** 🟡 In progress.
