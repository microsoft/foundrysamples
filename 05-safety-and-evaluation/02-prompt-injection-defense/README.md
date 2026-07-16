---
title: Defend Grounded Flows Against Prompt Injection
description: Contributor guide for treating retrieved content and tool arguments as untrusted input
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Layer deterministic controls around retrieval and tools so malicious document
instructions cannot override policy or authorize unsafe tool arguments.

## What to build

* A grounded flow with clearly delimited, untrusted retrieved content
* Tool allowlists, typed argument validation, and authorization checks
* Synthetic direct and indirect prompt-injection fixtures
* Tests proving blocked instructions cannot trigger a sensitive action

## Acceptance criteria

* Security decisions do not depend only on the model following a prompt
* Retrieved instructions cannot modify tool policy or system configuration
* Tool arguments are authorized against application identity and current state
* Suspicious content follows a documented block or degrade path
* Tests include benign content to detect excessive blocking

## Contribution notes

Use harmless simulated tools and synthetic attack text. Document residual risk
and avoid absolute claims such as "injection proof." Keep controls visible at the
trust boundaries where retrieval and tool execution enter the application.

## References

* [Microsoft guidance for securing generative AI](https://learn.microsoft.com/security/ai-red-team/)
* [OWASP LLM prompt injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)