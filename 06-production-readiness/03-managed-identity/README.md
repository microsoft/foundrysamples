---
title: Use Local Credentials and Managed Identity
description: Contributor guide for one DefaultAzureCredential path across local and Azure environments
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Use `DefaultAzureCredential` for local development and managed identity in Azure
without API keys, environment-specific authentication branches, or silent fallbacks.

## What to build

* A runnable client factory with explicit endpoint and deployment settings
* Local authentication through supported developer credentials
* System-assigned and user-assigned managed identity configuration examples
* Offline tests for configuration plus a marked live identity test

## Acceptance criteria

* Production guidance excludes interactive and developer-only credentials
* User-assigned identity selection is explicit when configured
* Role assignments follow least privilege and are documented separately
* Authentication failures identify the next action without printing tokens
* No API-key fallback is added

## Contribution notes

Do not provision Azure resources from the Python sample. Document the required
role, scope, identity configuration, and token audience using official guidance,
and keep tenant-specific values in `.env.example` placeholders.

## References

* [DefaultAzureCredential overview](https://learn.microsoft.com/python/api/overview/azure/identity-readme#defaultazurecredential)
* [Azure OpenAI keyless authentication](https://learn.microsoft.com/azure/developer/ai/keyless-connections)