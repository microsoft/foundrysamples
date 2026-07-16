---
title: Return Validated Structured Output
description: Contributor guide for converting model output into a validated Python model
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Request structured data from a Foundry model, validate it as a typed Python
model, and reject responses that do not satisfy the application contract.

## What to build

* A runnable `structured_output.py` example
* A small schema with required fields, constraints, and a clear business use
* Handling for refusal, incomplete output, and validation failure
* Deterministic tests for valid and invalid model responses

## Acceptance criteria

* The SDK receives an explicit response schema
* Application code uses the validated object rather than parsing text manually
* Validation errors produce an actionable message without exposing secrets
* Tests make no network requests and cover every failure branch
* The completed README includes setup, expected output, live-test, and cost notes

## Contribution notes

Keep the schema and model call in the primary file so readers can copy the
pattern. Prefer an already-installed validation library or SDK feature over a
custom parser. Run the sample and its focused tests from the repository root.

## References

* [Azure OpenAI structured outputs](https://learn.microsoft.com/azure/foundry/openai/how-to/structured-outputs)
* [OpenAI Python structured outputs](https://github.com/openai/openai-python#parsing-structured-outputs)