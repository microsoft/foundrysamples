---
title: Generate Grounded Answers with Citations
description: Contributor guide for retrieval-augmented answers with citations and a no-answer path
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Combine retrieval and generation while requiring claims to cite retrieved
sources and returning a clear no-answer result when evidence is insufficient.

## What to build

* A runnable retrieval-augmented generation flow
* A structured answer contract containing answer, citations, and status
* Citation validation against the chunks supplied to the model
* Tests for supported, unsupported, conflicting, and empty retrieval results

## Acceptance criteria

* Retrieved text is delimited and treated as untrusted data
* Every emitted citation resolves to a supplied source
* Low-evidence queries return the documented no-answer status
* The prompt does not ask the model to invent missing source metadata
* Tests use deterministic fake retrieval and model responses

## Contribution notes

Keep retrieval, prompt assembly, response validation, and citation checking as
visible steps. Do not measure groundedness by checking whether citations merely
exist; validate their identifiers and cover unsupported claims in evaluation.

## References

* [Azure AI Search retrieval-augmented generation](https://learn.microsoft.com/azure/search/retrieval-augmented-generation-overview)
* [Azure AI Search relevance](https://learn.microsoft.com/azure/search/search-relevance-overview)