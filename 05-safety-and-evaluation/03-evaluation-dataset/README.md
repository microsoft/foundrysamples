---
title: Build a Versioned Evaluation Dataset
description: Contributor guide for a reviewed JSON Lines dataset with stable evaluation cases
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Create a small, versioned JSON Lines dataset that represents expected use,
edge cases, no-answer behavior, safety cases, and task-specific success.

## What to build

* A documented record schema and a small redistributable `.jsonl` dataset
* Stable case identifiers, inputs, expected behavior, and category metadata
* A validation script for schema, duplicates, encoding, and required coverage
* Tests that fail when the dataset contract is broken

## Acceptance criteria

* Every record has provenance and licensing suitable for open source
* No record contains credentials, customer data, or unnecessary personal data
* Expected outcomes are reviewable and do not require exact model wording
* Dataset changes are visible in source control and include a change rationale
* Validation runs offline from the repository root

## Contribution notes

Keep the first dataset small enough for code review. Contributors adding records
should explain the behavior gap represented, run validation, and avoid duplicating
near-identical cases solely to increase the count.

## References

* [Azure AI evaluation datasets](https://learn.microsoft.com/azure/ai-foundry/how-to/develop/evaluate-sdk)
* [JSON Lines format](https://jsonlines.org/)