# Baseline Retrieval Test Cases

Source: `data/source/Zava_Company_Overview.md`
Chunk set: `data/chunks/001-semantic-chunks.md`

These are the first ground-truth-style test cases for the RAG lab. Relevance is defined at the chunk level.

| ID | Query | Expected relevant chunk(s) | Relevance rationale |
|---|---|---|---|
| Q001 | How many weeks of vacation does a Senior employee receive? | zava-vacation-perks-001 | Directly answered by the Senior row in the vacation table. |
| Q002 | What additional benefit comes with the Executive vacation tier? | zava-vacation-perks-001 | Directly answered by the Executive row. |
| Q003 | What are Zava's core values? | zava-company-overview-001 | The Core Values subsection is contained in this chunk. |
| Q004 | When was Zava founded? | zava-history-001 | The History section states the founding year. |
| Q005 | What happened in 2000? | zava-history-001 | The 2000 milestone is in the History table. |
| Q006 | How does Zava recognize employees? | zava-employee-recognition-001 | The chunk contains the recognition methods. |
| Q007 | Where can someone find Zava's careers information? | zava-join-us-001 | The Join Us section contains the careers link. |
| Q008 | Which vacation tier includes travel vouchers? | zava-vacation-perks-001 | The Senior row identifies the additional benefit. |

## Ground-truth convention

- Relevant chunk = contains the evidence needed to answer the query.
- Non-relevant chunk = does not contain sufficient evidence.
- For the first retrieval experiment, use binary relevance: `1 = relevant`, `0 = not relevant`.

## Important

These are not generated answers. They define the retrieval target so that later keyword/vector/hybrid experiments can be compared against the same queries.
