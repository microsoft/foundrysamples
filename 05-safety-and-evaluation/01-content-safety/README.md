---
title: Apply Input and Output Content Safety Checks
description: Contributor guide for enforcing content safety policy around a Foundry model call
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Apply an explicit application policy to user input and model output, then return
safe, useful outcomes for allowed, blocked, and unavailable-check conditions.

## What to build

* A runnable model flow with input and output safety decisions
* Configurable category thresholds and an application-owned result contract
* Safe handling for blocked content and safety-service failure
* Tests using synthetic fixtures for each policy branch

## Acceptance criteria

* Input is checked before it reaches downstream tools or retrieval
* Output is checked before it is shown or persisted
* Logs record policy outcomes without storing raw sensitive content
* The behavior when safety checks are unavailable is documented
* Test fixtures are minimal, synthetic, and suitable for the repository

## Contribution notes

Distinguish platform filters from application policy and avoid claiming that one
check makes an application safe. The README must describe limitations, expected
Azure usage, and how developers can adjust thresholds responsibly.

## References

* [Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/overview)
* [Azure OpenAI content filtering](https://learn.microsoft.com/azure/foundry/openai/concepts/content-filter)