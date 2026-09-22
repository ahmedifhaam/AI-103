# RAG Lab Data

## Source data

The initial lab corpus comes from the public Microsoft Azure RAG sample:

https://github.com/Azure-Samples/azure-search-openai-demo/tree/main/data

Selected files:

- Zava_Company_Overview.md
- employee_handbook.pdf
- Benefit_Options.pdf
- Northwind_Health_Plus_Benefits_Details.pdf
- Northwind_Standard_Benefits_Details.pdf

## Why we keep the source manifest

The lab should remain reproducible and traceable to the exact public sample rather than silently copying or modifying source material.

The first experiment will start with the small Markdown document. We will add the PDF corpus when we move into richer document extraction/chunking experiments.

## Source commit/reference

Record the upstream commit used for each imported dataset before running experiments so that retrieval results remain reproducible.
