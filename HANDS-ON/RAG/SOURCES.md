# RAG Lab Sources

## Primary application

- Repository: https://github.com/Azure-Samples/azure-search-openai-demo
- License: MIT
- Purpose: Microsoft Azure RAG sample using Azure AI Search + Azure OpenAI.

## Selected source documents

These are from the sample application's `data/` directory.

| Source | Purpose in lab |
|---|---|
| `Zava_Company_Overview.md` | Small, easy-to-inspect document for initial ingestion/chunking experiments |
| `employee_handbook.pdf` | Richer policy/HR corpus for retrieval questions |
| `Benefit_Options.pdf` | Benefits-focused retrieval |
| `Northwind_Health_Plus_Benefits_Details.pdf` | Detailed benefits retrieval and comparison |
| `Northwind_Standard_Benefits_Details.pdf` | Benefits comparison / retrieval contrast |

## Upstream data

https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/data

## Evaluation reference

Microsoft's Azure-Samples/rag-evaluator repository documents a JSONL evaluation format containing questions, responses, contexts, retrieved documents, and ground-truth documents:

https://github.com/Azure-Samples/rag-evaluator/blob/main/docs/datasets.md

We will use this as a reference for structuring our own evaluation data, while aligning evaluator names and behavior with the current Microsoft Foundry documentation.

## Attribution

The source application and source documents remain attributed to Azure Samples. The source repository is licensed under MIT.
