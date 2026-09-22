# Experiment 001 — Baseline Semantic Chunking

## Objective

Create a small, inspectable baseline corpus from the real Zava source document using semantic boundaries.

## Source

`data/source/Zava_Company_Overview.md`

## Strategy

Keep headings, explanatory text, and structured content together when they describe the same concept.

Baseline chunks:

1. History + milestone table
2. Company Overview + Core Values
3. Vacation Perks + vacation-tier table
4. Employee Recognition
5. Join Us

Each chunk has explicit metadata for document, section, and chunk ID.

## Why this is the baseline

This is intentionally simple. We want a known starting point before introducing different chunk sizes, overlap, or automated chunking.

## Expected retrieval behavior

A query about vacation duration should retrieve the Vacation Perks chunk with the table intact.

A query about Zava's values should retrieve the Company Overview/Core Values chunk.

A query about company milestones should retrieve the History chunk.

## Next experiment

Use these chunks as the baseline retrieval corpus, then compare keyword, vector, and hybrid retrieval.

## AI-103 connection

This experiment demonstrates that chunking is part of the ingestion/indexing stage. Poor chunk boundaries can cause relevant information to be separated, reducing retrieval quality even when the source document contains the answer.
