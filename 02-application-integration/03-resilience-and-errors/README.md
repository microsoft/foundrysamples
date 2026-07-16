---
title: Handle Timeouts, Throttling, Retries, and Errors
description: Contributor guide for bounded retries and actionable Foundry service error handling
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Make an external model call predictable under timeout, throttling, transient
service failure, authentication failure, and invalid-request conditions.

## What to build

* A runnable request with explicit connect and response timeouts
* Bounded retry behavior that honors server guidance and adds jitter
* Error classification into retryable and non-retryable application errors
* Deterministic tests with a fake clock or injected delay function

## Acceptance criteria

* Retries are limited by both attempt count and total elapsed time
* `Retry-After` is honored when available
* Authentication, validation, and permission failures are not retried
* Cancellation interrupts waiting and in-flight work
* Tests cover eventual success, exhausted retries, and immediate failure

## Contribution notes

Use retry behavior already provided by the installed SDK when it meets these
requirements. Avoid stacked retry layers. Tests must not sleep in real time, and
logs must exclude credentials and prompt content.

## References

* [Azure architecture retry pattern](https://learn.microsoft.com/azure/architecture/patterns/retry)
* [Azure OpenAI quotas and limits](https://learn.microsoft.com/azure/foundry/openai/quotas-limits)