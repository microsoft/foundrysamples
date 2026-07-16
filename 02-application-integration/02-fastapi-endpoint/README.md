---
title: Add an AI Endpoint to FastAPI
description: Contributor guide for integrating a Foundry model service into an existing FastAPI application
ms.date: 2026-07-16
ms.topic: tutorial
---

## Sample status

This sample is planned and ready for implementation.

## Goal

Add one production-shaped AI route to a small existing FastAPI application with
validated input, dependency injection, cancellation, and stable HTTP errors.

## What to build

* A minimal FastAPI application with one non-AI route already present
* An asynchronous AI endpoint that calls the sample 5 service boundary
* Request and response models with useful validation constraints
* Local API tests using a fake model service

## Acceptance criteria

* Client disconnect or task cancellation reaches the model call
* Authentication and the SDK client are initialized outside the route handler
* Service failures map to documented, non-sensitive HTTP responses
* Tests cover success, invalid input, timeout, and dependency failure
* The README documents startup, request examples, and expected JSON responses

## Contribution notes

Add only the dependencies needed by the sample and pin them in `pyproject.toml`.
Do not turn this folder into a starter application; the endpoint integration is
the teaching point.

## References

* [FastAPI dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/)
* [FastAPI testing](https://fastapi.tiangolo.com/tutorial/testing/)