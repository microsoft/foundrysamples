---
title: Record Latency, Tokens, Errors, and Estimated Cost
description: Contributor guide for useful AI operational metrics without logging secrets
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Measure model latency, token usage, errors, and clearly labeled cost estimates
using bounded-cardinality telemetry that is suitable for aggregation.

## What to build

* Metrics around a representative model call
* Input, output, and total token counters from SDK usage metadata
* A versioned price configuration with currency and effective date
* Tests for metric values, missing usage, error paths, and cost calculations

## Acceptance criteria

* Cost is labeled as an estimate and never replaces Azure billing data
* Model and deployment labels are normalized to bounded known values
* Prompts, responses, tokens, credentials, and user identifiers are not logged
* Latency uses a monotonic clock and records cancelled requests separately
* Tests cover rounding and unknown-model pricing behavior

## Contribution notes

Keep pricing data small and visibly dated because rates vary by model, region,
and purchase option. Unknown pricing should produce no estimate rather than a
misleading zero.

## References

* [Azure OpenAI pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
* [OpenTelemetry metrics](https://opentelemetry.io/docs/concepts/signals/metrics/)