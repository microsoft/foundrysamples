---
title: Test AI-Dependent Code with Fakes
description: Contributor guide for deterministic tests of code that depends on model responses
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Test application behavior without network calls, credentials, model variability,
or mocks coupled to internal SDK implementation details.

## What to build

* A small application function with an injected model dependency
* A reusable fake that returns scripted responses and records requests
* Fixtures for success, refusal, malformed output, timeout, and service failure
* One separately marked live integration test

## Acceptance criteria

* Local tests are deterministic and work offline
* Assertions focus on application contracts and observable behavior
* The fake fails clearly when it receives an unexpected request
* Test data contains no customer information, secrets, or unstable timestamps
* Live tests skip with an actionable reason when configuration is absent

## Contribution notes

Prefer a small handwritten fake over patching nested SDK methods. Keep fixtures
near the tests that own them, and document the command for running local tests
separately from live tests.

## References

* [pytest fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
* [Python unittest mock guidance](https://docs.python.org/3/library/unittest.mock.html)