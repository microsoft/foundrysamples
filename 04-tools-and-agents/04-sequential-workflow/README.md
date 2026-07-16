---
title: Coordinate a Sequential Agent Workflow
description: Contributor guide for a small typed workflow using Microsoft Agent Framework
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Coordinate a small sequence of specialized steps with typed inputs, explicit
handoffs, bounded execution, and a deterministic final application result.

## What to build

* A two- or three-step workflow with a concrete business-shaped task
* Typed state passed between steps using Agent Framework workflow APIs
* Per-step timeout, failure, cancellation, and final validation behavior
* Tests for ordering, handoff data, short-circuiting, and resume behavior

## Acceptance criteria

* Each step has one responsibility and a documented contract
* The workflow has maximum step and model-call limits
* Failed validation prevents downstream execution
* State transitions are observable without logging prompt content
* Tests use deterministic fake executors and make no network calls

## Contribution notes

Use a direct function call where a model is not needed. The README should compare
this workflow with the typed function-tool and multi-turn samples so developers
can choose the smallest sufficient pattern.

## References

* [Microsoft Agent Framework workflows](https://learn.microsoft.com/agent-framework/workflows/)
* [Microsoft Agent Framework repository](https://github.com/microsoft/agent-framework)