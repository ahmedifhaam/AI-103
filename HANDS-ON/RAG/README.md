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
- [x] Bring selected source documents into the lab workspace
- [ ] Build/prepare the RAG environment
- [ ] Run baseline retrieval
- [ ] Capture retrieved documents
- [ ] Create evaluation dataset
- [ ] Run Document Retrieval evaluation
- [ ] Compare keyword/vector/hybrid
- [ ] Diagnose a deliberate retrieval failure
- [ ] Evaluate groundedness/relevance/completeness
- [ ] Record final exam takeaways

## Current experiment: source inspection and chunking

The first imported corpus document is `data/source/Zava_Company_Overview.md`.

For the initial chunking experiment, preserve semantic units: headings should remain associated with the content they describe, and structured content such as the vacation table should stay with its surrounding context. Avoid splitting purely by arbitrary character boundaries.

### Upstream provenance

- Repository: `Azure-Samples/azure-search-openai-demo`
- Upstream branch: `main`
- Upstream commit captured for this lab: `3f4a21f03ae3d565aca37cc300e3d38b0c7b582a`
- Source file: `data/Zava_Company_Overview.md`
- Upstream file blob SHA: `cba112d1edfba4cd717e727c8a9ebed77156d41f`

## Lab rule

We learn each concept immediately against the running system where possible. Hypothetical examples are used only when a real experiment cannot demonstrate the concept cleanly.
