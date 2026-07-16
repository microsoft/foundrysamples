---
title: Retrieve from Azure AI Search with Filters
description: Contributor guide for secure vector retrieval with Azure AI Search filters
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Create or reuse a documented Azure AI Search index and retrieve authorized
chunks with vector or hybrid search plus metadata filters.

## What to build

* A minimal index schema with vector, text, source, and filterable fields
* A runnable query using Microsoft Entra ID authentication
* A small indexing path for the repository fixture corpus
* Tests for query construction and filters plus a marked live test

## Acceptance criteria

* No query runs without the required authorization filter when one is configured
* Index and embedding dimensions are validated before upload
* Search keys are neither required by default nor committed
* Results include scores, stable identifiers, and citation metadata
* Provisioning, expected Azure charges, and complete cleanup are documented

## Contribution notes

Keep infrastructure optional and separate from the query teaching point. Reuse
an existing index when configured, and use unique names for resources created by
live tests to prevent accidental deletion of shared data.

## References

* [Azure AI Search vector queries](https://learn.microsoft.com/azure/search/vector-search-how-to-query)
* [Azure AI Search role-based access](https://learn.microsoft.com/azure/search/search-security-rbac)