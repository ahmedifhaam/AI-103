# RAG Evaluation

This area stores evaluation datasets and experiment results.

## Planned evaluation layers

1. Retrieval
2. Document Retrieval
3. Groundedness
4. Relevance
5. Response Completeness

## Ground truth

For retrieval evaluation, record which source documents/chunks are expected to be relevant to each query.

For answer evaluation, record the expected answer when appropriate.

## Experiment discipline

Every evaluation run should record:

- dataset/version
- retrieval configuration
- chunking configuration
- top-K
- filters
- ranking/reranking configuration
- model/deployment where relevant
- metric results
- observed failure
- remediation
- before/after result

Do not overwrite old experiment results. Treat each meaningful configuration change as a new experiment.
