---
title: Stream a Response and Handle Cancellation
description: Contributor guide for streaming model output and stopping cleanly when a caller cancels
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation. It should extend the
authentication and configuration pattern from the minimal text request without
copying unrelated helpers into this folder.

## Goal

Show how an existing Python application can display model output as it arrives,
cancel an in-progress request, and release the response stream cleanly.

## What to build

* A runnable `streaming_response.py` example using the Responses API
* Incremental text output without buffering the complete response
* Cancellation through `Ctrl+C` or an `asyncio` cancellation signal
* Actionable handling for authentication, timeout, and service errors
* A deterministic test using a fake stream, including cancellation cleanup

## Prerequisites

* Python 3.11 or later
* `uv` and the dependencies declared in the repository `pyproject.toml`
* An Azure OpenAI model deployment in Microsoft Foundry
* Microsoft Entra ID access with the Cognitive Services OpenAI User role

## Suggested interface

Run the completed sample from the repository root:

```powershell
uv run python 01-model-basics/02-streaming-response/streaming_response.py
```

Keep endpoint and deployment configuration compatible with sample 1. Add an
`.env.example` only if this sample introduces a new setting.

## Acceptance criteria

* Text is printed as response events arrive
* Cancellation stops iteration and closes the stream without a traceback
* Partial output is not presented as a complete answer
* No credential, token, or prompt content is written to logs
* Local tests make no network requests and cover normal and cancelled streams
* A live test is marked and skipped when Azure configuration is unavailable

## Contribution notes

Keep the streaming event loop visible in the primary file. Avoid a shared
abstraction that hides the event types or cancellation path this sample teaches.
Update this README with exact setup, expected output, troubleshooting, test, and
cleanup instructions when adding the implementation.

## Cost and cleanup

Model usage incurs token charges. The sample should create no Azure resources,
so no cleanup beyond stopping the process is expected.

## References

* [Azure OpenAI Responses API](https://learn.microsoft.com/azure/foundry/openai/how-to/responses)
* [Python asyncio task cancellation](https://docs.python.org/3/library/asyncio-task.html#task-cancellation)