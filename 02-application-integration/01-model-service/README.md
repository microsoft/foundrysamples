---
title: Wrap Model Access in an Application Service
description: Contributor guide for isolating Foundry model access behind an application-owned interface
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Place model access behind a small application service so business code does not
depend directly on SDK response types or a specific model deployment.

## What to build

* A runnable example with an application-owned request and response contract
* A model service that owns SDK calls, timeout, and error translation
* A calling function that depends on the service contract
* Deterministic tests using dependency injection and a fake service

## Acceptance criteria

* SDK objects do not escape the model service boundary
* Configuration is supplied at startup rather than read throughout the code
* Business logic can be tested without Azure credentials or network access
* Errors preserve useful context without leaking prompts or secrets
* The README explains when this boundary is useful and when it is unnecessary

## Contribution notes

Use plain Python protocols or callables unless an existing dependency already
provides the needed boundary. Keep the example small enough to copy into an
existing application and avoid introducing a framework solely for injection.

## References

* [Python typing protocols](https://docs.python.org/3/library/typing.html#typing.Protocol)
* [Azure OpenAI keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections)