---
title: Build and Query a Local Vector Index
description: Contributor guide for indexing embeddings locally and returning ranked document chunks
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Make retrieval mechanics visible by storing a small embedding corpus locally and
ranking chunks for a query with a proven vector-search library.

## What to build

* A runnable index-build and query example
* Persistence of vectors, text, stable identifiers, and citation metadata
* Top-k retrieval with scores and deterministic tie handling
* Offline tests using fixed vectors, including empty-index behavior

## Acceptance criteria

* Query and document vectors use the same deployment and dimensions
* The implementation uses an established installed library, not custom ANN code
* Returned results retain source metadata and have stable ordering
* Corrupt or incompatible index files fail clearly
* Generated index files are documented and safe to delete

## Contribution notes

This is a teaching-scale local index, not a production search service. State the
data-size ceiling in the implementation and point larger or shared workloads to
the Azure AI Search sample.

## References

* [Azure OpenAI embeddings concepts](https://learn.microsoft.com/azure/foundry/openai/concepts/understand-embeddings)
* [Azure AI Search vector search](https://learn.microsoft.com/azure/search/vector-search-overview)