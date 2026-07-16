---
title: Define and Execute a Typed Function Tool
description: Contributor guide for validating and executing model-requested function calls
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Expose one read-only Python function to a model, validate its arguments, execute
it under application control, and return a typed result to the model.

## What to build

* A runnable function-calling loop with one narrowly scoped tool
* A generated or explicit JSON schema derived from typed arguments
* Argument validation, an allowlist, timeout, and result-size limit
* Tests for valid, unknown, malformed, and repeated tool calls

## Acceptance criteria

* The model never invokes Python functions directly
* Tool name and arguments are validated before execution
* Tool output is treated as untrusted data and excludes secrets
* The loop has a maximum number of tool rounds
* Tests make no model or external-service requests

## Contribution notes

Use a harmless deterministic tool so contributors can run the sample locally.
Keep dispatch explicit; dynamic imports, `eval`, shell execution, and unrestricted
file access are outside this sample's scope.

## References

* [Azure OpenAI function calling](https://learn.microsoft.com/azure/foundry/openai/how-to/function-calling)
* [JSON Schema](https://json-schema.org/learn/getting-started-step-by-step)