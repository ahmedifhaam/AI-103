# 02 — Search Strategy + Grounding

## Objective
Distinguish keyword, vector, and hybrid search and separate retrieval, chunking, and grounding failures.

## Teaching Method
ASCII diagrams, short definitions, comparison scenarios, exam-trap distinctions, immediate feedback, and a final troubleshooting mental model. Grounding was introduced explicitly only after the user identified that it had not yet been taught.

## Mental Model
```text
Keyword → exact terms / IDs / codes
Vector  → semantic meaning / different wording
Hybrid  → exact identifiers + semantic meaning

Retrieval → find evidence
Chunking  → divide evidence into useful retrievable units
Grounding → keep answer supported by evidence
```

### RAG troubleshooting flow
```text
Documents
   ↓
Chunking
   ↓
Embeddings + Index
   ↓
Retrieval
   ↓
Relevant context
   ↓
Grounding
   ↓
LLM generates answer
```

## Concepts

### Keyword search
Useful when exact terms matter, especially identifiers, product numbers, and error codes.

### Vector search
Uses embeddings to retrieve semantically similar content even when the user's wording differs from the knowledge-base wording.

### Hybrid search
Combines keyword and vector retrieval signals. A natural-language query containing an exact identifier is a typical fit.

### Retrieval vs chunking
Retrieval determines which chunks/documents are returned. Chunking determines how source information is divided into retrievable units. Poor chunking can hurt retrieval quality, but a question explicitly describing irrelevant returned chunks points first to retrieval.

### Grounding
Grounding means keeping a generated answer supported by trusted retrieved context instead of unsupported model knowledge. Retrieved chunks act as evidence/context for generation.

```text
Retrieval → "Did we find the right information?"
Grounding → "Did the answer stay supported by that information?"
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
   - **Reasoning:** The immediate problem is which chunks are being returned. The user correctly noted that chunking can influence this, but the stated failure is at retrieval.
   - **Result:** Correct.

5. Correct document is retrieved but generated answer is unsupported.
   - **Answer:** Grounding failed.
   - **Reasoning:** The evidence was retrieved successfully; the answer did not follow/support itself with that evidence.
   - **Result:** Correct.

6. Retrieved chunk says “Refunds are available within 30 days of purchase,” but the LLM answers “You have 60 days.”
   - **Answer:** Grounding.
   - **Reasoning:** The correct evidence was found, but the generated answer contradicted/ignored it. The user selected B and explained that the model was answering from its own knowledge rather than staying grounded.
   - **Result:** Correct.

## Correction / Learning Moment

The user initially said **C** for the refund scenario, then immediately clarified that **B** was intended. The conceptual reasoning was already correct: the system found the right evidence, but generation did not stay grounded. No chunking failure was indicated.

## Exam Rules
> Wrong/unrelated chunks returned → **retrieval issue**.

> Relevant information split into poor fragments → **chunking issue**.

> Correct evidence retrieved but unsupported answer generated → **grounding issue**.

> **Keyword = exact. Vector = meaning. Hybrid = both.**

## Session Result
**Conceptual checks:** 6/6 meaningful scenarios passed (including the user's correction/clarification on the final grounding question).

**Confidence:** 5/5 was explicitly established during this session.

**Hands-on:** Not yet completed.

**Gate:** 🟡 In progress. Conceptual checks are strong, but hands-on work and the repository's full topic-gate requirements remain incomplete.

## Next Learning Target
RAG retrieval + evaluation, including retrieval quality, groundedness/grounding, evaluation concepts, and common RAG failure modes.
