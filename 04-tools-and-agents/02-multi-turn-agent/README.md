---
title: Run a Multi-Turn Agent with Conversation State
description: Contributor guide for bounded multi-turn state using Microsoft Agent Framework
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Use Microsoft Agent Framework to continue a conversation across turns while
making state ownership, retention, size limits, and reset behavior explicit.

## What to build

* A runnable command-line agent with a short system instruction
* Conversation creation, continuation, inspection, and reset
* A bounded state policy and stable application conversation identifier
* Tests for state continuity and isolation between conversations

## Acceptance criteria

* State from one conversation cannot appear in another
* The application does not persist secrets or sensitive prompt content by default
* Conversation growth has a documented limit or compaction strategy
* Cancellation and model failure leave state in a defined condition
* Tests use a fake agent or model and require no Azure connection

## Contribution notes

Pin the Agent Framework package version and use its public state APIs. Avoid
adding retrieval or multiple agents here; this sample should answer when stateful
agent behavior adds value beyond a direct model call.

## References

* [Microsoft Agent Framework overview](https://learn.microsoft.com/agent-framework/overview/)
* [Microsoft Agent Framework Python repository](https://github.com/microsoft/agent-framework/tree/main/python)