---
title: Require Human Approval for a Sensitive Tool
description: Contributor guide for pausing an agent before sensitive tool execution
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Pause before a simulated sensitive action, present the exact validated action to
an approver, and execute only after explicit, current approval.

## What to build

* A harmless read tool and a simulated sensitive write tool
* An approval request containing normalized arguments and risk context
* Approve, deny, expire, cancel, and resume paths
* Tests proving no side effect occurs without matching approval

## Acceptance criteria

* Approval is bound to the exact tool name and normalized arguments
* Modified, stale, replayed, or already-used approval is rejected
* Denial and timeout return a safe result to the agent
* Audit events exclude credentials and unnecessary sensitive content
* The sample never changes a real external resource

## Contribution notes

Keep policy enforcement in application code, not in prompt wording. Use an
in-memory approval store for this teaching sample and document that production
systems need durable identity, authorization, concurrency, and audit controls.

## References

* [Microsoft Agent Framework workflows](https://learn.microsoft.com/agent-framework/workflows/)
* [Azure Architecture Center compensating transaction pattern](https://learn.microsoft.com/azure/architecture/patterns/compensating-transaction)