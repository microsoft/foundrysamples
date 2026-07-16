---
title: Create Embeddings for Local Documents
description: Contributor guide for chunking local documents and creating vector embeddings
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Turn a small set of local, redistributable documents into validated chunks and
embedding vectors while preserving the metadata needed for later citation.

## What to build

* A runnable `create_embeddings.py` example
* Plain-text sample documents with source and license metadata
* Deterministic chunking with stable document and chunk identifiers
* Tests for chunk boundaries, empty input, metadata, and vector dimensions

## Acceptance criteria

* The embedding deployment and expected dimensions are configuration values
* Empty, oversized, and unsupported documents fail with actionable messages
* Batching respects documented service limits
* Generated artifacts contain no credentials or customer information
* The README documents input, output, cost, and artifact cleanup

## Contribution notes

Keep chunking separate from the model call so it can be tested offline. Use a
small fixture corpus that future retrieval samples can share without requiring a
download or accepting a restrictive license.

## References

* [Azure OpenAI embeddings](https://learn.microsoft.com/azure/foundry/openai/how-to/embeddings)
* [Azure OpenAI quotas and limits](https://learn.microsoft.com/azure/foundry/openai/quotas-limits)