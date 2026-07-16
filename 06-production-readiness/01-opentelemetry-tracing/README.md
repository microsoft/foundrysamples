---
title: Trace Model, Retrieval, and Tool Calls
description: Contributor guide for privacy-conscious OpenTelemetry tracing of an AI request
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Trace one request across model, retrieval, and tool boundaries with correlated
spans while excluding prompt, response, credential, and sensitive tool data.

## What to build

* A runnable flow instrumented with OpenTelemetry
* Parent and child spans with stable low-cardinality attributes
* Console export for local inspection and optional Azure Monitor export
* Tests using an in-memory exporter to verify spans and redaction

## Acceptance criteria

* Trace context flows across asynchronous boundaries
* Span status and errors are recorded without sensitive exception content
* Prompt and response capture is disabled by default
* Export failure does not fail the application request
* The README documents sampling, retention, Azure cost, and configuration

## Contribution notes

Prefer semantic conventions and existing SDK instrumentation where available.
Document every custom attribute and avoid user identifiers, full URLs, query
text, or other high-cardinality values.

## References

* [OpenTelemetry Python](https://opentelemetry.io/docs/languages/python/)
* [Azure Monitor OpenTelemetry](https://learn.microsoft.com/azure/azure-monitor/app/opentelemetry-enable)