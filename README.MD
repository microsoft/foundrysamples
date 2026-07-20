---
title: Microsoft AI Python Samples
description: Roadmap for Python samples that add Microsoft AI capabilities to existing applications
ms.date: 2026-07-15
ms.topic: overview
keywords:
  - Microsoft Foundry
  - Python
  - generative AI
  - reference samples
---

## Purpose

This repository will provide small, runnable Python references for developers who
want to add Microsoft AI capabilities to an existing application. The collection
will progress from a single model call to retrieval, agents, evaluation, and
production operations without requiring developers to adopt a complete starter
application.

The first release will contain **24 snippets across six modules** and **one
capstone application**. Each snippet will teach one integration pattern and take
about 10 to 20 minutes to understand and run.

## Audience and scope

The samples target Python developers who can run a virtual environment and know
basic HTTP and asynchronous programming. They may be adding AI to a web API,
worker, command-line tool, or existing business application.

The series will use current Microsoft-supported libraries where each one owns the
problem:

* The OpenAI Python client for direct model inference through Microsoft Foundry
* `azure-identity` for local and managed identity authentication
* `azure-ai-projects` for Foundry project operations
* Microsoft Agent Framework for agent and workflow patterns
* `azure-search-documents` for production retrieval
* `azure-ai-evaluation` for quality measurement
* OpenTelemetry and Azure Monitor for tracing and operations

SDK versions and model names will be pinned in each module. Shared helpers will
be limited to authentication and configuration so readers can copy a snippet
into an existing project without importing this repository.

## Sample catalog

### Module 1: Connect to a model

1. [Send a minimal text request using Microsoft Entra ID](01-model-basics/01-minimal-text-request/)
2. [Stream a response and handle cancellation](01-model-basics/02-streaming-response/)
3. [Return validated structured output as a Python model](01-model-basics/03-structured-output/)
4. [Send text and an image in a multimodal request](01-model-basics/04-multimodal-request/)

Outcome: developers can make secure model calls and choose between text,
streaming, structured, and multimodal responses.

### Module 2: Integrate with an application

5. [Wrap model access behind an application service](02-application-integration/01-model-service/)
6. [Add an AI endpoint to an existing FastAPI application](02-application-integration/02-fastapi-endpoint/)
7. [Handle timeouts, throttling, retries, and service errors](02-application-integration/03-resilience-and-errors/)
8. [Test AI-dependent code with a fake client and deterministic fixtures](02-application-integration/04-testing-with-fakes/)

Outcome: developers can add AI without coupling business logic to an SDK or a
specific model deployment.

### Module 3: Ground responses with data

9. [Create embeddings for local documents](03-grounding-and-search/01-document-embeddings/)
10. [Build and query a small local vector index](03-grounding-and-search/02-local-vector-index/)
11. [Retrieve from Azure AI Search with filters](03-grounding-and-search/03-azure-ai-search/)
12. [Generate a grounded answer with citations and a no-answer path](03-grounding-and-search/04-grounded-answers-with-citations/)

Outcome: developers can build a retrieval-augmented generation flow, understand
its moving parts, and avoid unsupported answers.

### Module 4: Add tools and agents

13. [Define and execute a typed function tool](04-tools-and-agents/01-typed-function-tool/)
14. [Run a multi-turn agent with conversation state](04-tools-and-agents/02-multi-turn-agent/)
15. [Require human approval before a sensitive tool call](04-tools-and-agents/03-human-approval/)
16. [Coordinate a small sequential workflow with Microsoft Agent Framework](04-tools-and-agents/04-sequential-workflow/)

Outcome: developers can decide when function calling is enough and when an agent
or workflow is justified.

### Module 5: Improve safety and quality

17. [Apply input and output content safety checks](05-safety-and-evaluation/01-content-safety/)
18. [Defend a grounded flow against prompt injection and unsafe tool arguments](05-safety-and-evaluation/02-prompt-injection-defense/)
19. [Build a versioned JSON Lines evaluation dataset](05-safety-and-evaluation/03-evaluation-dataset/)
20. [Run relevance, groundedness, safety, and task-success evaluations](05-safety-and-evaluation/04-quality-evaluation/)

Outcome: developers can define measurable quality gates before releasing an AI
feature.

### Module 6: Prepare for production

21. [Trace model, retrieval, and tool calls with OpenTelemetry](06-production-readiness/01-opentelemetry-tracing/)
22. [Record latency, token usage, errors, and estimated cost without logging secrets](06-production-readiness/02-metrics-and-cost/)
23. [Use `DefaultAzureCredential` locally and managed identity in Azure](06-production-readiness/03-managed-identity/)
24. [Add concurrency limits, fallback behavior, and graceful degradation](06-production-readiness/04-concurrency-and-fallbacks/)

Outcome: developers can observe, secure, and operate an AI feature in an existing
service.

## Capstone application

The capstone will be a support-answer API added to a small existing FastAPI
service. It will reuse the patterns from the snippets to provide retrieval with
citations, a read-only ticket lookup tool, structured responses, safety checks,
evaluation, and tracing.

The capstone is an integration example, not a new framework. Its code will link
back to the relevant snippets so developers can adopt only the pieces they need.

## Repository layout

```text
foundrysamples/
|-- 01-model-basics/
|-- 02-application-integration/
|-- 03-grounding-and-search/
|-- 04-tools-and-agents/
|-- 05-safety-and-evaluation/
|-- 06-production-readiness/
|-- capstone-support-api/
|-- shared/
|-- .env.example
|-- pyproject.toml
`-- README.MD
```

Each numbered snippet folder will contain:

* A focused `README.md` with prerequisites, setup, expected output, and cleanup
* One primary runnable Python file
* A test or self-check that can fail when the demonstrated behavior breaks
* An `.env.example` entry only when the snippet needs additional configuration
* Sample input data that contains no credentials or customer information

## Sample contract

Every snippet must meet the same reference standard:

* Run independently from the repository root with one documented command
* Authenticate without API keys by default
* Keep secrets out of source code, output, traces, and sample data
* Validate inputs and structured model outputs
* Include timeout and actionable error handling at external boundaries
* State expected Azure usage and any resources that may incur cost
* Include a deterministic test for local logic and a marked live integration test
* Show cleanup steps for resources or indexed data created by the sample
* Link to the official Microsoft documentation for the demonstrated feature
* Avoid hiding the teaching point in shared abstractions

## Delivery plan

### Milestone 1: Foundation

Build snippets 1 through 8, establish packaging and linting, and validate the
copy-into-an-existing-project experience. This milestone is the minimum useful
release.

### Milestone 2: Data and agents

Build snippets 9 through 16. Keep local retrieval available for learning, then
show Azure AI Search as the production path. Introduce agents only after direct
model calls and function tools are clear.

### Milestone 3: Quality and operations

Build snippets 17 through 24, add evaluation datasets and CI quality gates, and
verify that telemetry excludes prompts and sensitive content by default.

### Milestone 4: Capstone and release

Assemble the capstone from existing patterns, run all local and live test suites,
review documentation links and costs, and publish a compatibility matrix for
Python, SDK, and model versions.

## Definition of done

The first release is complete when all 24 snippets pass their local checks, live
tests pass against a documented Foundry project configuration, and the capstone
can be run from a clean clone by following its README. A developer must be able
to copy any individual pattern without depending on the capstone or undocumented
shared state.

## Support statement

All code samples are provided "as-is" without warranties or support commitments.
Users are responsible for validating security, compliance, reliability, and
operational requirements before production use.

please reach out to nitinkum@microsoft.com or gaccount4m@gmail.com in case you want to discuss on this
