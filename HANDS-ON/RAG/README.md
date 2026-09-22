# RAG Hands-On Lab

## Objective

Build and evaluate a real RAG workflow using Microsoft's public Azure RAG sample rather than synthetic P123/P678 documents.

## Primary source application

[Azure-Samples/azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo)

The sample is a RAG application using Azure AI Search for retrieval and Azure OpenAI for generation. Its repository includes sample data and evaluation-related functionality.

## Learning objectives

- Inspect real source documents.
- Understand ingestion and chunking.
- Build/search an index.
- Compare keyword, vector, and hybrid retrieval.
- Inspect retrieved chunks.
- Create retrieval ground truth.
- Evaluate retrieval quality.
- Understand NDCG and related retrieval metrics from actual results.
- Introduce retrieval failures and diagnose them.
- Evaluate groundedness and answer quality.
- Connect the practical workflow to Microsoft Foundry evaluation concepts.

## Current status

- [x] Select real Microsoft sample
- [x] Create hands-on tracking area
- [x] Identify source documents
- [ ] Bring selected source documents into the lab workspace
- [ ] Build/prepare the RAG environment
- [ ] Run baseline retrieval
- [ ] Capture retrieved documents
- [ ] Create evaluation dataset
- [ ] Run Document Retrieval evaluation
- [ ] Compare keyword/vector/hybrid
- [ ] Diagnose a deliberate retrieval failure
- [ ] Evaluate groundedness/relevance/completeness
- [ ] Record final exam takeaways

## Lab rule

We learn each concept immediately against the running system where possible. Hypothetical examples are used only when a real experiment cannot demonstrate the concept cleanly.
