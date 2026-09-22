# Experiment 002 — Keyword Retrieval Baseline

## Objective

Run the first retrieval experiment against the real Zava corpus using a local BM25-style lexical scorer.

This is intentionally a lightweight baseline. It does **not** claim to reproduce Azure AI Search scoring. The purpose is to establish observable lexical-retrieval behavior before introducing vector and hybrid retrieval.

## Results

| Query | Expected chunk | Top result | Result |
|---|---|---|---|
| Q001 | Vacation | Vacation | Correct |
| Q002 | Vacation | Vacation | Correct |
| Q003 | Company/Values | Company/Values | Correct |
| Q004 | History | History | Correct |
| Q005 | History | History | Correct |
| Q006 | Recognition | Company/Values | **Miss** |
| Q007 | Join Us | Join Us | Correct |
| Q008 | Vacation | Vacation | Correct |

**Top-1 accuracy: 7/8 (87.5%)**

## Important failure

Q006 asks:

> How does Zava recognize employees?

The relevant section is **Employee Recognition**, but a lexical scorer can struggle because the query uses **recognize** while the document uses **recognition**.

This is a concrete example of why exact lexical matching can miss semantically relevant content even when the answer is clearly present.

## AI-103 connection

- Keyword search is strong when query terms overlap the source.
- Different word forms or different wording can reduce lexical retrieval quality.
- Vector/semantic retrieval is designed to capture meaning beyond exact token overlap.
- Hybrid retrieval combines lexical and semantic signals.

## Next

Run the same eight queries with vector retrieval and compare which failures disappear or appear.
