---
title: Add Concurrency Limits and Graceful Degradation
description: Contributor guide for bounded AI workload concurrency, fallback, and overload behavior
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Protect an application and its model quota with bounded concurrency, queueing,
deadlines, cancellation, fallback behavior, and explicit degraded responses.

## What to build

* An asynchronous workload with a configured concurrency limit
* Queue timeout and end-to-end request deadline behavior
* One honest fallback that does not present stale or partial data as model output
* Deterministic tests using controlled tasks rather than real-time sleeps

## Acceptance criteria

* In-flight model calls never exceed the configured limit
* Cancelled and timed-out work releases permits
* Overload returns a documented retryable or degraded result
* Fallback is bounded and cannot create retry amplification
* Tests cover saturation, fairness, cancellation, failure, and recovery

## Contribution notes

Use `asyncio` primitives from the standard library unless an installed framework
already owns concurrency. State that an in-process limit applies per process and
document when a distributed queue or platform-level control becomes necessary.

## References

* [Python asyncio synchronization primitives](https://docs.python.org/3/library/asyncio-sync.html)
* [Azure architecture throttling pattern](https://learn.microsoft.com/azure/architecture/patterns/throttling)