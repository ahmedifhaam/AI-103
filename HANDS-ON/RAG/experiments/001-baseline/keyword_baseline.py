"""Minimal keyword retrieval harness for the RAG lab.

This intentionally avoids Azure dependencies. It gives us a reproducible lexical
baseline over the five manually created semantic chunks. Later experiments can
replace this scorer with Azure AI Search keyword/vector/hybrid retrieval.
"""

import math
import re
from pathlib import Path

CHUNKS = {
    "zava-history-001": "Zava founded 1985 1990 handheld personal computer 2000 AI robotics 2015 sustainable eco-friendly product lines.",
    "zava-company-overview-001": "Zava company overview dynamic inclusive workplace core values innovation diversity sustainability.",
    "zava-vacation-perks-001": "Vacation Perks Standard 2 weeks wellness stipend Senior 4 weeks travel vouchers Executive 6 weeks luxury resort.",
    "zava-employee-recognition-001": "Employee Recognition monthly Innovator awards annual gala team-building retreats.",
    "zava-join-us-001": "Join Us talented individuals careers page opportunities.",
}

QUERIES = [
    ("Q001", "How many weeks of vacation does a Senior employee receive?", "zava-vacation-perks-001"),
    ("Q002", "What additional benefit comes with the Executive vacation tier?", "zava-vacation-perks-001"),
    ("Q003", "What are Zava's core values?", "zava-company-overview-001"),
    ("Q004", "When was Zava founded?", "zava-history-001"),
    ("Q005", "What happened in 2000?", "zava-history-001"),
    ("Q006", "How does Zava recognize employees?", "zava-employee-recognition-001"),
    ("Q007", "Where can someone find Zava's careers information?", "zava-join-us-001"),
    ("Q008", "Which vacation tier includes travel vouchers?", "zava-vacation-perks-001"),
]


def tokens(text):
    return re.findall(r"[a-z0-9]+", text.lower())


DOCS = {key: tokens(value) for key, value in CHUNKS.items()}
N = len(DOCS)
DF = {}
for doc in DOCS.values():
    for term in set(doc):
        DF[term] = DF.get(term, 0) + 1

AVG_LEN = sum(map(len, DOCS.values())) / N
K1, B = 1.5, 0.75


def bm25(query, document):
    score = 0.0
    for term in tokens(query):
        if term not in DF or term not in document:
            continue
        frequency = document.count(term)
        idf = math.log(1 + (N - DF[term] + 0.5) / (DF[term] + 0.5))
        denominator = frequency + K1 * (1 - B + B * len(document) / AVG_LEN)
        score += idf * frequency * (K1 + 1) / denominator
    return score


for query_id, query, expected in QUERIES:
    ranked = sorted(
        ((bm25(query, document), chunk_id) for chunk_id, document in DOCS.items()),
        reverse=True,
    )
    print(f"{query_id}: expected={expected}")
    for score, chunk_id in ranked:
        print(f"  {score:.3f}  {chunk_id}")
